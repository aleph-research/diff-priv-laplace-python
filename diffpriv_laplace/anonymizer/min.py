from diffpriv_laplace.global_sensitivity.min import MinGlobalSensitivity
from diffpriv_laplace.anonymizer.base import DiffPrivAnonymizer


class DiffPrivMinAnonymizer(DiffPrivAnonymizer):
    def __init__(self, epsilon):
        gs = MinGlobalSensitivity()
        super().__init__(gs, epsilon)
