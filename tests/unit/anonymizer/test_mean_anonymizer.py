import unittest
import numpy as np
from diffpriv_laplace.anonymizer.mean import DiffPrivMeanAnonymizer


class TestDiffPrivMeanAnonymizer(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def set_seed(self):
        np.random.seed(31337)

    def test_length_getter(self):
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        anonymizer = DiffPrivMeanAnonymizer(epsilon, lower, upper, n)
        self.assertEqual(anonymizer.n, n)

    def test_lower_getter(self):
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        anonymizer = DiffPrivMeanAnonymizer(epsilon, lower, upper, n)
        self.assertEqual(anonymizer.lower, lower)

    def test_upper_getter(self):
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        anonymizer = DiffPrivMeanAnonymizer(epsilon, lower, upper, n)
        self.assertEqual(anonymizer.upper, upper)

    def test_global_sensitivity_getter(self):
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        gs_value = (upper - lower) / n
        anonymizer = DiffPrivMeanAnonymizer(epsilon, lower, upper, n)
        np.testing.assert_almost_equal(anonymizer.global_sensitivity.value, gs_value)

    def test_epsilon_getter(self):
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        anonymizer = DiffPrivMeanAnonymizer(epsilon, lower, upper, n)
        self.assertEqual(anonymizer.epsilon, epsilon)

    def test_scale_getter(self):
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        gs_value = (upper - lower) / n
        scale = gs_value / epsilon
        anonymizer = DiffPrivMeanAnonymizer(epsilon, lower, upper, n)
        self.assertEqual(anonymizer.scale, scale)

    def test_apply_single(self):
        expected_value = 87.52194507326827
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        anonymizer = DiffPrivMeanAnonymizer(epsilon, lower, upper, n)
        self.set_seed()
        value = anonymizer.apply(87.0)
        np.testing.assert_almost_equal(value, expected_value)

    def test_apply_single_many(self):
        expected_values = np.array([87.5219451, 89.4041544, 86.5122696])
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        anonymizer = DiffPrivMeanAnonymizer(epsilon, lower, upper, n)
        self.set_seed()
        values = anonymizer.apply(87.0, size=3)
        np.testing.assert_almost_equal(values, expected_values)

    def test_apply_multiple(self):
        expected_values = np.array([87.5219451, 437.4041544])
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        anonymizer = DiffPrivMeanAnonymizer(epsilon, lower, upper, n)
        self.set_seed()
        values = anonymizer.apply([87.0, 435.0])
        np.testing.assert_almost_equal(values, expected_values)
