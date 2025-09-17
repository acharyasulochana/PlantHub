import re
from controllers import user_controller


def route_request(handler, method, path):
    if path == "/api/users" and method == "GET":
        return user_controller.list_users(handler)
    elif path == "/api/user" and method == "POST":
        return user_controller.add_users(handler)
    else:
        handler.send_response(404)
        handler.end_headers()
        handler.wfile.write(b"Not Found")