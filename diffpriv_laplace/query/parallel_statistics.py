from diffpriv_laplace.statistics import DiffPrivStatistics


class DiffPrivParallelStatisticsQuery(object):
    """
    The parallel composition statistics query class.
    """

    @classmethod
    def query(cls, data, kinds, epsilon, axis=None):
        """
        Performs parallel composition by decomposing a multiple statistic queries
        into sub-queries (each subset assigned to each data slice) which use the
        defined privacy budget which should correspond to the maximum budget of
        the queries.

        Parameters
        ----------
        data : list|ndarray
            The data to retrieve the anonymized statistic value(s) from.
        kind : DiffPrivStatisticKind|list
            The kind of statistics to perform on each data slice.
        epsilon : list
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
        results = DiffPrivStatistics.apply_kind_on_data_slice(
            data, kinds, epsilon, axis=axis
        )
        return results
