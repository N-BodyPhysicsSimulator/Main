from argparse import ArgumentTypeError
from os.path import isfile, isdir, dirname, abspath
from socket import socket, AF_INET, SOCK_STREAM
from types import FunctionType


def int_greater_than_zero(time: int) -> int:
    """
    >>> int_greater_than_zero(1)
    1

    >>> int_greater_than_zero(0)
    Traceback (most recent call last):
    argparse.ArgumentTypeError: Value should be greater than 0.

    >>> int_greater_than_zero(-10)
    Traceback (most recent call last):
    argparse.ArgumentTypeError: Value should be greater than 0.
    """
    time = int(time)

    if time <= 0:
        raise ArgumentTypeError('Value should be greater than 0.')

    return time


def int_is_valid_port(port: int) -> int:
    """
    >>> int_is_valid_port(4092)
    4092
    
    >>> int_is_valid_port(80)
    Traceback (most recent call last):
    argparse.ArgumentTypeError: Privileged port used.

    >>> int_is_valid_port(9999999)
    Traceback (most recent call last):
    argparse.ArgumentTypeError: Port outside port range.

    >>> int_is_valid_port(-4092)
    Traceback (most recent call last):
    argparse.ArgumentTypeError: Port outside port range.
    """
    port = int(port)

    if port in range(1, 1024):
        raise ArgumentTypeError("Privileged port used.")
    elif not port in range(1024, 2 ** 16):
        raise ArgumentTypeError("Port outside port range.")
    else:
        return int_is_open_port(port)

def int_is_open_port(port: int) -> int:
    port = int(port)

    sock = socket(AF_INET, SOCK_STREAM)
    is_open = (sock.connect_ex(('127.0.0.1', port)) != 0)

    if is_open:
        return port
    else:
        raise ArgumentTypeError('Port is not open')


def str_is_existing_path(path: str) -> str:
    """
    >>> import tempfile

    >>> with tempfile.TemporaryFile() as f:
    ...     str_is_existing_file(f.name) == f.name
    True

    >>> with tempfile.TemporaryDirectory() as path:
    ...     str_is_existing_path(path) == path
    True

    >>> str_is_existing_path('')
    Traceback (most recent call last):
    argparse.ArgumentTypeError: Given path is not an existing file or directory.

    >>> str_is_existing_path('/non/existing/dir')
    Traceback (most recent call last):
    argparse.ArgumentTypeError: Given path is not an existing file or directory.
    """
    if isfile(path) or isdir(path):
        return path
    else:
        raise ArgumentTypeError("Given path is not an existing file or directory.")


def str_is_existing_dir(path: str) -> str:
    """
    >>> import tempfile

    >>> with tempfile.TemporaryDirectory() as path:
    ...     str_is_existing_dir(path) == path
    True

    >>> str_is_existing_dir('')
    Traceback (most recent call last):
    argparse.ArgumentTypeError: Given path is not an existing directory.

    >>> str_is_existing_dir('/non/existing/dir')
    Traceback (most recent call last):
    argparse.ArgumentTypeError: Given path is not an existing directory.
    """
    if isdir(path):
        return path
    else:
        raise ArgumentTypeError("Given path is not an existing directory.")


def str_is_existing_file(path: str) -> str:
    """
    >>> import tempfile

    >>> with tempfile.TemporaryFile() as f:
    ...     str_is_existing_file(f.name) == f.name
    True
    
    >>> str_is_existing_file('/home')
    Traceback (most recent call last):
    argparse.ArgumentTypeError: Given path is not an existing file.
    
    >>> str_is_existing_file('')
    Traceback (most recent call last):
    argparse.ArgumentTypeError: Given path is not an existing file.
    
    >>> str_is_existing_file('/non/existing/file')
    Traceback (most recent call last):
    argparse.ArgumentTypeError: Given path is not an existing file.
    """
    if isfile(path):
        return path
    else:
        raise ArgumentTypeError("Given path is not an existing file.")

def dirname_is_existing_dir(path: str) -> str:
    """
    >>> import tempfile

    >>> with tempfile.TemporaryDirectory() as dir:
    ...     dirname_is_existing_dir(dir) == dir
    True
    
    >>> dirname_is_existing_dir('/non/existing/dir')
    Traceback (most recent call last):
    argparse.ArgumentTypeError: Dirname of path is not an existing directory.
    """
    
    if isdir(dirname(abspath(path))):
        return path
    else:
        raise ArgumentTypeError("Dirname of path is not an existing directory.")

def change_delta_time_settings_to_tuples(value: str) -> list:
    """
    Value has format <time1>,<time2>:<distance1>,<distance2>
    
    >>> change_delta_time_settings_to_tuples("500,300,90:2,1,4")
    ([90, 300, 500], [1, 2, 4])
    """
    return tuple(
        [
            sorted(l) for l in [
                [int(v) for v in l.split(',')] for l in value.split(':')
            ]
        ]
    )

def enumerater_getter(v: str):
    """
    >>> func = enumerater_getter("first")
    >>> func([23,19,3])
    23
    >>> func = enumerater_getter("LAST")
    >>> func([23, 19, 123])
    123
    >>> func = enumerater_getter("3")
    >>> func([1, 3, 5, 7, 11, 13])
    7
    """
    v = v.lower().strip()
    
    if v == "first":
        return lambda enum: enum[0]
    if v == "last":
        return max
    else:
        return lambda enum: enum[int(v)]
