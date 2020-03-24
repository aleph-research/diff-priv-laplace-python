import unittest
import numpy as np
from diffpriv_laplace.anonymizer.sum import DiffPrivSumAnonymizer


class TestDiffPrivSumAnonymizer(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def set_seed(self):
        np.random.seed(31337)

    def test_lower_getter(self):
        lower = 10.0
        upper = 99.0
        epsilon = 1.0
        anonymizer = DiffPrivSumAnonymizer(epsilon, lower, upper)
        self.assertEqual(anonymizer.lower, lower)

    def test_upper_getter(self):
        lower = 10.0
        upper = 99.0
        epsilon = 1.0
        anonymizer = DiffPrivSumAnonymizer(epsilon, lower, upper)
        self.assertEqual(anonymizer.upper, upper)

    def test_global_sensitivity_getter(self):
        lower = 10.0
        upper = 99.0
        epsilon = 1.0
        gs_value = np.max([np.abs(lower), np.abs(upper)])
        anonymizer = DiffPrivSumAnonymizer(epsilon, lower, upper)
        np.testing.assert_almost_equal(anonymizer.global_sensitivity.value, gs_value)

    def test_epsilon_getter(self):
        lower = 10.0
        upper = 99.0
        epsilon = 1.0
        anonymizer = DiffPrivSumAnonymizer(epsilon, lower, upper)
        self.assertEqual(anonymizer.epsilon, epsilon)

    def test_scale_getter(self):
        lower = 10.0
        upper = 99.0
        epsilon = 1.0
        gs_value = np.max([np.abs(lower), np.abs(upper)])
        scale = gs_value / epsilon
        anonymizer = DiffPrivSumAnonymizer(epsilon, lower, upper)
        self.assertEqual(anonymizer.scale, scale)

    def test_apply_single(self):
        expected_value = 145.05905871186388
        lower = 10.0
        upper = 99.0
        epsilon = 1.0
        anonymizer = DiffPrivSumAnonymizer(epsilon, lower, upper)
        self.set_seed()
        value = anonymizer.apply(87.0)
        np.testing.assert_almost_equal(value, expected_value)

    def test_apply_single_many(self):
        expected_values = np.array([145.0590587, 354.4284063, 32.746848])
        lower = 10.0
        upper = 99.0
        epsilon = 1.0
        anonymizer = DiffPrivSumAnonymizer(epsilon, lower, upper)
        self.set_seed()
        values = anonymizer.apply(87.0, size=3)
        np.testing.assert_almost_equal(values, expected_values)

    def test_apply_multiple(self):
        expected_values = np.array([145.0590587, 702.4284063])
        lower = 10.0
        upper = 99.0
        epsilon = 1.0
        anonymizer = DiffPrivSumAnonymizer(epsilon, lower, upper)
        self.set_seed()
        values = anonymizer.apply([87.0, 435.0])
        np.testing.assert_almost_equal(values, expected_values)
