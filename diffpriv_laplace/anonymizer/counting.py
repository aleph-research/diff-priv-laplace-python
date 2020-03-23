from diffpriv_laplace.global_sensitivity.counting import CountingGlobalSensitivity
from diffpriv_laplace.anonymizer.base import DiffPrivAnonymizer


class DiffPrivCountingAnonymizer(DiffPrivAnonymizer):
    def __init__(self, epsilon):
        gs = CountingGlobalSensitivity()
        super().__init__(gs, epsilon)
