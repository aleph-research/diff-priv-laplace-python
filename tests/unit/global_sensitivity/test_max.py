import unittest
from diffpriv_laplace.global_sensitivity.max import MaxGlobalSensitivity


class TestMaxGlobalSensitivity(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_value(self):
        gs = MaxGlobalSensitivity()
        self.assertEqual(gs.value, 1.0)
