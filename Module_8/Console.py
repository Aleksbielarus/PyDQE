from datetime import date
from datetime import datetime
from package import console_menu, insert_note, text_transform_module
from tests import test_module
# import os
import json


class Note:
    datetime = datetime.now().strftime('%d/%m/%Y %H.%M')
    note_date = date.today().strftime('%d/%m/%Y')

    def __init__(self, flag, note_text):
        self.flag = flag
        self.note_text = note_text

    def print_type(self):
        return self.flag

    def print_note_text(self):
        return self.note_text

    def print_date(self):
        return self.note_date

    def print_datetime(self):
        return self.datetime


class News(Note):
    def __init__(self, flag, note_text, city):
        Note.__init__(self, flag=flag, note_text=note_text)
        self.city = city

    def print_city(self):
        return self.city


class PrivateAd(Note):
    def __init__(self, flag, note_text, note_date):
        Note.__init__(self, flag=flag, note_text=note_text)
        self.note_date = note_date

    def print_news_text(self):
        return self.note_text

    def print_days_left(self):
        return (datetime.strptime(self.note_date, '%d/%m/%Y') - datetime.now()).days


class Weather(Note):
    def __init__(self, flag, note_text, city, note_date, degrees):
        Note.__init__(self, flag=flag, note_text=note_text)
        self.note_date = note_date
        self.degrees = degrees
        self.city = city

    def print_degrees(self):
        return self.degrees

    def print_city(self):
        return self.city


def news(flag):
    note_text = text_transform_module.text_formatting(console_menu.note_text())
    note_city = text_transform_module.text_formatting(console_menu.note_city())
    new_note = News('News', note_text, note_city)
    insert_row = insert_note.insert_news_note(new_note)
    add_new_note(insert_row)
    print(console_menu.creation_confirm_message(flag))


def private_ad(flag):
    note_text = text_transform_module.text_formatting(console_menu.note_text())
    note_date = console_menu.note_date()
    new_note = PrivateAd('Private Ad', note_text, note_date)
    insert_row = insert_note.insert_private_note(new_note)
    add_new_note(insert_row)
    print(console_menu.creation_confirm_message(flag))


def weather(flag):
    note_text = text_transform_module.text_formatting(console_menu.note_text())
    note_city = text_transform_module.text_formatting(console_menu.note_city())
    note_degrees = console_menu.note_degrees()
    note_date = console_menu.note_date()
    new_note = Weather('Weather', note_text, note_city, note_date, note_degrees)
    insert_row = insert_note.insert_news_note(new_note)
    add_new_note(insert_row)
    print(console_menu.creation_confirm_message(flag))


# add new note to text file.
def add_new_note(new_note):
    with open("file.txt", "a") as text_file:
        text_file.write(new_note + '\n')


def import_load(flag):
    try:
        flag = int(flag)
        # NOT VALID TYPE
        if int(flag) not in [1, 2, 3, 4, 0]:
            print(console_menu.error_not_valid_flag(flag))
        # IMPORT FROM CUSTOM FILE FORMAT
        elif flag == 1:
            path_to_file = console_menu.input_file_path('input_file')
            file_text = list(open(path_to_file, 'r'))
            return file_text, path_to_file
        # IMPORT FROM CSV FILE FORMAT
        elif flag == 2:
            print(console_menu.error_unavailable_now())
        elif flag == 3:
            path_to_file = console_menu.input_file_path('file.json')
            file_text = json.load(open('file.json',))
            return file_text, path_to_file
        # IMPORT FROM XML FILE FORMAT
        elif flag == 4:
            print(console_menu.error_unavailable_now())
    except ValueError:
        print(console_menu.error_import_type())


def input_note(input_type, flag):
    if input_type == 'm':
        if flag == 1:
            news(flag)
        elif flag == 2:
            private_ad(flag)
        elif flag == 3:
            weather(flag)
    elif input_type == 'i':
        list_and_path = import_load(flag)
        list_of_dict = list_and_path[0]
        file_path = list_and_path[1]
        for note in list_of_dict:
            if isinstance(note, str):
                note = json.loads(note)
            note_type = note['header'].lower()
            if note_type == 'news':
                note_text = text_transform_module.text_formatting(note['text'])
                note_city = text_transform_module.text_formatting(note['city'])
                new_note = News('News', note_text, note_city)
                insert_row = insert_note.insert_news_note(new_note)
                add_new_note(insert_row)
                print(console_menu.creation_confirm_message(note_type))
            elif note_type == 'weather':
                note_text = text_transform_module.text_formatting(note['text'])
                note_city = text_transform_module.text_formatting(note['city'])
                note_degrees = note['temp']
                note_date = note['date']
                new_note = Weather('Weather', note_text, note_city, note_date, note_degrees)
                insert_row = insert_note.insert_news_note(new_note)
                add_new_note(insert_row)
                print(console_menu.creation_confirm_message(note_type))
            elif note_type == 'private ad':
                note_text = text_transform_module.text_formatting(note['text'])
                note_date = note['date']
                new_note = PrivateAd('Private Ad', note_text, note_date)
                insert_row = insert_note.insert_private_note(new_note)
                add_new_note(insert_row)
                print(console_menu.creation_confirm_message(note_type))
            # add count tests
            added_date = datetime.now().strftime('%d/%m/%Y %H.%M.%S')
            test_module.word_count(note_text, 'word_count.csv', note_type, added_date)
            test_module.letter_count(note_text, 'letter_count.csv', note_type, added_date)
        console_menu.drop_file(file_path)
    else:
        print('error')


def console():
    flag = str()
    cnt = 0
    welcome_message = console_menu.welcome_message()
    manual_input = console_menu.manual_input()
    import_input = console_menu.import_input()
    while flag != 0:
        print('Hi, ' + welcome_message) if cnt == 0 else print(welcome_message.capitalize())
        flag = input('> ')
        # ERROR MESSAGE DATA TYPE
        try:
            flag = int(flag)
            # NOT VALID TYPE
            if int(flag) not in [1, 2, 0]:
                print(console_menu.error_not_valid_flag(flag))
            # MANUAL INPUT
            elif int(flag) == 1:
                flag = input(manual_input.capitalize()+'\n> ')
                # ERROR MESSAGE DATA TYPE
                try:
                    flag = int(flag)
                    # NOT VALID TYPE
                    if int(flag) not in console_menu.dict_of_notes().keys():
                        print(console_menu.error_not_valid_flag(flag))
                    # GO TO INPUT NOTE
                    elif int(flag) in console_menu.dict_of_notes().keys():
                        input_note('m', flag)
                # TYPE ERROR
                except ValueError:
                    print(console_menu.error_data_type())
            # IMPORT INPUT
            elif int(flag) == 2:
                flag = input(import_input.capitalize()+'\n> ')
                try:
                    flag = int(flag)
                    if int(flag) not in [1, 2, 3, 0]:
                        print(console_menu.error_not_valid_flag(flag))
                    elif int(flag) == 0:
                        print(console_menu.goodbye_message())
                    else:
                        input_note('i', flag)
                except ValueError:
                    print(console_menu.error_data_type())
        except ValueError:
            print(console_menu.error_data_type())
        # EXIT
        if flag != 0:
            flag = console_menu.continue_massage()
        if flag == 0:
            print(console_menu.goodbye_message())
        cnt += 1


console()
