import sqlite3, os, json
from urllib.parse import parse_qs
from models import user_model
from utils.response import json_response
from views.html_view import html_response

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "planthub.db")


def parse_body(handler):
    length = int(handler.headers.get("Content-Length", 0))
    body = handler.rfile.read(length).decode()
    if "application/json" in handler.headers.get("Content-Type", ""):
        return json.loads(body)
    return {k: v[0] for k, v in parse_qs(body).items()}


def get_all_users(handler):
    users = user_model.get_all_user()
    return json_response(handler, 200, {"users": users})


def get_user(handler, user_id):
    user = user_model.get_user(user_id)
    if user:
        return json_response(handler, 200, user)
    return json_response(handler, 404, {"error": "User not found"})


def add_user(handler):
    length = int(handler.headers.get("Content-Length", 0))
    body = handler.rfile.read(length).decode()
    data = json.loads(body)
    new_id = user_model.add_user(data)
    return json_response(handler, 201, {"message": "User created", "id": new_id})


def update_user(handler, user_id):
    length = int(handler.headers.get("Content-Length", 0))
    body = handler.rfile.read(length).decode()
    data = json.loads(body)
    new_id = user_model.update_user(data,user_id)
    return json_response(handler, 201, {"message": "User created", "id": new_id})














