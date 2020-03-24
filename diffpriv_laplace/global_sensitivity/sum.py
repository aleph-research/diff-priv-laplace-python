import numpy as np
from diffpriv_laplace.global_sensitivity.base import GlobalSensitivity


class SumGlobalSensitivity(GlobalSensitivity):
    @classmethod
    def calculate_value(cls, lower, upper):
        value = np.max([np.abs(upper), np.abs(lower)])
        return value

    def __init__(self, lower, upper):
        self.__lower = float(lower)
        self.__upper = float(upper)
        super().__init__(self.calculate_value(self.__lower, self.__upper))

    @property
    def lower(self):
        return self.__lower

    @property
    def upper(self):
        return self.__upper
