"""Opens A Socket"""
import socket


class Socket():
    """socket helper web server"""

    def __init__(self, address: tuple[str, int]) -> None:
        """init the class and create the socket"""

        self.address = address

        self.socket = socket.socket()
        self.socket.bind(self.address)
        self.socket.listen(1)

    def get_info(self) -> dict:
        """
            Get info on the socket.
            RETURNS:
                address: tuple(
                    ip_address: str
                    port: int
                )
        """
        return self.address,
