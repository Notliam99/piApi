"""Manage the wifi on the board"""
from network import WLAN, STA_IF, AP_IF
from time import sleep


class Wifi:
    """Connect to or setup a network."""

    def __init__(
        self,
        ssid: str,
        password: str,
        ap_ssid=None,
        ap_password=None,
        hostname=None
    ) -> None:

        # Set Default Values If One Is Not Given.
        if not ap_ssid:
            ap_ssid = "micropython"

        if not ap_password:
            ap_password = "password"

        if not hostname:
            hostname = "micropython.local"

        # If Ssid Is Invalid It Will Use AP Mode.
        if len(ssid) <= 1:
            # AP MODE
            print("using AP")
            self.wlan = WLAN(AP_IF)
            self.wlan.config(
                ssid=ap_ssid,
                password=ap_password,
                security=0,
                hostname=hostname
            )
            self.wlan.active(True)
            while self.wlan.active() is False:
                print('Waiting for connection...')
                sleep(1)
        else:
            # WIFI MODE
            print("using WIFI")
            self.password = password
            self.ssid = ssid
            self.wlan = WLAN(STA_IF)
            self.wlan.config(hostname=hostname)
            self.wlan.active(True)
            self.wlan.connect(self.ssid, self.password)
            while self.wlan.isconnected() is False:
                print('Waiting for connection...')
                sleep(1)

    def get_info(self) -> dict:
        '''
        returns dictionary
        {
            ip: str,
            subnet_mask: str,
            gateway: str,
            dns: str,
            ssid: str,
            hostname: str,
        }
        '''
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
