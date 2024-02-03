from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class MyHandler(BaseHTTPRequestHandler):
    def handle_request(self, data):
        input_param = data.get('input', [''])[0]

        response_text = f"Received input: {input_param}"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response_text.encode())

    def do_GET(self):
        parsed_params = parse_qs(self.path.split('?', 1)[-1])
        self.handle_request(parsed_params)

class MyServer:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.server = HTTPServer((self.host, self.port), MyHandler)

    def start(self):
        print(f"Server listening on {self.host}:{self.port}")
        self.server.serve_forever()

    def stop(self):
        print("Server shutting down")
        self.server.shutdown()
        self.server.server_close()

if __name__ == '__main__':
    my_server = MyServer()
    try:
        my_server.start()
    except KeyboardInterrupt:
        my_server.stop()
