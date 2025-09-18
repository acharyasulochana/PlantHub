import re
from controllers import user_controller


def route_request(handler, method, path):
    if path == "/api/users" and method == "GET":
        return user_controller.get_all_users(handler)
    elif re.match(r"^/api/users/\d+$", path) and method == "GET":
        user_id = int(path.split("/")[-1])
        return user_controller.get_user(handler, user_id)
    elif path == "/api/user" and method == "POST":
        return user_controller.add_users(handler)
    else:
        handler.send_response(404)
        handler.send_header("Content-Type", "text/plain")
        handler.end_headers()
        handler.wfile.write(b"Not Found")
