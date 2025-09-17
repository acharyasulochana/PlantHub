from http.server import BaseHTTPRequestHandler, HTTPServer
from utils.router import route_request
from database.setup import init_db


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        route_request(self, "GET", self.path)

    def do_POST(self):
        route_request(self, "POST", self.path)


if __name__ == "__main__":
    init_db()
    server = HTTPServer(("localhost", 8000), RequestHandler)
    print("Server running at http://localhost:8000")
    server.serve_forever()