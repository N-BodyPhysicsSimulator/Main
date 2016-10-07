import numpy

from nbp.bodies import Body
from nbp.bodies import BodyState


def distance_to(one_body: Body, other_body: Body) -> numpy.ndarray:
    """Takes two instances of a bodies and calculates the distance.

    Returns a Vector. Use numpy.linalg.norm(<Vector>) to get real distance in a float.
    
    This test is based on the output of the function we wrote the test for.
    TODO: Write better test
    
    >>> earth = Body.from_tuple_parameters("Earth", 5.972*(10**24), 100, (1.506*(10**11), 0, 100), (0, 29290, 0))
    >>> moon = Body.from_tuple_parameters("Moon", 0.0735*(10**24), 100, (1.496*(10**11), 384.4*(10**6), -500), (1050, 29290, 0))
    >>> distance_to(moon, earth)
    array([[  1.00000000e+09],
           [ -3.84400000e+08],
           [  6.00000000e+02]])

    Distance to itself is always 0 in all directions.

    >>> moon = Body.from_tuple_parameters("Moon", 0.0735*(10**24), 100, (1.496*(10**11), 384.4*(10**6), -500), (1050, 29290, 0))
    >>> distance_to(moon, moon)
    array([[ 0.],
           [ 0.],
           [ 0.]])

    >>> from nbp.helpers.numpy import tuple_to_numpy
    >>> import numpy as np
    >>> velocity = tuple_to_numpy((0, 0, 0))
    >>> one = Body('saturn', 100, 100, np.array([[0.], [0.], [0.]]), velocity)
    >>> two = Body('neptune', 100, 100, tuple_to_numpy((0, 146.2, 0)), velocity)
    >>> distance_to(one, two)
    array([[   0. ],
           [ 146.2],
           [   0. ]])
    """
    return other_body.position - one_body.position


def absolute_distance_to_one(one_body: Body, other_body: Body) -> float:
    """Takes two instances of a bodies and calculates the absolute distance.
    
    This test is based on the output of the function we wrote the test for.
    TODO: Write better test
    
    >>> earth = Body.from_tuple_parameters("Earth", 5.972*(10**24), 100.0, (1.496*(10**11), 0, 0), (0, 29290, 0))
    >>> moon = Body.from_tuple_parameters("Moon", 0.0735*(10**24), 100.0, (1.496*(10**11), 384.4*(10**6), 0), (1050, 29290, 0))
    >>> absolute_distance_to_one(moon, earth)
    384400000.0
    
    >>> earth = Body.from_tuple_parameters("Earth", 5.972*(10**24), 100.0, (1.496*(10**11), 0, 0), (0, 29290, 0))
    >>> moon = Body.from_tuple_parameters("Moon", 0.0735*(10**24), 100.0, (1.496*(10**11), -384.4*(10**6), -69834), (1050, 29290, 0))
    >>> absolute_distance_to_one(moon, earth)
    384400006.34337604

    >>> from nbp.helpers.numpy import tuple_to_numpy
    >>> import numpy as np
    >>> velocity = tuple_to_numpy((0, 0, 0))
    >>> one = Body('saturn', 100, 100, np.array([[0.], [0.], [0.]]), velocity)
    >>> two = Body('neptune', 100, 100, tuple_to_numpy((0, 146.2, 0)), velocity)
    >>> dist = absolute_distance_to_one(one, two)
    >>> float("{0:.1f}".format(dist))
    146.2
    """
    return numpy.linalg.norm(distance_to(one_body, other_body))


def acceleration_to_one(one_body: Body, other_body: Body) -> numpy.ndarray:
    """Return acceleration in x, y, z directions.
    
    This test is based on the output of the function we wrote the test for.
    TODO: Write better test
    
    >>> earth = Body.from_tuple_parameters("Earth", (5.972*(10**24)), 100.0, (0, 0, 0), (0, 0, 0))
    >>> kg = Body.from_tuple_parameters("kg", 1.0, 100.0, (0, 6371000, 0), (0, 0, 0))
    >>> acceleration_to_one(kg, earth)
    array([[ 0.        ],
           [-9.81964974],
           [ 0.        ]])
    """
    if one_body == other_body:
        return numpy.array([[0],
                            [0],
                            [0]]).astype('float64')

    distance_vector = distance_to(one_body, other_body)
    distance = absolute_distance_to_one(one_body, other_body)

    force = calculate_force(one_body.mass, other_body.mass, distance)
    force_ratio = force / distance

    return (distance_vector * force_ratio) / one_body.mass


