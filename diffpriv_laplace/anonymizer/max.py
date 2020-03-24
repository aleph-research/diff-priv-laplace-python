from diffpriv_laplace.global_sensitivity.max import MaxGlobalSensitivity
from diffpriv_laplace.anonymizer.base import DiffPrivAnonymizer


class DiffPrivMaxAnonymizer(DiffPrivAnonymizer):
    def __init__(self, epsilon):
        gs = MaxGlobalSensitivity()
        super().__init__(gs, epsilon)
