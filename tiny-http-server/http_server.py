#!/usr/bin/env python3
import socket
import sys
import urllib.parse
import json

MAX_BODY_SIZE = 16 * 1024  # 16KB limit


class HTTPRequest:
    def __init__(self, raw_request: bytes):
        self.method = None
        self.path = None
        self.version = None
        self.headers = {}
        self.body = b""
        self.parse(raw_request)

    def parse(self, raw_request: bytes):
        try:
            request_text = raw_request.decode("utf-8", errors="replace")
            header_part, _, body = request_text.partition("\r\n\r\n")

            # Request line
            lines = header_part.split("\r\n")
            request_line = lines[0].split(" ")
            self.method, self.path, self.version = request_line

            # Headers
            for line in lines[1:]:
                if ": " in line:
                    k, v = line.split(": ", 1)
                    self.headers[k.strip()] = v.strip()

            # Body
            if "Content-Length" in self.headers:
                length = int(self.headers["Content-Length"])
                self.body = body.encode()[:length]
            else:
                self.body = body.encode()[:MAX_BODY_SIZE]
        except Exception as e:
            print(f"Failed to parse request: {e}")


class HTTPResponse:
    def __init__(self, status_code=200, reason="OK", body=b"", headers=None):
        self.status_code = status_code
        self.reason = reason
        self.body = body if isinstance(body, bytes) else body.encode()
        self.headers = headers or {}

        self.headers["Content-Length"] = str(len(self.body))
        if "Content-Type" not in self.headers:
            self.headers["Content-Type"] = "text/plain"

    def build(self) -> bytes:
        response_line = f"HTTP/1.1 {self.status_code} {self.reason}\r\n"
        headers = "".join([f"{k}: {v}\r\n" for k, v in self.headers.items()])
        return (response_line + headers + "\r\n").encode() + self.body


def run_server(host="127.0.0.1", port=8080):
    print(f"Starting HTTP server on {host}:{port} ...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)
        while True:
            conn, addr = server_socket.accept()
            with conn:
                raw_request = conn.recv(4096)
                request = HTTPRequest(raw_request)
                print(f"Received {request.method} {request.path} from {addr}")

                # Routing logic
                if request.path == "/":
                    body = "Welcome to the HTTP Server!\nAvailable routes:\n - /hello\n - /echo"
                    response = HTTPResponse(body=body)

                elif request.path.startswith("/hello"):
                    body = "Hello! You reached /hello"
                    response = HTTPResponse(body=body)

                elif request.path.startswith("/echo"):
                    content_type = request.headers.get("Content-Type", "")

                    if request.method == "POST":
                        if "application/json" in content_type:
                            try:
                                data = json.loads(request.body.decode("utf-8"))
                                msg = data.get("msg", "")
                                body = json.dumps({"echo": msg})
                                response = HTTPResponse(body=body, headers={"Content-Type": "application/json"})
                            except Exception:
                                body = json.dumps({"error": "Invalid JSON"})
                                response = HTTPResponse(status_code=400, reason="Bad Request",
                                                        body=body, headers={"Content-Type": "application/json"})
                        else:
                            # Fallback: treat body as plain text
                            body = f"Echo: {request.body.decode('utf-8', errors='replace')}"
                            response = HTTPResponse(body=body)

                    elif request.method == "GET":
                        parsed = urllib.parse.urlparse(request.path)
                        query = urllib.parse.parse_qs(parsed.query)
                        msg = query.get("msg", [""])[0]
                        if "application/json" in content_type:
                            body = json.dumps({"echo": msg})
                            response = HTTPResponse(body=body, headers={"Content-Type": "application/json"})
                        else:
                            body = f"Echo: {msg}" if msg else "Echo: (no message)"
                            response = HTTPResponse(body=body)

                    else:
                        body = "405 Method Not Allowed"
                        response = HTTPResponse(status_code=405, reason="Method Not Allowed", body=body)

                else:
                    body = f"404 Not Found: {request.path}"
                    response = HTTPResponse(status_code=404, reason="Not Found", body=body)

                conn.sendall(response.build())


# ---- Simple Tests ----
def run_tests():
    print("Running tests...")

    raw = b"GET /test HTTP/1.1\r\nHost: localhost\r\n\r\n"
    req = HTTPRequest(raw)
    assert req.method == "GET"
    assert req.path == "/test"
    assert req.version == "HTTP/1.1"

    res = HTTPResponse(body="Hello World")
    data = res.build()
    assert b"Hello World" in data
    assert b"Content-Length" in data

    print("✅ All tests passed!")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        run_server()
