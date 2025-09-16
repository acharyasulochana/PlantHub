import sqlite3, os, json
from urllib.parse import parse_qs
from models.user_model import get_all_user, add_user
from views.response import json_response
from views.html_view import html_response

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "planthub.db")


def list_user(handler):
    users = get_all_user()
    return json_response(handler, 200, users)


def list_users_view(handler):
    users = get_all_user()
    rows = [(p["id"], p["first_name"], p["lats_name"],p["address"], p["email"]) for p in users]
    headers = ["ID", "First Name", "Last Name", "Adderss", "Email"]
    return html_response(handler, "users_view.html", headers, rows)


def create_user(handler):
    length = int(handler.headers.get("Content-Length", 0))
    body = handler.rfile.read(length).decode()
    data = parse_qs(body)

    first_name = data.get("first_name", [""])[0]
    last_name = data.get("last_name", [""])[0]
    address = data.get("address", [""])[0]
    email = data.get("email", [""])[0]

    # Insert into DB
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (first_name, last_name, address, email) VALUES (?, ?, ?, ?)",
        (first_name, last_name, address, email),
    )
    conn.commit()
    conn.close()

    handler.send_response(303)
    handler.send_header("Location", "/users/view")
    handler.end_headers()