import numpy as np
from diffpriv_laplace.statistics import DiffPrivStatistics


class DiffPrivSequentialStatisticsQuery(object):
    """
    The sequential composition statistics query class.
    """

    @classmethod
    def query_count(cls, kinds):
        """
        Determines the amount of queries to perform.

        Parameters
        ----------
        kinds : list
            The list of `DiffPrivStatisticKind` to calculate the queries from.

        Returns
        -------
        float
            The amount of queries to perform.

        """
        query_count = np.sum([kind.size for kind in kinds])
        return float(query_count)

    @classmethod
    def calculate_query_epsilon(cls, kinds, epsilon):
        """
        Calculates the privacy budget to use for each query.

        Parameters
        ----------
        kinds : list
            The list of `DiffPrivStatisticKind` to calculate the queries from.
        epsilon : float
            The privacy budget to calculate the query privacy budget from.

        Returns
        -------
        float
            The calculated privacy budget to use for each query.

        """
        query_count = cls.query_count(kinds)
        query_epsilon = np.divide(epsilon, query_count)
        return query_epsilon

    @classmethod
    def query(cls, data, kinds, epsilon, axis=None):
        """
        Performs sequential composition by decomposing a multiple statistic queries
        into sub-queries (each subset assigned to each data slice) which use a
        portion of the defined privacy budget.

        Parameters
        ----------
        data : list|ndarray
            The data to retrieve the anonymized statistic value(s) from.
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
            The list of anonymized statistics requested.

        Raises
        ------
        DiffPrivStatisticsInvalidDimensions
            The exception is raised when the data dimension is invalid.
        DiffPrivStatisticsSizeMismatch
            The exception is raised when the length of the `kind` list is of
            different size than the amount of data slices in `data` defined
            through `axis`.

        """
        query_epsilon = (
            cls.calculate_query_epsilon(kinds, epsilon)
            if isinstance(kinds, list)
            else epsilon
        )
        results = DiffPrivStatistics.apply_kind_on_data_slice(
            data, kinds, query_epsilon, axis=axis
        )
        return results
