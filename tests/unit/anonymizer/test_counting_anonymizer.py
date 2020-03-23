import unittest
import numpy as np
from diffpriv_laplace.anonymizer.counting import DiffPrivCountingAnonymizer


class TestDiffPrivCountingAnonymizer(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def set_seed(self):
        np.random.seed(31337)

    def test_global_sensitivity_getter(self):
        epsilon = 1.0
        anonymizer = DiffPrivCountingAnonymizer(epsilon)
        self.assertEqual(anonymizer.global_sensitivity.value, 1.0)

    def test_epsilon_getter(self):
        epsilon = 1.0
        anonymizer = DiffPrivCountingAnonymizer(epsilon)
        self.assertEqual(anonymizer.epsilon, epsilon)

    def test_scale_getter(self):
        epsilon = 1.0
        scale = 1.0 / epsilon
        anonymizer = DiffPrivCountingAnonymizer(epsilon)
        self.assertEqual(anonymizer.scale, scale)

    def test_apply_single(self):
        expected_value = 87.58645513850368
        epsilon = 1.0
        anonymizer = DiffPrivCountingAnonymizer(epsilon)
        self.set_seed()
        value = anonymizer.apply(87.0)
        np.testing.assert_almost_equal(value, expected_value)

    def test_apply_single_many(self):
        expected_values = np.array([87.5864551, 89.701297, 86.4519884])
        epsilon = 1.0
        anonymizer = DiffPrivCountingAnonymizer(epsilon)
        self.set_seed()
        values = anonymizer.apply(87.0, size=3)
        np.testing.assert_almost_equal(values, expected_values)

    def test_apply_multiple(self):
        expected_values = np.array([87.5864551, 437.701297])
        epsilon = 1.0
        anonymizer = DiffPrivCountingAnonymizer(epsilon)
        self.set_seed()
        values = anonymizer.apply([87.0, 435.0])
        np.testing.assert_almost_equal(values, expected_values)
