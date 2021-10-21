# ----------------------- INSERT NEWS NOTE -----------------------
def insert_news_note(new_note):
    insert_row = f"{new_note.print_type()} {(30 - len(new_note.print_type())) * '-'}\n" \
                 f"{new_note.print_note_text()}\n" \
                 f"{new_note.print_city()}, {new_note.print_datetime()}\n" \
                 f"{31 * '-'}\n"
    return insert_row


# ----------------------- INSERT PRIVATE NOTE -----------------------
def insert_private_note(new_note):
    insert_row = f"{new_note.print_type()} {(30 - len(new_note.print_type())) * '-'}\n" \
                 f"{new_note.print_note_text()}\n" \
                 f"Actual until: {new_note.print_date()}, {new_note.print_days_left()} days left\n" \
                 f"{31 * '-'}\n"
    return insert_row


# ----------------------- INSERT WEATHER NOTE -----------------------
def insert_weather_note(new_note):
    insert_row = f"{new_note.print_type()} {(30 - len(new_note.print_type())) * '-'}\n" \
                 f"{new_note.print_note_text()}\n" \
                 f"{new_note.print_city()}, {new_note.print_degrees()} degrees {new_note.print_date()}\n" \
                 f"{31 * '-'}\n"
    return insert_row
