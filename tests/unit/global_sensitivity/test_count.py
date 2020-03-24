import unittest
from diffpriv_laplace.global_sensitivity.count import CountGlobalSensitivity


class TestCountGlobalSensitivity(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_value(self):
        gs = CountGlobalSensitivity()
        self.assertEqual(gs.value, 1.0)
