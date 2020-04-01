Differential privacy using Laplace mechanism documentation
==========================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

The Laplace mechanism consists of adding noise, generated through the Laplace distribution
and the privacy budget, to a value. The derived value is said to be "anonymized" if the
privacy budget used is good enough.

Privacy budget
--------------

The privacy budget ``epsilon`` defines how much privacy protection to apply.

  - If ``epsilon`` is large less noise will be added and therefore more information leakage exists, so less privacy protection will be present.
  - If ``epsilon`` is small (must be larger than zero) more noise will be added and therefore less information leakage exists, so more privacy protection will be present.

Sequential composition
----------------------

When using a data set one tends to issue multiple statistical queries such that one output
might be correlated with another. In doing so we reveal more, therefore leak more information
so less privacy protection will be present. In order to address this problem, we divide the
provided privacy budget into the amount of queries performed creating a query privacy budget.
This query privacy budget is then used for each statistic query in order to strengthen the
privacy protection.

.. currentmodule:: diffpriv_laplace

.. autoclass:: DiffPrivSequentialStatisticsQuery
    :members:

Examples:

- Perform mean and variance statistic queries for single data slice:

.. code-block:: python

  import numpy as np
  from diffpriv_laplace import DiffPrivSequentialStatisticsQuery, DiffPrivStatisticKind


  epsilon = 0.1
  data = np.array(list(range(0, 20)) + [100.0])
  kinds = DiffPrivStatisticKind.mean | DiffPrivStatisticKind.variance
  results = DiffPrivSequentialStatisticsQuery.query(data, kinds, epsilon)

- Perform mean and variance statistic queries for multiple data slices:

.. code-block:: python

  import numpy as np
  from diffpriv_laplace import DiffPrivSequentialStatisticsQuery, DiffPrivStatisticKind


  epsilon = 0.1
  data = np.array([list(range(0, 20)) + [100.0]] * 3)
  kinds = [DiffPrivStatisticKind.mean | DiffPrivStatisticKind.variance] * 3
  results = DiffPrivSequentialStatisticsQuery.query(data, kinds, epsilon, axis=1)

Parallel composition
--------------------

Unlike the pessimistic approach of sequential composition, when using disjoint data sets we
assume there isn't any correlation between statistical queries. Therefore, if we have a privacy
budget for each query we choose the maximum one and use it for all queries.

.. currentmodule:: diffpriv_laplace

.. autoclass:: DiffPrivParallelStatisticsQuery
    :members:

Examples:

- Perform mean and variance statistic queries for single data slice:

.. code-block:: python

  import numpy as np
  from diffpriv_laplace import DiffPrivParallelStatisticsQuery, DiffPrivStatisticKind


  epsilon = 0.1
  data = np.array(list(range(0, 20)) + [100.0])
  kinds = DiffPrivStatisticKind.mean | DiffPrivStatisticKind.variance
  results = DiffPrivParallelStatisticsQuery.query(data, kinds, epsilon)

- Perform mean and variance statistic queries for multiple data slices:

.. code-block:: python

  import numpy as np
  from diffpriv_laplace import DiffPrivParallelStatisticsQuery, DiffPrivStatisticKind


  epsilon = 0.1
  data = np.array([list(range(0, 20)) + [100.0]] * 3)
  kinds = [DiffPrivStatisticKind.mean | DiffPrivStatisticKind.variance] * 3
  results = DiffPrivParallelStatisticsQuery.query(data, kinds, epsilon, axis=1)


Laplace sanitizer
-----------------

The Laplace sanitizer is an extension to the Laplace mechanism that is usable if it's possible
to decompose categorical data into disjoint/independent subsets (e.g. a histogram or a
contingency table). Under these circumstances it's possible to use parallel composition statistical
queries.

.. currentmodule:: diffpriv_laplace

.. autoclass:: DiffPrivLaplaceSanitizer
    :members:

Examples:

- Perform categorical anonymized count:

