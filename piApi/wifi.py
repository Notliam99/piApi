"""Manage the wifi on the board"""
from network import WLAN, STA_IF, AP_IF
from time import sleep


class Wifi:
    """Connect to or setup a network."""

    def __init__(self, wifi_config: dict) -> None:
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

    def get_info(self) -> dict:
        return dict(
            {
                "ip": self.wlan.ifconfig()[0],
                "subnet_mask": self.wlan.ifconfig()[1],
                "Gateway": self.wlan.ifconfig()[2],
                "dns": self.wlan.ifconfig()[3],
                "ssid": self.wlan.config("ssid"),
                "hostname": self.wlan.config("hostname")
            }
        )
