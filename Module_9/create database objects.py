# create tables.
from Connection import connector

dbname = 'notes_database'
conn = connector.connect(dbname)

cursor = conn.cursor()

cursor.execute('''DROP TABLE IF EXISTS notes.news_notes''')
cursor.execute('''CREATE TABLE notes.news_notes(
                    note_name varchar,
                    note_text varchar,
                    note_city varchar
                    )''')
conn.commit()

cursor.execute('''DROP TABLE IF EXISTS notes.private_ad_notes''')
cursor.execute('''CREATE TABLE notes.private_ad_notes(
                    note_name varchar,
                    note_text varchar,
                    note_date varchar
                    )''')
conn.commit()

cursor.execute('''DROP TABLE IF EXISTS notes.weather_notes''')
cursor.execute('''CREATE TABLE notes.weather_notes(
                    note_name varchar,
                    note_text varchar,
                    note_city varchar,
                    note_degrees varchar,
                    note_date varchar
                    )''')
conn.commit()
