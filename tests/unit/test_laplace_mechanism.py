import unittest
import numpy as np
from diffpriv_laplace.anonymizer.count import DiffPrivCountAnonymizer
from diffpriv_laplace.anonymizer.counting import DiffPrivCountingAnonymizer
from diffpriv_laplace.anonymizer.min import DiffPrivMinAnonymizer
from diffpriv_laplace.anonymizer.max import DiffPrivMaxAnonymizer
from diffpriv_laplace.anonymizer.median import DiffPrivMedianAnonymizer
from diffpriv_laplace.anonymizer.proportion import DiffPrivProportionAnonymizer
from diffpriv_laplace.anonymizer.sum import DiffPrivSumAnonymizer
from diffpriv_laplace.anonymizer.mean import DiffPrivMeanAnonymizer
from diffpriv_laplace.anonymizer.variance import DiffPrivVarianceAnonymizer
from diffpriv_laplace import DiffPrivLaplaceMechanism


class TestDiffPrivLaplaceMechanism(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def set_seed(self):
        np.random.seed(31337)

    def test_create_count_anonymizer(self):
        epsilon = 0.1
        anonymizer = DiffPrivLaplaceMechanism.create_count_anonymizer(epsilon)
        self.assertIsInstance(anonymizer, DiffPrivCountAnonymizer)
        self.assertEqual(anonymizer.epsilon, epsilon)

    def test_create_counting_anonymizer(self):
        epsilon = 0.1
        anonymizer = DiffPrivLaplaceMechanism.create_counting_anonymizer(epsilon)
        self.assertIsInstance(anonymizer, DiffPrivCountingAnonymizer)
        self.assertEqual(anonymizer.epsilon, epsilon)

    def test_create_min_anonymizer(self):
        epsilon = 0.1
        anonymizer = DiffPrivLaplaceMechanism.create_min_anonymizer(epsilon)
        self.assertIsInstance(anonymizer, DiffPrivMinAnonymizer)
        self.assertEqual(anonymizer.epsilon, epsilon)

    def test_create_max_anonymizer(self):
        epsilon = 0.1
        anonymizer = DiffPrivLaplaceMechanism.create_max_anonymizer(epsilon)
        self.assertIsInstance(anonymizer, DiffPrivMaxAnonymizer)
        self.assertEqual(anonymizer.epsilon, epsilon)

    def test_create_median_anonymizer(self):
        epsilon = 0.1
        anonymizer = DiffPrivLaplaceMechanism.create_median_anonymizer(epsilon)
        self.assertIsInstance(anonymizer, DiffPrivMedianAnonymizer)
        self.assertEqual(anonymizer.epsilon, epsilon)

    def test_create_proportion_anonymizer(self):
        epsilon = 0.1
        n = 10.0
        anonymizer = DiffPrivLaplaceMechanism.create_proportion_anonymizer(epsilon, n)
        self.assertIsInstance(anonymizer, DiffPrivProportionAnonymizer)
        self.assertEqual(anonymizer.epsilon, epsilon)
        self.assertEqual(anonymizer.n, n)

    def test_create_sum_anonymizer(self):
        epsilon = 1.0
        lower = 10.0
        upper = 99.0
        anonymizer = DiffPrivLaplaceMechanism.create_sum_anonymizer(
            epsilon, lower, upper
        )
        self.assertIsInstance(anonymizer, DiffPrivSumAnonymizer)
        self.assertEqual(anonymizer.epsilon, epsilon)
        self.assertEqual(anonymizer.lower, lower)
        self.assertEqual(anonymizer.upper, upper)

    def test_create_mean_anonymizer(self):
        epsilon = 1.0
        lower = 10.0
        upper = 99.0
        n = 100.0
        anonymizer = DiffPrivLaplaceMechanism.create_mean_anonymizer(
            epsilon, lower, upper, n
        )
        self.assertIsInstance(anonymizer, DiffPrivMeanAnonymizer)
        self.assertEqual(anonymizer.epsilon, epsilon)
        self.assertEqual(anonymizer.lower, lower)
        self.assertEqual(anonymizer.upper, upper)
        self.assertEqual(anonymizer.n, n)

    def test_create_variance_anonymizer(self):
        epsilon = 1.0
        lower = 10.0
        upper = 99.0
        n = 100.0
        anonymizer = DiffPrivLaplaceMechanism.create_variance_anonymizer(
            epsilon, lower, upper, n
        )
        self.assertIsInstance(anonymizer, DiffPrivVarianceAnonymizer)
        self.assertEqual(anonymizer.epsilon, epsilon)
        self.assertEqual(anonymizer.lower, lower)
        self.assertEqual(anonymizer.upper, upper)
        self.assertEqual(anonymizer.n, n)

    def test_anonymize_count_with_budget_single(self):
        expected_value = 87.58645513850368
        epsilon = 1.0
        self.set_seed()
        anonymized = DiffPrivLaplaceMechanism.anonymize_count_with_budget(87.0, epsilon)
        np.testing.assert_almost_equal(anonymized, expected_value)

    def test_anonymize_count_with_budget_single_many(self):
        expected_values = np.array([87.5864551, 89.701297, 86.4519884])
        epsilon = 1.0
        self.set_seed()
        anonymized = DiffPrivLaplaceMechanism.anonymize_count_with_budget(
            87.0, epsilon, size=3
        )
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_count_with_budget_multiple(self):
        expected_values = np.array([87.5864551, 437.701297])
        epsilon = 1.0
        self.set_seed()
        anonymized = DiffPrivLaplaceMechanism.anonymize_count_with_budget(
            [87.0, 435.0], epsilon
        )
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_min_with_budget_single(self):
        expected_value = 87.58645513850368
        epsilon = 1.0
        self.set_seed()
        anonymized = DiffPrivLaplaceMechanism.anonymize_min_with_budget(87.0, epsilon)
        np.testing.assert_almost_equal(anonymized, expected_value)

    def test_anonymize_min_with_budget_single_many(self):
        expected_values = np.array([87.5864551, 89.701297, 86.4519884])
        epsilon = 1.0
        self.set_seed()
        anonymized = DiffPrivLaplaceMechanism.anonymize_min_with_budget(
            87.0, epsilon, size=3
        )
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_min_with_budget_multiple(self):
        expected_values = np.array([87.5864551, 437.701297])
        epsilon = 1.0
        self.set_seed()
        anonymized = DiffPrivLaplaceMechanism.anonymize_min_with_budget(
            [87.0, 435.0], epsilon
        )
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_max_with_budget_single(self):
        expected_value = 87.58645513850368
        epsilon = 1.0
        self.set_seed()
        anonymized = DiffPrivLaplaceMechanism.anonymize_max_with_budget(87.0, epsilon)
        np.testing.assert_almost_equal(anonymized, expected_value)

    def test_anonymize_max_with_budget_single_many(self):
        expected_values = np.array([87.5864551, 89.701297, 86.4519884])
        epsilon = 1.0
        self.set_seed()
        anonymized = DiffPrivLaplaceMechanism.anonymize_max_with_budget(
            87.0, epsilon, size=3
        )
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_max_with_budget_multiple(self):
        expected_values = np.array([87.5864551, 437.701297])
        epsilon = 1.0
        self.set_seed()
        anonymized = DiffPrivLaplaceMechanism.anonymize_max_with_budget(
            [87.0, 435.0], epsilon
        )
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_median_with_budget_single(self):
        expected_value = 87.58645513850368
        epsilon = 1.0
        self.set_seed()
        anonymized = DiffPrivLaplaceMechanism.anonymize_median_with_budget(
            87.0, epsilon
        )
        np.testing.assert_almost_equal(anonymized, expected_value)

    def test_anonymize_median_with_budget_single_many(self):
        expected_values = np.array([87.5864551, 89.701297, 86.4519884])
        epsilon = 1.0
        self.set_seed()
        anonymized = DiffPrivLaplaceMechanism.anonymize_median_with_budget(
            87.0, epsilon, size=3
        )
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_median_with_budget_multiple(self):
        expected_values = np.array([87.5864551, 437.701297])
        epsilon = 1.0
        self.set_seed()
        anonymized = DiffPrivLaplaceMechanism.anonymize_median_with_budget(
            [87.0, 435.0], epsilon
        )
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_proportion_with_budget_single(self):
        expected_value = 87.05864551385037
        n = 10.0
        epsilon = 1.0
        self.set_seed()
        anonymized = DiffPrivLaplaceMechanism.anonymize_proportion_with_budget(
            87.0, n, epsilon
        )
        np.testing.assert_almost_equal(anonymized, expected_value)

    def test_anonymize_proportion_with_budget_single_many(self):
        expected_values = np.array([87.0586455, 87.2701297, 86.9451988])
        n = 10.0
        epsilon = 1.0
        self.set_seed()
        anonymized = DiffPrivLaplaceMechanism.anonymize_proportion_with_budget(
            87.0, n, epsilon, size=3
        )
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_proportion_with_budget_multiple(self):
        expected_values = np.array([87.0586455, 435.2701297])
        n = 10.0
        epsilon = 1.0
        self.set_seed()
        anonymized = DiffPrivLaplaceMechanism.anonymize_proportion_with_budget(
            [87.0, 435.0], n, epsilon
        )
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_sum_with_budget_single(self):
        expected_value = 145.05905871186388
        lower = 10.0
        upper = 99.0
        epsilon = 1.0
        self.set_seed()
        anonymized = DiffPrivLaplaceMechanism.anonymize_sum_with_budget(
            87.0, lower, upper, epsilon
        )
        np.testing.assert_almost_equal(anonymized, expected_value)

    def test_anonymize_sum_with_budget_single_many(self):
        expected_values = np.array([145.0590587, 354.4284063, 32.746848])
        lower = 10.0
        upper = 99.0
        epsilon = 1.0
        self.set_seed()
        anonymized = DiffPrivLaplaceMechanism.anonymize_sum_with_budget(
            87.0, lower, upper, epsilon, size=3
        )
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_sum_with_budget_multiple(self):
        expected_values = np.array([145.0590587, 702.4284063])
        lower = 10.0
        upper = 99.0
        epsilon = 1.0
        self.set_seed()
        anonymized = DiffPrivLaplaceMechanism.anonymize_sum_with_budget(
            [87.0, 435.0], lower, upper, epsilon
        )
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_mean_with_budget_single(self):
        expected_value = 87.52194507326827
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        self.set_seed()
        anonymized = DiffPrivLaplaceMechanism.anonymize_mean_with_budget(
            87.0, lower, upper, n, epsilon
        )
        np.testing.assert_almost_equal(anonymized, expected_value)

    def test_anonymize_mean_with_budget_single_many(self):
        expected_values = np.array([87.5219451, 89.4041544, 86.5122696])
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        self.set_seed()
        anonymized = DiffPrivLaplaceMechanism.anonymize_mean_with_budget(
            87.0, lower, upper, n, epsilon, size=3
        )
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_mean_with_budget_multiple(self):
        expected_values = np.array([87.5219451, 437.4041544])
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        self.set_seed()
        anonymized = DiffPrivLaplaceMechanism.anonymize_mean_with_budget(
            [87.0, 435.0], lower, upper, n, epsilon
        )
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_variance_with_budget_single(self):
        expected_value = 133.45311152087612
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        self.set_seed()
        anonymized = DiffPrivLaplaceMechanism.anonymize_variance_with_budget(
            87.0, lower, upper, n, epsilon
        )
        np.testing.assert_almost_equal(anonymized, expected_value)

    def test_anonymize_variance_with_budget_single_many(self):
        expected_values = np.array([133.4531115, 300.969738, 43.5919983])
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        self.set_seed()
        anonymized = DiffPrivLaplaceMechanism.anonymize_variance_with_budget(
            87.0, lower, upper, n, epsilon, size=3
        )
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_variance_with_budget_multiple(self):
        expected_values = np.array([133.4531115, 648.969738])
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        self.set_seed()
        anonymized = DiffPrivLaplaceMechanism.anonymize_variance_with_budget(
            [87.0, 435.0], lower, upper, n, epsilon
        )
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_epsilon_getter(self):
        epsilon = 0.1
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.assertEqual(anonymizer.epsilon, epsilon)

    def test_anonymize_count_single(self):
        expected_value = 87.58645513850368
        epsilon = 1.0
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.set_seed()
        anonymized = anonymizer.anonymize_count(87.0)
        np.testing.assert_almost_equal(anonymized, expected_value)

    def test_anonymize_count_single_many(self):
        expected_values = np.array([87.5864551, 89.701297, 86.4519884])
        epsilon = 1.0
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.set_seed()
        anonymized = anonymizer.anonymize_count(87.0, size=3)
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_count_multiple(self):
        expected_values = np.array([87.5864551, 437.701297])
        epsilon = 1.0
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.set_seed()
        anonymized = anonymizer.anonymize_count([87.0, 435.0])
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_min_single(self):
        expected_value = 87.58645513850368
        epsilon = 1.0
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.set_seed()
        anonymized = anonymizer.anonymize_min(87.0)
        np.testing.assert_almost_equal(anonymized, expected_value)

    def test_anonymize_min_single_many(self):
        expected_values = np.array([87.5864551, 89.701297, 86.4519884])
        epsilon = 1.0
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.set_seed()
        anonymized = anonymizer.anonymize_min(87.0, size=3)
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_min_multiple(self):
        expected_values = np.array([87.5864551, 437.701297])
        epsilon = 1.0
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.set_seed()
        anonymized = anonymizer.anonymize_min([87.0, 435.0])
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_max_single(self):
        expected_value = 87.58645513850368
        epsilon = 1.0
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.set_seed()
        anonymized = anonymizer.anonymize_max(87.0)
        np.testing.assert_almost_equal(anonymized, expected_value)

    def test_anonymize_max_single_many(self):
        expected_values = np.array([87.5864551, 89.701297, 86.4519884])
        epsilon = 1.0
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.set_seed()
        anonymized = anonymizer.anonymize_max(87.0, size=3)
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_max_multiple(self):
        expected_values = np.array([87.5864551, 437.701297])
        epsilon = 1.0
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.set_seed()
        anonymized = anonymizer.anonymize_max([87.0, 435.0])
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_median_single(self):
        expected_value = 87.58645513850368
        epsilon = 1.0
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.set_seed()
        anonymized = anonymizer.anonymize_median(87.0)
        np.testing.assert_almost_equal(anonymized, expected_value)

    def test_anonymize_median_single_many(self):
        expected_values = np.array([87.5864551, 89.701297, 86.4519884])
        epsilon = 1.0
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.set_seed()
        anonymized = anonymizer.anonymize_median(87.0, size=3)
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_median_multiple(self):
        expected_values = np.array([87.5864551, 437.701297])
        epsilon = 1.0
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.set_seed()
        anonymized = anonymizer.anonymize_median([87.0, 435.0])
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_proportion_single(self):
        expected_value = 87.05864551385037
        n = 10.0
        epsilon = 1.0
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.set_seed()
        anonymized = anonymizer.anonymize_proportion(87.0, n)
        np.testing.assert_almost_equal(anonymized, expected_value)

    def test_anonymize_proportion_single_many(self):
        expected_values = np.array([87.0586455, 87.2701297, 86.9451988])
        n = 10.0
        epsilon = 1.0
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.set_seed()
        anonymized = anonymizer.anonymize_proportion(87.0, n, size=3)
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_proportion_multiple(self):
        expected_values = np.array([87.0586455, 435.2701297])
        n = 10.0
        epsilon = 1.0
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.set_seed()
        anonymized = anonymizer.anonymize_proportion([87.0, 435.0], n)
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_sum_single(self):
        expected_value = 145.05905871186388
        lower = 10.0
        upper = 99.0
        epsilon = 1.0
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.set_seed()
        anonymized = anonymizer.anonymize_sum(87.0, lower, upper)
        np.testing.assert_almost_equal(anonymized, expected_value)

    def test_anonymize_sum_single_many(self):
        expected_values = np.array([145.0590587, 354.4284063, 32.746848])
        lower = 10.0
        upper = 99.0
        epsilon = 1.0
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.set_seed()
        anonymized = anonymizer.anonymize_sum(87.0, lower, upper, size=3)
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_sum_multiple(self):
        expected_values = np.array([145.0590587, 702.4284063])
        lower = 10.0
        upper = 99.0
        epsilon = 1.0
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.set_seed()
        anonymized = anonymizer.anonymize_sum([87.0, 435.0], lower, upper)
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_mean_single(self):
        expected_value = 87.52194507326827
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.set_seed()
        anonymized = anonymizer.anonymize_mean(87.0, lower, upper, n)
        np.testing.assert_almost_equal(anonymized, expected_value)

    def test_anonymize_mean_single_many(self):
        expected_values = np.array([87.5219451, 89.4041544, 86.5122696])
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.set_seed()
        anonymized = anonymizer.anonymize_mean(87.0, lower, upper, n, size=3)
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_mean_multiple(self):
        expected_values = np.array([87.5219451, 437.4041544])
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.set_seed()
        anonymized = anonymizer.anonymize_mean([87.0, 435.0], lower, upper, n)
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_variance_single(self):
        expected_value = 133.45311152087612
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.set_seed()
        anonymized = anonymizer.anonymize_variance(87.0, lower, upper, n)
        np.testing.assert_almost_equal(anonymized, expected_value)

    def test_anonymize_variance_single_many(self):
        expected_values = np.array([133.4531115, 300.969738, 43.5919983])
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.set_seed()
        anonymized = anonymizer.anonymize_variance(87.0, lower, upper, n, size=3)
        np.testing.assert_almost_equal(anonymized, expected_values)

    def test_anonymize_variance_multiple(self):
        expected_values = np.array([133.4531115, 648.969738])
        lower = 10.0
        upper = 99.0
        n = 100.0
        epsilon = 1.0
        anonymizer = DiffPrivLaplaceMechanism(epsilon)
        self.set_seed()
        anonymized = anonymizer.anonymize_variance([87.0, 435.0], lower, upper, n)
        np.testing.assert_almost_equal(anonymized, expected_values)
