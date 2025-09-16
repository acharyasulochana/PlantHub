import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "planthub.db")


def get_all_user():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    conn.close()
    return [{"id": r[0], "first_name": r[1], "lats_name": r[2], "address": r[3], "email": r[4]} for r in rows]


def add_user(first_name, last_name, address, email):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO users (first_name, last_name, address, email) VALUES (?,?,?,?)", ("Sulochana", "Acharya", "Bochum", "acharya@email.com"))
    conn.commit()
    conn.close()
    return {"id": cur.lastrowid, "first_name": first_name, "last_name": last_name, "address": address, "email": email}
