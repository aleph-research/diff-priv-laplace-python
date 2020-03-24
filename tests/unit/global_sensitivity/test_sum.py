import unittest
import numpy as np
from diffpriv_laplace.global_sensitivity.sum import SumGlobalSensitivity


class TestSumGlobalSensitivity(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_value(self):
        lower = 10.0
        upper = 99.0
        value = np.max([np.abs(lower), np.abs(upper)])
        gs = SumGlobalSensitivity(lower, upper)
        self.assertEqual(gs.value, value)

    def test_lower_getter(self):
        lower = 10.0
        upper = 99.0
        gs = SumGlobalSensitivity(lower, upper)
        self.assertEqual(gs.lower, lower)

    def test_upper_getter(self):
        lower = 10.0
        upper = 99.0
        gs = SumGlobalSensitivity(lower, upper)
        self.assertEqual(gs.upper, upper)
