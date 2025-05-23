import sqlite3
from datetime import datetime

DB_NAME = "leads.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            address TEXT,
            owner_name TEXT,
            phone TEXT,
            email TEXT,
            occupancy TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_lead(address, owner_name, phone, email, occupancy):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO leads (timestamp, address, owner_name, phone, email, occupancy)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (datetime.utcnow().isoformat(), address, owner_name, phone, email, occupancy))
    conn.commit()
    conn.close()

def get_all_leads():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT * FROM leads ORDER BY timestamp DESC')
    rows = c.fetchall()
    conn.close()
    return rows
