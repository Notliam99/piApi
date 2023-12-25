"""module with many utils and boilerplate code for the api"""

from .wifi import Wifi
from .utils.config import Config
from .socket import Socket
import time
from .utils.request_parse import request_parse


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

        self.routes_dict = dict({
            "CONNECT": {},
            "DELETE": {},
            "GET": {},
            "HEAD": {},
            "OPTIONS": {},
            "POST": {},
            "PUT": {},
            "TRACE": {},
            "ERROR": None
        })

        wifi = Wifi(
            ssid=data["wifi"]["ssid"],
            password=data["wifi"]["password"],
            ap_ssid=ap_ssid,
            ap_password=ap_password,
            hostname=hostname
        )

        print(wifi.get_info())

    def error(self, func):
        def wraper(request: str, error_code: int, *args, **kwargs):
            value = func(
                request,
                error_code,
                *args,
                **kwargs
            )
            return value
        self.routes_dict['ERROR'] = wraper
        return wraper

    def run(self, port: int, addr="0.0.0.0") -> None:
        socket = Socket((addr, port))
        self.address = socket.get_info()["address"]
        print(f"lissening on {self.address}")

        if not self.routes_dict['ERROR']:
            @self.error
            def default_error(request, error):
                """
                default error responce

                ARGS:
                    request: dict,
                    error: int
                RETURN:
                    html_document
                """
                return f'<center><h1>Error: {error}<h1></center><hr>'

            self.routes_dict['ERROR'] == default_error

        while True:
            conn, address = socket.socket.accept()
            request = request_parse(str(conn.recv(1024)))

            print(f'{time.time} {self.routes_dict}')

            try:
                document = self.routes_dict[request['method']
                                            ][request['path']]()
            except Exception as exce:
                print(exce)
                document = self.routes_dict['ERROR'](request, 404)

            conn.send(
                '''
                HTTP/1.1 200 OK
                Content-Type: text/html
                Connection: close
                '''
            )
            conn.sendall(document)
            conn.close()
