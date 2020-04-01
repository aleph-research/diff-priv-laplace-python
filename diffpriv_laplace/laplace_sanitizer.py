import numpy as np
from diffpriv_laplace.statistics import DiffPrivStatisticKind
from diffpriv_laplace.query.parallel_statistics import DiffPrivParallelStatisticsQuery
from diffpriv_laplace.exceptions import (
    DiffPrivInvalidDimensions,
    DiffPrivSizeMismatch,
    DiffPrivInvalidDecomposition,
)


class DiffPrivLaplaceSanitizer(object):
    """
    Differential privacy Laplace sanitizer.
    """

    @classmethod
    def decompose_data_slice(cls, data, selectors):
        """
        Decomposes a data slice into a category subsets of independent/disjoint data
        derived from the provided `selectors`.

        Parameters
        ----------
        data : list|ndarray
            The data slice to split.
        selectors : list
            The list of selector functions to apply to the data such that the data
            slice is decomposed into n subsets of the same size, where n is the number
            of decomposing functions. Each selector function should return a boolean
            `ndarray` or `list` where the value is `True` if it belongs to that category
            and `False` otherwise.

        Returns
        -------
        ndarray
            The decomposed data slice.

        Raises
        ------
        DiffPrivInvalidDecomposition
            The exception is raised when there are overlapping elements in the
            decomposed data slice subsets meaning that there is at least one element
            which is present in other subsets. This means that the data slice subsets
            are not independent/disjoint with respect to  each other which is a
            requirement for the Laplace sanitizer.

        """
        n = len(data)
        selectors_len = len(selectors)
        decomposed = np.array([None] * selectors_len * n)
        decomposed = decomposed.reshape((selectors_len, n))
        for index in range(selectors_len):
            select = selectors[index]
            subset = select(data)
            decomposed[index] = np.array(subset)

        if any(decomposed.sum(axis=0) != 1):
            raise DiffPrivInvalidDecomposition(
                "The constructed subsets are not independent! decomposed = {}".format(
                    decomposed
                )
            )

        return decomposed

    @classmethod
    def constrain_anonymized_counts(cls, counts, n):
        """
        Constrain the anonymized counts by a defined quantity.

        Parameters
        ----------
        counts : ndarray
            The anonymized counts.
        n : float
            The quantity to constrain the values by.

        Returns
        -------
        ndarray
            The constrained anonymized counts.

        """
        constrained = (counts / np.sum(counts)) * n
        constrained = np.round(constrained)
        return constrained

    @classmethod
    def count(cls, data, selectors, epsilon, axis=None, postprocess=True):
        """
        Performs Laplace sanitizer counting by selecting the data into
        independent/disjoint data slice subsets and then applying parallel composition
        on each using the defined privacy budget which should correspond to the
        maximum budget of all the count queries. This process creates a histogram
        for each data slice where the counts correspond to the frequency for each
        category.

        Parameters
        ----------
        data : list|ndarray
            The data to retrieve the anonymized statistic value(s) from.
        selectors : list
            The list of lists of selector functions to apply to the data such that
            each collection of functions in index i is applied to its corresponding
            data slice i. If an entry is is `None`, no selecting is performed.
        epsilon : list
            The privacy budget.
        [axis] : int|tuple
            Axis or tuple of axes along which to obtain the anonymized statistic
            value(s).
        [postprocess] : bool
            Indicates whether or not to constrain the anonymized count values.

        Returns
        -------
        ndarray
            The list of anonymized statistics requested subject to the decomposed
            data.

        Raises
        ------
        DiffPrivInvalidDimensions
            The exception is raised when the data dimension is invalid.
        DiffPrivSizeMismatch
            The exception is raised when the length of the `selectors` list is of
            different size than the amount of data slices in `data` defined
            through `axis`.
        DiffPrivInvalidDecomposition
            The exception is raised when there are overlapping elements in the
            decomposed data slice subsets meaning that there is at least one element
            which is present in other subsets. This means that the data slice subsets
            are not independent/disjoint with respect to  each other which is a
            requirement for the Laplace sanitizer.

        """
        if np.ndim(data) == 1:
            data = np.array([data])
            axis = 1

        data_dim = np.ndim(data)
        if data_dim != 2:
            raise DiffPrivInvalidDimensions(
                "Invalid data dimension: {}".format(data_dim)
            )

        if np.ndim(selectors) == 1:
            selectors = [selectors]

        shape = np.shape(data)
        iter_axis = (axis if axis else 0) - 1
        n = shape[iter_axis]
        selectors_len = len(selectors)
        if n != selectors_len:
            raise DiffPrivSizeMismatch(
                "Data slices and selectors have different sizes! [{} != {}]".format(
                    n, selectors_len
                )
            )

        data_slice_len = np.size(data, axis=axis)
        results = [None] * selectors_len
        for index in range(0, selectors_len):
            data_slice_selectors = selectors[index]
            if data_slice_selectors and isinstance(data_slice_selectors, list):
                data_slice = np.take(data, [index], axis=iter_axis)
                data_slice = np.ravel(data_slice)
                decomposed = cls.decompose_data_slice(data_slice, data_slice_selectors)
                kind = [DiffPrivStatisticKind.count] * len(data_slice_selectors)
                result = DiffPrivParallelStatisticsQuery.query(
                    decomposed, kind, epsilon, axis=1
                )
                counts = np.array(
                    [value[DiffPrivStatisticKind.count] for value in result]
                )
                if postprocess:
                    counts = cls.constrain_anonymized_counts(counts, data_slice_len)

                results[index] = counts

        return results
