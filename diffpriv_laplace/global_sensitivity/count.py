from diffpriv_laplace.global_sensitivity.base import GlobalSensitivity


class CountGlobalSensitivity(GlobalSensitivity):
    def __init__(self):
        super().__init__(1.0)
