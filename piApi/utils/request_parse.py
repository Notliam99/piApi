"""parse the request string"""
import re


def request_parse(request: str):
    """
    parse the request sting

    ARGS:
        request: sting

    RETURNS:
        output: dict{
            "method": ("CONNECT"|"DELETE"|"GET"|"HEAD"|"OPTIONS"|"POST"|"PUT"|"TRACE"),: str,
            "path": "/...",:str
            "http_version": ("HTTP/1.1"|"HTTP/2"|"HTTP/3"),:str
            "...": "...":any
        }
    """
    regex = re.compile(
        r"(CONNECT|DELETE|GET|HEAD|OPTIONS|POST|PUT|TRACE) (\S*)\s(HTTP/1.1|HTTP/2|HTTP/3)")
    headers = regex.search(request)
    regex = re.compile(r'(^[^?#]+)')
    path = regex.search(headers.group(0).split(' ')[1])
    print(path)
    output = {
        "method": headers.group(0).split(' ')[0],
        "path": path.group(0),
        "http_version": headers.group(0).split(' ')[2]
    }
    request = request[(headers.span()[1]):]
    request = request.split(r"\r\n")
    for i in request:
        if not i or ":" not in i:
            continue
        value = i.split(":")
        output[value[0]] = value[1]

    return output
