import psycopg2

def create_table(conn, cur):
    sql = """
    CREATE TABLE IF NOT EXISTS schreibtisch_distanz (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        distance NUMERIC NOT NULL,
        timestamp TEXT NOT NULL
    );
    """
    cur.execute(sql)
    conn.commit()
    print("Tabelle 'schreibtisch_distanz' wurde erstellt.")

def prep_db():
    try:
        conn = psycopg2.connect(
            host="DEIN_HOST",
            database="DEIN_DATABASE_NAME",
            user="DEIN_BENUTZERNAME",
            password="DEIN_PASSWORT"
        )

        cur = conn.cursor()

        cur.execute("""
            SELECT EXISTS (
                SELECT 1
                FROM information_schema.tables
                WHERE table_name = 'schreibtisch_distanz'
            );
        """)
        table_exists = cur.fetchone()[0]

        if not table_exists:
            create_table(conn, cur)

        print("Datenbankvorbereitung erfolgreich abgeschlossen.")

    except (Exception, psycopg2.Error) as error:
        print("Fehler bei der Datenbankvorbereitung:", error)

    finally:
        if conn:
            conn.close()

    
