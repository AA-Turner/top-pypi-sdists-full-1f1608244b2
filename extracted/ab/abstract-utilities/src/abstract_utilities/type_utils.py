"""
type_utils.py

This module provides a collection of utility functions for type checking and conversion.
It includes functions to determine the type of an object, check if an object is a specific type,
and perform type conversions. These functions help simplify the process of handling different
types of data and ensure consistent behavior across different data types.

Usage:
    import abstract_utilities.type_utils as type_utils

Functions:
- is_iterable(obj: any) -> bool
- is_number(obj: any) -> bool
- is_str(obj: any) -> bool
- is_int(obj: any) -> bool
- is_float(obj: any) -> bool
- is_bool(obj: any) -> bool
- is_list(obj: any) -> bool
- is_tuple(obj: any) -> bool
- is_set(obj: any) -> bool
- is_dict(obj: any) -> bool
- is_frozenset(obj: any) -> bool
- is_bytearray(obj: any) -> bool
- is_bytes(obj: any) -> bool
- is_memoryview(obj: any) -> bool
- is_range(obj: any) -> bool
- is_enumerate(obj: any) -> bool
- is_zip(obj: any) -> bool
- is_filter(obj: any) -> bool
- is_map(obj: any) -> bool
- is_property(obj: any) -> bool
- is_slice(obj: any) -> bool
- is_super(obj: any) -> bool
- is_type(obj: any) -> bool
- is_Exception(obj: any) -> bool
- is_none(obj: any) -> bool
- is_str_convertible_dict(obj: any) -> bool
- is_dict_or_convertable(obj: any) -> bool
- dict_check_conversion(obj: any) -> Union[dict, any]
- make_list(obj: any) -> list
- make_list_lower(ls: list) -> list
- make_float(obj: Union[str, float, int]) -> float
- make_bool(obj: Union[bool, int, str]) -> Union[bool, str]
- make_str(obj: any) -> str
- get_obj_obj(obj_type: str, obj: any) -> any
- get_len_or_num(obj: any) -> int
- get_types_list() -> list
- det_bool_F(obj: (tuple or list or bool) = False) -> bool
- det_bool_T(obj: (tuple or list or bool) = False) -> bool
- T_or_F_obj_eq(event: any = '', obj: any = '') -> bool

This module is part of the `abstract_utilities` package.

Author: putkoff
Date: 05/31/2023
Version: 0.1.2
"""
import os
from typing import Union
from .path_utils import get_all_item_paths,get_files
from .list_utils import make_list
MIME_TYPES_JS = media_types = {
        'image': {
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.png': 'image/png',
            '.gif': 'image/gif',
            '.bmp': 'image/bmp',
            '.tiff': 'image/tiff',
            '.webp': 'image/webp',
            '.svg': 'image/svg+xml'
        },
        'video': {
            '.mp4': 'video/mp4',
            '.avi': 'video/x-msvideo',
            '.mov': 'video/quicktime',
            '.wmv': 'video/x-ms-wmv',
            '.flv': 'video/x-flv',
            '.mkv': 'video/x-matroska',
            '.webm': 'video/webm'
        },
        'audio': {
            '.mp3': 'audio/mpeg',
            '.wav': 'audio/wav',
            '.ogg': 'audio/ogg',
            '.flac': 'audio/flac',
            '.aac': 'audio/x-aac',
            '.m4a': 'audio/mp4'
        },
        'document': {
            '.pdf': 'application/pdf',
            '.doc': 'application/msword',
            '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            '.txt': 'text/plain',
            '.rtf': 'application/rtf'
        },
        'presentation': {
            '.ppt': 'application/vnd.ms-powerpoint',
            '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
        },
        'spreadsheet': {
            '.xls': 'application/vnd.ms-excel',
            '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            '.csv': 'text/csv'
        }
    }
