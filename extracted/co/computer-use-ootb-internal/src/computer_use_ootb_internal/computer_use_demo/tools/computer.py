import subprocess
import platform
import pyautogui
import asyncio
import base64
import os
import time
if platform.system() == "Darwin":
    import Quartz  # uncomment this line if you are on macOS
from enum import StrEnum
from pathlib import Path
from typing import Literal, TypedDict
from uuid import uuid4
from screeninfo import get_monitors

from PIL import ImageGrab, Image
from functools import partial

from anthropic.types.beta import BetaToolComputerUse20241022Param

from computer_use_ootb_internal.computer_use_demo.tools.base import BaseAnthropicTool, ToolError, ToolResult
from computer_use_ootb_internal.computer_use_demo.tools.run import run

from computer_use_ootb_internal.computer_use_demo.tools.computer_marbot import MarbotAutoGUI
from computer_use_ootb_internal.computer_use_demo.animation.click_animation import show_click, show_move_to


OUTPUT_DIR = "./tmp/outputs"

TYPING_DELAY_MS = 12
TYPING_GROUP_SIZE = 50

Action = Literal[
    "key",
    "type",
    "mouse_move",
    "left_click",
    "left_click_drag",
    "right_click",
    "middle_click",
    "double_click",
    "triple_click",
    "left_press",
    "key_down",
    "key_up",
    "scroll_down",
    "scroll_up",
    "screenshot",
    "cursor_position",
    "sr_scroll_down",
    "sr_scroll_up",
    "wait",
    # starrail browser mode
    "left_click_windll",
    "mouse_move_windll",
    "right_click_windll",
    "key_down_windll",
    "key_up_windll",
]


class Resolution(TypedDict):
    width: int
    height: int


MAX_SCALING_TARGETS: dict[str, Resolution] = {
    "XGA": Resolution(width=1024, height=768),  # 4:3
    "WXGA": Resolution(width=1280, height=800),  # 16:10
    "FWXGA": Resolution(width=1366, height=768),  # ~16:9
}


class ScalingSource(StrEnum):
    COMPUTER = "computer"
    API = "api"


class ComputerToolOptions(TypedDict):
    display_height_px: int
    display_width_px: int
    display_number: int | None


def chunks(s: str, chunk_size: int) -> list[str]:
    return [s[i : i + chunk_size] for i in range(0, len(s), chunk_size)]


def get_screen_details():
    screens = get_monitors()
    screen_details = []

    # Sort screens by x position to arrange from left to right
    sorted_screens = sorted(screens, key=lambda s: s.x)

    # Loop through sorted screens and assign positions
    primary_index = 0
    for i, screen in enumerate(sorted_screens):
        if i == 0:
            layout = "Left"
        elif i == len(sorted_screens) - 1:
            layout = "Right"
        else:
            layout = "Center"
        
        if screen.is_primary:
            position = "Primary" 
            primary_index = i
        else:
            position = "Secondary"
        screen_info = f"Screen {i + 1}: {screen.width}x{screen.height}, {layout}, {position}"
        screen_details.append(screen_info)

    return screen_details, primary_index


