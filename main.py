from piApi import Api

# default_config = dict({
#     "wifi": {
#         "ssid": "",
#     "password": ""
#     }
# })

# Config = config(file_name="./config.json", default_config=default_config)

# Wlan = wifi(wifi_config=Config.data["wifi"])

api = Api()


def Main():
    api.run(80)


if __name__ == '__main__':
    Main()