MEDIA_TYPES = {
            'image': {'.svg', '.bmp', '.tiff', '.jpg', '.png', '.webp', '.gif', '.jpeg'},
            'video': {'.mp4', '.webm', '.avi', '.wmv', '.flv', '.mov', '.mkv'},
            'audio': {'.flac', '.ogg', '.wav', '.m4a', '.aac', '.mp3'},
            'document': {'.rtf', '.txt', '.doc', '.pdf', '.docx'},
            'presentation': {'.pptx', '.ppt'},
            'spreadsheet': {'.xls', '.xlsx', '.csv'}
        }
def get_all_key_values(keys=None,dict_obj=None):
    keys = keys or []
    dict_obj = dict_obj or {}
    new_dict_obj = {}
    for key in keys:
        values = dict_obj.get(key)
        if values:
            new_dict_obj[key]=values
    return new_dict_obj
def get_all_key_values(keys=None,dict_obj=None):
    keys = keys or []
    dict_obj = dict_obj or {}
    new_dict_obj = {}
    for key in keys:
        values = dict_obj.get(key)
        if values:
            new_dict_obj[key]=values
    return new_dict_obj

def get_media_types(types=None):
    types = make_list(types or [])
    media_types = MEDIA_TYPES
    if types:
        media_types = get_all_key_values(keys=types,dict_obj=MEDIA_TYPES)
    return media_types
def get_media_exts(types=None):
    all_exts = []
    types = make_list(types or [])
    for typ in types:
        exts = MEDIA_TYPES.get(str(typ)) or []
        if exts:
            all_exts+=list(exts)
    return all_exts
def confirm_type(file_path=None,media_types=None,ext=None):
    media_types = media_types or get_media_types('video')
    ext = ext or os.path.splitext(file_path)[-1]
    for typ,exts in media_types.items():
        if ext in exts:
             return typ
def is_media_type(file_path,media_types=None,ext=None):
    media_types = make_list(media_types or [])
    ext = ext or os.path.splitext(file_path)[-1]
    media_types_js = get_media_types()
    for media_type in media_types:
        exts = media_types_js.get(media_type)
        if exts and ext in exts:
            return True
    return False
def get_mime_type(file_path):
    ext = os.path.splitext(file_path)[-1]
    media = confirm_type(file_path=file_path,ext=ext)
    mime_type = MIME_TYPES_JS.get(media,{}).get(ext) or 'application/octet-stream'
    return mime_type
def get_all_types(types=None,directory=None):
    if not directory or not os.path.isdir(directory):
        return []
    item_paths = get_all_item_paths(directory)
    media_types = get_media_types(types=types)
    item_paths = [item_path for item_path in item_paths if confirm_type(item_path,media_types=media_types)]
    return item_paths
def get_all_file_types(types=None,directory=None):
    if not directory or not os.path.isdir(directory):
        return []
    item_paths = get_files(directory)
    media_types = get_media_types(types=types)
    item_paths = [item_path for item_path in item_paths if confirm_type(item_path,media_types=media_types)]
    return item_paths

def is_iterable(obj:any):
    try:
        iterator=iter(obj)
    except TypeError:
        return False
    else:
        return True
    return True

def get_type(obj:any) -> any:
    """
    Determines the type of the input object.

    Args:
        obj: The object to determine the type of.

    Returns:
        any: The object with the updated type.
    """
    if is_number(obj):
        obj = int(obj)
    if is_float(obj):
        return float(obj)
    elif obj == 'None':
        obj = None
    elif is_str(obj):
        obj = str(obj)
    return obj

def is_number(obj:any) -> bool:
    """
    Checks whether the input object can be represented as a number.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object can be represented as a number, False otherwise.
    """
    try:
        float(obj)
        return True
    except (TypeError, ValueError):
        return False
def is_object(obj:any) -> bool:
    """
    Checks whether the input object is of type 'object'.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'object', False otherwise.
    """
    return isinstance(obj, object)
def is_str(obj:any) -> bool:
    """
    Checks whether the input object is of type 'str'.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'str', False otherwise.
    """
    return isinstance(obj, str)
