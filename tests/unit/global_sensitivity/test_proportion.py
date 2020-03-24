import unittest
from diffpriv_laplace.global_sensitivity.proportion import ProportionGlobalSensitivity


class TestProportionGlobalSensitivity(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_value(self):
        n = 100.0
        value = 1.0 / n
        gs = ProportionGlobalSensitivity(n)
        self.assertEqual(gs.value, value)

    def test_length_getter(self):
        n = 100.0
        gs = ProportionGlobalSensitivity(n)
        self.assertEqual(gs.n, n)
