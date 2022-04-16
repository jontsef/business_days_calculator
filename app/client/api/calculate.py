from http.server import BaseHTTPRequestHandler
from urllib import parse

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        s = self.path
        query = dict(parse.parse_qsl(parse.urlsplit(s).query))

        if "name" in query:
            message = "Hello, " + query["name"] + "!"
        else:
            message = "Hello, stranger!"

        self.wfile.write(message.encode())
        return