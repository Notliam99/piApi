import ujson as json


class Config:
    '''
        Reads and writes to the config.
        ARGS:
            file_name: str
            default_config
        RETURNS:
            None # get the config using the data varible
    '''

    def __init__(self, file_name: str, default_config: dict) -> None:
        self.default_config = default_config
        self.data = dict({})

        while self.data == {}:
            try:
                with open(file_name) as file:
                    self.data = json.load(file)

            except Exception as exe:
                print(exe)
                with open(file_name, 'w') as file:
                    json.dump(default_config, file)
