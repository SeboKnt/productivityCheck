import psycopg2
from datetime import datetime

def format_timestamp(timestamp):
    return timestamp.strftime('%Y%m%d%H%M%S')

def insert_db(name, distance):
    try:
        conn = psycopg2.connect(
            host="DEIN_HOST",
            database="DEIN_DATABASE_NAME",
            user="DEIN_BENUTZERNAME",
            password="DEIN_PASSWORT"
        )
        
        cur = conn.cursor()
        timestamp = format_timestamp(datetime.now())
        sql = "INSERT INTO schreibtisch_distanz (name, distance, timestamp) VALUES (%s, %s, %s);"
        values = (name, distance, timestamp)
        cur.execute(sql, values)
        conn.commit()

        print("Daten erfolgreich in die Datenbank eingefügt!")

    except (Exception, psycopg2.Error) as error:
        print("Fehler beim Einfügen der Daten in die Datenbank:", error)

    finally:
        if conn:
            conn.close()
