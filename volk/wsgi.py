import os
import sys


class WSGIApplication:

    def __init__(self, application):
        self.environ = {
            "wsgi.input": sys.stdin.buffer,
            "wsgi.errors": sys.stderr,
            "wsgi.version": (1, 0),
            "wsgi.multithread": False,
            "wsgi.multiprocess": False,
            "wsgi.run_once": True,
        }
        result = application(self.environ, self.start_response)

    def start_response(self, status, response_headers, exec_info=None):
        pass
