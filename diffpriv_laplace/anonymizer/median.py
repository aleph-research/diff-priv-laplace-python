from diffpriv_laplace.global_sensitivity.median import MedianGlobalSensitivity
from diffpriv_laplace.anonymizer.base import DiffPrivAnonymizer


class DiffPrivMedianAnonymizer(DiffPrivAnonymizer):
    def __init__(self, epsilon):
        gs = MedianGlobalSensitivity()
        super().__init__(gs, epsilon)