def acceleration_to_all(one_body: Body, bodies: [Body]) -> numpy.ndarray:
    """ Return the acceleration in vectors to alll other bodies
    
    This test is based on the output of the function we wrote the test for.
    TODO: Write better test
    
    >>> kg = Body.from_tuple_parameters("kg", 1.0, 100.0, (0, 0, 0), (0, 0, 0))
    >>> earth1 = Body.from_tuple_parameters("Earth1", (5.972*(10**24)), 100.0, (0, 6371000, 6280), (0, 0, 0))
    >>> earth2 = Body.from_tuple_parameters("Earth4", (5.972*(10**24)), 100.0, (-6371000, 0, 0), (0, 0, 0))
    >>> moon = Body.from_tuple_parameters("Moon", 0.0735*(10**24), 100.0, (0, 384.4*(10**6), -1000), (0, 0, 0))

    >>> acceleration_to_all(moon, [kg, earth1, earth2, moon])
    array([[ -4.46878801e-05],
           [ -5.48536334e-03],
           [  6.07257588e-08]])

    """
    total_acceleration = numpy.array([[0],
                                      [0],
                                      [0]]).astype("float64")

    for other_body in bodies:
        total_acceleration = total_acceleration + acceleration_to_one(one_body, other_body)

    return total_acceleration


def calculate_position(body: Body, delta_time: float) -> numpy.ndarray:
    """ Calculates a new position for a new tick
    
    This test is based on the output of the function we wrote the test for.
    TODO: Write better test
    
    >>> test_body = Body.from_tuple_parameters("Test_body", 1.0, 1.0, (60, -20, 15), (4, 10.2, -6))
    >>> calculate_position(test_body, 3.0)
    array([[ 72. ],
           [ 10.6],
           [ -3. ]])
    """
    return body.position + (delta_time * body.velocity)


def calculate_velocity(one_body: Body, delta_time: float, other_bodies: [Body]) -> numpy.ndarray:
    """ Calculates new velocity for a new tick.

        This test is based on the output of the function we wrote the test for.
        TODO: Write better test
        
        >>> kg = Body.from_tuple_parameters("kg", 1.0, 100.0, (0, 0, 0), (0, 0, 0))
        >>> e1 = Body.from_tuple_parameters("Earth1", (5.972*(10**24)), 100.0, (0, 6371000, 0), (0, 0, 0))
        >>> e2 = Body.from_tuple_parameters("Earth2", (5.972*(10**24)), 100.0, (0, -6371000, 0), (0, 0, 0))
        >>> e3 = Body.from_tuple_parameters("Earth3", (5.972*(10**24)), 100.0, (6371000, 0, 0), (0, 0, 0))
        >>> e4 = Body.from_tuple_parameters("Earth4", (5.972*(10**24)), 100.0, (-6371000, 0, 0), (0, 0, 0))
        >>> e5 = Body.from_tuple_parameters("Earth5", (5.972*(10**24)), 100.0, (6371000, 9000, -532), (0, 0, 0))
        >>> e6 = Body.from_tuple_parameters("Earth6", (5.972*(10**24)), 100.0, (-6371000, -9000, 532), (0, 0, 0))
        >>> calculate_velocity(kg, 314.0, [kg, e1, e2, e3, e4, e5, e6])
        array([[ 0.],
               [ 0.],
               [ 0.]])

        >>> kg = Body.from_tuple_parameters("kg", 1.0, 100.0, (0, 0, 0), (0, 0, 0))
        >>> earth1 = Body.from_tuple_parameters("Earth1", (5.972*(10**24)), 100.0, (0, 6371000, 6280), (0, 0, 0))
        >>> moon = Body.from_tuple_parameters("Moon", 0.0735*(10**24), 100.0, (0, 384.4*(10**6), -1000), (0, 0, 0))
        >>> calculate_velocity(kg, 16.0, [kg, earth1, moon])
        array([[  0.00000000e+00],
               [  1.57114698e+02],
               [  1.54870030e-01]])
    """

    return one_body.velocity + (delta_time * acceleration_to_all(one_body, other_bodies))


