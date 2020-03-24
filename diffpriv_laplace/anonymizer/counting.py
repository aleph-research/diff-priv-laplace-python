from diffpriv_laplace.anonymizer.count import DiffPrivCountAnonymizer


class DiffPrivCountingAnonymizer(DiffPrivCountAnonymizer):
    def __init__(self, epsilon):
        super().__init__(epsilon)
