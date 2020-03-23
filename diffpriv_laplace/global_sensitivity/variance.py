import numpy as np
from diffpriv_laplace.global_sensitivity.base import GlobalSensitivity


class VarianceGlobalSensitivity(GlobalSensitivity):
    @classmethod
    def calculate_value(cls, lower, upper, n):
        value = np.square(upper - lower) / n
        return value

    def __init__(self, lower, upper, n):
        self.__lower = float(lower)
        self.__upper = float(upper)
        self.__n = float(n)
        super().__init__(self.calculate_value(self.__lower, self.__upper, self.__n))

    @property
    def lower(self):
        return self.__lower

    @property
    def upper(self):
        return self.__upper

    @property
    def n(self):
        return self.__n
