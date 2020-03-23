import unittest
from diffpriv_laplace.global_sensitivity.mean import MeanGlobalSensitivity


class TestMeanGlobalSensitivity(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_value(self):
        lower = 10.0
        upper = 99.0
        n = 100.0
        value = (upper - lower) / n
        gs = MeanGlobalSensitivity(lower, upper, n)
        self.assertEqual(gs.value, value)

    def test_length_getter(self):
        lower = 10.0
        upper = 99.0
        n = 100.0
        gs = MeanGlobalSensitivity(lower, upper, n)
        self.assertEqual(gs.n, n)

    def test_lower_getter(self):
        lower = 10.0
        upper = 99.0
        n = 100.0
        gs = MeanGlobalSensitivity(lower, upper, n)
        self.assertEqual(gs.lower, lower)

    def test_upper_getter(self):
        lower = 10.0
        upper = 99.0
        n = 100.0
        gs = MeanGlobalSensitivity(lower, upper, n)
        self.assertEqual(gs.upper, upper)
