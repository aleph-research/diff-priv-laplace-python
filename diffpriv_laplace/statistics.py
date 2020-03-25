import numpy as np
from enum import Flag, auto
from diffpriv_laplace import DiffPrivLaplaceMechanism


class DiffPrivStatisticKind(Flag):
    """
    The kind flag representing each statistic operation.
    """

    count = auto()
    min = auto()
    max = auto()
    median = auto()
    proportion = auto()
    sum = auto()
    mean = auto()
    variance = auto()
    all = count | min | max | median | proportion | sum | mean | variance

    @property
    def size(self):
        """
        Calculates the amount of statistic kind in the flag.

        Returns
        -------
        int
            The total amount of statistic kind in the flag.

        """
        value = 0
        if self == DiffPrivStatisticKind.all:
            value = len(DiffPrivStatisticKind) - 1
        else:
            for kind in DiffPrivStatisticKind:
                if kind != self.all and bool(self & kind):
                    value = value + 1

        return value


class DiffPrivStatistics(object):
    """
    Differential privacy Laplace mechanism statistics.
    """

    @classmethod
    def count(cls, data, epsilon, condition=None, axis=None):
        """
        Performs the count operation and anonymizes the value(s) using the provided
        privacy budget.

        The operation counts non-zero or non-False values. When a condition
        function is provided, it is invoked so that the data can be transformed
        before counting.

        Parameters
        ----------
        data : list|ndarray
            The data to retrieve the count(s) from.
        epsilon : float
            The privacy budget.
        [condition] : function
            A condition function that receives the data as a parameter and returns
            a list or ndarray of the same size in which for each element is either
            a zero or False when it should not be counted and non-zero or True when
            it should.
        [axis] : int|tuple
            Axis or tuple of axes along which to count non-zeros or non-False value(s).

        Returns
        -------
        float|ndarray
            The anonymized count(s).

        """
        if condition:
            data = condition(data)

        value = np.count_nonzero(data, axis=axis)
        anonymized = DiffPrivLaplaceMechanism.anonymize_count_with_budget(
            value, epsilon
        )
        return anonymized

    @classmethod
    def min(cls, data, epsilon, axis=None):
        """
        Performs the min operation and anonymizes the value(s) using the provided
        privacy budget.

        Parameters
        ----------
        data : list|ndarray
            The data to retrieve the min value(s) from.
        epsilon : float
            The privacy budget.
        [axis] : int|tuple
            Axis or tuple of axes along which to obtain the min value(s).

        Returns
        -------
        float|ndarray
            The anonymized min value(s).

        """
        value = np.min(data, axis=axis)
        anonymized = DiffPrivLaplaceMechanism.anonymize_min_with_budget(value, epsilon)
        return anonymized

    @classmethod
    def max(cls, data, epsilon, axis=None):
        """
        Performs the max operation and anonymizes the value(s) using the provided
        privacy budget.

        Parameters
        ----------
        data : list|ndarray
            The data to retrieve the max value(s) from.
        epsilon : float
            The privacy budget.
        [axis] : int|tuple
            Axis or tuple of axes along which to obtain the max value(s).

        Returns
        -------
        float|ndarray
            The anonymized max value(s).

        """
        value = np.max(data, axis=axis)
        anonymized = DiffPrivLaplaceMechanism.anonymize_max_with_budget(value, epsilon)
        return anonymized

    @classmethod
    def median(cls, data, epsilon, axis=None):
        """
        Performs the median operation and anonymizes the value(s) using the provided
        privacy budget.

        Parameters
        ----------
        data : list|ndarray
            The data to retrieve the median value(s) from.
        epsilon : float
            The privacy budget.
        [axis] : int|tuple
            Axis or tuple of axes along which to obtain the median value(s).

        Returns
        -------
        float|ndarray
            The anonymized median value(s).

        """
        value = np.median(data, axis=axis)
        anonymized = DiffPrivLaplaceMechanism.anonymize_median_with_budget(
            value, epsilon
        )
        return anonymized

    @classmethod
    def proportion(cls, data, epsilon, condition=None, axis=None):
        """
        Performs the proportion operation and anonymizes the value(s) using the
        provided privacy budget.

        The operation counts non-zero or non-False values. When a condition
        function is provided, it is invoked so that the data can be transformed
        before counting. Afterwords, the proportion is calculated using the total
        amount of values.

        Parameters
        ----------
        data : list|ndarray
            The data to retrieve the proportion(s) from.
        epsilon : float
            The privacy budget.
        [condition] : function
            A condition function that receives the data as a parameter and returns
            a list or ndarray of the same size in which for each element is either
            a zero or False when it should not be counted and non-zero or True when
            it should.
        [axis] : int|tuple
            Axis or tuple of axes along which to count non-zeros or non-False value(s).

        Returns
        -------
        float|ndarray
            The anonymized count(s).

        """
        n = np.size(data, axis=axis)
        if condition:
            data = condition(data)

        value = np.count_nonzero(data, axis=axis)
        value = np.divide(value, n)
        anonymized = DiffPrivLaplaceMechanism.anonymize_proportion_with_budget(
            value, n, epsilon
        )
        return anonymized

    @classmethod
    def sum(cls, data, epsilon, axis=None):
        """
        Performs the sum operation and anonymizes the value(s) using the provided
        privacy budget.

        Parameters
        ----------
        data : list|ndarray
            The data to retrieve the sum value(s) from.
        epsilon : float
            The privacy budget.
        [axis] : int|tuple
            Axis or tuple of axes along which to obtain the sum value(s).

        Returns
        -------
        float|ndarray
            The anonymized sum value(s).

        """
        lower = np.min(data, axis=axis)
        upper = np.max(data, axis=axis)
        value = np.sum(data, axis=axis)
        if np.isscalar(lower):
            anonymized = DiffPrivLaplaceMechanism.anonymize_sum_with_budget(
                value, lower, upper, epsilon
            )
        else:
            size = lower.size
            anonymized = np.zeros(size)
            for index in range(0, size):
                anonymized[index] = DiffPrivLaplaceMechanism.anonymize_sum_with_budget(
                    value[index], lower[index], upper[index], epsilon
                )

        return anonymized

    @classmethod
    def mean(cls, data, epsilon, axis=None):
        """
        Performs the mean operation and anonymizes the value(s) using the provided
        privacy budget.

        Parameters
        ----------
        data : list|ndarray
            The data to retrieve the mean value(s) from.
        epsilon : float
            The privacy budget.
        [axis] : int|tuple
            Axis or tuple of axes along which to obtain the mean value(s).

        Returns
        -------
        float|ndarray
            The anonymized mean value(s).

        """
        n = np.size(data, axis=axis)
        lower = np.min(data, axis=axis)
        upper = np.max(data, axis=axis)
        value = np.mean(data, axis=axis)
        if np.isscalar(lower):
            anonymized = DiffPrivLaplaceMechanism.anonymize_mean_with_budget(
                value, lower, upper, n, epsilon
            )
        else:
            size = lower.size
            anonymized = np.zeros(size)
            for index in range(0, size):
                mean_value = DiffPrivLaplaceMechanism.anonymize_mean_with_budget(
                    value[index], lower[index], upper[index], n, epsilon
                )
                anonymized[index] = mean_value

        return anonymized

    @classmethod
    def variance(cls, data, epsilon, axis=None):
        """
        Performs the variance operation and anonymizes the value(s) using the provided
        privacy budget.

        Parameters
        ----------
        data : list|ndarray
            The data to retrieve the variance value(s) from.
        epsilon : float
            The privacy budget.
        [axis] : int|tuple
            Axis or tuple of axes along which to obtain the variance value(s).

        Returns
        -------
        float|ndarray
            The anonymized variance value(s).

        """
        n = np.size(data, axis=axis)
        lower = np.min(data, axis=axis)
        upper = np.max(data, axis=axis)
        value = np.var(data, axis=axis)
        if np.isscalar(lower):
            anonymized = DiffPrivLaplaceMechanism.anonymize_variance_with_budget(
                value, lower, upper, n, epsilon
            )
        else:
            size = lower.size
            anonymized = np.zeros(size)
            for index in range(0, size):
                var_value = DiffPrivLaplaceMechanism.anonymize_variance_with_budget(
                    value[index], lower[index], upper[index], n, epsilon
                )
                anonymized[index] = var_value

        return anonymized
