import psycopg2
from Connection import config
# import config


def connect(dbname):
    try:
        return psycopg2.connect(
            user=config.user,
            password=config.password,
            host=config.host,
            port=config.port,
            database=dbname)
    except "Error" as e:
        print(e)
