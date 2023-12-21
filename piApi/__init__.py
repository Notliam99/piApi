"""module with many utils and boilerplate code for the api"""

from .wifi import Wifi
from .utils.config import Config
from .socket import Socket
from time import sleep

__version__ = 0.0


default_config = dict({
    "wifi": {
        "ssid": "",
        "password": ""
    }
})


class Api():
    def __init__(
        self,
        diy=False,
        default_config=default_config,
        config_name="config.json",
        ap_ssid=None,
        ap_password=None,
        hostname=None
    ):
        if diy is True:
            pass

        self.config = Config(config_name, default_config)
        data = self.config.data

        self.routes_dict = dict({"GET": {"/wow"}, "PUT": {}})

        wifi = Wifi(
            ssid=data["wifi"]["ssid"],
            password=data["wifi"]["password"],
            ap_ssid=ap_ssid,
            ap_password=ap_password,
            hostname=hostname
        )

        print(wifi.get_info())

    def get(self, func: callable, path: str) -> None:
        def wraper(*args, **kwargs):
            out = func(*args, **kwargs)
            return str(out)
        self.routes_dict["get"][path] = wraper()

    def post(self):
        pass

    def run(self, port: int, addr="0.0.0.0") -> None:
        socket = Socket((addr, port))
        self.address = socket.get_info()["address"]
        print(f"lissening on {self.address}")

        request, address = socket.socket.accept()

        print(str(request.recv(1024)))

        while True:
            responce = str('')

            conn, address = socket.socket.accept()
            request = str(conn.recv(1024))

            print(self.routes_dict)

            for key in self.routes_dict.keys():
                if request.find(key) == 2:
                    request_method = key

            for key in self.routes_dict[request_method]:
                if request.find(f"{key} ") == 6:
                    pass

            if responce == str(''):
                conn.send(
                    'HTTP/1.1 200 OK\nContent-Type: text/html\nConnection: close\n\n')
                conn.sendall("error 404")
            conn.close()
