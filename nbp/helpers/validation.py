from argparse import ArgumentTypeError
from os.path import isfile, isdir, dirname
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
    ...     str_is_existing_path(path) == path
    True

    >>> str_is_existing_dir('')
    Traceback (most recent call last):
    argparse.ArgumentTypeError: Given path is not an existing directory.

    >>> str_is_existing_dir('/non/existing/dir')
    Traceback (most recent call last):
    argparse.ArgumentTypeError: Given path is not an existing directory.
    """
    if not isdir(path):
        raise ArgumentTypeError("Given path is not an existing directory.")
    else:
        return path


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
    if not isfile(path):
        raise ArgumentTypeError("Given path is not an existing file.")
    else:
        return path

def dirname_is_existing_dir(path: str) -> str:
    """
    >>> import tempfile

    >>> with tempfile.TemporaryFile() as f:
    ...     dirname_is_existing_dir(f.name) == f.name
    True
    
    >>> dirname_is_existing_dir('')
    Traceback (most recent call last):
    argparse.ArgumentTypeError: Dirname of path is not an existing directory.
    
    >>> dirname_is_existing_dir('/non/existing/dir')
    Traceback (most recent call last):
    argparse.ArgumentTypeError: Dirname of path is not an existing directory.
    """
    if not isdir(dirname(path)):
        raise ArgumentTypeError("Dirname of path is not an existing directory.")
    else:
        return path
