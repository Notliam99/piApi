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


# @api.error
# def error(request, error_code):
#     doc = f'<center><h1>Error: {error_code}<h1></center><hr>'
#     return doc


def Main():
    api.run(80)


if __name__ == '__main__':
    Main()
