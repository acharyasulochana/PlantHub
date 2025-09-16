import json
from models.user_model import get_all_user, add_user
from views.response import json_response

def list_user(handler):
    users = get_all_user()
    return json_response(handler, 200, users)

def create_user(handler):
    content_length = int(handler.headers.get("Content-Length", 0))
    body = handler.rfile.read(content_length)
    data = json.loads(body)
    new_user = add_user(data["name"], data.get("description", ""))
    return json_response(handler, 201, new_user)