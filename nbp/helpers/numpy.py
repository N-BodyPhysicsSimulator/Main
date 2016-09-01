import numpy


def tuple_to_numpy(t: tuple) -> numpy.ndarray:
    """ How to test this private function!? """
    return numpy.array([[t[0]],
                        [t[1]],
                        [t[2]]]).astype('float64')


def numpy_to_list(array: numpy.ndarray) -> list:
    return [array[0][0], array[1][0], array[2][0]]


def numpy_to_dict(array: numpy.ndarray) -> dict:
    return {
        'x': array[0][0],
        'y': array[1][0],
        'z': array[2][0]
    }


def dict_to_numpy(dictionary: dict) -> numpy.ndarray:
    return tuple_to_numpy((
        dictionary['x'],
        dictionary['y'],
        dictionary['z']
    ))