.. code-block:: python

  import numpy as np
  from diffpriv_laplace import DiffPrivLaplaceSanitizer


  epsilon = 0.1
  data = np.array([0.01, -0.01, 0.03, -0.001, 0.1] * 2)

  def selector_positive(data):
      return data >= 0.0

  def selector_negative(data):
      return data < 0.0

  selectors = [selector_positive, selector_negative]
  value = DiffPrivLaplaceSanitizer.count(data, selectors, epsilon)

Statistics
----------

.. currentmodule:: diffpriv_laplace

.. autoclass:: DiffPrivStatistics
    :members:

Examples:

- Perform anonymized count:

.. code-block:: python

  import numpy as np
  from diffpriv_laplace import DiffPrivStatistics


  epsilon = 0.1
  data = np.array([True, False, True, False, True] * 2)
  value = DiffPrivStatistics.count(data, epsilon)

- Perform anonymized count with condition function:

.. code-block:: python

  import numpy as np
  from diffpriv_laplace import DiffPrivStatistics


  epsilon = 0.1
  data = np.array([0.01, -0.01, 0.03, -0.001, 0.1] * 2)

  def condition(data):
      return data >= 0.0

  value = DiffPrivStatistics.count(data, epsilon, condition=condition)

- Perform anonymized min:

.. code-block:: python

  import numpy as np
  from diffpriv_laplace import DiffPrivStatistics


  epsilon = 0.1
  data = np.array(list(range(1, 101)))
  value = DiffPrivStatistics.min(data, epsilon)

- Perform anonymized max:

.. code-block:: python

  import numpy as np
  from diffpriv_laplace import DiffPrivStatistics


  epsilon = 0.1
  data = np.array(list(range(1, 101)))
  value = DiffPrivStatistics.max(data, epsilon)

- Perform anonymized median:

.. code-block:: python

  import numpy as np
  from diffpriv_laplace import DiffPrivStatistics


  epsilon = 0.1
  data = np.array(list(range(1, 101)))
  value = DiffPrivStatistics.median(data, epsilon)

- Perform anonymized proportion:

.. code-block:: python

  import numpy as np
  from diffpriv_laplace import DiffPrivStatistics


  epsilon = 0.1
  data = np.array([True, False, True, False, True] * 2)
  value = DiffPrivStatistics.proportion(data, epsilon)

- Perform anonymized proportion with condition function:

.. code-block:: python

  import numpy as np
  from diffpriv_laplace import DiffPrivStatistics


  epsilon = 0.1
  data = np.array([0.01, -0.01, 0.03, -0.001, 0.1] * 2)

  def condition(data):
      return data >= 0.0

  value = DiffPrivStatistics.proportion(data, epsilon, condition=condition)

- Perform anonymized sum:

.. code-block:: python

  import numpy as np
  from diffpriv_laplace import DiffPrivStatistics


  epsilon = 0.1
  data = np.array(list(range(1, 101)))
  value = DiffPrivStatistics.sum(data, epsilon)

- Perform anonymized mean:

.. code-block:: python

  import numpy as np
  from diffpriv_laplace import DiffPrivStatistics


  epsilon = 0.1
  data = np.array(list(range(1, 101)))
  value = DiffPrivStatistics.mean(data, epsilon)

- Perform anonymized variance:

.. code-block:: python

  import numpy as np
  from diffpriv_laplace import DiffPrivStatistics


  epsilon = 0.1
  data = np.array(list(range(1, 101)))
  value = DiffPrivStatistics.variance(data, epsilon)

Laplace mechanism
-----------------

.. currentmodule:: diffpriv_laplace

.. autoclass:: DiffPrivLaplaceMechanism
    :members:
    :special-members:

Examples:

- Create an instance with a defined privacy budget:

.. code-block:: python

  from diffpriv_laplace import DiffPrivLaplaceMechanism


  epsilon = 0.1
  anonymizer = DiffPrivLaplaceMechanism(epsilon)

