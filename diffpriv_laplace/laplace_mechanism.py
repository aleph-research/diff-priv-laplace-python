from enum import Enum
from diffpriv_laplace.anonymizer.counting import DiffPrivCountingAnonymizer
from diffpriv_laplace.anonymizer.proportion import DiffPrivProportionAnonymizer
from diffpriv_laplace.anonymizer.mean import DiffPrivMeanAnonymizer
from diffpriv_laplace.anonymizer.variance import DiffPrivVarianceAnonymizer


class DiffPrivAnonymizerType(Enum):
    counting = "counting"
    proportion = "proportion"
    mean = "mean"
    variance = "variance"


class DiffPrivLaplaceMechanism(object):
    """
    The differential privacy Laplace mechanism.
    """

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
