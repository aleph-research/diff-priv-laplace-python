import unittest
import numpy as np
from diffpriv_laplace.anonymizer.proportion import DiffPrivProportionAnonymizer


class TestDiffPrivProportionAnonymizer(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def set_seed(self):
        np.random.seed(31337)

    def test_length_getter(self):
        n = 10.0
        epsilon = 1.0
        anonymizer = DiffPrivProportionAnonymizer(epsilon, n)
        self.assertEqual(anonymizer.n, n)

    def test_global_sensitivity_getter(self):
        n = 10.0
        epsilon = 1.0
        gs_value = 1.0 / n
        anonymizer = DiffPrivProportionAnonymizer(epsilon, n)
        np.testing.assert_almost_equal(anonymizer.global_sensitivity.value, gs_value)

    def test_epsilon_getter(self):
        n = 10.0
        epsilon = 1.0
        anonymizer = DiffPrivProportionAnonymizer(epsilon, n)
        self.assertEqual(anonymizer.epsilon, epsilon)

    def test_scale_getter(self):
        n = 10.0
        gs_value = 1.0 / n
        epsilon = 1.0
        scale = gs_value / epsilon
        anonymizer = DiffPrivProportionAnonymizer(epsilon, n)
        self.assertEqual(anonymizer.scale, scale)

    def test_apply_single(self):
        expected_value = 87.05864551385037
        n = 10.0
        epsilon = 1.0
        anonymizer = DiffPrivProportionAnonymizer(epsilon, n)
        self.set_seed()
        value = anonymizer.apply(87.0)
        np.testing.assert_almost_equal(value, expected_value)

    def test_apply_single_many(self):
        expected_values = np.array([87.0586455, 87.2701297, 86.9451988])
        n = 10.0
        epsilon = 1.0
        anonymizer = DiffPrivProportionAnonymizer(epsilon, n)
        self.set_seed()
        values = anonymizer.apply(87.0, size=3)
        np.testing.assert_almost_equal(values, expected_values)

    def test_apply_multiple(self):
        expected_values = np.array([87.0586455, 435.2701297])
        n = 10.0
        epsilon = 1.0
        anonymizer = DiffPrivProportionAnonymizer(epsilon, n)
        self.set_seed()
        values = anonymizer.apply([87.0, 435.0])
        np.testing.assert_almost_equal(values, expected_values)