- Anonymize a count value:

.. code-block:: python

  from diffpriv_laplace import DiffPrivLaplaceMechanism


  epsilon = 0.1
  value = 32.0

  # Using the class method
  anonymized = DiffPrivLaplaceMechanism.anonymize_count_with_budget(value, epsilon)

  # Using an instance
  anonymizer = DiffPrivLaplaceMechanism(epsilon)
  anonymized = anonymizer.anonymize_count(value)


- Anonymize a min value:

.. code-block:: python

  from diffpriv_laplace import DiffPrivLaplaceMechanism


  epsilon = 0.1
  value = 32.0

  # Using the class method
  anonymized = DiffPrivLaplaceMechanism.anonymize_min_with_budget(value, epsilon)

  # Using an instance
  anonymizer = DiffPrivLaplaceMechanism(epsilon)
  anonymized = anonymizer.anonymize_min(value)

- Anonymize a max value:

.. code-block:: python

  from diffpriv_laplace import DiffPrivLaplaceMechanism


  epsilon = 0.1
  value = 32.0

  # Using the class method
  anonymized = DiffPrivLaplaceMechanism.anonymize_max_with_budget(value, epsilon)

  # Using an instance
  anonymizer = DiffPrivLaplaceMechanism(epsilon)
  anonymized = anonymizer.anonymize_max(value)

-Anonymize a median value:

.. code-block:: python

  from diffpriv_laplace import DiffPrivLaplaceMechanism


  epsilon = 0.1
  value = 32.0

  # Using the class method
  anonymized = DiffPrivLaplaceMechanism.anonymize_median_with_budget(value, epsilon)

  # Using an instance
  anonymizer = DiffPrivLaplaceMechanism(epsilon)
  anonymized = anonymizer.anonymize_median(value)

- Anonymize a proportion value:

.. code-block:: python

  from diffpriv_laplace import DiffPrivLaplaceMechanism


  epsilon = 0.1
  n = 50.0
  value = 32.0

  # Using the class method
  anonymized = DiffPrivLaplaceMechanism.anonymize_proportion_with_budget(value, n, epsilon)

  # Using an instance
  anonymizer = DiffPrivLaplaceMechanism(epsilon)
  anonymized = anonymizer.anonymize_proportion(value, n)

- Anonymize a sum value:

.. code-block:: python

  from diffpriv_laplace import DiffPrivLaplaceMechanism


  epsilon = 0.1
  lower = 0.1
  upper = 100.3
  value = 32.0

  # Using the class method
  anonymized = DiffPrivLaplaceMechanism.anonymize_sum_with_budget(value, lower, upper, epsilon)

  # Using an instance
  anonymizer = DiffPrivLaplaceMechanism(epsilon)
  anonymized = anonymizer.anonymize_sum(value, lower, upper)

- Anonymize a mean value:

.. code-block:: python

  from diffpriv_laplace import DiffPrivLaplaceMechanism


  epsilon = 0.1
  lower = 0.1
  upper = 100.3
  n = 50.0
  value = 32.0

  # Using the class method
  anonymized = DiffPrivLaplaceMechanism.anonymize_mean_with_budget(value, lower, upper, n, epsilon)

  # Using an instance
  anonymizer = DiffPrivLaplaceMechanism(epsilon)
  anonymized = anonymizer.anonymize_mean(value, lower, upper, n)


- Anonymize a variance value:

.. code-block:: python

  from diffpriv_laplace import DiffPrivLaplaceMechanism


  epsilon = 0.1
  lower = 0.1
  upper = 100.3
  n = 50.0
  value = 32.0

  # Using the class method
  anonymized = DiffPrivLaplaceMechanism.anonymize_variance_with_budget(value, lower, upper, n, epsilon)

  # Using an instance
  anonymizer = DiffPrivLaplaceMechanism(epsilon)
  anonymized = anonymizer.anonymize_variance(value, lower, upper, n)

Index
=====

* :ref:`genindex`
