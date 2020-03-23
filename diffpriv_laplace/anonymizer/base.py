import numpy as np


class DiffPrivAnonymizer(object):
    @classmethod
    def calculate_scale(cls, gs, epsilon):
        scale = gs.value / epsilon
        return scale

    def __init__(self, gs, epsilon):
        super().__init__()
        self.__gs = gs
        self.__epsilon = float(epsilon)
        self.__scale = self.calculate_scale(self.__gs, self.__epsilon)

    def apply(self, values, size=None):
        samples = np.random.laplace(loc=values, scale=self.__scale, size=size)
        return samples

    @property
    def scale(self):
        return self.__scale

    @property
    def global_sensitivity(self):
        return self.__gs

    @property
    def epsilon(self):
        return self.__epsilon
