import string
import re


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
    rtrn_txt = str()
    max_row = len(txt.split("\n"))
    cnt_row = 0
    for row in txt.split("\n"):
        cnt = 0
        for item in row:
            if item in string.whitespace:
                rtrn_txt += item
            # first latter of the string capitalized.
            elif item in string.ascii_letters and cnt == 0:
                rtrn_txt += item.capitalize()
                cnt = 1
            elif cnt != 0:
                rtrn_txt += item.lower()
        cnt_row += 1
        if cnt_row < max_row:
            rtrn_txt += '\n'
    rtrn_txt = ". ".join((i[0].capitalize() + i[1:]) for i in rtrn_txt.split(". "))
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
        add_text(place_to_add, text_to_add, txt):
    Fuction description: 
        fuction add text to string object to the required place
    Params:
        place_to_add - it's a str formatting text. text_to_add would be added after place_to_add.
        text_to_add - it's a text for adding.
        txt - it's a str formatting text. This is the text to which the  text_to_add will be added.
    Return:
        proc_text - it's an string text with the added new text.
'''


def add_text(place_to_add, text_to_add, txt):
    # proc_text = txt[0:txt.find(place_to_add) + len(place_to_add)] + " " \
    #                 + text_to_add + txt[txt.find(place_to_add)+len(place_to_add):]
    proc_text = str()
    for paragraph in txt.split('\n'):
        if place_to_add in paragraph:
            proc_text += (paragraph + ' ' + text_to_add + '\n')
        else:
            proc_text += (paragraph + '\n')
    return proc_text


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
    proc_text = txt
    # proc_text = remove_empty_lines(proc_text)     # remove empty lines
    proc_text = remove_spaces(proc_text)          # remove useless spaces
    proc_text = register_normalize(proc_text)       # apply register correction
    proc_text = rplc(proc_text, ' iz ', ' is ')     # typo correction   OK
    proc_text = rplc(proc_text, ' tex.', ' text.')  # typo correction   OK
    proc_text = rplc(proc_text, ' tex ', ' text ')  # typo correction   OK

    return proc_text
