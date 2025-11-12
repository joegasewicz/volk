import os
import sys
import socket

from volk.utils.logging import log


class Volk:

    wsgi_application: WSGIApplication

    server_running = False

    host = "127.0.0.1"

    port = 8888

    status: int

    environ = {
        "wsgi.input": sys.stdin.buffer,
        "wsgi.errors": sys.stderr,
        "wsgi.version": (1, 0),
        "wsgi.multithread": False,
        "wsgi.multiprocess": False,
        "wsgi.run_once": True,
    }

    def __init__(self, *, wsgi_application = None):
        self.wsgi_application = wsgi_application

    def serve(self):
        log.info(f"Running server on http://{self.host}:{self.port}")
        self.server_running = True

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen(1)
            conn, addr = s.accept()
            with conn:

                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    log.debug(f"Client data: {data}")
                    # Update environ
                    self.environ["PATH_INFO"] = "/"
                    self.environ["REQUEST_METHOD"] = "GET"
                    self.environ["QUERY_STRING"] = ""
                    result = self.wsgi_application(self.environ, self.start_response)
                    log.debug(f"result: {result}")
                    byte_data = b"HTTP/1.1 " + str(self.status).encode("utf-8") + b"OK\r\n"
                    byte_data += b"Content-Type: text/html; charset=utf-8\r\n"
                    byte_data += b"Content-Length: 1000\r\n\r\n"
                    byte_data += result[0]
                    conn.sendall(byte_data)

    def start_response(self, status, response_headers, exec_info=None):
        self.status = status
        log.debug(f"status: {status}")
        log.debug(f"response_headers: {response_headers}")
        log.debug(f"exec_info: {exec_info}")

