import random
import string
import re


'''
1.CREATE S LIST OF RANDOM NUMBER OF DICT (FROM 2 TO 10)
'''


'''
    Function name: 
        dict_count(first, last):
    Fuction description: 
        generate random number from first to last.
    Params:
            first - it's an int value. First possible generated value.
            last - it's an int value. Last possible generated value.
    Return:
            dct_count - it's an random int value from first to last.
'''


def dict_count(first, last):
    dct_count = random.randrange(first, last + 1)
    return dct_count


'''
    Function name: 
        gen_dict_list(first, last)
    Function description: 
        generate random number of dicts and input it into one list.
    Params:
            first - it's a param that used for func:  dict_count(first, last), min count of dictionaries in list.
            last - it's a param that used for func:  dict_count(first, last), max count of dictionaries in list.
    Return:
            dict_list - it's a list of dict with the len = dict_count(first, last). max len of each dict = 26.
'''


def gen_dict_list(first, last):
    dict_list = []
    lst = dict_count(first, last)
    for dct in range(1, lst):
        dictionary = {}
        dict_len = random.randrange(len(string.ascii_lowercase))
        for i in range(1, dict_len + 1):
            key = random.choice(string.ascii_lowercase)
            value = random.randrange(0, 101)
            while key in dictionary:
                key = random.choice(string.ascii_lowercase)
            dictionary[key] = value
        # update dict_list with new dictionary
        dict_list.append(dictionary)
    return dict_list


'''
    2. GET PREVIOUSLY GENERATED LIST OF DICTS AND CREATE ONE COMMON DICT
'''

'''
    Function name: 
        split_dict_from_list(dict_list)
    Function description: 
        Split list of dicts to one dict.
    Params:
        dict_list - it's a list of dictionary.
    Return:
        result_dict - it's dict generated from input list of dicts.
'''


def split_dict_from_list(dict_list):
    # create set of keys
    all_keys = set().union(*(d.keys() for d in dict_list))
    result_dict = {}
    # keys iteration
    for key in all_keys:
        max_value = 0
        key_index = 0
        update = 0  # kostyl
        # dict iterate
        for dct in range(0, len(dict_list)):
            # keys and values iteration
            for k, v in dict_list[dct].items():
                if k == key:
                    update += 1
                    if v >= max_value:
                        key_index = dct + 1
                        max_value = v
        if update == 1:
            result_dict.update({str(key): max_value})
        elif update > 1:
            result_dict.update({str(key) + '_' + str(key_index): max_value})
    return result_dict


# create a variable with the text from hometask.
text = '''homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''

'''
    Function name: 
        register_normalize(txt)
    Function description: 
        convert all text to lowercase, then raises letter to 
        uppercase everywhere after ". ".
    Params:
            txt - it's a str formatting text.
    Return:
            rtrn_txt - register normalized text in str format.
'''


def register_normalize(txt):
    rtrn_txt = ". ".join(i.capitalize() for i in txt.lower().split(". "))
    rtrn_txt = "\n ".join(i.capitalize() for i in rtrn_txt.split("\n "))
    return rtrn_txt


'''
    Function name: 
        remove_empty_lines(txt)
    Function description: 
        this function remove empty lines from string object
    Params:
            txt - it's a str formatting text.
    Return:
            string_without_empty_lines - string text without empty lines.
'''


def remove_empty_lines(txt):
    lines = txt.split("\n")
    non_empty_lines = [line for line in lines if line.strip() != ""]
    string_without_empty_lines = ""
    for line in non_empty_lines:
        string_without_empty_lines += line + "\n"
    return string_without_empty_lines


'''
    Function name: 
        rplc(txt, old, new)
    Function description: 
        replace one str value to another.
    Params:
            txt - it's a str formatting text.
    Return:
            txt - string formatting text with changes applied.
'''


def rplc(txt, old, new):
    txt = txt.replace(f'{old}', f'{new}')
    return txt


'''
    Function name: 
        remove_spaces(txt)
    Function description: 
        remove more than 1 space between words
    Params:
            txt - it's a str formatting text.
    Return:
            txt - string formatting text with changes applied.
'''


def remove_spaces(txt):
    txt = re.sub(" +", " ", txt)
    return txt


'''
    Function name: 
        create_sentence(txt)
    Function description: 
        fuction create sentence, that consists from the 
        last word of each sentance of the input text.
    Params:
        txt - it's a str formatting text.
    Return:
        new_row - string formatting sentence consists from 
                  last word of each sentance of the input text.
'''


def create_sentence(txt):  # grubaya sila
    add_word = str()
    new_row = str()
    for i in txt:
        if i == '.':
            new_row += f'{add_word} '
            add_word = ''
        elif i in (',', ';', ':', ' '):
            add_word = ''
        else:
            add_word += i
    return new_row.capitalize() + '.'


'''
    Function name: 
        space_calc(txt)
    Function description: 
        fuction calculate sum of spaces and line breaks.
    Params:
        txt - it's a str formatting text.
    Return:
        count_of_spaces - it's an integer value (sum of of spaces and line breaks)
'''


def space_calc(txt):
    count_of_spaces = len([1 for i in txt if i in string.whitespace])
    return count_of_spaces


'''
    Function name: 
        text_formatting(txt):
    Function description: 
        this func used for execute another functions.
    Params:
            txt - it's a str formatting text.
    Return:
            proc_text - ready-to-use fully formatted text in str format.
'''


def text_formatting(txt):
    proc_text = remove_empty_lines(txt)  # remove empty lines
    proc_text = remove_spaces(proc_text)  # remove useless spaces
    proc_text = register_normalize(proc_text)  # apply register correction
    proc_text = rplc(proc_text, ' iz ', ' is ')  # typo correction
    proc_text = rplc(proc_text, ' tex.', ' text.')  # typo correction
    proc_text = rplc(proc_text, ' tex ', ' text ')  # typo correction
    proc_text = proc_text + ' ' + rplc(create_sentence(proc_text).lower(), ' .',
                                       '.').capitalize()  # add required sentence
    return proc_text


list_of_dicts = gen_dict_list(2, 10)
print(list_of_dicts)
print(split_dict_from_list(list_of_dicts))
print(text_formatting(text))
print(f'Count of spaces in formatted text is: {space_calc(text_formatting(text))}')
print(f'Count of spaces in input text is: {space_calc(text)}')
