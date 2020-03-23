from diffpriv_laplace.global_sensitivity.base import GlobalSensitivity


class ProportionGlobalSensitivity(GlobalSensitivity):
    @classmethod
    def calculate_value(cls, n):
        value = 1.0 / n
        return value

    def __init__(self, n):
        self.__n = float(n)
        super().__init__(self.calculate_value(self.__n))

    @property
    def n(self):
        return self.__n
