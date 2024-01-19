"""module with many utils and boilerplate code for the api"""

from .wifi import Wifi
from .utils.config import Config
from .socket import Socket
import time
from .utils.request_parse import request_parse
from .utils.responce_headers import responce_headers

__version__ = 1.0


default_config = dict({
    "wifi": {
        "ssid": "",
        "password": ""
    }
})


class Api():
    '''Api Class'''

    def __init__(
        self,
        diy=False,
        default_config=default_config,
        config_name="config.json",
        ap_ssid=None,
        ap_password=None,
        hostname=None
    ) -> None:
        '''
            The init function for the api class.
            ARGS:
                diy: bool # doesnt init any modules
                default_config: dict optional
                config_name: str optional # names the config file
                ap_ssid: str optional
                ap_password: str optional
                hostname: optional
        '''
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
        '''
            Error decorator is a catchall it must follow.
            ARGS:
                    request: dict # containing the raw request
            RETURN:
                    document: str
                    responce_code: int optional

                # need to have the responce code
                custom_responce_args: dict optional
        '''
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

    def connect(self, path: str):
        '''
            The function being decorated must follow.
            ARGS:
                    request: dict # containing the raw request
            RETURN:
                    document: str
                    responce_code: int optional

                # need to have the responce code
                custom_responce_args: dict optional
        '''
        def decorator(func):
            def wraper(request: str, *args, **kwargs):
                value = func(
                    request,
                    *args,
                    **kwargs
                )
                if type(value) is tuple:
                    if len(value) == 3:
                        return value[0], value[1], value[2]
                    else:
                        return value[0], value[1], {}
                else:
                    return value, 200, {}
            self.routes_dict['CONNECT'][path] = wraper
            return wraper
        return decorator

    def delete(self, path: str):
        '''
            The function being decorated must follow.
            ARGS:
                    request: dict # containing the raw request
            RETURN:
                    document: str
                    responce_code: int optional

                # need to have the responce code
                custom_responce_args: dict optional
        '''
        def decorator(func):
            def wraper(request: str, *args, **kwargs):
                value = func(
                    request,
                    *args,
                    **kwargs
                )
                if type(value) is tuple:
                    if len(value) == 3:
                        return value[0], value[1], value[2]
                    else:
                        return value[0], value[1], {}
                else:
                    return value, 200, {}
            self.routes_dict['DELETE'][path] = wraper
            return wraper
        return decorator

    def get(self, path: str):
        '''
            The function being decorated must follow.
            ARGS:
                    request: dict # containing the raw request
            RETURN:
                    document: str
                    responce_code: int optional

                # need to have the responce code
                custom_responce_args: dict optional
        '''
        def decorator(func):
            def wraper(request: str, *args, **kwargs):
                value = func(
                    request,
                    *args,
                    **kwargs
                )
                if type(value) is tuple:
                    if len(value) == 3:
                        return value[0], value[1], value[2]
                    else:
                        return value[0], value[1], {}
                else:
                    return value, 200, {}
            self.routes_dict['GET'][path] = wraper
            return wraper
        return decorator

    def head(self, path: str):
        '''
            The function being decorated must follow.
            ARGS:
                    request: dict # containing the raw request
            RETURN:
                    document: str
                    responce_code: int optional

                # need to have the responce code
                custom_responce_args: dict optional
        '''
        def decorator(func):
            def wraper(request: str, *args, **kwargs):
                value = func(
                    request,
                    *args,
                    **kwargs
                )
                if type(value) is tuple:
                    if len(value) == 3:
                        return value[0], value[1], value[2]
                    else:
                        return value[0], value[1], {}
                else:
                    return value, 200, {}
            self.routes_dict['HEAD'][path] = wraper
            return wraper
        return decorator

    def options(self, path: str):
        '''
            The function being decorated must follow.
            ARGS:
                    request: dict # containing the raw request
            RETURN:
                    document: str
                    responce_code: int optional

                # need to have the responce code
                custom_responce_args: dict optional
        '''
        def decorator(func):
            def wraper(request: str, *args, **kwargs):
                value = func(
                    request,
                    *args,
                    **kwargs
                )
                if type(value) is tuple:
                    if len(value) == 3:
                        return value[0], value[1], value[2]
                    else:
                        return value[0], value[1], {}
                else:
                    return value, 200, {}
            self.routes_dict['OPTIONS'][path] = wraper
            return wraper
        return decorator

    def post(self, path: str):
        '''
            The function being decorated must follow.
            ARGS:
                    request: dict # containing the raw request
            RETURN:
                    document: str
                    responce_code: int optional

                # need to have the responce code
                custom_responce_args: dict optional
        '''
        def decorator(func):
            def wraper(request: str, *args, **kwargs):
                value = func(
                    request,
                    *args,
                    **kwargs
                )
                if type(value) is tuple:
                    if len(value) == 3:
                        return value[0], value[1], value[2]
                    else:
                        return value[0], value[1], {}
                else:
                    return value, 200, {}
            self.routes_dict['POST'][path] = wraper
            return wraper
        return decorator

    def put(self, path: str):
        '''
            The function being decorated must follow.
            ARGS:
                    request: dict # containing the raw request
            RETURN:
                    document: str
                    responce_code: int optional

                # need to have the responce code
                custom_responce_args: dict optional
        '''
        def decorator(func):
            def wraper(request: str, *args, **kwargs):
                value = func(
                    request,
                    *args,
                    **kwargs
                )
                if type(value) is tuple:
                    if len(value) == 3:
                        return value[0], value[1], value[2]
                    else:
                        return value[0], value[1], {}
                else:
                    return value, 200, {}
            self.routes_dict['PUT'][path] = wraper
            return wraper
        return decorator

    def trace(self, path: str):
        '''
            The function being decorated must follow.
            ARGS:
                    request: dict # containing the raw request
            RETURN:
                    document: str
                    responce_code: int optional

                # need to have the responce code
                custom_responce_args: dict optional
        '''
        def decorator(func):
            def wraper(request: str, *args, **kwargs):
                value = func(
                    request,
                    *args,
                    **kwargs
                )
                if type(value) is tuple:
                    if len(value) == 3:
                        return value[0], value[1], value[2]
                    else:
                        return value[0], value[1], {}
                else:
                    return value, 200, {}
            self.routes_dict['TRACE'][path] = wraper
            return wraper
        return decorator

    def run(
        self,
        port: int,
        address="0.0.0.0",
        server_name="micropython"
    ) -> None:
        '''
            Run the web server
            ARGS:
                port: int
                address: str optional
                server_name: str optional
        '''
        # socket init
        socket = Socket((address, port))
        self.address = socket.get_info()
        print(f"lissening on {self.address}")

        # catch all
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

            # if theres a error starts from the beginning
            try:
                request = request_parse(str(conn.recv(1024)))
            except Exeption as error:
                pass
            
            headers = dict({})

            try:
                document, responce_code, headers = self.routes_dict[request['method']][request['path']](
                    request)

            except Exception as exce:
                print(exce)
                responce_code = 404
                document = self.routes_dict['ERROR'](request, responce_code)

            if "Content-Type" not in headers.keys():
                headers['Content-Type'] = "text/html"

            if "Server" not in headers.keys():
                headers["Server"] = server_name

            localtime = time.localtime()

            print(
                f'{localtime[5]}:{localtime[4]}:{localtime[3]},',
                f'{localtime[2]}D:{localtime[1]}M:{localtime[0]}Y',
                f'({request["method"]}: {request["path"]},',
                f'status: {responce_code})'
            )

            conn.send(responce_headers(
                http_version=request['http_version'],
                responce_code=responce_code,
                custom_headers=headers
            ))
            conn.sendall(str(document))
            conn.close()
