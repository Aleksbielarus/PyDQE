from datetime import date
from datetime import datetime
from package import console_menu
import os


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
    note_text = console_menu.note_text()
    note_city = console_menu.note_city()
    new_note = News('News', note_text, note_city)
    insert_row = f"{new_note.print_type()} {(30 - len(new_note.print_type())) * '-'}\n" \
                 f"{new_note.print_note_text()}\n" \
                 f"{new_note.print_city()}, {new_note.print_datetime()}\n" \
                 f"{31 * '-'}\n"
    add_new_note(insert_row)
    print(console_menu.creation_confirm_message(flag))


def private_add(flag):
    note_text = console_menu.note_text()
    note_date = console_menu.note_date()
    new_note = PrivateAd('Private Add', note_text, note_date)
    insert_row = f"{new_note.print_type()} {(30 - len(new_note.print_type())) * '-'}\n" \
                 f"{new_note.print_note_text()}\n" \
                 f"Actual until: {new_note.print_date()}, {new_note.print_days_left()} days left\n" \
                 f"{31 * '-'}\n"
    add_new_note(insert_row)
    print(console_menu.creation_confirm_message(flag))


def weather(flag):
    note_text = console_menu.note_text()
    note_city = console_menu.note_city()
    note_degrees = console_menu.note_degrees()
    note_date = console_menu.note_date()
    new_note = Weather('Weather', note_text, note_city, note_date, note_degrees)
    insert_row = f"{new_note.print_type()} {(30 - len(new_note.print_type())) * '-'}\n" \
                 f"{new_note.print_note_text()}\n" \
                 f"{new_note.print_city()}, {new_note.print_degrees()} degrees {new_note.print_date()}\n" \
                 f"{31 * '-'}\n"
    add_new_note(insert_row)
    print(console_menu.creation_confirm_message(flag))


def import_load(flag):
    try:
        flag = int(flag)
        # NOT VALID TYPE
        if int(flag) not in [1, 2, 3, 4, 0]:
            print(f'"{flag}" is not valid value. Please, try again')
        # IMPORT FROM CUSTOM FILE FORMAT
        elif flag == 1:
            path_to_file = str(input("Please, specify the file path\n> "))
            # specify default path to file(current directory)
            # !!!! need to add strong specification to current dir.
            if path_to_file == '':
                path_to_file = os.getcwd()
            file_text = list(open(path_to_file, 'r'))
            print(file_text)
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
        elif note_type.lower() == 'private add':
            private_add(flag)
        elif note_type.lower() == 'weather':
            weather(flag)
    elif input_type == 'i':
        import_load(flag)
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
            elif int(flag) == 1:
                print(manual_input.capitalize())
                flag = input('> ')
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
                        input_note('m', 2, 'private add')
                    # MY UNIQUE NOTE (WEATHER)
                    elif flag == 3:
                        input_note('m', 3, 'weather')
                # TYPE ERROR
                except ValueError:
                    print(console_menu.error_date_type())
                flag = console_menu.continue_massage()
            elif int(flag) == 2:
                print(import_input)
                flag = input('> ')
                input_note('i', flag)
        except ValueError:
            print(console_menu.error_date_type())
        # EXIT
        if flag == 0:
            print(console_menu.goodbye_message())
        cnt += 1


console()
