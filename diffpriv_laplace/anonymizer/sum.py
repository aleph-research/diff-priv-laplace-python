from diffpriv_laplace.global_sensitivity.sum import SumGlobalSensitivity
from diffpriv_laplace.anonymizer.base import DiffPrivAnonymizer


class DiffPrivSumAnonymizer(DiffPrivAnonymizer):
    def __init__(self, epsilon, lower, upper):
        gs = SumGlobalSensitivity(lower, upper)
        super().__init__(gs, epsilon)

    @property
    def lower(self):
        return self.global_sensitivity.lower

    @property
    def upper(self):
        return self.global_sensitivity.upper
