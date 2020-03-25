diff-priv-laplace-python
=========================

Implementation of [differential privacy][1] value anonymization using [Laplace mechanism][2].

## Table of Contents

- [diff-priv-laplace-python](#diff-priv-laplace-python)
  * [Install](#install)
  * [Documentation](#documentation)
  * [Examples](#examples)
    + [Statistics](#statistics)
    + [Laplace mechanism](#laplace-mechanism)
  * [License](#license)

## Install

```console
$ pip install diff-priv-laplace-python
```

## Documentation

The privacy budget `epsilon` defines how much privacy protection to apply.

  - If `epsilon` is large, less noise will be added, therefore more information leakage exists so less privacy protection will be present.
  - If `epsilon` is small (must be larger than zero), more noise will be added, therefore less information leakage so more privacy protection will be present.

For a complete API documentation checkout the [python docs][3].

## Examples

### Statistics

The anonymized statistics.

#### Perform anonymized count

```python
import numpy as np
from diffpriv_laplace import DiffPrivStatistics


epsilon = 0.1
data = np.array([True, False, True, False, True] * 2)
value = DiffPrivStatistics.count(data, epsilon)
```

#### Perform anonymized count with condition function

```python
import numpy as np
from diffpriv_laplace import DiffPrivStatistics


epsilon = 0.1
data = np.array([0.01, -0.01, 0.03, -0.001, 0.1] * 2)

def condition(data):
    return data >= 0.0

value = DiffPrivStatistics.count(data, epsilon, condition=condition)
```

#### Perform anonymized min

```python
import numpy as np
from diffpriv_laplace import DiffPrivStatistics


epsilon = 0.1
data = np.array(list(range(1, 101)))
value = DiffPrivStatistics.min(data, epsilon)
```

#### Perform anonymized max

```python
import numpy as np
from diffpriv_laplace import DiffPrivStatistics


epsilon = 0.1
data = np.array(list(range(1, 101)))
value = DiffPrivStatistics.max(data, epsilon)
```

#### Perform anonymized median

```python
import numpy as np
from diffpriv_laplace import DiffPrivStatistics


epsilon = 0.1
data = np.array(list(range(1, 101)))
value = DiffPrivStatistics.median(data, epsilon)
```

#### Perform anonymized proportion

```python
import numpy as np
from diffpriv_laplace import DiffPrivStatistics


epsilon = 0.1
data = np.array([True, False, True, False, True] * 2)
value = DiffPrivStatistics.proportion(data, epsilon)
```

#### Perform anonymized proportion with condition function

```python
import numpy as np
from diffpriv_laplace import DiffPrivStatistics


epsilon = 0.1
data = np.array([0.01, -0.01, 0.03, -0.001, 0.1] * 2)

def condition(data):
    return data >= 0.0

value = DiffPrivStatistics.proportion(data, epsilon, condition=condition)
```

#### Perform anonymized sum

```python
import numpy as np
from diffpriv_laplace import DiffPrivStatistics


epsilon = 0.1
data = np.array(list(range(1, 101)))
value = DiffPrivStatistics.sum(data, epsilon)
```

#### Perform anonymized mean

```python
import numpy as np
from diffpriv_laplace import DiffPrivStatistics


epsilon = 0.1
data = np.array(list(range(1, 101)))
value = DiffPrivStatistics.mean(data, epsilon)
```

#### Perform anonymized variance

```python
import numpy as np
from diffpriv_laplace import DiffPrivStatistics


epsilon = 0.1
data = np.array(list(range(1, 101)))
value = DiffPrivStatistics.variance(data, epsilon)
```

### Laplace mechanism

The core Laplace mechanism used to construct the anonymized statistics.

#### Create an instance with a defined privacy budget

```python
from diffpriv_laplace import DiffPrivLaplaceMechanism


epsilon = 0.1
anonymizer = DiffPrivLaplaceMechanism(epsilon)
```

#### Anonymize a count value

```python
from diffpriv_laplace import DiffPrivLaplaceMechanism


epsilon = 0.1
value = 32.0

# Using the class method
anonymized = DiffPrivLaplaceMechanism.anonymize_count_with_budget(value, epsilon)

# Using an instance
anonymizer = DiffPrivLaplaceMechanism(epsilon)
anonymized = anonymizer.anonymize_count(value)
```

#### Anonymize a min value

```python
from diffpriv_laplace import DiffPrivLaplaceMechanism


epsilon = 0.1
value = 32.0

# Using the class method
anonymized = DiffPrivLaplaceMechanism.anonymize_min_with_budget(value, epsilon)

# Using an instance
anonymizer = DiffPrivLaplaceMechanism(epsilon)
anonymized = anonymizer.anonymize_min(value)
```

#### Anonymize a max value

```python
from diffpriv_laplace import DiffPrivLaplaceMechanism


epsilon = 0.1
value = 32.0

# Using the class method
anonymized = DiffPrivLaplaceMechanism.anonymize_max_with_budget(value, epsilon)

# Using an instance
anonymizer = DiffPrivLaplaceMechanism(epsilon)
anonymized = anonymizer.anonymize_max(value)
```

#### Anonymize a median value

```python
from diffpriv_laplace import DiffPrivLaplaceMechanism


epsilon = 0.1
value = 32.0

# Using the class method
anonymized = DiffPrivLaplaceMechanism.anonymize_median_with_budget(value, epsilon)

# Using an instance
anonymizer = DiffPrivLaplaceMechanism(epsilon)
anonymized = anonymizer.anonymize_median(value)
```

#### Anonymize a proportion value

```python
from diffpriv_laplace import DiffPrivLaplaceMechanism


epsilon = 0.1
n = 50.0
value = 32.0

# Using the class method
anonymized = DiffPrivLaplaceMechanism.anonymize_proportion_with_budget(value, n, epsilon)

# Using an instance
anonymizer = DiffPrivLaplaceMechanism(epsilon)
anonymized = anonymizer.anonymize_proportion(value, n)
```

#### Anonymize a sum value

```python
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
```

#### Anonymize a mean value

```python
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
```

#### Anonymize a variance value

```python
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
```

## Known Issues

Please open an [issue][4] for anything not on this list!

## License
[MIT][5]

[1]: https://en.wikipedia.org/wiki/Differential_privacy
[2]: https://en.wikipedia.org/wiki/Differential_privacy#The_Laplace_mechanism
[3]: https://aleph-research.github.io/diff-priv-laplace-python/
[4]: https://github.com/aleph-research/diff-priv-laplace-python/issues/new
[5]: https://github.com/plaid/aleph-research/diff-priv-laplace-python/blob/master/LICENSE
