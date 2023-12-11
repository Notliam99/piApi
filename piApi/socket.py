"""Opens A Socket"""
from socket import socket


class soc():
    """socket opject"""

    def __init__(self, port: int, wifi_dict: dict, ip=0) -> None:
        """init the class and create the socket"""
        if ip == 0:
            self.ip = wifi_dict["ip"]
        else:
            self.ip = ip

        self.port = port

        self.socket = socket()
        self.socket.bind(self.ip, self.port)
        self.socket.listen(1)
