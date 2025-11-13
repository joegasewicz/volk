from abc import ABC, abstractmethod
from typing import Tuple


class BaseMessage(ABC):

    @abstractmethod
    def get_method(self) -> Tuple[bytes, bytes]: ...

    @abstractmethod
    def get_path(self, *, byte_stream: bytes) -> Tuple[bytes, bytes]: ...

    @abstractmethod
    def get_version(self, *, byte_stream: bytes) -> Tuple[bytes, bytes]: ...


class ResponseMessage(BaseMessage):
    pass


class RequestMessage(BaseMessage):
    byte_steam: bytes

    def __init__(self, *, byte_stream: bytes):
        self.byte_stream = byte_stream

    def get_method(self) -> Tuple[bytes, bytes]:
        """
        :returns [Bytes, Bytes]:  Returns a tuple pair representing the
        method & the rest of the message bytes.
        """
        method, _, b = self.byte_stream.partition(b" ")
        return method, b

    def get_path(self, *, byte_stream: bytes) -> Tuple[bytes, bytes]:
        """
        :return [Bytes, Bytes]
        """
        path, _, b = byte_stream.partition(b" ")
        return path, b

    def get_version(self, *, byte_stream: bytes) -> Tuple[bytes, bytes]:
        """
        """
        version, _, b = byte_stream.partition(b"\r")

        return version, b
