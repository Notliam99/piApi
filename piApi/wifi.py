"""Manage the wifi on the board"""
from network import WLAN, STA_IF, AP_IF
from time import sleep


class wifi:
    """Connect to or setup a network."""

    def __init__(self, wifi_config: dict):
        if len(wifi_config["ssid"]) <= 1:
            print("using AP")
            self.wlan = WLAN(AP_IF)
            self.wlan.config(
                ssid="Sprikiley",
                password='12345678',
                security=0,
                hostname="sprikiley.local"
            )
            self.wlan.active(True)
            while self.wlan.active() is False:
                print('Waiting for connection...')
                sleep(1)
        else:
            print("using WIFI")
            self.password = wifi_config["password"]
            self.ssid = wifi_config["ssid"]
            self.wlan = WLAN(STA_IF)
            # self.wlan.config(hostname="sprikiley.local")
            self.wlan.active(True)
            self.wlan.connect(self.ssid, self.password)
            while self.wlan.isconnected() is False:
                print('Waiting for connection...')
                sleep(1)
        info = (
            f'Ip Address:({self.wlan.ifconfig()[0]})',
            f'Dns Server:({self.wlan.ifconfig()[3]})',
            f'Gateway:({self.wlan.ifconfig()[2]})',
            f'Subnet Mask:({self.wlan.ifconfig()[1]})'
        )
        print(
            f"|{'CONNECTED':-^38}|\n|{info[0]: <38}|\n|{info[1]: <38}|\n|{info[2]: <38}|\n|{info[3]: <38}|\n|{'-'*38}|"
        )
        sleep(240)
