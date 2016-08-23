""" N-Body Physics simulator """

from .bodies import Body

from .io import InputProvider
from .io import FileInputProvider
from .io import CSVStartValueInputProvider

from .cli import cli
