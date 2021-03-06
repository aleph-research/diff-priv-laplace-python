import unittest
import numpy as np
from diffpriv_laplace import DiffPrivSequentialStatisticsQuery, DiffPrivStatisticKind


class TestDiffPrivSequentialStatisticsQuery(unittest.TestCase):
    epsilon = 100000000
    decimal_places = 2

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def set_seed(self):
        np.random.seed(31337)

    def test_query_count(self):
        kinds = [
            DiffPrivStatisticKind.count,
            DiffPrivStatisticKind.count | DiffPrivStatisticKind.max,
            DiffPrivStatisticKind.count
            | DiffPrivStatisticKind.max
            | DiffPrivStatisticKind.min,
            DiffPrivStatisticKind.count
            | DiffPrivStatisticKind.max
            | DiffPrivStatisticKind.min
            | DiffPrivStatisticKind.sum,
            DiffPrivStatisticKind.count
            | DiffPrivStatisticKind.max
            | DiffPrivStatisticKind.min
            | DiffPrivStatisticKind.sum
            | DiffPrivStatisticKind.mean,
            DiffPrivStatisticKind.count
            | DiffPrivStatisticKind.max
            | DiffPrivStatisticKind.min
            | DiffPrivStatisticKind.sum
            | DiffPrivStatisticKind.mean
            | DiffPrivStatisticKind.median,
            DiffPrivStatisticKind.count
            | DiffPrivStatisticKind.max
            | DiffPrivStatisticKind.min
            | DiffPrivStatisticKind.sum
            | DiffPrivStatisticKind.mean
            | DiffPrivStatisticKind.median
            | DiffPrivStatisticKind.proportion,
            DiffPrivStatisticKind.count
            | DiffPrivStatisticKind.max
            | DiffPrivStatisticKind.min
            | DiffPrivStatisticKind.sum
            | DiffPrivStatisticKind.mean
            | DiffPrivStatisticKind.median
            | DiffPrivStatisticKind.proportion
            | DiffPrivStatisticKind.variance,
        ]
        query_count = DiffPrivSequentialStatisticsQuery.query_count(kinds)
        self.assertAlmostEqual(query_count, np.sum(list(range(1, 9))))

    def test_calculate_query_epsilon(self):
        kinds = [
            DiffPrivStatisticKind.count,
            DiffPrivStatisticKind.count | DiffPrivStatisticKind.max,
            DiffPrivStatisticKind.count
            | DiffPrivStatisticKind.max
            | DiffPrivStatisticKind.min,
            DiffPrivStatisticKind.count
            | DiffPrivStatisticKind.max
            | DiffPrivStatisticKind.min
            | DiffPrivStatisticKind.sum,
            DiffPrivStatisticKind.count
            | DiffPrivStatisticKind.max
            | DiffPrivStatisticKind.min
            | DiffPrivStatisticKind.sum
            | DiffPrivStatisticKind.mean,
            DiffPrivStatisticKind.count
            | DiffPrivStatisticKind.max
            | DiffPrivStatisticKind.min
            | DiffPrivStatisticKind.sum
            | DiffPrivStatisticKind.mean
            | DiffPrivStatisticKind.median,
            DiffPrivStatisticKind.count
            | DiffPrivStatisticKind.max
            | DiffPrivStatisticKind.min
            | DiffPrivStatisticKind.sum
            | DiffPrivStatisticKind.mean
            | DiffPrivStatisticKind.median
            | DiffPrivStatisticKind.proportion,
            DiffPrivStatisticKind.count
            | DiffPrivStatisticKind.max
            | DiffPrivStatisticKind.min
            | DiffPrivStatisticKind.sum
            | DiffPrivStatisticKind.mean
            | DiffPrivStatisticKind.median
            | DiffPrivStatisticKind.proportion
            | DiffPrivStatisticKind.variance,
        ]
        epsilon = 360.0
        expected_value = 10.0
        value = DiffPrivSequentialStatisticsQuery.calculate_query_epsilon(
            kinds, epsilon
        )
        self.assertAlmostEqual(value, expected_value)

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

    def test_query_single(self):
        data = np.array(list(range(0, 20)) + [100.0])
        kinds = DiffPrivStatisticKind.all
        expected_results = [self.calculate_stats(data)]
        self.set_seed()
        results = DiffPrivSequentialStatisticsQuery.query(data, kinds, self.epsilon)
        self.assertEqual(len(results), len(expected_results))
        for index in range(len(expected_results)):
            result = results[index]
            expected_result = expected_results[index]
            self.assertEqual(len(result), len(expected_result))
            for key, value in expected_result.items():
                value = result[key]
                expected_value = expected_result[key]
                self.assertAlmostEqual(value, expected_value, self.decimal_places)

    def test_query_single_with_axis_0(self):
        data = np.array(list(range(0, 20)) + [100.0])
        kinds = DiffPrivStatisticKind.all
        expected_results = [self.calculate_stats(data)]
        self.set_seed()
        results = DiffPrivSequentialStatisticsQuery.query(
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

    def test_query_single_with_axis_1(self):
        data = np.array(list(range(0, 20)) + [100.0])
        kinds = DiffPrivStatisticKind.all
        expected_results = [self.calculate_stats(data)]
        data = np.transpose(data)
        self.set_seed()
        results = DiffPrivSequentialStatisticsQuery.query(
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

    def test_query_multiple_axis_0(self):
        data = np.array([list(range(0, 20)) + [100.0]] * 3)
        kinds = [DiffPrivStatisticKind.all] * 3
        expected_results = [
            self.calculate_stats(data[0]),
            self.calculate_stats(data[1]),
            self.calculate_stats(data[2]),
        ]
        data = np.transpose(data)
        self.set_seed()
        results = DiffPrivSequentialStatisticsQuery.query(
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

    def test_query_multiple_axis_1(self):
        data = np.array([list(range(0, 20)) + [100.0]] * 3)
        kinds = [DiffPrivStatisticKind.all] * 3
        expected_results = [
            self.calculate_stats(data[0]),
            self.calculate_stats(data[1]),
            self.calculate_stats(data[2]),
        ]
        self.set_seed()
        results = DiffPrivSequentialStatisticsQuery.query(
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
