from http.server import BaseHTTPRequestHandler, HTTPServer
from utils.router import route_request
from database.setup import init_db
import os


TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/api/"):
            route_request(self, "GET", self.path)
        else:
            self.serve_static()

    def do_POST(self):
        if self.path.startswith("/api/"):
            route_request(self, "POST", self.path)
        else:
            self.send_error(405, "Method Not Allowed")

    def do_PUT(self):
        if self.path.startswith("/api/"):
            route_request(self, "PUT", self.path)
        else:
            self.send_error(405, "Method Not Allowed")

    def do_DELETE(self):
        if self.path.startswith("/api/"):
            route_request(self, "DELETE", self.path)
        else:
            self.send_error(405, "Method Not Allowed")

    def serve_static(self):
        """Serve HTML, CSS, JS files from frontend/"""
        if self.path == "/":
            filepath = os.path.join(TEMPLATE_DIR, "users_view.html")
        else:
            filepath = os.path.join(TEMPLATE_DIR, self.path.lstrip("/"))

        if os.path.isfile(filepath):
            # Determine Content-Type
            if filepath.endswith(".html"):
                content_type = "text/html"
            elif filepath.endswith(".css"):
                content_type = "text/css"
            elif filepath.endswith(".js"):
                content_type = "application/javascript"
            else:
                content_type = "text/html"

            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.end_headers()
            with open(filepath, "rb") as f:
                self.wfile.write(f.read())
        else:
            self.send_error(404, "File Not Found")


if __name__ == "__main__":
    init_db()
    server = HTTPServer(("localhost", 8000), RequestHandler)
    print("Server running at http://localhost:8000")
    server.serve_forever()