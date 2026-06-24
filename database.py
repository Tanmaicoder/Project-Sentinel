import sqlite3

def create_database():

    conn = sqlite3.connect("disasters.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS disasters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        location TEXT,
        severity TEXT,
        risk_score INTEGER
    )
    """)

    conn.commit()
    conn.close()


def save_disaster(location, severity, risk_score):

    conn = sqlite3.connect("disasters.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO disasters(
        location,
        severity,
        risk_score
    )
    VALUES(?,?,?)
    """, (
        location,
        severity,
        risk_score
    ))

    conn.commit()
    conn.close()


def get_disasters():

    conn = sqlite3.connect("disasters.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT location,
           severity,
           risk_score
    FROM disasters
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows