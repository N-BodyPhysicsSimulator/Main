import numpy as np
import os

class CSVOutputWriter(object):
    def __init__(self, pipe, kwargs):
        path = kwargs.get('path')

        if not os.path.isdir(path):
            raise ValueError("Path %s is not a valid path." % path)
        
        while True:
            self.__tick(path, pipe.recv())

    def __tick(self, path, body_state):
        for body in body_state.bodies:
            filepath = os.path.join(path, (body.name + '.csv') )

            if not os.path.exists(filepath):
                f = open(filepath, 'a+')
                f.write('name,mass,radius,pos.x,pos.y,pos.z,vel.x,vel.y,vel.z,ticks,time,delta_time')
                f.close()

            data  = [body.name, body.mass, body.radius]
            data += self.__to_list(body.position)
            data += self.__to_list(body.velocity)
            data += [body_state.ticks, body_state.time, body_state.delta_time]

            f = open(filepath, 'a+')
            f.write("\n")
            f.write(','.join([str(item) for item in data]))
            f.close()

    def __to_list(self, item):
        return [item[0][0], item[1][0], item[2][0]]