def is_int(obj:any) -> bool:
    """
    Checks whether the input object is of type 'int'.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'int', False otherwise.
    """
    return isinstance(obj, int)
def is_float(obj:any) -> bool:
    """
    Checks whether the input object is of type 'float'.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'float', False otherwise.
    """
    return isinstance(obj, float)
def is_bool(obj:any) -> bool:
    """
    Checks whether the input object is of type 'bool'.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'bool', False otherwise.
    """
    return isinstance(obj, bool)


def is_list(obj:any) -> bool:
    """
    Checks whether the input object is of type 'list'.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'list', False otherwise.
    """
    return isinstance(obj, list)
def is_tuple(obj:any) -> bool:
    """
    Checks whether the input object is of type 'tuple'.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'tuple', False otherwise.
    """
    return isinstance(obj, tuple)
def is_set(obj:any) -> bool:
    """
    Checks whether the input object is of type 'set'.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'set', False otherwise.
    """
    return isinstance(obj, set)
def is_dict(obj:any) -> bool:
    """
    Checks whether the input object is of type 'dict'.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'dict', False otherwise.
    """
    return isinstance(obj, dict)
def is_frozenset(obj:any) -> bool:
    """
    Checks whether the input object is of type 'frozenset'.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'frozenset', False otherwise.
    """
    return isinstance(obj, frozenset)
def is_bytearray(obj:any) -> bool:
    """
    Checks whether the input object is of type 'bytearray'.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'bytearray', False otherwise.
    """
    return isinstance(obj, bytearray)
def is_bytes(obj:any) -> bool:
    """
    Checks whether the input object is of type 'bytes'.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'bytes', False otherwise.
    """
    return isinstance(obj, bytes)
def is_memoryview(obj:any) -> bool:
    """
    Checks whether the input object is of type 'memoryview'.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'memoryview', False otherwise.
    """
    return isinstance(obj, memoryview)
def is_range(obj:any) -> bool:
    """
    Checks whether the input object is

 of type 'range'.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'range', False otherwise.
    """
    return isinstance(obj, range)
def is_enumerate(obj:any) -> bool:
    """
    Checks whether the input object is of type 'enumerate'.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'enumerate', False otherwise.
    """
    return isinstance(obj, enumerate)
def is_zip(obj:any) -> bool:
    """
    Checks whether the input object is of type 'zip'.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'zip', False otherwise.
    """
    return isinstance(obj, zip)
def is_filter(obj:any) -> bool:
    """
    Checks whether the input object is of type 'filter'.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'filter', False otherwise.
    """
    return isinstance(obj, filter)
def is_map(obj:any) -> bool:
    """
    Checks whether the input object is of type 'map'.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'map', False otherwise.
    """
    return isinstance(obj, map)
def is_property(obj:any) -> bool:
    """
    Checks whether the input object is of type 'property'.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'property', False otherwise.
    """
    return isinstance(obj, property)


def is_slice(obj:any) -> bool:
    """
    Checks whether the input object is of type 'slice'.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'slice', False otherwise.
    """
    return isinstance(obj, slice)


def is_super(obj:any) -> bool:
    """
    Checks whether the input object is of type 'super'.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'super', False otherwise.
    """
    return isinstance(obj, super)


def is_type(obj:any) -> bool:
    """
    Checks whether the input object is of type 'type'.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'type', False otherwise.
    """
    return isinstance(obj, type)


def is_Exception(obj:any) -> bool:
    """
    Checks whether the input object is of type 'Exception'.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'Exception', False otherwise.
    """
    return isinstance(obj, Exception)


def is_none(obj:any) -> bool:
    """
    Checks whether the input object is of type 'None'.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'None', False otherwise.
    """
    if type(obj) is None:
        return True
    else:
        return False



def is_dict_or_convertable(obj:any) -> bool:
    """
    Checks whether the input object is of type 'dict' or can be converted to a dictionary.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is of type 'dict' or can be converted to a dictionary, False otherwise.
    """
    if is_dict(obj):
        return True
    if is_str_convertible_dict(obj):
        return True
    return False
