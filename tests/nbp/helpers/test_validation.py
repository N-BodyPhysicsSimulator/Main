from __future__ import print_function

from argparse import ArgumentTypeError

import pytest
import socket

from nbp.helpers.validation import int_is_valid_port, int_is_open_port

def test_closed_port(capsys):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((socket.gethostname(), 0))
    serversocket.listen(5)
    host, port = serversocket.getsockname()

    with pytest.raises(ArgumentTypeError):
        assert int_is_open_port(port) != port

    with pytest.raises(ArgumentTypeError):
        assert int_is_valid_port(port) != port

    serversocket.close()

def test_open_port():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((socket.gethostname(), 0))
    host, port = serversocket.getsockname()

    assert int_is_valid_port(port) == port
    assert int_is_valid_port(port) == port
