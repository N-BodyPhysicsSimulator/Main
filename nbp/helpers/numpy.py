import numpy


def tuple_to_numpy(t: tuple) -> numpy.ndarray:
    """
    >>> tuple_to_numpy((1, 2, 3))
    array([[ 1.],
           [ 2.],
           [ 3.]])
    >>> tuple_to_numpy((123.123, 234.234, 345.345))
    array([[ 123.123],
           [ 234.234],
           [ 345.345]])
    """
    return numpy.array([[t[0]],
                        [t[1]],
                        [t[2]]]).astype('float64')


def numpy_to_list(array: numpy.ndarray) -> list:
    """
    >>> array = numpy.array([[1.2], [2.1], [2.2]])
    >>> numpy_to_list(array) == [1.2, 2.1, 2.2]
    True
    """
    return [array[0][0], array[1][0], array[2][0]]


def numpy_to_dict(array: numpy.ndarray) -> dict:
    """
    >>> array = numpy.array([[1.2], [2.1], [2.2]])
    >>> numpy_to_dict(array) == { 'x': 1.2, 'y': 2.1, 'z': 2.2 }
    True
    """
    return {
        'x': array[0][0],
        'y': array[1][0],
        'z': array[2][0]
    }


def dict_to_numpy(dictionary: dict) -> numpy.ndarray:
    """
    >>> a = dict_to_numpy({'x': 1.0, 'y': 2.0, 'z': 3.0})
    >>> a
    array([[ 1.],
           [ 2.],
           [ 3.]])
    >>> numpy_to_dict(a) == {'x': 1.0, 'y': 2.0, 'z': 3.0}
    True
    >>> dict_to_numpy({'x': 1.5, 'y': 2.5, 'z': 3.5})
    array([[ 1.5],
           [ 2.5],
           [ 3.5]])
    >>> dict_to_numpy({'x': -100, 'y': 212, 'z': 31234})
    array([[  -100.],
           [   212.],
           [ 31234.]])
    """
    return tuple_to_numpy((
        dictionary['x'],
        dictionary['y'],
        dictionary['z']
    ))
