from argparse import ArgumentTypeError
from os.path import isfile, isdir
from socket import socket, AF_INET, SOCK_STREAM
from types import FunctionType


def int_greater_than_zero(time: int) -> int:
    time = int(time)

    if time <= 0:
        raise ArgumentTypeError('Value should not be greater than 0.')

    return time


def from_dict(dictionary: dict, error_message: str) -> FunctionType:
    def func(key) -> object:
        item = dictionary.get(key)
        if item is None:
            raise ArgumentTypeError(error_message)
        else:
            return dictionary

    return func


def int_is_valid_port(port) -> int:
    port = int(port)

    if port in range(1, 1024):
        raise ArgumentTypeError("Privileged port used.")
    elif not port in range(1024, 2 ** 16):
        raise ArgumentTypeError("Port outside port range.")
    elif int_is_open_port(port) is not port:
        pass  # will raise anyway
    else:
        return port


def int_is_open_port(port: int) -> int:
    port = int(port)

    sock = socket(AF_INET, SOCK_STREAM)
    is_open = (sock.connect_ex(('127.0.0.1', port)) != 0)

    if is_open:
        return port
    else:
        raise ArgumentTypeError('Port is not open')


def str_is_existing_path(path: str) -> str:
    if isfile(path) or isdir(path):
        raise ArgumentTypeError("Given path is not an existing file or directory.")
    else:
        return path


def str_is_existing_dir(path: str) -> str:
    if not isdir(path):
        raise ArgumentTypeError("Given path is not an existing directory.")
    else:
        return path


def str_is_existing_file(path: str) -> str:
    if not isfile(path):
        raise ArgumentTypeError("Given path is not an existing file.")
    else:
        return path
