import unittest
from diffpriv_laplace.global_sensitivity.min import MinGlobalSensitivity


class TestMinGlobalSensitivity(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_value(self):
        gs = MinGlobalSensitivity()
        self.assertEqual(gs.value, 1.0)
