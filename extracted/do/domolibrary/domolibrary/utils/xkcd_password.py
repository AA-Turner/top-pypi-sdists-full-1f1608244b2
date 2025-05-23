# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/utils/xkcd_pass.ipynb.

# %% auto 0
__all__ = ['LEET', 'PADDING', 'add_leet_to_string', 'add_padding_characters_fn', 'process_add_leet', 'process_pad_suffix_fn',
           'process_random_capitalization_fn', 'process_first_capitalization_fn',
           'process_caps_first_word_add_year_and_add_suffix', 'generate_xkcd_password', 'generate_domo_password',
           'process_domo_password_fn']

# %% ../../nbs/utils/xkcd_pass.ipynb 3
from xkcdpass import xkcd_password as xp
import random
from typing import Callable
import datetime as dt
import nbdev

# %% ../../nbs/utils/xkcd_pass.ipynb 4
LEET = {'a':'@','i':'!','A':'@','I':'!', 'e':'3', 'E': '3'}

def add_leet_to_string(text, leet):
        return "".join(leet.get(k,k) for k in text)

# %% ../../nbs/utils/xkcd_pass.ipynb 6
PADDING = '.!?'

def add_padding_characters_fn(text,
                              padding,
                              n : int = 1, #num padding characters to add 
                             ):
    
    text+= "".join(random.choices(padding, k=n))
    return text


# %% ../../nbs/utils/xkcd_pass.ipynb 9
def process_add_leet(my_pass, **kwarags):
    leet = LEET
    keep_loop = False

    if not any((l for l in my_pass if l in leet.keys())):
        keep_loop = True
        return my_pass , keep_loop        
    
        
    my_pass = add_leet_to_string(my_pass, leet = leet) 
    return my_pass, keep_loop


def process_pad_suffix_fn(my_pass):
    return add_padding_characters_fn(my_pass, padding = PADDING, n = 1), False


def process_random_capitalization_fn(text, delimiter, **kwargs):
    if delimiter not in text:
        return text, False

    word_ls = text.split(delimiter)

    word_ls = [random.choice((str.upper, str.lower))(word) for word in word_ls]

    return delimiter.join(word_ls), False


def process_first_capitalization_fn(text, delimiter, **kwargs):
    if delimiter not in text:
        return text, False

    word_ls = text.split(delimiter)

    word_ls = [
        word.upper() if idx == 0 else word.lower() for idx, word in enumerate(word_ls)
    ]

    return delimiter.join(word_ls), False

def process_caps_first_word_add_year_and_add_suffix(my_pass, delimiter, **kwargs):
    word_ls = my_pass.split(delimiter)
    word_ls[0] = word_ls[0].upper() 
    my_pass = delimiter.join(word_ls)
    
    my_pass += dt.date.today().strftime( '%Y')
    my_pass, keep_loop = process_pad_suffix_fn(my_pass)
    
    return my_pass, keep_loop

def generate_xkcd_password(min_word_length = 5, max_word_length = 6, valid_chars = '[a-z]', delimiter = "-"):
    wordfile = xp.locate_wordfile()
    mywords = xp.generate_wordlist(wordfile=wordfile, min_length=min_word_length, max_length=max_word_length, valid_chars=valid_chars)
    return xp.generate_xkcdpassword(mywords, numwords = 3, delimiter = delimiter)


# %% ../../nbs/utils/xkcd_pass.ipynb 11
def generate_domo_password(delimiter = '-', 
                           process_fn : Callable = process_caps_first_word_add_year_and_add_suffix):
    keep_loop = True
    
    while keep_loop == True:
        keep_loop = False
        my_pass = generate_xkcd_password(min_word_length = 5, max_word_length = 6, valid_chars = '[a-z]', delimiter = delimiter)

        if process_fn:
            my_pass, keep_loop = process_fn(my_pass = my_pass, delimiter = delimiter) 
            
        return my_pass

# %% ../../nbs/utils/xkcd_pass.ipynb 14
def process_domo_password_fn(my_pass, delimiter):
    my_pass, keep_loop = process_first_capitalization_fn(my_pass, delimiter)
    my_pass += dt.date.today().strftime("%Y")
    my_pass, keep_loop = process_pad_suffix_fn(my_pass)

    return my_pass, keep_loop


def generate_domo_password(delimiter="-", 
                           process_fn: Callable = None # defaults to process_domo_password_fn
                           ):

    process_fn = process_fn or process_domo_password_fn

    wordfile = xp.locate_wordfile()
    mywords = xp.generate_wordlist(
        wordfile=wordfile, min_length=5, max_length=6, valid_chars="[a-z]"
    )

    my_pass = None
    keep_loop = True

    while keep_loop == True:
        my_pass = xp.generate_xkcdpassword(mywords, numwords=3, delimiter=delimiter)
        keep_loop = False

        if process_fn:
            my_pass, keep_loop = process_fn(my_pass=my_pass, delimiter=delimiter)

        return my_pass
