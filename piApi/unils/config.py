import ujson as json


def load_config(file_name, default_config):
    """Load The Config Or Setup The Defaut One"""
    data = dict({})
    while data == {}:
        try:
            with open("/config.json") as config_fs:
                data = json.load(config_fs)

        except Exception as exe:
            print(exe)
            with open("./config.json", 'w') as config_fs:
                json.dump(default_config, config_fs)

    return data


class config:
    def __init__(self, file_name: str, default_config: dict):
        self.data = load_config(
            file_name=file_name,
            default_config=default_config
        )
