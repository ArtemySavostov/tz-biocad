from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class HelloWorldHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/":
            self.send_error(404)
            return

        body = b"Hello world!\n"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    with ThreadingHTTPServer(("0.0.0.0", 32777), HelloWorldHandler) as server:
        print("Server running at http://localhost:32777", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
