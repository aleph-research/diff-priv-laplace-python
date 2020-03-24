from diffpriv_laplace.global_sensitivity.count import CountGlobalSensitivity
from diffpriv_laplace.anonymizer.base import DiffPrivAnonymizer


class DiffPrivCountAnonymizer(DiffPrivAnonymizer):
    def __init__(self, epsilon):
        gs = CountGlobalSensitivity()
        super().__init__(gs, epsilon)
