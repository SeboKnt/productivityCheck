import psycopg2
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

global db_user
global db_passwd
global db_host
global db_name

db_user = os.getenv("DB_USER")
db_passwd = os.getenv("DB_PASSWD")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")

def format_timestamp(timestamp):
    return timestamp.strftime('%Y%m%d%H%M%S')

def insert_db(name, distance):
    try:
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_passwd
        )
        
        cur = conn.cursor()
        timestamp = format_timestamp(datetime.now())
        sql = "INSERT INTO schreibtisch_distanz (name, distance, timestamp) VALUES (%s, %s, %s);"
        values = (name, distance, timestamp)
        cur.execute(sql, values)
        conn.commit()

    except (Exception, psycopg2.Error) as error:
        print("Fehler beim Einfügen der Daten in die Datenbank:", error)

    finally:
        if conn:
            conn.close()
