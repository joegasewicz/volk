import io
import os
import sys
import socket

from volk.utils.logging import log
from volk.message import RequestMessage, ResponseMessage, BaseMessage
from volk.wsgi import WSGI


class Volk:

    server_running = False

    host = "127.0.0.1"

    port = 8888

    request_message: BaseMessage

    def __init__(self, *, wsgi_application = None):
        self.wsgi_application = wsgi_application

    def serve(self):
        log.info(f"Running server on http://{self.host}:{self.port}")
        self.server_running = True

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen(1)

            while True:
                conn, addr = s.accept()
                with conn:
                    while True:
                        # Stay in bytes until WSGI section
                        byte_stream: bytes = conn.recv(1024)
                        if not byte_stream:
                            break
                        # Get request method
                        wsgi = WSGI()
                        self.request_message = RequestMessage(byte_stream=byte_stream)
                        method, byte_stream = self.request_message.get_method()
                        path, byte_stream = self.request_message.get_path(byte_stream=byte_stream)
                        version, byte_stream = self.request_message.get_version(byte_stream=byte_stream)

                        # Only convert bytes to strings for WSGI at this point
                        path = path.decode("ascii")
                        method = method.decode("ascii")
                        version = version.decode("ascii")

                        # Update WSGI environ
                        wsgi.environ["PATH_INFO"] = path
                        wsgi.environ["REQUEST_METHOD"] = method
                        wsgi.environ["SERVER_PROTOCOL"] = version
                        wsgi.environ["SERVER_PORT"] = self.port
                        wsgi.environ["wsgi.input"] = io.BytesIO(b"")

                        result = self.wsgi_application(wsgi.environ, self.start_response)

                        # Response
                        log.debug(f"result: {result}")
                        byte_stream = b"HTTP/1.1 " + str(self.status).encode("utf-8") + b"OK\r\n"
                        byte_stream += b"Content-Type: text/html; charset=utf-8\r\n"
                        byte_stream += b"Content-Length: 1000\r\n\r\n"
                        byte_stream += result[0]
                        conn.sendall(byte_stream)

    def start_response(self, status, response_headers, exec_info=None):
        self.status = status
        log.debug(f"status: {status}")
        log.debug(f"response_headers: {response_headers}")
        log.debug(f"exec_info: {exec_info}")

