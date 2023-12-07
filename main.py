from piApi import (
    wifi,
    config
)


default_config = dict({
    "wifi": {
        "ssid": "",
        "password": ""
    }
})

Config = config(file_name="./config.json", default_config=default_config)

Wlan = wifi(wifi_config=Config.data["wifi"])


def main():
    pass


if __name__ == '__main__':
    main()
