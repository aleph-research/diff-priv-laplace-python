import unittest
import numpy as np
from itertools import combinations
from functools import reduce
from diffpriv_laplace import DiffPrivStatistics, DiffPrivStatisticKind


class TestDiffPrivStatistics(unittest.TestCase):
    epsilon = 100000
    decimal_places = 2

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def set_seed(self):
        np.random.seed(31337)

    def test_count_single(self):
        data = np.array([True, False, True, True] * 10)
        expected_value = 30.0
        self.set_seed()
        value = DiffPrivStatistics.count(data, self.epsilon)
        self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_count_single_with_condition(self):
        data = np.array([0.1, -0.1, 0.1, 0.1] * 10)
        expected_value = 30.0

        def condition(data):
            return data >= 0.0

        self.set_seed()
        value = DiffPrivStatistics.count(data, self.epsilon, condition=condition)
        self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_count_multiple(self):
        data = np.array([[True, False, True, True] * 10] * 3)
        expected_values = np.array([30.0] * 3)
        self.set_seed()
        value = DiffPrivStatistics.count(data, self.epsilon, axis=1)
        np.testing.assert_almost_equal(value, expected_values, self.decimal_places)

    def test_count_multiple_with_condition(self):
        data = np.array([[0.1, -0.1, 0.1, 0.1] * 10] * 3)
        expected_values = np.array([30.0] * 3)

        def condition(data):
            return data >= 0.0

        self.set_seed()
        value = DiffPrivStatistics.count(
            data, self.epsilon, condition=condition, axis=1
        )
        np.testing.assert_almost_equal(value, expected_values, self.decimal_places)

    def test_min_single(self):
        data = list(range(3, 20))
        data.reverse()
        data = np.array(data)
        expected_value = 3.0
        self.set_seed()
        value = DiffPrivStatistics.min(data, self.epsilon)
        self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_min_multiple(self):
        data = list(range(3, 20))
        data.reverse()
        data = np.array([data] * 3)
        expected_values = np.array([3.0] * 3)
        self.set_seed()
        value = DiffPrivStatistics.min(data, self.epsilon, axis=1)
        np.testing.assert_almost_equal(value, expected_values, self.decimal_places)

    def test_max_single(self):
        data = np.array(list(range(3, 20)))
        expected_value = 19.0
        self.set_seed()
        value = DiffPrivStatistics.max(data, self.epsilon)
        self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_max_multiple(self):
        data = np.array([list(range(3, 20))] * 3)
        expected_values = np.array([19.0] * 3)
        self.set_seed()
        value = DiffPrivStatistics.max(data, self.epsilon, axis=1)
        np.testing.assert_almost_equal(value, expected_values, self.decimal_places)

    def test_median_single(self):
        data = np.array(list(range(0, 20)) + [100.0])
        expected_value = 10.0
        self.set_seed()
        value = DiffPrivStatistics.median(data, self.epsilon)
        self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_median_multiple(self):
        data = np.array([list(range(0, 20)) + [100.0]] * 3)
        expected_values = np.array([10.0] * 3)

        self.set_seed()
        value = DiffPrivStatistics.median(data, self.epsilon, axis=1)
        np.testing.assert_almost_equal(value, expected_values, self.decimal_places)

    def test_proportion_single(self):
        data = np.array([True, False, True, True] * 10)
        expected_value = 0.75
        self.set_seed()
        value = DiffPrivStatistics.proportion(data, self.epsilon)
        self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_proportion_single_with_condition(self):
        data = np.array([0.1, -0.1, 0.1, 0.1] * 10)
        expected_value = 0.75

        def condition(data):
            return data >= 0.0

        self.set_seed()
        value = DiffPrivStatistics.proportion(data, self.epsilon, condition=condition)
        self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_proportion_multiple(self):
        data = np.array([[True, False, True, True] * 10] * 3)
        expected_values = np.array([0.75] * 3)
        self.set_seed()
        value = DiffPrivStatistics.proportion(data, self.epsilon, axis=1)
        np.testing.assert_almost_equal(value, expected_values, self.decimal_places)

    def test_proportion_multiple_with_condition(self):
        data = np.array([[0.1, -0.1, 0.1, 0.1] * 10] * 3)
        expected_values = np.array([0.75] * 3)

        def condition(data):
            return data >= 0.0

        self.set_seed()
        value = DiffPrivStatistics.proportion(
            data, self.epsilon, condition=condition, axis=1
        )
        np.testing.assert_almost_equal(value, expected_values, self.decimal_places)

    def test_sum_single(self):
        data = np.array(list(range(0, 20)))
        expected_value = 190.0
        self.set_seed()
        value = DiffPrivStatistics.sum(data, self.epsilon)
        self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_sum_multiple(self):
        data = np.array([list(range(0, 20))] * 3)
        expected_values = np.array([190.0] * 3)
        self.set_seed()
        value = DiffPrivStatistics.sum(data, self.epsilon, axis=1)
        np.testing.assert_almost_equal(value, expected_values, self.decimal_places)

    def test_mean_single(self):
        data = np.array(list(range(0, 20)) + [100.0])
        expected_value = 13.81
        self.set_seed()
        value = DiffPrivStatistics.mean(data, self.epsilon)
        self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_mean_multiple(self):
        data = np.array([list(range(0, 20)) + [100.0]] * 3)
        expected_values = np.array([13.81] * 3)

        self.set_seed()
        value = DiffPrivStatistics.mean(data, self.epsilon, axis=1)
        np.testing.assert_almost_equal(value, expected_values, self.decimal_places)

    def test_variance_single(self):
        data = np.array(list(range(0, 20)) + [100.0])
        expected_value = 403.106
        self.set_seed()
        value = DiffPrivStatistics.variance(data, self.epsilon)
        self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_variance_multiple(self):
        data = np.array([list(range(0, 20)) + [100.0]] * 3)
        expected_values = np.array([403.106] * 3)

        self.set_seed()
        value = DiffPrivStatistics.variance(data, self.epsilon, axis=1)
        np.testing.assert_almost_equal(value, expected_values, self.decimal_places)


class TestDiffPrivStatisticsKind(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_size(self):
        kinds = []
        for kind in DiffPrivStatisticKind:
            if kind != DiffPrivStatisticKind.all:
                kinds.append(kind)

        for r in range(1, len(kinds) + 1):
            combinations_values = combinations(kinds, r)
            for combination in list(combinations_values):
                values = reduce(lambda a, b: a | b, combination)
                self.assertEqual(values.size, r)

    def test_size_all(self):
        self.assertEqual(DiffPrivStatisticKind.all.size, len(DiffPrivStatisticKind) - 1)
        self.assertEqual(
            (DiffPrivStatisticKind.all | DiffPrivStatisticKind.all).size,
            len(DiffPrivStatisticKind) - 1,
        )
