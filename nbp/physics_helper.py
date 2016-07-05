import numpy

from nbp.bodies import Body

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
    """
    return other_body.position - one_body.position

def absolute_distance_to_one(one_body: Body, other_body: Body) -> numpy.ndarray:
    """Takes two instances of a bodies and calculates the absolute distance.
    
    This test is based on the output of the function we wrote the test for.
    TODO: Write better test
    
    >>> earth = Body.from_tuple_parameters("Earth", 5.972*(10**24), 100.0, (1.496*(10**11), 0, 0), (0, 29290, 0))
    >>> moon = Body.from_tuple_parameters("Moon", 0.0735*(10**24), 100.0, (1.496*(10**11), 384.4*(10**6), 0), (1050, 29290, 0))
    >>> absolute_distance_to_one(moon,earth)
    384400000.0
    
    >>> earth = Body.from_tuple_parameters("Earth", 5.972*(10**24), 100.0, (1.496*(10**11), 0, 0), (0, 29290, 0))
    >>> moon = Body.from_tuple_parameters("Moon", 0.0735*(10**24), 100.0, (1.496*(10**11), -384.4*(10**6), -69834), (1050, 29290, 0))
    >>> absolute_distance_to_one(moon, earth)
    384400006.34337604
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
    forceratio = force / distance

    return (distance_vector * forceratio) / one_body.mass

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

def calculate_velocity(one_body: Body, other_bodies: [Body], delta_time: float) -> None:
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
        >>> calculate_velocity(kg, [kg, e1, e2, e3, e4, e5, e6], 314.0)
        array([[ 0.],
               [ 0.],
               [ 0.]])

        >>> kg = Body.from_tuple_parameters("kg", 1.0, 100.0, (0, 0, 0), (0, 0, 0))
        >>> earth1 = Body.from_tuple_parameters("Earth1", (5.972*(10**24)), 100.0, (0, 6371000, 6280), (0, 0, 0))
        >>> moon = Body.from_tuple_parameters("Moon", 0.0735*(10**24), 100.0, (0, 384.4*(10**6), -1000), (0, 0, 0))
        >>> calculate_velocity(kg, [kg, earth1, moon], 16.0)
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
    radius = ((one_body.radius ** 3) + (other_body.radius ** 3)) ** (1/3)

    if one_body.mass >= other_body.mass:
        name = one_body.mass
    else:
        name = other_body.mass

    return Body(name, mass, radius, position, velocity)

def calculate_force(one_mass, other_mass, distance):
    return (6.67408 * (10 ** -11)) * ((one_mass * other_mass) / (distance ** 2))
