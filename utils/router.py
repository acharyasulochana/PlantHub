from controllers import user_controller

def route_request(handler, method, path):
    if path == "/users" and method == "GET":
        return user_controller.list_user(handler)
    elif path == "/users/view" and method == "GET":
        return user_controller.list_users_view(handler)
    elif path == "/users/add" and method == "POST":
        return user_controller.create_user(handler)
    else:
        handler.send_response(404)
        handler.end_headers()
        handler.wfile.write(b"Not Found")