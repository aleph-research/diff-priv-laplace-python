from enum import Enum
from diffpriv_laplace.anonymizer.count import DiffPrivCountAnonymizer
from diffpriv_laplace.anonymizer.counting import DiffPrivCountingAnonymizer
from diffpriv_laplace.anonymizer.min import DiffPrivMinAnonymizer
from diffpriv_laplace.anonymizer.max import DiffPrivMaxAnonymizer
from diffpriv_laplace.anonymizer.median import DiffPrivMedianAnonymizer
from diffpriv_laplace.anonymizer.proportion import DiffPrivProportionAnonymizer
from diffpriv_laplace.anonymizer.sum import DiffPrivSumAnonymizer
from diffpriv_laplace.anonymizer.mean import DiffPrivMeanAnonymizer
from diffpriv_laplace.anonymizer.variance import DiffPrivVarianceAnonymizer


class DiffPrivAnonymizerType(Enum):
    count = "count"
    counting = "counting"
    min = "min"
    max = "max"
    median = "median"
    proportion = "proportion"
    sum = "sum"
    mean = "mean"
    variance = "variance"


class DiffPrivLaplaceMechanism(object):
    """
    The differential privacy Laplace mechanism.
    """

    @classmethod
    def create_count_anonymizer(cls, epsilon):
        """
        Creates a count anonymizer instance.

        Parameters
        ----------
        epsilon : float
            The privacy budget.

        Returns
        -------
        `DiffPrivCountAnonymizer`
            A count anonymizer with the provided privacy budget.

        """
        anonymizer = DiffPrivCountAnonymizer(epsilon)
        return anonymizer

    @classmethod
    def create_counting_anonymizer(cls, epsilon):
        """
        Creates a counting anonymizer instance.

        Parameters
        ----------
        epsilon : float
            The privacy budget.

        Returns
        -------
        `DiffPrivCountingAnonymizer`
            A counting anonymizer with the provided privacy budget.

        """
        anonymizer = DiffPrivCountingAnonymizer(epsilon)
        return anonymizer

    @classmethod
    def create_min_anonymizer(cls, epsilon):
        """
        Creates a min anonymizer instance.

        Parameters
        ----------
        epsilon : float
            The privacy budget.

        Returns
        -------
        `DiffPrivMinAnonymizer`
            A min anonymizer with the provided privacy budget.

        """
        anonymizer = DiffPrivMinAnonymizer(epsilon)
        return anonymizer

    @classmethod
    def create_max_anonymizer(cls, epsilon):
        """
        Creates a max anonymizer instance.

        Parameters
        ----------
        epsilon : float
            The privacy budget.

        Returns
        -------
        `DiffPrivMaxAnonymizer`
            A max anonymizer with the provided privacy budget.

        """
        anonymizer = DiffPrivMaxAnonymizer(epsilon)
        return anonymizer

    @classmethod
    def create_median_anonymizer(cls, epsilon):
        """
        Creates a median anonymizer instance.

        Parameters
        ----------
        epsilon : float
            The privacy budget.

        Returns
        -------
        `DiffPrivMedianAnonymizer`
            A median anonymizer with the provided privacy budget.

        """
        anonymizer = DiffPrivMedianAnonymizer(epsilon)
        return anonymizer

    @classmethod
    def create_proportion_anonymizer(cls, epsilon, n):
        """
        Creates a proportion anonymizer instance.

        Parameters
        ----------
        epsilon : float
            The privacy budget.
        n : float
            The total number of observations.

        Returns
        -------
        `DiffPrivProportionAnonymizer`
            A proportion anonymizer with the provided privacy budget.

        """
        anonymizer = DiffPrivProportionAnonymizer(epsilon, n)
        return anonymizer

    @classmethod
    def create_sum_anonymizer(cls, epsilon, lower, upper):
        """
        Creates a sum anonymizer instance.

        Parameters
        ----------
        epsilon : float
            The privacy budget.
        lower : float
            The lower bound of the data.
        upper : float
            The upper bound of the data.

        Returns
        -------
        `DiffPrivSumAnonymizer`
            A sum anonymizer with the provided privacy budget.

        """
        anonymizer = DiffPrivSumAnonymizer(epsilon, lower, upper)
        return anonymizer

    @classmethod
    def create_mean_anonymizer(cls, epsilon, lower, upper, n):
        """
        Creates a mean anonymizer instance.

        Parameters
        ----------
        epsilon : float
            The privacy budget.
        lower : float
            The lower bound of the data.
        upper : float
            The upper bound of the data.
        n : float
            The total number of observations.

        Returns
        -------
        `DiffPrivMeanAnonymizer`
            A mean anonymizer with the provided privacy budget.

        """
        anonymizer = DiffPrivMeanAnonymizer(epsilon, lower, upper, n)
        return anonymizer

    @classmethod
    def create_variance_anonymizer(cls, epsilon, lower, upper, n):
        """
        Creates a variance anonymizer instance.

        Parameters
        ----------
        epsilon : float
            The privacy budget.
        lower : float
            The lower bound of the data.
        upper : float
            The upper bound of the data.
        n : float
            The total number of observations.

        Returns
        -------
        `DiffPrivVarianceAnonymizer`
            A variance anonymizer with the provided privacy budget.

        """
        anonymizer = DiffPrivVarianceAnonymizer(epsilon, lower, upper, n)
        return anonymizer

    @classmethod
    def anonymize_count_with_budget(cls, value, epsilon, size=None):
        """
        Anonymizes one or many count value(s) for a given privacy budget.

        Parameters
        ----------
        value : float|[float]
            The count value(s).
        epsilon : float
            The privacy budget.
        [size] : int|tuple(int)
            Output shape.

        Returns
        -------
        float|[float]
            The anonymized count(s).

        """
        anonymizer = cls.create_counting_anonymizer(epsilon)
        anonymized = anonymizer.apply(value, size=size)
        return anonymized

    @classmethod
    def anonymize_min_with_budget(cls, value, epsilon, size=None):
        """
        Anonymizes one or many min value(s) for a given privacy budget.

        Parameters
        ----------
        value : float|[float]
            The min value(s).
        epsilon : float
            The privacy budget.
        [size] : int|tuple(int)
            Output shape.

        Returns
        -------
        float|[float]
            The anonymized min value(s).

        """
        anonymizer = cls.create_min_anonymizer(epsilon)
        anonymized = anonymizer.apply(value, size=size)
        return anonymized

    @classmethod
    def anonymize_max_with_budget(cls, value, epsilon, size=None):
        """
        Anonymizes one or many max value(s) for a given privacy budget.

        Parameters
        ----------
        value : float|[float]
            The max value(s).
        epsilon : float
            The privacy budget.
        [size] : int|tuple(int)
            Output shape.

        Returns
        -------
        float|[float]
            The anonymized max value(s).

        """
        anonymizer = cls.create_max_anonymizer(epsilon)
        anonymized = anonymizer.apply(value, size=size)
        return anonymized

    @classmethod
    def anonymize_median_with_budget(cls, value, epsilon, size=None):
        """
        Anonymizes one or many median value(s) for a given privacy budget.

        Parameters
        ----------
        value : float|[float]
            The median value(s).
        epsilon : float
            The privacy budget.
        [size] : int|tuple(int)
            Output shape.

        Returns
        -------
        float|[float]
            The anonymized median value(s).

        """
        anonymizer = cls.create_median_anonymizer(epsilon)
        anonymized = anonymizer.apply(value, size=size)
        return anonymized

    @classmethod
    def anonymize_proportion_with_budget(cls, value, n, epsilon, size=None):
        """
        Anonymizes one or many proportion value(s) for a given privacy budget.

        Parameters
        ----------
        value : float|[float]
            The proportion value(s).
        n : float
            The total number of observations.
        epsilon : float
            The privacy budget.
        [size] : int|tuple(int)
            Output shape.

        Returns
        -------
        float|[float]
            The anonymized proportion(s).

        """
        anonymizer = cls.create_proportion_anonymizer(epsilon, n)
        anonymized = anonymizer.apply(value, size=size)
        return anonymized

    @classmethod
    def anonymize_sum_with_budget(cls, value, lower, upper, epsilon, size=None):
        """
        Anonymizes one or many sum value(s) for a given privacy budget.

        Parameters
        ----------
        value : float|[float]
            The sum value(s).
        lower : float
            The lower bound of the data.
        upper : float
            The upper bound of the data.
        epsilon : float
            The privacy budget.
        [size] : int|tuple(int)
            Output shape.

        Returns
        -------
        float|[float]
            The anonymized sum value(s).

        """
        anonymizer = cls.create_sum_anonymizer(epsilon, lower, upper)
        anonymized = anonymizer.apply(value, size=size)
        return anonymized

    @classmethod
    def anonymize_mean_with_budget(cls, value, lower, upper, n, epsilon, size=None):
        """
        Anonymizes one or many mean value(s) for a given privacy budget.

        Parameters
        ----------
        value : float|[float]
            The mean value(s).
        lower : float
            The lower bound of the data.
        upper : float
            The upper bound of the data.
        n : float
            The total number of observations.
        epsilon : float
            The privacy budget.
        [size] : int|tuple(int)
            Output shape.

        Returns
        -------
        float|[float]
            The anonymized mean(s).

        """
        anonymizer = cls.create_mean_anonymizer(epsilon, lower, upper, n)
        anonymized = anonymizer.apply(value, size=size)
        return anonymized

    @classmethod
    def anonymize_variance_with_budget(cls, value, lower, upper, n, epsilon, size=None):
        """
        Anonymizes one or many variance value(s) for a given privacy budget.

        Parameters
        ----------
        value : float|[float]
            The variance value(s).
        lower : float
            The lower bound of the data.
        upper : float
            The upper bound of the data.
        n : float
            The total number of observations.
        epsilon : float
            The privacy budget.
        [size] : int|tuple(int)
            Output shape.

        Returns
        -------
        float|[float]
            The anonymized variance(s).

        """
        anonymizer = cls.create_variance_anonymizer(epsilon, lower, upper, n)
        anonymized = anonymizer.apply(value, size=size)
        return anonymized

    def __init__(self, epsilon):
        """
        Initialize the Laplace mechanism with a privacy budget.

        Parameters
        ----------
        epsilon : float
            The privacy budget value to use.

        """
        self.__epsilon = float(epsilon)
        super().__init__()

    @property
    def epsilon(self):
        """
        The privacy budget value.

        Returns
        -------
        float
            The privacy budget value.

        """
        return self.__epsilon

    def anonymize_count(self, value, size=None):
        """
        Anonymizes one or many count value(s).

        Parameters
        ----------
        value : float|[float]
            The count value(s).
        [size] : int|tuple(int)
            Output shape.

        Returns
        -------
        float|[float]
            The anonymized count(s).

        """
        anonymized = DiffPrivLaplaceMechanism.anonymize_count_with_budget(
            value, self.__epsilon, size=size
        )
        return anonymized

    def anonymize_min(self, value, size=None):
        """
        Anonymizes one or many min value(s).

        Parameters
        ----------
        value : float|[float]
            The min value(s).
        [size] : int|tuple(int)
            Output shape.

        Returns
        -------
        float|[float]
            The anonymized min value(s).

        """
        anonymized = DiffPrivLaplaceMechanism.anonymize_min_with_budget(
            value, self.__epsilon, size=size
        )
        return anonymized

    def anonymize_max(self, value, size=None):
        """
        Anonymizes one or many max value(s).

        Parameters
        ----------
        value : float|[float]
            The max value(s).
        [size] : int|tuple(int)
            Output shape.

        Returns
        -------
        float|[float]
            The anonymized max value(s).

        """
        anonymized = DiffPrivLaplaceMechanism.anonymize_max_with_budget(
            value, self.__epsilon, size=size
        )
        return anonymized

    def anonymize_median(self, value, size=None):
        """
        Anonymizes one or many ,median value(s).

        Parameters
        ----------
        value : float|[float]
            The median value(s).
        [size] : int|tuple(int)
            Output shape.

        Returns
        -------
        float|[float]
            The anonymized median value(s).

        """
        anonymized = DiffPrivLaplaceMechanism.anonymize_median_with_budget(
            value, self.__epsilon, size=size
        )
        return anonymized

    def anonymize_proportion(self, value, n, size=None):
        """
        Anonymizes one or many proportion value(s).

        Parameters
        ----------
        value : float|[float]
            The proportion value(s).
        n : float
            The total number of observations.
        [size] : int|tuple(int)
            Output shape.

        Returns
        -------
        float|[float]
            The anonymized proportion(s).

        """
        anonymized = DiffPrivLaplaceMechanism.anonymize_proportion_with_budget(
            value, n, self.__epsilon, size=size
        )
        return anonymized

    def anonymize_sum(self, value, lower, upper, size=None):
        """
        Anonymizes one or many sum value(s).

        Parameters
        ----------
        value : float|[float]
            The sum value(s).
        lower : float
            The lower bound of the data.
        upper : float
            The upper bound of the data.
        [size] : int|tuple(int)
            Output shape.

        Returns
        -------
        float|[float]
            The anonymized sum value(s).

        """
        anonymized = DiffPrivLaplaceMechanism.anonymize_sum_with_budget(
            value, lower, upper, self.__epsilon, size=size
        )
        return anonymized

    def anonymize_mean(self, value, lower, upper, n, size=None):
        """
        Anonymizes one or many mean value(s).

        Parameters
        ----------
        value : float|[float]
            The mean value(s).
        lower : float
            The lower bound of the data.
        upper : float
            The upper bound of the data.
        n : float
            The total number of observations.
        [size] : int|tuple(int)
            Output shape.

        Returns
        -------
        float|[float]
            The anonymized mean(s).

        """
        anonymized = DiffPrivLaplaceMechanism.anonymize_mean_with_budget(
            value, lower, upper, n, self.__epsilon, size=size
        )
        return anonymized

    def anonymize_variance(self, value, lower, upper, n, size=None):
        """
        Anonymizes one or many variance value(s).

        Parameters
        ----------
        value : float|[float]
            The variance value(s).
        lower : float
            The lower bound of the data.
        upper : float
            The upper bound of the data.
        n : float
            The total number of observations.
        [size] : int|tuple(int)
            Output shape.

        Returns
        -------
        float|[float]
            The anonymized variance(s).

        """
        anonymized = DiffPrivLaplaceMechanism.anonymize_variance_with_budget(
            value, lower, upper, n, self.__epsilon, size=size
        )
        return anonymized
