import string

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
    Fuction description: 
        convert all text to lowercase, then raises letter to 
        uppercase everywhere after ". ".
    Params:
            txt - it's a str formatting text.
    Return:
            rtrn_txt - register normalized text in str format.
'''
def register_normalize(txt):
    rtrn_txt = ". ".join(i.capitalize() for i in txt.lower().split(". "))
    return rtrn_txt


'''
    Function name: 
        remove_empty_lines(txt)
    Fuction description: 
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
    Fuction description: 
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
        create_sentence(txt)
    Fuction description: 
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
    Fuction description: 
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
    Fuction description: 
        this func used for execute another functions.
    Params:
            txt - it's a str formatting text.
    Return:
            proc_text - ready-to-use fully formatted text in str format.
'''
def text_formatting(txt):
    proc_text = remove_empty_lines(txt)             # remove empty lines
    proc_text = register_normalize(proc_text)       # apply register correction
    proc_text = rplc(proc_text, ' iz ', ' is ')     # typo correction
    proc_text = rplc(proc_text, ' tex.', ' text.')  # typo correction
    proc_text = rplc(proc_text, ' tex ', ' text ')  # typo correction
    proc_text = proc_text + ' ' * 2 + rplc(create_sentence(proc_text).lower(), ' .', '.')  # add required sentence
    return proc_text


print(text_formatting(text))
# count of white spaces after applying changes into input text.
print(f'Count of spaces is: {space_calc(text_formatting(text))}')
