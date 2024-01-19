'''Coverts peramiters into a responce string.'''


def responce_headers(
        http_version: str,
        responce_code: int,
        custom_headers: dict
):
    """
    takes in headers and outputs them in a string format

    ARGS:
        http_version: str
        responce_code: int
        custom_headers: dict
    OUT:
        value: str
    """
    value = str()

    value += f'{http_version} {responce_code}'
    for header_key, header_value in custom_headers.items():
        value += f'\r\n{header_key}: {header_value}'

    value += '\r\n\r\n'

    return value
