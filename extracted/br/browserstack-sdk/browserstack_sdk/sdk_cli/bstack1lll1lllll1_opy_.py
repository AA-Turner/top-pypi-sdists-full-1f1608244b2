# coding: UTF-8
import sys
bstack1l11_opy_ = sys.version_info [0] == 2
bstack111l1ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1ll_opy_ (bstack11111ll_opy_):
    global bstack1lll1l_opy_
    bstack1ll11_opy_ = ord (bstack11111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack11111ll_opy_ [:-1]
    bstack1l111l1_opy_ = bstack1ll11_opy_ % len (bstack1l1llll_opy_)
    bstack1l11ll_opy_ = bstack1l1llll_opy_ [:bstack1l111l1_opy_] + bstack1l1llll_opy_ [bstack1l111l1_opy_:]
    if bstack1l11_opy_:
        bstack111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack111l1ll_opy_ - (bstack1ll1l11_opy_ + bstack1ll11_opy_) % bstack11lll1l_opy_) for bstack1ll1l11_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack111l1_opy_ = str () .join ([chr (ord (char) - bstack111l1ll_opy_ - (bstack1ll1l11_opy_ + bstack1ll11_opy_) % bstack11lll1l_opy_) for bstack1ll1l11_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack111l1_opy_)
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1lll1l_opy_ import bstack1ll1llllll1_opy_
from browserstack_sdk.sdk_cli.bstack1lllllll1l1_opy_ import (
    bstack11111l11l1_opy_,
    bstack1llllll1lll_opy_,
    bstack1llllllllll_opy_,
)
from bstack_utils.helper import  bstack11ll11l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1ll1_opy_ import bstack1lll111l11l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1111l1l_opy_, bstack1lll1l11lll_opy_, bstack1lllll1l1ll_opy_, bstack1lll1l1ll1l_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack1l1ll11l1_opy_ import bstack1llll1l111_opy_
from browserstack_sdk.sdk_cli.bstack1ll1llll1ll_opy_ import bstack1lll1llllll_opy_
from bstack_utils.percy import bstack1l11l1llll_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1lll1l1l1ll_opy_(bstack1ll1llllll1_opy_):
    def __init__(self, bstack1l1ll11llll_opy_: Dict[str, str]):
        super().__init__()
        self.bstack1l1ll11llll_opy_ = bstack1l1ll11llll_opy_
        self.percy = bstack1l11l1llll_opy_()
        self.bstack1l1ll1l1ll_opy_ = bstack1llll1l111_opy_()
        self.bstack1l1ll11l1l1_opy_()
        bstack1lll111l11l_opy_.bstack1ll1l1l1ll1_opy_((bstack11111l11l1_opy_.bstack1111111ll1_opy_, bstack1llllll1lll_opy_.PRE), self.bstack1l1ll11l111_opy_)
        TestFramework.bstack1ll1l1l1ll1_opy_((bstack1lll1111l1l_opy_.TEST, bstack1lllll1l1ll_opy_.POST), self.bstack1ll11llllll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l1lll1l1l1_opy_(self, instance: bstack1llllllllll_opy_, driver: object):
        bstack1l1llllll1l_opy_ = TestFramework.bstack1lllllll1ll_opy_(instance.context)
        for t in bstack1l1llllll1l_opy_:
            bstack1ll111111ll_opy_ = TestFramework.bstack1111111lll_opy_(t, bstack1lll1llllll_opy_.bstack1l1lll1ll1l_opy_, [])
            if any(instance is d[1] for d in bstack1ll111111ll_opy_) or instance == driver:
                return t
    def bstack1l1ll11l111_opy_(
        self,
        f: bstack1lll111l11l_opy_,
        driver: object,
        exec: Tuple[bstack1llllllllll_opy_, str],
        bstack111111ll1l_opy_: Tuple[bstack11111l11l1_opy_, bstack1llllll1lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1lll111l11l_opy_.bstack1ll1l11l1ll_opy_(method_name):
                return
            platform_index = f.bstack1111111lll_opy_(instance, bstack1lll111l11l_opy_.bstack1ll1l1l111l_opy_, 0)
            bstack1l1lllllll1_opy_ = self.bstack1l1lll1l1l1_opy_(instance, driver)
            bstack1l1ll111l1l_opy_ = TestFramework.bstack1111111lll_opy_(bstack1l1lllllll1_opy_, TestFramework.bstack1l1ll111ll1_opy_, None)
            if not bstack1l1ll111l1l_opy_:
                self.logger.debug(bstack1ll_opy_ (u"ࠥࡳࡳࡥࡰࡳࡧࡢࡩࡽ࡫ࡣࡶࡶࡨ࠾ࠥࡸࡥࡵࡷࡵࡲ࡮ࡴࡧࠡࡣࡶࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥ࡯ࡳࠡࡰࡲࡸࠥࡿࡥࡵࠢࡶࡸࡦࡸࡴࡦࡦࠥ቎"))
                return
            driver_command = f.bstack1ll11llll11_opy_(*args)
            for command in bstack1l1111l1l_opy_:
                if command == driver_command:
                    self.bstack1l1ll1111l_opy_(driver, platform_index)
            bstack111l1l1l_opy_ = self.percy.bstack1l1l1111_opy_()
            if driver_command in bstack11lll11l_opy_[bstack111l1l1l_opy_]:
                self.bstack1l1ll1l1ll_opy_.bstack11lll1llll_opy_(bstack1l1ll111l1l_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack1ll_opy_ (u"ࠦࡴࡴ࡟ࡱࡴࡨࡣࡪࡾࡥࡤࡷࡷࡩ࠿ࠦࡥࡳࡴࡲࡶࠧ቏"), e)
    def bstack1ll11llllll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11lll_opy_,
        bstack111111ll1l_opy_: Tuple[bstack1lll1111l1l_opy_, bstack1lllll1l1ll_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack1ll1lll1l_opy_ import bstack1lll11l1lll_opy_
        bstack1ll111111ll_opy_ = f.bstack1111111lll_opy_(instance, bstack1lll1llllll_opy_.bstack1l1lll1ll1l_opy_, [])
        if not bstack1ll111111ll_opy_:
            self.logger.debug(bstack1ll_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢቐ") + str(kwargs) + bstack1ll_opy_ (u"ࠨࠢቑ"))
            return
        if len(bstack1ll111111ll_opy_) > 1:
            self.logger.debug(bstack1ll_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡽ࡯ࡩࡳ࠮ࡤࡳ࡫ࡹࡩࡷࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤቒ") + str(kwargs) + bstack1ll_opy_ (u"ࠣࠤቓ"))
        bstack1l1ll11lll1_opy_, bstack1l1ll11l1ll_opy_ = bstack1ll111111ll_opy_[0]
        driver = bstack1l1ll11lll1_opy_()
        if not driver:
            self.logger.debug(bstack1ll_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥቔ") + str(kwargs) + bstack1ll_opy_ (u"ࠥࠦቕ"))
            return
        bstack1l1ll11ll1l_opy_ = {
            TestFramework.bstack1ll1l1l11ll_opy_: bstack1ll_opy_ (u"ࠦࡹ࡫ࡳࡵࠢࡱࡥࡲ࡫ࠢቖ"),
            TestFramework.bstack1ll1l11111l_opy_: bstack1ll_opy_ (u"ࠧࡺࡥࡴࡶࠣࡹࡺ࡯ࡤࠣ቗"),
            TestFramework.bstack1l1ll111ll1_opy_: bstack1ll_opy_ (u"ࠨࡴࡦࡵࡷࠤࡷ࡫ࡲࡶࡰࠣࡲࡦࡳࡥࠣቘ")
        }
        bstack1l1ll11l11l_opy_ = { key: f.bstack1111111lll_opy_(instance, key) for key in bstack1l1ll11ll1l_opy_ }
        bstack1l1ll1111ll_opy_ = [key for key, value in bstack1l1ll11l11l_opy_.items() if not value]
        if bstack1l1ll1111ll_opy_:
            for key in bstack1l1ll1111ll_opy_:
                self.logger.debug(bstack1ll_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࠥ቙") + str(key) + bstack1ll_opy_ (u"ࠣࠤቚ"))
            return
        platform_index = f.bstack1111111lll_opy_(instance, bstack1lll111l11l_opy_.bstack1ll1l1l111l_opy_, 0)
        if self.bstack1l1ll11llll_opy_.percy_capture_mode == bstack1ll_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦቛ"):
            bstack11l1ll1l1_opy_ = bstack1l1ll11l11l_opy_.get(TestFramework.bstack1l1ll111ll1_opy_) + bstack1ll_opy_ (u"ࠥ࠱ࡹ࡫ࡳࡵࡥࡤࡷࡪࠨቜ")
            bstack1ll11lll1ll_opy_ = bstack1lll11l1lll_opy_.bstack1ll1ll11111_opy_(EVENTS.bstack1l1ll111l11_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack11l1ll1l1_opy_,
                bstack1l1l1lll1_opy_=bstack1l1ll11l11l_opy_[TestFramework.bstack1ll1l1l11ll_opy_],
                bstack1l111l1111_opy_=bstack1l1ll11l11l_opy_[TestFramework.bstack1ll1l11111l_opy_],
                bstack11l1l111_opy_=platform_index
            )
            bstack1lll11l1lll_opy_.end(EVENTS.bstack1l1ll111l11_opy_.value, bstack1ll11lll1ll_opy_+bstack1ll_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦቝ"), bstack1ll11lll1ll_opy_+bstack1ll_opy_ (u"ࠧࡀࡥ࡯ࡦࠥ቞"), True, None, None, None, None, test_name=bstack11l1ll1l1_opy_)
    def bstack1l1ll1111l_opy_(self, driver, platform_index):
        if self.bstack1l1ll1l1ll_opy_.bstack11l1llll11_opy_() is True or self.bstack1l1ll1l1ll_opy_.capturing() is True:
            return
        self.bstack1l1ll1l1ll_opy_.bstack11l11l1l11_opy_()
        while not self.bstack1l1ll1l1ll_opy_.bstack11l1llll11_opy_():
            bstack1l1ll111l1l_opy_ = self.bstack1l1ll1l1ll_opy_.bstack1lll1l1111_opy_()
            self.bstack1l1ll111l1_opy_(driver, bstack1l1ll111l1l_opy_, platform_index)
        self.bstack1l1ll1l1ll_opy_.bstack111lll1ll_opy_()
    def bstack1l1ll111l1_opy_(self, driver, bstack1l1111111_opy_, platform_index, test=None):
        from bstack_utils.bstack1ll1lll1l_opy_ import bstack1lll11l1lll_opy_
        bstack1ll11lll1ll_opy_ = bstack1lll11l1lll_opy_.bstack1ll1ll11111_opy_(EVENTS.bstack1111lll1l_opy_.value)
        if test != None:
            bstack1l1l1lll1_opy_ = getattr(test, bstack1ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ቟"), None)
            bstack1l111l1111_opy_ = getattr(test, bstack1ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬበ"), None)
            PercySDK.screenshot(driver, bstack1l1111111_opy_, bstack1l1l1lll1_opy_=bstack1l1l1lll1_opy_, bstack1l111l1111_opy_=bstack1l111l1111_opy_, bstack11l1l111_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack1l1111111_opy_)
        bstack1lll11l1lll_opy_.end(EVENTS.bstack1111lll1l_opy_.value, bstack1ll11lll1ll_opy_+bstack1ll_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣቡ"), bstack1ll11lll1ll_opy_+bstack1ll_opy_ (u"ࠤ࠽ࡩࡳࡪࠢቢ"), True, None, None, None, None, test_name=bstack1l1111111_opy_)
    def bstack1l1ll11l1l1_opy_(self):
        os.environ[bstack1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡉࡗࡉ࡙ࠨባ")] = str(self.bstack1l1ll11llll_opy_.success)
        os.environ[bstack1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࡡࡆࡅࡕ࡚ࡕࡓࡇࡢࡑࡔࡊࡅࠨቤ")] = str(self.bstack1l1ll11llll_opy_.percy_capture_mode)
        self.percy.bstack1l1ll11ll11_opy_(self.bstack1l1ll11llll_opy_.is_percy_auto_enabled)
        self.percy.bstack1l1ll111lll_opy_(self.bstack1l1ll11llll_opy_.percy_build_id)