def merge_bodies(one_body: Body, other_body: Body) -> Body:
    """ merges one body with a second body. Important note: This function doesn't delete any body!
    It assumed that the density will stay the same after collision.
    
    This test is based on the output of the function we wrote the test for.
    TODO: Write better test
    
    >>> earth = Body.from_tuple_parameters("Earth", 5.972*(10**24), 6371000, (1.506*(10**11), 500, 100), (-100, 29290, -2))
    >>> moon = Body.from_tuple_parameters("Moon", 0.0735*(10**24), 1738000, (1.496*(10**11), 384.4*(10**6), -500), (1050, -29290, 100))
    >>> planet = merge_bodies(earth, moon)

    >>> planet.position
    array([[  1.50587842e+11],
           [  4.67395352e+06],
           [  9.27053180e+01]])

    >>> planet.velocity
    array([[ -8.60185262e+01],
           [  2.85777959e+04],
           [ -7.59904061e-01]])

    >>> planet.radius
    6413824.949215559

    >>> planet.mass # Notice the strage 1 at the end.
    6.045500000000001e+24

    >>> huge = Body.from_tuple_parameters("huge", 5.972*(10**24), 173843647354234567632353, (1.506*(10**11), 500, 100), (-100, 29290, -2))
    >>> planet2 = merge_bodies(huge, planet)

    >>> planet2.radius
    1.7384364735423404e+23

    >>> large = Body.from_tuple_parameters("huge", 5.972*(10**24), 17380000000, (1.506*(10**11), 500, 100), (-100, 29290, -2)) # Notice that if the radius of large is 1738000000000 that the radius will get smaller with 2,7 milimeters
    >>> planet3 = merge_bodies(planet, large)
    >>> planet3.radius
    17380000000.291138
    """
    mass = one_body.mass + other_body.mass
    position = (one_body.position * one_body.mass + other_body.position * other_body.mass) / mass
    velocity = (one_body.velocity * one_body.mass + other_body.velocity * other_body.mass) / mass
    radius = ((one_body.radius ** 3) + (other_body.radius ** 3)) ** (1 / 3)

    if one_body.mass >= other_body.mass:
        name = one_body.mass
    else:
        name = other_body.mass

    return Body(name, mass, radius, position, velocity)


def calculate_force(one_mass, other_mass, distance):
    return (6.67408 * (10 ** -11)) * ((one_mass * other_mass) / (distance ** 2))


def minimal_distance(bodies: [Body]) -> float:
    """Return the smallest distance between all bodies.
    
    This test is based on the output of the function we wrote the test for.
    TODO: Write better test
    
    >>> sun = Body.from_tuple_parameters('Sun', 1989000000000000000000000000000, 100, (0, 0, 0), (0, 0, 0))
    >>> earth = Body.from_tuple_parameters('earth', 5972000000000000000000000, 100, (0, 152100000000, 1000), (29290, 0, 32))
    >>> moon = Body.from_tuple_parameters('moon', 73460000000000000000000, 100, (405500000, 152100000000, 175000), (29290, 964, 0))
    >>> jupiter = Body.from_tuple_parameters('jupiter', 1900000000000000000000000000, 100, (816620000000, 0, -1000), (40, 12440, 1))
    >>> saturn = Body.from_tuple_parameters('saturn', 568000000000000000000000000, 100, (0, 1352550000000, 0), (0, 10180, 0))
    >>> neptune = Body.from_tuple_parameters('neptune', 102413000000000000000000000, 100, (0, -4444450000000, 500000), (-5370, 0, 0))
    >>> minimal_distance([sun, earth, moon, jupiter, saturn, neptune])
    405500037.33168757

    >>> sun = Body.from_tuple_parameters('Sun', 1989000000000000000000000000000, 100, (0, 0, 0), (0, 0, 0))
    >>> earth = Body.from_tuple_parameters('earth', 5972000000000000000000000, 100, (0, 152100000000, 1000), (29290, 0, 32))
    >>> moon = Body.from_tuple_parameters('moon', 73460000000000000000000, 100, (-405500000, 152100000000, -174000), (29290, 964, 0))
    >>> jupiter = Body.from_tuple_parameters('jupiter', 1900000000000000000000000000, 100, (816620000000, 0, -1000), (40, 12440, 1))
    >>> saturn = Body.from_tuple_parameters('saturn', 568000000000000000000000000, 100, (0, 1352550000000, 0), (0, 10180, 0))
    >>> neptune = Body.from_tuple_parameters('neptune', 102413000000000000000000000, 100, (0, -4444450000000, 500000), (-5370, 0, 0))
    >>> minimal_distance([sun, earth, moon, jupiter, saturn, neptune])
    405500037.76202041
    
    >>> sun = Body.from_tuple_parameters('Sun', 1989000000000000000000000000000, 100, (0, 0, 0), (0, 0, 0))
    >>> earth = Body.from_tuple_parameters('earth', 5972000000000000000000000, 100, (107550941418, 107550941418, 100000), (29290, 0, 32))
    >>> jupiter = Body.from_tuple_parameters('jupiter', 1900000000000000000000000000, 100, (816620000000, 0, -1000), (40, 12440, 1))
    >>> saturn = Body.from_tuple_parameters('saturn', 568000000000000000000000000, 100, (0, 1352550000000, 0), (0, 10180, 0))
    >>> neptune = Body.from_tuple_parameters('neptune', 102413000000000000000000000, 100, (0, -4444450000000, 500000), (-5370, 0, 0))
    >>> minimal_distance([sun, earth, jupiter, saturn, neptune])
    152099999999.3627

    >>> from nbp.helpers.numpy import tuple_to_numpy
    >>> import numpy as np
    >>> velocity = tuple_to_numpy((0, 0, 0))
    >>> one = Body('saturn', 100, 100, np.array([[0.], [0.], [0.]]), velocity)
    >>> two = Body('neptune', 100, 100, tuple_to_numpy((0, 146.2, 0)), velocity)
    >>> dist = minimal_distance([one, two])
    >>> float("{0:.1f}".format(dist))
    146.2
    """
    smallest_distance = 0.0

    for body in bodies:
        for other_body in bodies:
            if body == other_body:
                continue

            distance = absolute_distance_to_one(body, other_body)
            if smallest_distance <= 0.0 or smallest_distance > distance:
                smallest_distance = distance

    return smallest_distance


