from diffpriv_laplace.global_sensitivity.proportion import ProportionGlobalSensitivity
from diffpriv_laplace.anonymizer.base import DiffPrivAnonymizer


class DiffPrivProportionAnonymizer(DiffPrivAnonymizer):
    def __init__(self, epsilon, n):
        gs = ProportionGlobalSensitivity(n)
        super().__init__(gs, epsilon)

    @property
    def n(self):
        return self.global_sensitivity.n
