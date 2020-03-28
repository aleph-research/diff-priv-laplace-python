import numpy as np
from enum import Flag, auto
from diffpriv_laplace import DiffPrivLaplaceMechanism


class DiffPrivStatisticsInvalidDimensions(Exception):
    pass


class DiffPrivStatisticsSizeMismatch(Exception):
    pass


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

    @classmethod
    def apply_kind_on_data_slice(cls, data, kind, epsilon, axis=None):
        """
        Performs the statistic operations for its corresponding data slice using the
        provided privacy budget. The statistics defined in `kind` at index i is only
        applied to data slice i. Therefore, the length of the `kind` list should be
        the same as the amount of data slices that are derived from `axis`.

        Parameters
        ----------
        data : list|ndarray
            The data to retrieve the variance anonymized statistic(s) from.
        kind : DiffPrivStatisticKind|list
            The kind of statistics to perform on each data slice.
        epsilon : float
            The privacy budget.
        [axis] : int|tuple
            Axis or tuple of axes along which to obtain the anonymized statistic
            value(s).

        Returns
        -------
        list
            The list of anonymized statistics requested and calculated for each data
            slice.

        Raises
        ------
        DiffPrivStatisticsInvalidDimensions
            The exception is raised when the data dimension is invalid.
        DiffPrivStatisticsSizeMismatch
            The exception is raised when the length of the `kind` list is of different
            size than the amount of data slices in `data` defined through `axis`.

        """
        kinds = kind
        if not isinstance(kind, list):
            kinds = [kind]

        if np.ndim(data) == 1:
            data = np.array([data])
            axis = 1

        data_dim = np.ndim(data)
        if data_dim != 2:
            raise DiffPrivStatisticsInvalidDimensions(
                "Invalid data dimension: {}".format(data_dim)
            )

        shape = np.shape(data)
        iter_axis = (axis if axis else 0) - 1
        n = shape[iter_axis]
        kind_len = len(kinds)
        if n != kind_len:
            raise DiffPrivStatisticsSizeMismatch(
                "Data slices and kind have different sizes! [{} != {}]".format(
                    n, kind_len
                )
            )

        results = [None] * kind_len
        for index in range(0, kind_len):
            kind = kinds[index]
            data_slice = np.take(data, [index], axis=iter_axis)
            stats = {}
            if bool(kind & DiffPrivStatisticKind.count):
                value = cls.count(data_slice, epsilon)
                stats[DiffPrivStatisticKind.count] = value

            if bool(kind & DiffPrivStatisticKind.min):
                value = cls.min(data_slice, epsilon)
                stats[DiffPrivStatisticKind.min] = value

            if bool(kind & DiffPrivStatisticKind.max):
                value = cls.max(data_slice, epsilon)
                stats[DiffPrivStatisticKind.max] = value

            if bool(kind & DiffPrivStatisticKind.median):
                value = cls.median(data_slice, epsilon)
                stats[DiffPrivStatisticKind.median] = value

            if bool(kind & DiffPrivStatisticKind.proportion):
                value = cls.proportion(data_slice, epsilon)
                stats[DiffPrivStatisticKind.proportion] = value

            if bool(kind & DiffPrivStatisticKind.sum):
                value = cls.sum(data_slice, epsilon)
                stats[DiffPrivStatisticKind.sum] = value

            if bool(kind & DiffPrivStatisticKind.mean):
                value = cls.mean(data_slice, epsilon)
                stats[DiffPrivStatisticKind.mean] = value

            if bool(kind & DiffPrivStatisticKind.variance):
                value = cls.variance(data_slice, epsilon)
                stats[DiffPrivStatisticKind.variance] = value

            results[index] = stats

        return results
