import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.animation import FuncAnimation

class TestOutputWriter(object):
    def __init__(self, body_states):
        plt.ion()

        self.__fig = plt.figure()
        self.__ax = self.__fig.add_subplot(111, projection='3d')

        self.__body_states = body_states

        self.draw()
    
    def draw(self):
        self.__ax.clear()

        state = next(self.__body_states)

        positions = [b.position for b in state.bodies]
        position_tuples = [(p[0][0], p[1][0], p[2][0]) for p in positions]

        ix = [p[0] for p in position_tuples]
        iy = [p[1] for p in position_tuples]
        iz = [p[2] for p in position_tuples]

        labels = [b.name for b in state.bodies]
        
        radius = [b.radius for b in state.bodies]

        self.__ax.scatter(ix, iy, iz, c='k', s=radius)
    
        plt.show()
    
    def __get_points(self, n):
        return np.random.rand(3, n, 1)
