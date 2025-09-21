import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "planthub.db")


def get_all_user():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = [dict(row) for row in cur.fetchall()]
    conn.close()
    return users


def get_user(user_id):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id=?", (user_id,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None


def add_user(data):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO users (first_name, last_name, Address, email) VALUES (?,?,?,?)", (data["first_name"], data["last_name"], data["address"], data["email"]),)
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return new_id


def update_user(data, user_id):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("Update users SET (first_name, last_name, Address, email) VALUES (?,?,?,?) WHERE id=?", (data["first_name"], data["last_name"], data["address"], data["email"]), user_id)
    conn.commit()
    conn.close()


def delete_user(user_id):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("Delete from users WHERE id=?",user_id)
    conn.commit()
    conn.close()