from diffpriv_laplace.global_sensitivity.base import GlobalSensitivity


class MedianGlobalSensitivity(GlobalSensitivity):
    def __init__(self):
        super().__init__(1.0)
