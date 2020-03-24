import unittest
import numpy as np
from diffpriv_laplace.anonymizer.variance import DiffPrivVarianceAnonymizer


class TestDiffPrivVarianceAnonymizer(unittest.TestCase):
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
        anonymizer = DiffPrivVarianceAnonymizer(epsilon, lower, upper, n)
        self.assertEqual(anonymizer.n, n)

    def test_lower_getter(self):
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        anonymizer = DiffPrivVarianceAnonymizer(epsilon, lower, upper, n)
        self.assertEqual(anonymizer.lower, lower)

    def test_upper_getter(self):
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        anonymizer = DiffPrivVarianceAnonymizer(epsilon, lower, upper, n)
        self.assertEqual(anonymizer.upper, upper)

    def test_global_sensitivity_getter(self):
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        gs_value = np.square(upper - lower) / n
        anonymizer = DiffPrivVarianceAnonymizer(epsilon, lower, upper, n)
        np.testing.assert_almost_equal(anonymizer.global_sensitivity.value, gs_value)

    def test_epsilon_getter(self):
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        anonymizer = DiffPrivVarianceAnonymizer(epsilon, lower, upper, n)
        self.assertEqual(anonymizer.epsilon, epsilon)

    def test_scale_getter(self):
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        gs_value = np.square(upper - lower) / n
        scale = gs_value / epsilon
        anonymizer = DiffPrivVarianceAnonymizer(epsilon, lower, upper, n)
        self.assertEqual(anonymizer.scale, scale)

    def test_apply_single(self):
        expected_value = 133.45311152087612
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        anonymizer = DiffPrivVarianceAnonymizer(epsilon, lower, upper, n)
        self.set_seed()
        value = anonymizer.apply(87.0)
        np.testing.assert_almost_equal(value, expected_value)

    def test_apply_single_many(self):
        expected_values = np.array([133.4531115, 300.969738, 43.5919983])
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        anonymizer = DiffPrivVarianceAnonymizer(epsilon, lower, upper, n)
        self.set_seed()
        values = anonymizer.apply(87.0, size=3)
        np.testing.assert_almost_equal(values, expected_values)

    def test_apply_multiple(self):
        expected_values = np.array([133.4531115, 648.969738])
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        anonymizer = DiffPrivVarianceAnonymizer(epsilon, lower, upper, n)
        self.set_seed()
        values = anonymizer.apply([87.0, 435.0])
        np.testing.assert_almost_equal(values, expected_values)
