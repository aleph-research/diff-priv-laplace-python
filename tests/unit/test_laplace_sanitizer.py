import unittest
import numpy as np
from diffpriv_laplace import DiffPrivLaplaceSanitizer
from diffpriv_laplace.exceptions import (
    DiffPrivInvalidDecomposition,
    DiffPrivInvalidDimensions,
    DiffPrivSizeMismatch,
)


class TestDiffPrivLaplaceSanitizer(unittest.TestCase):
    epsilon = 1000000
    decimal_places = 2

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def set_seed(self):
        np.random.seed(31337)

    def test_decompose_data_slice_two_selectors(self):
        data = np.array([0.1, -0.1, 0.1, 0.1] * 10)
        expected_result = np.array([data >= 0, data < 0],)

        def selector_positive(data):
            return data >= 0

        def selector_negative(data):
            return data < 0

        selectors = [
            selector_positive,
            selector_negative,
        ]

        result = DiffPrivLaplaceSanitizer.decompose_data_slice(data, selectors)
        self.assertEqual(len(result), len(selectors))
        for index in range(len(expected_result)):
            np.testing.assert_almost_equal(result[index], expected_result[index])

    def test_decompose_data_slice_three_selectors(self):
        data = np.array([0.1, -0.1, 0.01, -0.01, 0.1, 0.1] * 10)
        expected_result = np.array(
            [(data > -0.1) & (data < 0.1), data >= 0.1, data <= -0.1],
        )

        def selector_near_zero(data):
            return (data > -0.1) & (data < 0.1)

        def selector_positive(data):
            return data >= 0.1

        def selector_negative(data):
            return data <= -0.1

        selectors = [
            selector_near_zero,
            selector_positive,
            selector_negative,
        ]

        result = DiffPrivLaplaceSanitizer.decompose_data_slice(data, selectors)
        self.assertEqual(len(result), len(selectors))
        for index in range(len(expected_result)):
            np.testing.assert_almost_equal(result[index], expected_result[index])

    def test_decompose_data_slice_invalid_decomposition_error(self):
        data = np.array([0.1, -0.1, 0.01, 0.0, -0.01, 0.1, 0.1] * 10)

        def selector_positive(data):
            return data != 0.0

        def selector_negative(data):
            return data != 0.0

        selectors = [
            selector_positive,
            selector_negative,
        ]

        with self.assertRaises(DiffPrivInvalidDecomposition):
            DiffPrivLaplaceSanitizer.decompose_data_slice(data, selectors)

    def test_count_example(self):
        epsilon = 0.1
        data = np.array([0.01, -0.01, 0.03, -0.001, 0.1] * 2)
        expected_value = np.array([np.array([5.0, 5.0])])

        def selector_positive(data):
            return data >= 0.0

        def selector_negative(data):
            return data < 0.0

        selectors = [selector_positive, selector_negative]
        self.set_seed()
        value = DiffPrivLaplaceSanitizer.count(data, selectors, epsilon)
        np.testing.assert_almost_equal(value, expected_value)

    def test_count_invalid_dimension_error(self):
        data = np.array([np.array([np.array([0.1, -0.1, 0.1, 0.1] * 10)])])

        def selector_positive(data):
            return data >= 0

        def selector_negative(data):
            return data < 0

        selectors = [
            selector_positive,
            selector_negative,
        ]

        self.set_seed()
        with self.assertRaises(DiffPrivInvalidDimensions):
            DiffPrivLaplaceSanitizer.count(data, selectors, self.epsilon)

    def test_count_size_mismatch_error(self):
        data = np.array(
            [np.array([0.1, -0.1, 0.1, 0.1] * 10), np.array([0.1, -0.1, 0.1, 0.1] * 10)]
        )
        selectors = [[]]

        self.set_seed()
        with self.assertRaises(DiffPrivSizeMismatch):
            DiffPrivLaplaceSanitizer.count(data, selectors, self.epsilon)

    def test_count_single_no_postprocess(self):
        data = np.array([0.1, -0.1, 0.1, 0.1] * 10)
        postprocess = False
        expected_result = [np.array([np.sum(data >= 0), np.sum(data < 0)])]

        def selector_positive(data):
            return data >= 0

        def selector_negative(data):
            return data < 0

        selectors = [
            selector_positive,
            selector_negative,
        ]

        self.set_seed()
        results = DiffPrivLaplaceSanitizer.count(
            data, selectors, self.epsilon, postprocess=postprocess
        )

        for index in range(len(expected_result)):
            np.testing.assert_almost_equal(results[index], expected_result[index])

    def test_count_single_no_postprocess_with_axis_0(self):
        data = np.array([0.1, -0.1, 0.1, 0.1] * 10)
        postprocess = False
        expected_result = [np.array([np.sum(data >= 0), np.sum(data < 0)])]

        def selector_positive(data):
            return data >= 0

        def selector_negative(data):
            return data < 0

        selectors = [
            selector_positive,
            selector_negative,
        ]

        self.set_seed()
        results = DiffPrivLaplaceSanitizer.count(
            data, selectors, self.epsilon, axis=0, postprocess=postprocess
        )

        for index in range(len(expected_result)):
            np.testing.assert_almost_equal(results[index], expected_result[index])

    def test_count_single_no_postprocess_with_axis_1(self):
        data = np.array([0.1, -0.1, 0.1, 0.1] * 10)
        postprocess = False
        expected_result = [np.array([np.sum(data >= 0), np.sum(data < 0)])]

        def selector_positive(data):
            return data >= 0

        def selector_negative(data):
            return data < 0

        selectors = [
            selector_positive,
            selector_negative,
        ]

        data = data.transpose()
        self.set_seed()
        results = DiffPrivLaplaceSanitizer.count(
            data, selectors, self.epsilon, axis=1, postprocess=postprocess
        )

        for index in range(len(expected_result)):
            np.testing.assert_almost_equal(results[index], expected_result[index])

    def test_count_single_with_postprocess(self):
        data = np.array([0.1, -0.1, 0.1, 0.1] * 10)
        postprocess = True
        expected_result = [np.array([np.sum(data >= 0), np.sum(data < 0)])]

        def selector_positive(data):
            return data >= 0

        def selector_negative(data):
            return data < 0

        selectors = [
            selector_positive,
            selector_negative,
        ]

        self.set_seed()
        results = DiffPrivLaplaceSanitizer.count(
            data, selectors, self.epsilon, postprocess=postprocess
        )

        for index in range(len(expected_result)):
            np.testing.assert_almost_equal(results[index], expected_result[index])

    def test_count_single_with_postprocess_with_axis_0(self):
        data = np.array([0.1, -0.1, 0.1, 0.1] * 10)
        postprocess = True
        expected_result = [np.array([np.sum(data >= 0), np.sum(data < 0)])]

        def selector_positive(data):
            return data >= 0

        def selector_negative(data):
            return data < 0

        selectors = [
            selector_positive,
            selector_negative,
        ]

        self.set_seed()
        results = DiffPrivLaplaceSanitizer.count(
            data, selectors, self.epsilon, axis=0, postprocess=postprocess
        )

        for index in range(len(expected_result)):
            np.testing.assert_almost_equal(results[index], expected_result[index])

    def test_count_single_with_postprocess_with_axis_1(self):
        data = np.array([0.1, -0.1, 0.1, 0.1] * 10)
        postprocess = True
        expected_result = [np.array([np.sum(data >= 0), np.sum(data < 0)])]

        def selector_positive(data):
            return data >= 0

        def selector_negative(data):
            return data < 0

        selectors = [
            selector_positive,
            selector_negative,
        ]

        data = data.transpose()
        self.set_seed()
        results = DiffPrivLaplaceSanitizer.count(
            data, selectors, self.epsilon, axis=1, postprocess=postprocess
        )

        for index in range(len(expected_result)):
            np.testing.assert_almost_equal(results[index], expected_result[index])

    def test_count_multiple_no_postprocess_with_axis_0(self):
        data = np.array(
            [
                np.array([0.1, -0.1, 0.1, 0.1] * 10),
                np.array([0.1, -0.1, 0.1, 0.1] * 10),
            ]
        )
        postprocess = False
        expected_result = [
            np.array([np.sum(data[0] >= 0), np.sum(data[0] < 0)]),
            np.array([np.sum(data[1] >= 0), np.sum(data[1] < 0)]),
        ]

        def selector_positive(data):
            return data >= 0

        def selector_negative(data):
            return data < 0

        selectors = [
            [selector_positive, selector_negative],
            [selector_positive, selector_negative],
        ]

        data = np.transpose(data)
        self.set_seed()
        results = DiffPrivLaplaceSanitizer.count(
            data, selectors, self.epsilon, axis=0, postprocess=postprocess
        )

        for index in range(len(expected_result)):
            np.testing.assert_almost_equal(results[index], expected_result[index])

    def test_count_multiple_no_postprocess_with_axis_1(self):
        data = np.array(
            [
                np.array([0.1, -0.1, 0.1, 0.1] * 10),
                np.array([0.1, -0.1, 0.1, 0.1] * 10),
            ]
        )
        postprocess = False
        expected_result = [
            np.array([np.sum(data[0] >= 0), np.sum(data[0] < 0)]),
            np.array([np.sum(data[1] >= 0), np.sum(data[1] < 0)]),
        ]

        def selector_positive(data):
            return data >= 0

        def selector_negative(data):
            return data < 0

        selectors = [
            [selector_positive, selector_negative],
            [selector_positive, selector_negative],
        ]

        self.set_seed()
        results = DiffPrivLaplaceSanitizer.count(
            data, selectors, self.epsilon, axis=1, postprocess=postprocess
        )

        for index in range(len(expected_result)):
            np.testing.assert_almost_equal(results[index], expected_result[index])

    def test_count_multiple_with_postprocess_with_axis_0(self):
        data = np.array(
            [
                np.array([0.1, -0.1, 0.1, 0.1] * 10),
                np.array([0.1, -0.1, 0.1, 0.1] * 10),
            ]
        )
        postprocess = False
        expected_result = [
            np.array([np.sum(data[0] >= 0), np.sum(data[0] < 0)]),
            np.array([np.sum(data[1] >= 0), np.sum(data[1] < 0)]),
        ]

        def selector_positive(data):
            return data >= 0

        def selector_negative(data):
            return data < 0

        selectors = [
            [selector_positive, selector_negative],
            [selector_positive, selector_negative],
        ]

        data = np.transpose(data)
        self.set_seed()
        results = DiffPrivLaplaceSanitizer.count(
            data, selectors, self.epsilon, axis=0, postprocess=postprocess
        )

        for index in range(len(expected_result)):
            np.testing.assert_almost_equal(results[index], expected_result[index])

    def test_count_multiple_with_postprocess_with_axis_1(self):
        data = np.array(
            [
                np.array([0.1, -0.1, 0.1, 0.1] * 10),
                np.array([0.1, -0.1, 0.1, 0.1] * 10),
            ]
        )
        postprocess = True
        expected_result = [
            np.array([np.sum(data[0] >= 0), np.sum(data[0] < 0)]),
            np.array([np.sum(data[1] >= 0), np.sum(data[1] < 0)]),
        ]

        def selector_positive(data):
            return data >= 0

        def selector_negative(data):
            return data < 0

        selectors = [
            [selector_positive, selector_negative],
            [selector_positive, selector_negative],
        ]

        self.set_seed()
        results = DiffPrivLaplaceSanitizer.count(
            data, selectors, self.epsilon, axis=1, postprocess=postprocess
        )

        for index in range(len(expected_result)):
            np.testing.assert_almost_equal(results[index], expected_result[index])
