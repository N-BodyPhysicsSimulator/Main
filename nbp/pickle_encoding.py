import pickle

from base64 import b64encode, b64decode

def to_pickle(self):
    """Export to Pickle"""
    return b64encode(pickle.dumps(self)).decode('utf-8')

def from_pickle(text):
    """Import from Pickle

    Actual Body will not be a dictionary, but that is irrelevant. This is just an example.

    >>> moon = {'name': 'Moon', 'mass': 3.1415, 'radius': 11.2, 'position': (9, 8, 7), 'velocity': (1, 2, 3)}

    >>> moon_from_pickle = from_pickle(to_pickle(moon))
    >>> moon_from_pickle['name']
    'Moon'
    >>> moon_from_pickle['position'] == moon['position']
    True
    >>> moon_from_pickle['name'] == moon['name']
    True
    >>> moon_from_pickle['velocity'] == moon['velocity']
    True
    >>> moon_from_pickle['radius'] == moon['radius']
    True
    >>> moon_from_pickle['mass'] == moon['mass']
    True
    """
    return pickle.loads(b64decode(text.encode('utf-8')))
