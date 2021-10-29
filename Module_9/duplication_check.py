from Connection import connector
from tests import queries


def no_duplicate_check(table_queries):
    conn = connector.connect('notes_database')
    cursor = conn.cursor()
    for query in table_queries:
        cursor.execute(query)
        records = cursor.fetchall()
        if not records:
            print('There is no duplicated rows in the table.')
        else:
            print(records)


no_duplicate_check(queries.table_queries)
