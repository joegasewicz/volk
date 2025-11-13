from typing import ByteString

from volk.message import BaseMessage, RequestMessage, ResponseMessage


class WSGI:

    environ = {
        "REQUEST_METHOD": "",
        "SCRIPT_NAME": "",
        "PATH_INFO": "",
        "QUERY_STRING": "",
        "CONTENT_TYPE": "",
        "CONTENT_LENGTH": "",
        "SERVER_NAME": "Volk",
        "SERVER_PORT": 80,
        "SERVER_PROTOCOL": "",
        "wsgi.version": (1, 0),  # WSGI version
        "wsgi.url_scheme": "",
        "wsgi.input": None,
        "wsgi.errors": None,
        "wsgi.multithread": False,
        "wsgi.multiprocess": False,
        "wsgi.run_once": False,
    }

    def __init__(
        self,
        # request_message: BaseMessage,
        # response_message: BaseMessage,
    ):
        # self.request_message = request_message TODO
        # self.response_message = response_message TODO
        pass

    def handle_request(self, message: ByteString):
        pass


    def handle_response(self):
        pass
