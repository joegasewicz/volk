import os
import sys

from volk.utils.logging import log
from volk.wsgi import WSGIApplication


class Volk:

    wsgi_application: WSGIApplication

    server_running = False

    environ = {
        "wsgi.input": sys.stdin.buffer,
        "wsgi.errors": sys.stderr,
        "wsgi.version": (1, 0),
        "wsgi.multithread": False,
        "wsgi.multiprocess": False,
        "wsgi.run_once": True,
    }

    def __init__(self, *, wsgi_application: WSGIApplication = None):
        self.wsgi_application = wsgi_application

    def serve(self):
        self.server_running = True
        while self.server_running:
            log.info("Running server on http://localhost:8888")

            # Update environ
            self.environ["PATH_INFO"] = "/"
            self.environ["REQUEST_METHOD"] = "GET"
            self.environ["QUERY_STRING"] = ""

            result = self.wsgi_application(self.environ, self.start_response)
            log.debug(f"WSGI application result: {result}")
            self.server_running = False

    def start_response(self, status, response_headers, exec_info=None):
        pass


