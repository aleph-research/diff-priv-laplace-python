import unittest
import numpy as np
from itertools import combinations
from functools import reduce
from diffpriv_laplace import DiffPrivStatistics, DiffPrivStatisticKind
from diffpriv_laplace.statistics import (
    DiffPrivStatisticsInvalidDimensions,
    DiffPrivStatisticsSizeMismatch,
)


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


class TestDiffPrivStatistics(unittest.TestCase):
    epsilon = 1000000
    decimal_places = 2

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def set_seed(self):
        np.random.seed(31337)

    def test_count_single(self):
        data = np.array([True, False, True, True] * 10)
        expected_value = np.count_nonzero(data)
        self.set_seed()
        value = DiffPrivStatistics.count(data, self.epsilon)
        self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_count_single_with_condition(self):
        data = np.array([0.1, -0.1, 0.1, 0.1] * 10)
        expected_value = np.count_nonzero(data >= 0)

        def condition(data):
            return data >= 0.0

        self.set_seed()
        value = DiffPrivStatistics.count(data, self.epsilon, condition=condition)
        self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_count_multiple(self):
        data = np.array([[True, False, True, True] * 10] * 3)
        expected_values = np.count_nonzero(data, axis=1)
        self.set_seed()
        value = DiffPrivStatistics.count(data, self.epsilon, axis=1)
        np.testing.assert_almost_equal(value, expected_values, self.decimal_places)

    def test_count_multiple_with_condition(self):
        data = np.array([[0.1, -0.1, 0.1, 0.1] * 10] * 3)
        expected_values = np.count_nonzero(data >= 0, axis=1)

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
        expected_value = np.min(data)
        self.set_seed()
        value = DiffPrivStatistics.min(data, self.epsilon)
        self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_min_multiple(self):
        data = list(range(3, 20))
        data.reverse()
        data = np.array([data] * 3)
        expected_values = np.min(data, axis=1)
        self.set_seed()
        value = DiffPrivStatistics.min(data, self.epsilon, axis=1)
        np.testing.assert_almost_equal(value, expected_values, self.decimal_places)

    def test_max_single(self):
        data = np.array(list(range(3, 20)))
        expected_value = np.max(data)
        self.set_seed()
        value = DiffPrivStatistics.max(data, self.epsilon)
        self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_max_multiple(self):
        data = np.array([list(range(3, 20))] * 3)
        expected_values = np.max(data, axis=1)
        self.set_seed()
        value = DiffPrivStatistics.max(data, self.epsilon, axis=1)
        np.testing.assert_almost_equal(value, expected_values, self.decimal_places)

    def test_median_single(self):
        data = np.array(list(range(0, 20)) + [100.0])
        expected_value = np.median(data)
        self.set_seed()
        value = DiffPrivStatistics.median(data, self.epsilon)
        self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_median_multiple(self):
        data = np.array([list(range(0, 20)) + [100.0]] * 3)
        expected_values = np.median(data, axis=1)

        self.set_seed()
        value = DiffPrivStatistics.median(data, self.epsilon, axis=1)
        np.testing.assert_almost_equal(value, expected_values, self.decimal_places)

    def test_proportion_single(self):
        data = np.array([True, False, True, True] * 10)
        expected_value = np.count_nonzero(data)
        expected_value = np.divide(expected_value, np.size(data))
        self.set_seed()
        value = DiffPrivStatistics.proportion(data, self.epsilon)
        self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_proportion_single_with_condition(self):
        data = np.array([0.1, -0.1, 0.1, 0.1] * 10)
        expected_value = np.count_nonzero(data >= 0)
        expected_value = np.divide(expected_value, np.size(data))

        def condition(data):
            return data >= 0.0

        self.set_seed()
        value = DiffPrivStatistics.proportion(data, self.epsilon, condition=condition)
        self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_proportion_multiple(self):
        data = np.array([[True, False, True, True] * 10] * 3)
        expected_values = np.count_nonzero(data, axis=1)
        expected_values = np.divide(expected_values, np.size(data, axis=1))
        self.set_seed()
        value = DiffPrivStatistics.proportion(data, self.epsilon, axis=1)
        np.testing.assert_almost_equal(value, expected_values, self.decimal_places)

    def test_proportion_multiple_with_condition(self):
        data = np.array([[0.1, -0.1, 0.1, 0.1] * 10] * 3)
        expected_values = np.count_nonzero(data >= 0.0, axis=1)
        expected_values = np.divide(expected_values, np.size(data, axis=1))

        def condition(data):
            return data >= 0.0

        self.set_seed()
        value = DiffPrivStatistics.proportion(
            data, self.epsilon, condition=condition, axis=1
        )
        np.testing.assert_almost_equal(value, expected_values, self.decimal_places)

    def test_sum_single(self):
        data = np.array(list(range(0, 20)))
        expected_value = np.sum(data)
        self.set_seed()
        value = DiffPrivStatistics.sum(data, self.epsilon)
        self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_sum_multiple(self):
        data = np.array([list(range(0, 20))] * 3)
        expected_values = np.sum(data, axis=1)
        self.set_seed()
        value = DiffPrivStatistics.sum(data, self.epsilon, axis=1)
        np.testing.assert_almost_equal(value, expected_values, self.decimal_places)

    def test_mean_single(self):
        data = np.array(list(range(0, 20)) + [100.0])
        expected_value = np.mean(data)
        self.set_seed()
        value = DiffPrivStatistics.mean(data, self.epsilon)
        self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_mean_multiple(self):
        data = np.array([list(range(0, 20)) + [100.0]] * 3)
        expected_values = np.mean(data, axis=1)
        self.set_seed()
        value = DiffPrivStatistics.mean(data, self.epsilon, axis=1)
        np.testing.assert_almost_equal(value, expected_values, self.decimal_places)

    def test_variance_single(self):
        data = np.array(list(range(0, 20)) + [100.0])
        expected_value = np.var(data)
        self.set_seed()
        value = DiffPrivStatistics.variance(data, self.epsilon)
        self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_variance_multiple(self):
        data = np.array([list(range(0, 20)) + [100.0]] * 3)
        expected_values = np.var(data, axis=1)
        self.set_seed()
        value = DiffPrivStatistics.variance(data, self.epsilon, axis=1)
        np.testing.assert_almost_equal(value, expected_values, self.decimal_places)

    def test_apply_kind_on_data_slice_invalid_dimension_error(self):
        data = np.array([[list(range(0, 20)) + [100.0]]])
        kinds = DiffPrivStatisticKind.all
        self.set_seed()
        with self.assertRaises(DiffPrivStatisticsInvalidDimensions):
            DiffPrivStatistics.apply_kind_on_data_slice(data, kinds, self.epsilon)

    def test_apply_kind_on_data_slice_size_mismatch_error(self):
        data = np.array(list(range(0, 20)) + [100.0])
        kinds = [DiffPrivStatisticKind.all, DiffPrivStatisticKind.all]
        self.set_seed()
        with self.assertRaises(DiffPrivStatisticsSizeMismatch):
            DiffPrivStatistics.apply_kind_on_data_slice(data, kinds, self.epsilon)

    def calculate_stats(self, data, axis=None):
        stats = {
            DiffPrivStatisticKind.count: np.count_nonzero(data, axis=axis),
            DiffPrivStatisticKind.min: np.min(data, axis=axis),
            DiffPrivStatisticKind.max: np.max(data, axis=axis),
            DiffPrivStatisticKind.median: np.median(data, axis=axis),
            DiffPrivStatisticKind.proportion: np.divide(
                np.count_nonzero(data, axis=axis), np.size(data, axis=axis)
            ),
            DiffPrivStatisticKind.sum: np.sum(data, axis=axis),
            DiffPrivStatisticKind.mean: np.mean(data, axis=axis),
            DiffPrivStatisticKind.variance: np.var(data, axis=axis),
        }
        return stats

    def test_apply_kind_on_data_slice_single(self):
        data = np.array(list(range(0, 20)) + [100.0])
        kinds = DiffPrivStatisticKind.all
        expected_results = [self.calculate_stats(data)]
        self.set_seed()
        results = DiffPrivStatistics.apply_kind_on_data_slice(data, kinds, self.epsilon)
        self.assertEqual(len(results), len(expected_results))
        for index in range(len(expected_results)):
            result = results[index]
            expected_result = expected_results[index]
            self.assertEqual(len(result), len(expected_result))
            for key, value in expected_result.items():
                value = result[key]
                expected_value = expected_result[key]
                self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_apply_kind_on_data_slice_single_with_axis_0(self):
        data = np.array(list(range(0, 20)) + [100.0])
        kinds = DiffPrivStatisticKind.all
        expected_results = [self.calculate_stats(data)]
        self.set_seed()
        results = DiffPrivStatistics.apply_kind_on_data_slice(
            data, kinds, self.epsilon, axis=0
        )
        self.assertEqual(len(results), len(expected_results))
        for index in range(len(expected_results)):
            result = results[index]
            expected_result = expected_results[index]
            self.assertEqual(len(result), len(expected_result))
            for key, value in expected_result.items():
                value = result[key]
                expected_value = expected_result[key]
                self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_apply_kind_on_data_slice_single_with_axis_1(self):
        data = np.array(list(range(0, 20)) + [100.0])
        kinds = DiffPrivStatisticKind.all
        expected_results = [self.calculate_stats(data)]
        data = np.transpose(data)
        self.set_seed()
        results = DiffPrivStatistics.apply_kind_on_data_slice(
            data, kinds, self.epsilon, axis=1
        )
        self.assertEqual(len(results), len(expected_results))
        for index in range(len(expected_results)):
            result = results[index]
            expected_result = expected_results[index]
            self.assertEqual(len(result), len(expected_result))
            for key, value in expected_result.items():
                value = result[key]
                expected_value = expected_result[key]
                self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_apply_kind_on_data_slice_multiple_axis_0(self):
        data = np.array([list(range(0, 20)) + [100.0]] * 3)
        kinds = [DiffPrivStatisticKind.all] * 3
        expected_results = [
            self.calculate_stats(data[0]),
            self.calculate_stats(data[1]),
            self.calculate_stats(data[2]),
        ]
        data = np.transpose(data)
        self.set_seed()
        results = DiffPrivStatistics.apply_kind_on_data_slice(
            data, kinds, self.epsilon, axis=0
        )
        self.assertEqual(len(results), len(expected_results))
        for index in range(len(expected_results)):
            result = results[index]
            expected_result = expected_results[index]
            self.assertEqual(len(result), len(expected_result))
            for key, value in expected_result.items():
                value = result[key]
                expected_value = expected_result[key]
                self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_apply_kind_on_data_slice_multiple_axis_1(self):
        data = np.array([list(range(0, 20)) + [100.0]] * 3)
        kinds = [DiffPrivStatisticKind.all] * 3
        expected_results = [
            self.calculate_stats(data[0]),
            self.calculate_stats(data[1]),
            self.calculate_stats(data[2]),
        ]
        self.set_seed()
        results = DiffPrivStatistics.apply_kind_on_data_slice(
            data, kinds, self.epsilon, axis=1
        )
        self.assertEqual(len(results), len(expected_results))
        for index in range(len(expected_results)):
            result = results[index]
            expected_result = expected_results[index]
            self.assertEqual(len(result), len(expected_result))
            for key, value in expected_result.items():
                value = result[key]
                expected_value = expected_result[key]
                self.assertAlmostEqual(value, expected_value, self.decimal_places)
