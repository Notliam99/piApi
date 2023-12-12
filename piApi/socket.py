"""Opens A Socket"""
from socket import socket


class Socket():
    """socket opject"""

    def __init__(self, soc_config: dict, wifi_config: dict) -> None:
        """init the class and create the socket"""

        self.ip = wifi_config["ip"]

        self.port = soc_config

        self.socket = socket()
        self.socket.bind(self.ip, self.port)
        self.socket.listen(1)