class ComputerTool(BaseAnthropicTool):
    """
    A tool that allows the agent to interact with the screen, keyboard, and mouse of the current computer.
    Adapted for Windows using 'pyautogui'.
    """

    name: Literal["computer"] = "computer"
    api_type: Literal["computer_20241022"] = "computer_20241022"
    width: int
    height: int
    display_num: int | None

    _screenshot_delay = 2.0
    _scaling_enabled = True

    @property
    def options(self) -> ComputerToolOptions:
        width, height = self.scale_coordinates(
            ScalingSource.COMPUTER, self.width, self.height
        )
        return {
            "display_width_px": width,
            "display_height_px": height,
            "display_number": self.display_num,
        }

    def to_params(self) -> BetaToolComputerUse20241022Param:
        return {"name": self.name, "type": self.api_type, **self.options}

    def __init__(self, selected_screen: int = 0, is_scaling: bool = True):
        super().__init__()

        # Get screen width and height using Windows command
        self.display_num = None
        self.offset_x = 0
        self.offset_y = 0
        self.selected_screen = selected_screen   
        self.is_scaling = is_scaling
        self.width, self.height = self.get_screen_size()     

        # Path to cliclick
        self.cliclick = "cliclick"
        self.key_conversion = {"Page_Down": "pagedown",
                               "Page_Up": "pageup",
                               "Super_L": "win",
                               "Escape": "esc"}
        
        system = platform.system()        # Detect platform
        if system == "Windows":
            screens = get_monitors()
            sorted_screens = sorted(screens, key=lambda s: s.x)
            if self.selected_screen < 0 or self.selected_screen >= len(screens):
                raise IndexError("Invalid screen index.")
            screen = sorted_screens[self.selected_screen]
            bbox = (screen.x, screen.y, screen.x + screen.width, screen.y + screen.height)

        elif system == "Darwin":  # macOS
            max_displays = 32  # Maximum number of displays to handle
            active_displays = Quartz.CGGetActiveDisplayList(max_displays, None, None)[1]
            screens = []
            for display_id in active_displays:
                bounds = Quartz.CGDisplayBounds(display_id)
                screens.append({
                    'id': display_id, 'x': int(bounds.origin.x), 'y': int(bounds.origin.y),
                    'width': int(bounds.size.width), 'height': int(bounds.size.height),
                    'is_primary': Quartz.CGDisplayIsMain(display_id)  # Check if this is the primary display
                })
            sorted_screens = sorted(screens, key=lambda s: s['x'])
            if self.selected_screen < 0 or self.selected_screen >= len(screens):
                raise IndexError("Invalid screen index.")
            screen = sorted_screens[self.selected_screen]
            bbox = (screen['x'], screen['y'], screen['x'] + screen['width'], screen['y'] + screen['height'])
        else:  # Linux or other OS
            cmd = "xrandr | grep ' primary' | awk '{print $4}'"
            try:
                output = subprocess.check_output(cmd, shell=True).decode()
                resolution = output.strip().split()[0]
                width, height = map(int, resolution.split('x'))
                bbox = (0, 0, width, height)  # Assuming single primary screen for simplicity
            except subprocess.CalledProcessError:
                raise RuntimeError("Failed to get screen resolution on Linux.")
            
        self.offset_x = screen['x'] if system == "Darwin" else screen.x
        self.offset_y = screen['y'] if system == "Darwin" else screen.y
        self.bbox = bbox

        self.marbot_auto_gui = MarbotAutoGUI()
        
    
    async def __call__(
        self,
        *,
        action: Action,
        text: str | None = None,
        coordinate: tuple[int, int] | None = None,
        **kwargs,
    ):
        print(f"action: {action}, text: {text}, coordinate: {coordinate}")
       
        # Action Type 1: Required coordinates
        # Actions: mouse_move, left_click_drag

        if action in ("mouse_move", "left_click_drag"):
            if coordinate is None:
                raise ToolError(output=f"coordinate is required for {action}", action_base_type="error")
            if text is not None:
                raise ToolError(output=f"text is not accepted for {action}", action_base_type="error")
            if not isinstance(coordinate, (list, tuple)) or len(coordinate) != 2:
                raise ToolError(output=f"{coordinate} must be a tuple of length 2", action_base_type="error")
            if not all(isinstance(i, int) for i in coordinate):
                raise ToolError(output=f"{coordinate} must be a tuple of non-negative ints", action_base_type="error")
            
            if self.is_scaling:
                x, y = self.scale_coordinates(
                    ScalingSource.API, coordinate[0], coordinate[1]
                )
            else:
                x, y = coordinate
            
            x += self.offset_x
            y += self.offset_y

            if action == "mouse_move":
                pyautogui.moveTo(x, y)
                return ToolResult(output=f"Mouse move", action_base_type="move")
            
            elif action == "left_click_drag":
                current_x, current_y = pyautogui.position()
                pyautogui.dragTo(x, y, duration=0.5)  # Adjust duration as needed
                return ToolResult(output=f"Mouse drag", action_base_type="move")

        # Action Type 2: Required text (keynames)
        # Actions: key, type, key_down, key_up
        if action in ("key", "type", "key_down", "key_up"):
            if text is None:
                raise ToolError(output=f"text is required for {action}", action_base_type="error")
            if coordinate is not None:
                raise ToolError(output=f"coordinate is not accepted for {action}", action_base_type="error")
            if not isinstance(text, str):
                raise ToolError(output=f"{text} must be a string", action_base_type="error")

            if action == "key":
                # Handle key combinations
                keys = text.split('+')
                for key in keys:
                    key = self.key_conversion.get(key.strip(), key.strip())
                    key = key.lower()
                    pyautogui.keyDown(key)  # Press down each key
                for key in reversed(keys):
                    key = self.key_conversion.get(key.strip(), key.strip())
                    key = key.lower()
                    pyautogui.keyUp(key)    # Release each key in reverse order
                return ToolResult(output=f"Press key '{text}'", action_base_type="key")
            
            elif action == "key_down":
                pyautogui.keyDown(text)
                return ToolResult(output=f"Press key '{text}'", action_base_type="key")
            elif action == "key_up":
                pyautogui.keyUp(text)
                return ToolResult(output=f"Release key '{text}'", action_base_type="key")

            elif action == "type":
                pyautogui.typewrite(text, interval=TYPING_DELAY_MS / 1000)  # Convert ms to seconds
                # screenshot_base64 = (await self.screenshot()).base64_image
                return ToolResult(output=f"Type '{text}'", action_base_type="type") #  base64_image=screenshot_base64)

        # Action Type 3: No required text or coordinates
        # Actions: left_click, right_click, double_click, middle_click, left_press, scroll_down, scroll_up
        if action in (
            "left_click",
            "right_click",
            "double_click",
            "triple_click",
            "middle_click",
            "left_press",
            "scroll_down",
            "scroll_up",
            "wait",
        ):
            if text is not None:
                raise ToolError(output=f"text is not accepted for {action}", action_base_type="error")
            # if coordinate is not None:
            #     raise ToolError(output=f"coordinate is not accepted for {action}", action_base_type="error")

            if coordinate is not None:
                x, y = coordinate
                x += self.offset_x
                y += self.offset_y
            else:
                x, y = pyautogui.position()

            if action == "left_click":
                show_click(x, y)
                pyautogui.click(x=x, y=y)
                return ToolResult(output="Left click", action_base_type="click")
            elif action == "right_click":
                show_click(x, y)
                pyautogui.rightClick(x=x, y=y)
                return ToolResult(output="Right click", action_base_type="click")
            elif action == "middle_click":
                show_click(x, y)
                pyautogui.middleClick(x=x, y=y)
                return ToolResult(output="Middle click", action_base_type="click")
            elif action == "double_click":
                show_click(x, y)
                pyautogui.doubleClick(x=x, y=y)
                return ToolResult(output="Double click", action_base_type="click")
            elif action == "triple_click":
                show_click(x, y)
                pyautogui.click(x=x, y=y, clicks=3, interval=0.1)  # 3 clicks with 0.1s interval
                return ToolResult(output="Triple click", action_base_type="click")
            elif action == "left_press":
                show_click(x, y)
                pyautogui.mouseDown(x=x, y=y)
                time.sleep(1)
                pyautogui.mouseUp(x=x, y=y)
                return ToolResult(output="Left press", action_base_type="click")

            elif action == "scroll_down":
                pyautogui.scroll(-200)  # Adjust scroll amount as needed
                return ToolResult(output="Scrolled down", action_base_type="scroll")
            
            elif action == "scroll_up":
                pyautogui.scroll(200)   # Adjust scroll amount as needed
                return ToolResult(output="Scrolled up", action_base_type="scroll")
            
            elif action == "wait":
                time.sleep(15)
                return ToolResult(output="Wait for next event", action_base_type="wait")
            
            return ToolResult(output=f"Performed {action}", action_base_type="unknown")
        
        # Action Type 4: Miscs. No required text or coordinates
        # Actions: screenshot, cursor_position
        if action in ("screenshot", "cursor_position"):
            if text is not None:
                raise ToolError(output=f"text is not accepted for {action}", action_base_type="error")
            if coordinate is not None:
                raise ToolError(output=f"coordinate is not accepted for {action}", action_base_type="error")
            
            if action == "screenshot":
                return await self.screenshot()
            elif action == "cursor_position":
                x, y = pyautogui.position()
                # x, y = self.scale_coordinates(ScalingSource.COMPUTER, x, y)
                return ToolResult(output=f"Cursor position ({x},{y})", action_base_type="unknown")

        # Action Type 5: StarRail Mode
        # Actions: sr_scroll_down, sr_scroll_up
        if action in ("sr_scroll_down", "sr_scroll_up"):
            if text is not None:
                raise ToolError(output=f"text is not accepted for {action}", action_base_type="error")

            if action == "sr_scroll_down":
                for _ in range(20):
                    pyautogui.scroll(-100)  # Adjust scroll amount as needed
                    time.sleep(0.001)
                return ToolResult(output="Scroll down", action_base_type="scroll")
            elif action == "sr_scroll_up":
                for _ in range(20):
                    pyautogui.scroll(100)   # Adjust scroll amount as needed
                    time.sleep(0.001)
                return ToolResult(output="Scroll up", action_base_type="scroll")

        # starrail browser mode
        if action in ("left_click_windll", "mouse_move_windll", "right_click_windll", "key_down_windll", "key_up_windll"):
            if action == "left_click_windll":
                if coordinate is None:
                    time.sleep(0.25)
                    x, y = pyautogui.position()
                    show_click(x, y)
                    self.marbot_auto_gui.click()
                else:
                    x = coordinate[0]+self.offset_x
                    y = coordinate[1]+self.offset_y
                    show_click(x, y)
                    time.sleep(0.25)
                    self.marbot_auto_gui.click(x=x, y=y)
                    # self.marbot_auto_gui.click(x=x, y=y)
                return ToolResult(output=f"Left click", action_base_type="click")

            elif action == "mouse_move_windll":
                if coordinate is None:
                    raise ToolError(output=f"coordinate is required for {action}", action_base_type="error")
                
                x0, y0 = pyautogui.position()
                # x0, y0 = self.scale_coordinates(ScalingSource.COMPUTER, x0, y0)
                x1 = coordinate[0]+self.offset_x
                y1 = coordinate[1]+self.offset_y

                show_move_to(x0, y0, x1, y1)
                self.marbot_auto_gui.moveTo(x=x1, y=y1)
                time.sleep(0.25)
            
                return ToolResult(output=f"Mouse move", action_base_type="move")
            
            # elif action == "right_click_windll":
            #     self.marbot_auto_gui.rightClick(x=coordinate[0], y=coordinate[1])
            elif action == "key_down_windll":
                self.marbot_auto_gui.keyDown(text)
                time.sleep(0.25)
                return ToolResult(output=f"Key down '{text}'", type="hidden", action_base_type="key")
            
            elif action == "key_up_windll":
                time.sleep(0.25)
                self.marbot_auto_gui.keyUp(text)
                return ToolResult(output=f"Key up '{text}'", type="hidden", action_base_type="key")
            
            return ToolResult(output=f"Performed dll action:{action}", action_base_type="unknown")

        raise ToolError(output=f"Invalid action: {action}", type="hidden", action_base_type="error")


    async def screenshot(self):
        
        import time
        time.sleep(1)
        
        """Take a screenshot of the current screen and return a ToolResult with the base64 encoded image."""
        output_dir = Path(OUTPUT_DIR)
        output_dir.mkdir(parents=True, exist_ok=True)
        path = output_dir / f"screenshot_{uuid4().hex}.png"

        ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

        # Detect platform
        system = platform.system()

        if system == "Windows":
            # Windows: Use screeninfo to get monitor details
            screens = get_monitors()

            # Sort screens by x position to arrange from left to right
            sorted_screens = sorted(screens, key=lambda s: s.x)

            if self.selected_screen < 0 or self.selected_screen >= len(screens):
                raise IndexError("Invalid screen index.")

            screen = sorted_screens[self.selected_screen]
            bbox = (screen.x, screen.y, screen.x + screen.width, screen.y + screen.height)

        elif system == "Darwin":  # macOS
            # macOS: Use Quartz to get monitor details
            max_displays = 32  # Maximum number of displays to handle
            active_displays = Quartz.CGGetActiveDisplayList(max_displays, None, None)[1]

            # Get the display bounds (resolution) for each active display
            screens = []
            for display_id in active_displays:
                bounds = Quartz.CGDisplayBounds(display_id)
                screens.append({
                    'id': display_id,
                    'x': int(bounds.origin.x),
                    'y': int(bounds.origin.y),
                    'width': int(bounds.size.width),
                    'height': int(bounds.size.height),
                    'is_primary': Quartz.CGDisplayIsMain(display_id)  # Check if this is the primary display
                })

            # Sort screens by x position to arrange from left to right
            sorted_screens = sorted(screens, key=lambda s: s['x'])

            if self.selected_screen < 0 or self.selected_screen >= len(screens):
                raise IndexError("Invalid screen index.")

            screen = sorted_screens[self.selected_screen]
            bbox = (screen['x'], screen['y'], screen['x'] + screen['width'], screen['y'] + screen['height'])

        else:  # Linux or other OS
            cmd = "xrandr | grep ' primary' | awk '{print $4}'"
            try:
                output = subprocess.check_output(cmd, shell=True).decode()
                resolution = output.strip().split()[0]
                width, height = map(int, resolution.split('x'))
                bbox = (0, 0, width, height)  # Assuming single primary screen for simplicity
            except subprocess.CalledProcessError:
                raise RuntimeError("Failed to get screen resolution on Linux.")

        # Take screenshot using the bounding box
        screenshot = ImageGrab.grab(bbox=bbox)

        # Set offsets (for potential future use)
        self.offset_x = screen['x'] if system == "Darwin" else screen.x
        self.offset_y = screen['y'] if system == "Darwin" else screen.y

        print(f"target_dimension {self.target_dimension}")
        
        if not hasattr(self, 'target_dimension'):
            screenshot = self.padding_image(screenshot)
            self.target_dimension = MAX_SCALING_TARGETS["WXGA"]

        # Resize if target_dimensions are specified
        print(f"offset is {self.offset_x}, {self.offset_y}")
        print(f"target_dimension is {self.target_dimension}")
        screenshot = screenshot.resize((self.target_dimension["width"], self.target_dimension["height"]))

        # Save the screenshot
        screenshot.save(str(path))

        if path.exists():
            # Return a ToolResult instance instead of a dictionary
            return ToolResult(base64_image=base64.b64encode(path.read_bytes()).decode(), action_base_type="screenshot")
        
        raise ToolError(output=f"Failed to take screenshot: {path} does not exist.", action_base_type="error")

    def padding_image(self, screenshot):
        """Pad the screenshot to 16:10 aspect ratio, when the aspect ratio is not 16:10."""
        _, height = screenshot.size
        new_width = height * 16 // 10

        padding_image = Image.new("RGB", (new_width, height), (255, 255, 255))
        # padding to top left
        padding_image.paste(screenshot, (0, 0))
        return padding_image

    # async def shell(self, command: str, take_screenshot=True) -> ToolResult:
    #     """Run a shell command and return the output, error, and optionally a screenshot."""
    #     _, stdout, stderr = await run(command)
    #     base64_image = None

    #     if take_screenshot:
    #         # delay to let things settle before taking a screenshot
    #         await asyncio.sleep(self._screenshot_delay)
    #         base64_image = (await self.screenshot()).base64_image

    #     return ToolResult(output=stdout, error=stderr, base64_image=base64_image)

    def scale_coordinates(self, source: ScalingSource, x: int, y: int):
        """Scale coordinates to a target maximum resolution."""
        if not self._scaling_enabled:
            return x, y
        ratio = self.width / self.height
        target_dimension = None

        for target_name, dimension in MAX_SCALING_TARGETS.items():
            # allow some error in the aspect ratio - not ratios are exactly 16:9
            if abs(dimension["width"] / dimension["height"] - ratio) < 0.02:
                if dimension["width"] < self.width:
                    target_dimension = dimension
                    self.target_dimension = target_dimension
                    # print(f"target_dimension: {target_dimension}")
                break

        if target_dimension is None:
            # TODO: currently we force the target to be WXGA (16:10), when it cannot find a match
            target_dimension = MAX_SCALING_TARGETS["WXGA"]
            self.target_dimension = MAX_SCALING_TARGETS["WXGA"]

        # should be less than 1
        x_scaling_factor = target_dimension["width"] / self.width
        y_scaling_factor = target_dimension["height"] / self.height
        if source == ScalingSource.API:
            if x > self.width or y > self.height:
                raise ToolError(output=f"Coordinates {x}, {y} are out of bounds", action_base_type="error")
            # scale up
            return round(x / x_scaling_factor), round(y / y_scaling_factor)
        # scale down
        return round(x * x_scaling_factor), round(y * y_scaling_factor)

    def get_screen_size(self):
        if platform.system() == "Windows":
            # Use screeninfo to get primary monitor on Windows
            screens = get_monitors()

            # Sort screens by x position to arrange from left to right
            sorted_screens = sorted(screens, key=lambda s: s.x)
            
            if self.selected_screen is None:
                primary_monitor = next((m for m in get_monitors() if m.is_primary), None)
                return primary_monitor.width, primary_monitor.height
            elif self.selected_screen < 0 or self.selected_screen >= len(screens):
                raise IndexError("Invalid screen index.")
            else:
                screen = sorted_screens[self.selected_screen]
                return screen.width, screen.height

        elif platform.system() == "Darwin":
            # macOS part using Quartz to get screen information
            max_displays = 32  # Maximum number of displays to handle
            active_displays = Quartz.CGGetActiveDisplayList(max_displays, None, None)[1]

            # Get the display bounds (resolution) for each active display
            screens = []
            for display_id in active_displays:
                bounds = Quartz.CGDisplayBounds(display_id)
                screens.append({
                    'id': display_id,
                    'x': int(bounds.origin.x),
                    'y': int(bounds.origin.y),
                    'width': int(bounds.size.width),
                    'height': int(bounds.size.height),
                    'is_primary': Quartz.CGDisplayIsMain(display_id)  # Check if this is the primary display
                })

            # Sort screens by x position to arrange from left to right
            sorted_screens = sorted(screens, key=lambda s: s['x'])

            if self.selected_screen is None:
                # Find the primary monitor
                primary_monitor = next((screen for screen in screens if screen['is_primary']), None)
                if primary_monitor:
                    return primary_monitor['width'], primary_monitor['height']
                else:
                    raise RuntimeError("No primary monitor found.")
            elif self.selected_screen < 0 or self.selected_screen >= len(screens):
                raise IndexError("Invalid screen index.")
            else:
                # Return the resolution of the selected screen
                screen = sorted_screens[self.selected_screen]
                return screen['width'], screen['height']

        else:  # Linux or other OS
            cmd = "xrandr | grep ' primary' | awk '{print $4}'"
            try:
                output = subprocess.check_output(cmd, shell=True).decode()
                resolution = output.strip().split()[0]
                width, height = map(int, resolution.split('x'))
                return width, height
            except subprocess.CalledProcessError:
                raise RuntimeError("Failed to get screen resolution on Linux.")
    
    def get_mouse_position(self):
        # TODO: enhance this func
        from AppKit import NSEvent
        from Quartz import CGEventSourceCreate, kCGEventSourceStateCombinedSessionState

        loc = NSEvent.mouseLocation()
        # Adjust for different coordinate system
        return int(loc.x), int(self.height - loc.y)



if __name__ == "__main__":
    computer = ComputerTool()
    # test left_click_windll
    # asyncio.run(computer(action="left_click_windll", coordinate=(500, 500)))
    asyncio.run(computer(action="mouse_move_windll", coordinate=(500, 500)))
    asyncio.run(computer(action="left_click_windll", coordinate=(500, 500)))