def get_delta_time(bodies: [Body], settings: tuple) -> float:
    """ Changes delta time based on the distance between bodies.
    Takes a tuple (and bodies) from the state in the form off (<radius>, <time>)
    And returns the appropiate delta time based on the minimal_distance.
    >>> from nbp.helpers.numpy import tuple_to_numpy
    >>> import numpy as np

    time_settings = {'time': [3, 2, 4, 1], 'radius': [200, 300, 100, 400]}
    
    >>> time_settings = ([1, 2, 3, 4], [100, 200, 300, 400])
    >>> velocity = tuple_to_numpy((0, 0, 0))
    >>> body1 = Body('body1', 1, 100, np.array([[0.], [0.], [0.]]), velocity)
    >>> body2 = Body('body2', 1, 100, np.array([[0.], [99.], [0.]]), velocity)
    >>> bodies = [body1, body2]
    >>> get_delta_time(bodies, time_settings)
    1
    >>> body1 = Body('body1', 1, 100, np.array([[0.], [0.], [0.]]), velocity)
    >>> body2 = Body('body2', 1, 100, tuple_to_numpy((0, 146.32, 0)), velocity)
    >>> bodies = [body1, body2]
    >>> get_delta_time(bodies, time_settings)
    2
    >>> body2 = Body('body2', 1, 100, tuple_to_numpy((0, 200, 0)), velocity)
    >>> bodies = [body1, body2]
    >>> get_delta_time(bodies, time_settings)
    2
    >>> body2 = Body('body2', 1, 100, tuple_to_numpy((0, 201, 0)), velocity)
    >>> bodies = [body1, body2]
    >>> get_delta_time(bodies, time_settings)
    3
    >>> body2 = Body('body2', 1, 100, tuple_to_numpy((0, 314, 0)), velocity)
    >>> bodies = [body1, body2]
    >>> get_delta_time(bodies, time_settings)
    4
    >>> body2 = Body('body2', 1, 100, tuple_to_numpy((0, 403, 0)), velocity)
    >>> bodies = [body1, body2]
    >>> get_delta_time(bodies, time_settings)
    4
    >>> body2 = Body('body2', 1, 100, tuple_to_numpy((0, -152100000000, 0)), velocity)
    >>> bodies = [body1, body2]
    >>> get_delta_time(bodies, time_settings)
    4
    >>> body2 = Body('body2', 1, 100, tuple_to_numpy((0, -153, 0)), velocity)
    >>> bodies = [body1, body2]
    >>> get_delta_time(bodies, time_settings)
    2
    >>> body2 = Body('body2', 1, 100, tuple_to_numpy((0, 3, 0)), velocity)
    >>> bodies = [body1, body2]
    >>> get_delta_time(bodies, time_settings)
    1
    """
    time_settings, radius_settings = settings
    time_settings = sorted(time_settings)
    radius_settings = sorted(radius_settings)

    min_distance = minimal_distance(bodies)
    
    new_delta_time = min(time_settings)

    if min_distance > max(radius_settings):
        return max(time_settings)

    for i, distance in enumerate(radius_settings):
        if min_distance <= distance:
            return time_settings[i]
