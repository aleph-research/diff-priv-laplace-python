import unittest
from diffpriv_laplace.global_sensitivity.counting import CountingGlobalSensitivity


class TestCountingGlobalSensitivity(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_value(self):
        gs = CountingGlobalSensitivity()
        self.assertEqual(gs.value, 1.0)
