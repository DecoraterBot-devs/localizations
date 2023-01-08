"""
Creates a database from sql script files.
"""
import sqlite3


def create_database(db_name):
    conn = sqlite3.connect(db_name)
    with open('Tables/Localizations.sql', encoding='utf-8') as f:
        conn.executescript(f.read())
    with open('Tables/StringTable.sql', encoding='utf-8') as f:
        conn.executescript(f.read())
    with open('Data/Localizations.sql', encoding='utf-8') as f:
        conn.executescript(f.read())
    with open('Data/StringTable.en.sql', encoding='utf-8') as f:
        conn.executescript(f.read())
    with open('Data/StringTable.ko.sql', encoding='utf-8') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()


create_database('localizations.db')
