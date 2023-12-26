from piApi import Api
import ujson
import machine

# default_config = dict({
#     "wifi": {
#         "ssid": "",
#     "password": ""
#     }
# })

# Config = config(file_name="./config.json", default_config=default_config)

# Wlan = wifi(wifi_config=Config.data["wifi"])

api = Api()


@api.get('/')
def hello_world(request):
    doc = f'<center><h1>Hello World<h1></center><hr><center>{request}</center>'
    return doc, 200


@api.get('/request')
def request(request):
    return (
        ujson.dumps(request),
        200,
        {"content-type": "application/json; charset=UTF-8"}
    )


def Main():
    api.run(80)


if __name__ == '__main__':
    Main()
