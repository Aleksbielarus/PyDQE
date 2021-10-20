from datetime import date
from datetime import datetime
from package import console_menu, insert_note, text_transform_module
from tests import test_module
import os
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


# add new note to text file.
def add_new_note(new_note):
    with open("file.txt", "a") as text_file:
        text_file.write(new_note + '\n')


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
        # IMPORT FROM JSON FILE FORMAT
        elif flag == 3:
            print(console_menu.error_unavailable_now())
        # IMPORT FROM XML FILE FORMAT
        elif flag == 4:
            print(console_menu.error_unavailable_now())
    except ValueError:
        print(console_menu.error_import_type())


def input_note(input_type, flag, note_type='news'):  # default param is news
    if input_type == 'm':
        if note_type.lower() == 'news':
            news(flag)
        elif note_type.lower() == 'private ad':
            private_ad(flag)
        elif note_type.lower() == 'weather':
            weather(flag)
    elif input_type == 'i':
        list_and_path = import_load(flag)
        list_of_dict = list_and_path[0]
        file_path = list_and_path[1]
        for note in list_of_dict:
            note = json.loads(note)
            print(note)
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
            date = datetime.now().strftime('%d/%m/%Y %H.%M.%S')
            test_module.word_count(note_text, 'word_count.csv', note_type, date)
            test_module.letter_count(note_text, 'letter_count.csv', note_type, date)
        drop_file(file_path)
    else:
        print('error')


def drop_file(path_to_file):
    os.remove(path_to_file)
    print("File was removed!")


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
                    if int(flag) not in [1, 2, 3, 0]:
                        print(console_menu.error_not_valid_flag(flag))
                    # NEWS NOTE
                    elif int(flag) == 1:
                        input_note('m', 1, 'news')
                    # PRIVATE AD
                    elif flag == 2:
                        input_note('m', 2, 'private ad')
                    # MY UNIQUE NOTE (WEATHER)
                    elif flag == 3:
                        input_note('m', 3, 'weather')
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
