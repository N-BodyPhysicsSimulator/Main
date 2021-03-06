from __future__ import print_function

from argparse import ArgumentTypeError

import pytest
import http.server
import socketserver
import threading
import socket

from nbp.helpers.validation import int_is_valid_port, int_is_open_port

def test_closed_port(capsys):
    httpd = socketserver.TCPServer(("", 0), http.server.SimpleHTTPRequestHandler)
    host, port = httpd.socket.getsockname()
    threading.Thread(target=httpd.serve_forever, args=(), daemon=True).start()

    with pytest.raises(ArgumentTypeError):
        assert int_is_open_port(port) != port

    with pytest.raises(ArgumentTypeError):
        assert int_is_valid_port(port) != port

def test_open_port():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((socket.gethostname(), 0))
    host, port = serversocket.getsockname()

    assert int_is_valid_port(port) == port
    assert int_is_valid_port(port) == port
