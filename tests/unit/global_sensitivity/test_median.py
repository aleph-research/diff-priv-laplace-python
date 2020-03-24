import unittest
from diffpriv_laplace.global_sensitivity.median import MedianGlobalSensitivity


class TestMedianGlobalSensitivity(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_value(self):
        gs = MedianGlobalSensitivity()
        self.assertEqual(gs.value, 1.0)
