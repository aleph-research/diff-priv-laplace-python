from diffpriv_laplace.global_sensitivity.mean import MeanGlobalSensitivity
from diffpriv_laplace.anonymizer.base import DiffPrivAnonymizer


class DiffPrivMeanAnonymizer(DiffPrivAnonymizer):
    def __init__(self, epsilon, lower, upper, n):
        gs = MeanGlobalSensitivity(lower, upper, n)
        super().__init__(gs, epsilon)

    @property
    def lower(self):
        return self.global_sensitivity.lower

    @property
    def upper(self):
        return self.global_sensitivity.upper

    @property
    def n(self):
        return self.global_sensitivity.n