def is_str_convertible_dict(obj:any) -> bool:
    """
    Checks whether the input object is a string that can be converted to a dict.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object can be converted to a dict, False otherwise.
    """
    import json

    if isinstance(obj, str):
        try:
            json.loads(obj)
            return True
        except json.JSONDecodeError:
            return False

    return False

def dict_check_conversion(obj:any) -> Union[dict,any]:
    """
    Converts the input object to a dictionary if possible.

    Args:
        obj: The object to convert.

    Returns:
        The object converted to a dictionary if possible, otherwise the original object.
    """
    import json

    if is_dict_or_convertable(obj):
        if is_dict(obj):
            return obj
        return json.loads(obj)
    
    return obj

    
def make_list_lower(ls: list) -> list:
    """
    Converts all elements in a list to lowercase. Ignores None values.
    
    Args:
        ls: The list to convert.
        
    Returns:
        list: The list with all strings converted to lowercase.
    """
    return [item.lower() if isinstance(item, str) else item for item in ls]


def make_float(obj:Union[str,float,int]) -> float:
    """
    Converts the input object to a float.
    
    Args:
        x: The object to convert.
        
    Returns:
        float: The float representation of the object.
    """
    try:
        return float(obj)
    except (TypeError, ValueError):
        return 1.0

def make_bool(obj: Union[bool, int, str]) -> Union[bool, str]:
    """
    Converts the input object to a boolean representation if possible.

    The function attempts to convert various objects, including integers and strings, to their boolean equivalents. 
    If the conversion is not possible, the original object is returned.

    Args:
        obj: The object to be converted.

    Returns:
        bool or original type: The boolean representation of the object if conversion is possible. Otherwise, it returns the original object.

    Examples:
        make_bool("true") -> True
        make_bool(1)      -> True
        make_bool("0")    -> False
        make_bool(2)      -> 2
    """
    if isinstance(obj, bool):
        return obj
    if isinstance(obj, int):
        if obj == 0:
            return False
        if obj == 1:
            return True
    if isinstance(obj, str):
        if obj.lower() in ['0', "false"]:
            return False
        if obj.lower() in ['1', "true"]:
            return True
    return obj

def make_str(obj: any) -> str:
    """
    Converts the input object to a string.
    
    Args:
        obj: The object to convert.
        
    Returns:
        str: The string representation of the object.
    """
    return str(obj)


def get_obj_obj(obj_type: str, obj: any) -> any:
    """
    Returns the object converted according to the given type string.
    
    Args:
        obj_type: The string representing the type to convert to.
        obj: The object to convert.
        
    Returns:
        any: The object converted to the specified type.
    """
    if obj_type == 'str':
        return make_str(obj)
    elif obj_type == 'bool':
        return make_bool(obj)
    elif obj_type == 'float':
        return make_float(obj)
    elif obj_type == 'int':
        try:
            return int(obj)
        except (TypeError, ValueError):
            return obj
    else:
        return obj
def get_len_or_num(obj: any) -> int:
    """
    Returns the length of the object if it can be converted to a string, else the integer representation of the object.
    
    Args:
        obj: The object to process.
        
    Returns:
        int: The length of the object as a string or the integer representation of the object.
    """
    if is_int(obj) or is_float(obj):
        return int(obj)
    else:
        try:
            return len(str(obj))
        except (TypeError, ValueError):
            return 0
def get_types_list()->list:
    return ['list', 'bool', 'str', 'int', 'float', 'set', 'dict', 'frozenset', 'bytearray', 'bytes', 'memoryview', 'range', 'enumerate', 'zip', 'filter', 'map', 'property', 'slice', 'super', 'type', 'Exception', 'NoneType']
def det_bool_F(obj: (tuple or list or bool) = False):
    """
    Determines if the given object is a boolean False value.

    Args:
        obj (tuple or list or bool): The object to determine the boolean False value.

    Returns:
        bool: True if the object is a boolean False value, False otherwise.
    """
    if isinstance(obj, bool):
        return obj
    return all(obj)
