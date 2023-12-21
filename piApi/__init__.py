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

        wifi = Wifi(
            ssid=data["wifi"]["ssid"],
            password=data["wifi"]["password"],
            ap_ssid=ap_ssid,
            ap_password=ap_password,
            hostname=hostname
        )

        print(wifi.get_info())
        socket = Socket(("0.0.0.0", 80))

        print(socket.get_info())

        sleep(200)
