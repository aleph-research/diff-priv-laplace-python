import unittest
from diffpriv_laplace.global_sensitivity.base import GlobalSensitivity


class TestGlobalSensitivity(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_getter(self):
        value = 5
        gs = GlobalSensitivity(value)
        self.assertEqual(gs.value, value)

    def test_setter(self):
        value = 5
        gs = GlobalSensitivity(value)
        new_value = 6
        gs.value = new_value
        self.assertEqual(gs.value, new_value)