def det_bool_T(obj: (tuple or list or bool) = False):
    """
    Determines if the given object is a boolean True value.

    Args:
        obj (tuple or list or bool): The object to determine the boolean True value.

    Returns:
        bool: True if the object is a boolean True value, False otherwise.
    """
    if isinstance(obj, bool):
        return obj 
    return any(obj)
def T_or_F_obj_eq(event: any = '', obj: any = ''):
    """
    Compares two objects and returns True if they are equal, False otherwise.

    Args:
        event (any): The first object to compare.
        obj (any): The second object to compare.

    Returns:
        bool: True if the objects are equal, False otherwise.
    """
    return True if event == obj else False
def ensure_integer(page_value:any, default_value:int):
    """
    Ensures the given value is an integer. If not, it tries to extract 
    the numeric part of the value. If still unsuccessful, it defaults 
    to the given default value.

    Parameters:
    - page_value (str|int|any): The value to ensure as integer. 
                                Non-numeric characters are stripped if necessary.
    - default_value (int): The default value to return if conversion 
                           to integer is unsuccessful.

    Returns:
    - int: The ensured integer value.
    """
    # Check if page_value is already a number
    if not is_number(page_value):
        # Convert to string in case it's not already
        page_value = str(page_value)
        
        # Remove non-numeric characters from the beginning
        while len(page_value) > 0 and page_value[0] not in '0123456789'.split(','):
            page_value = page_value[1:]

        # Remove non-numeric characters from the end
        while len(page_value) > 0 and page_value[-1] not in '0123456789'.split(','):
            page_value = page_value[:-1]

    # If page_value is empty or still not a number, use the default value
    if len(page_value) == 0 or not is_number(page_value):
        return default_value

    # Convert page_value to an integer and return
    return int(page_value)
def if_default_return_obj(obj:any,default:any=None,default_compare:any=None):
    if default == default_compare:
        return obj
    return default


            
def convert_to_number(value):
    value_str = str(value)
    if is_number(value_str):
        return float(value_str) if '.' in value_str else int(value_str)
    return value_str
def is_number(s):
    if s:
        try:
            float(s)
            return True
        except:
            return False
    return False

def makeInt(obj):
    if is_number(obj):
       return int(obj)
    return obj

def str_lower(obj):
    try:
        obj=str(obj).lower()
    except Exception as e:
        print(f"{e}")
    return obj

def get_bool_response(bool_response,json_data):
    if not isinstance(bool_response,bool):
        try:
            bool_response = json_data.get(bool_response) in [None,'',[],"",{}]
        except:
            pass       
    return bool_response
def if_true_get_string(data, key):
    return key if data.get(key) else None
def find_for_string(string, parts):
    return [part for part in parts if string.lower() in str(part).lower()]


def is_strings_in_string(strings, parts):
    strings = make_list(strings)
    for string in strings:
        parts = find_for_string(string, parts)
        if not parts:
            return []
    return parts
# Function: is_number
# Function: is_str
# Function: is_int
# Function: get_type
# Function: is_float
# Function: is_object
# Function: is_bool
# Function: is_list
# Function: is_tuple
# Function: is_set
# Function: is_dict
# Function: is_frozenset
# Function: is_bytearray
# Function: is_bytes
# Function: is_memoryview
# Function: is_range
# Function: is_enumerate
# Function: is_zip
# Function: is_filter
# Function: is_map
# Function: is_property
# Function: is_slice
# Function: is_super
# Function: is_type
# Function: is_Exception
# Function: is_none
# Function: is_str_convertible_dict
# Function: is_dict_or_convertable
# Function: dict_check_conversion
# Function: make_list
# Function: make_list_lower
# Function: make_float
# Function: make_bool
# Function: make_str
# Function: get_obj_obj
# Function: get_len_or_num
# Function: get_types_list
