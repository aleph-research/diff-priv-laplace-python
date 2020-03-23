import unittest
import mock
import numpy as np
from diffpriv_laplace.anonymizer.base import DiffPrivAnonymizer


class TestDiffPrivAnonymizer(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def set_seed(self):
        np.random.seed(31337)

    def create_mock_gs(self):
        gs = mock.MagicMock()
        type(gs).value = mock.PropertyMock(return_value=1.0)
        return gs

    def test_global_sensitivity_getter(self):
        gs = self.create_mock_gs()
        epsilon = 1.0
        anonymizer = DiffPrivAnonymizer(gs, epsilon)
        self.assertEqual(anonymizer.global_sensitivity, gs)
        self.assertEqual(anonymizer.global_sensitivity.value, gs.value)

    def test_epsilon_getter(self):
        gs = self.create_mock_gs()
        epsilon = 1.0
        anonymizer = DiffPrivAnonymizer(gs, epsilon)
        self.assertEqual(anonymizer.epsilon, epsilon)

    def test_scale_getter(self):
        gs = self.create_mock_gs()
        epsilon = 1.0
        scale = gs.value / epsilon
        anonymizer = DiffPrivAnonymizer(gs, epsilon)
        self.assertEqual(anonymizer.scale, scale)

    def test_apply_single_one(self):
        expected_value = 87.58645513850368
        gs = self.create_mock_gs()
        epsilon = 1.0
        anonymizer = DiffPrivAnonymizer(gs, epsilon)
        self.set_seed()
        value = anonymizer.apply(87.0)
        np.testing.assert_almost_equal(value, expected_value)

    def test_apply_single_many(self):
        expected_values = np.array([87.5864551, 89.701297, 86.4519884])
        gs = self.create_mock_gs()
        epsilon = 1.0
        anonymizer = DiffPrivAnonymizer(gs, epsilon)
        self.set_seed()
        values = anonymizer.apply(87.0, size=3)
        np.testing.assert_almost_equal(values, expected_values)

    def test_apply_multiple(self):
        expected_values = np.array([87.5864551, 437.701297])
        gs = self.create_mock_gs()
        epsilon = 1.0
        anonymizer = DiffPrivAnonymizer(gs, epsilon)
        self.set_seed()
        values = anonymizer.apply([87.0, 435.0])
        np.testing.assert_almost_equal(values, expected_values)
