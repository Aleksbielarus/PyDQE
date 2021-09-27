from datetime import date
from datetime import datetime


# add new note to text file.
def add_new_note(new_note):
    with open("file.txt", "a") as text_file:
        text_file.write(new_note + '\n')


class Note:
    datetime = datetime.now().strftime('%d/%m/%Y %H.%M')
    date = date.today().strftime('%d/%m/%Y')

    def __init__(self, type, note_text):
        self.type = type
        self.note_text = note_text

    def print_type(self):
        return self.type

    def print_note_text(self):
        return self.note_text

    def print_date(self):
        return self.date

    def print_datetime(self):
        return self.datetime


class News(Note):
    def __init__(self, type, note_text, city):
        Note.__init__(self, type=type, note_text=note_text)
        self.city = city

    def print_city(self):
        return self.city


class PrivateAd(Note):
    def __init__(self, type, note_text, date):
        Note.__init__(self, type=type, note_text=note_text)
        self.date = date

    def print_news_text(self):
        return self.note_text

    def print_days_left(self):
        return (datetime.strptime(self.date, '%d/%m/%Y') - datetime.now()).days


def console():
    type = str()
    while type != 0:
        # need to add try/except.
        type = int(input('Hi, \nplease, choose the note type:\n'
                         ' input "1" if news\n'
                         ' input "2" if private ad\n'
                         ' input "0" if you want to stop\n'
                         '> '))
        # NEWS NOTE
        if type == 1:
            note_text = input("Please input message text:\n> ").capitalize()
            note_city = input("Please input message city:\n> ").capitalize()
            new_note = News('News', note_text, note_city)
            insert_row = f"{new_note.print_type()} {(30 - len(new_note.print_type()))*'-'}\n" \
                         f"{new_note.print_note_text()}\n" \
                         f"{new_note.print_city()}, {new_note.print_datetime()}\n" \
                         f"{31*'-'}\n"
            add_new_note(insert_row)
        # PRIVATE AD
        elif type == 2:
            note_text = input("Please input message text:\n> ").capitalize()
            date = input("Please input message date(example '31/10/2021':\n> ")
            new_note = PrivateAd('Private Add', note_text, date)
            insert_row = f"{new_note.print_type()} {(30 - len(new_note.print_type())) * '-'}\n" \
                         f"{new_note.print_note_text()}\n" \
                         f"Actual until: {new_note.print_date()}, {new_note.print_days_left()} days left\n" \
                         f"{31 * '-'}\n"
            add_new_note(insert_row)
        # MY UNIQUE NOTE
        elif type == 3:
            pass
        # EXIT
        elif type == 0:
            print("Have a good day!")
        # ERROR MESSAGE
        else:
            print(f'"{type}" is not valid value. Please, try again')
            type = input('Please, choose the note type:\n'
                         ' input "1" if news\n'
                         ' input "2" if private ad\n'
                         ' input "0" if you want to stop\n'
                         '> ')


console()
