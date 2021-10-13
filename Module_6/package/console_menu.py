# ----------------------- MANUAL INPUT FUNCTIONS -----------------------
def note_text():
    return input("Please input message text:\n> ").capitalize()


def note_city():
    return input("Please input message city:\n> ").capitalize()


def note_date():
    return input("Please input message date(example '31/10/2021':\n> ")


def note_degrees():
    return input("Please input degrees:\n> ").capitalize()


# ----------------------- OTHER MESSAGES -----------------------
def welcome_message():
    return 'please choose input type:\n' \
                       ' input "1" if manual\n' \
                       ' input "2" if using import from file\n' \
                       ' input "0" if you want to stop'


def manual_input():
    return 'please, choose the note type:\n' \
                   ' input "1" if news\n' \
                   ' input "2" if private ad\n' \
                   ' input "3" if weather\n' \
                   ' input "0" if you want to stop'


def import_input():
    return 'please, choose the import  file format:\n' \
                   ' input "1" from custom format\n' \
                   ' input "2" from csv format\n' \
                   ' input "3" from json format\n' \
                   ' input "4" from xml format\n' \
                   ' input "0" if you want to stop'


def creation_confirm_message(flag):
    return f'Message with type {flag} was created.'


def continue_massage():
    return int(input('Do you wish continue to add news?\n print "1" if yes\n print "0" if no.\n> '))


def goodbye_message():
    return "Have a good day!"


def input_file_path():
    return str(input("Please, specify the file path\n> "))


# ----------------------- ERROR MESSAGES -----------------------
def error_unavailable_now():
    return "Will be available soon. Please choose another file format"


def error_not_valid_flag(flag):
    return f'"{flag}" is not valid value. Please, try again'


def error_import_type():
    return 'Not valid import type.'


def error_date_type():
    return 'Not valid data type, please try again.'
