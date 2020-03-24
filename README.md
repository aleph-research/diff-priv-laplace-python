diff-priv-laplace-python
=========================

Implementation of differential privacy value anonymization using [Laplace mechanism][1].

## Table of Contents

- [diff-priv-laplace-python](#diff-priv-laplace-python)
  * [Install](#install)
  * [Documentation](#documentation)
  * [Examples](#examples)
  * [License](#license)

## Install

```console
$ pip install diff-priv-laplace-python
```

## Documentation

For a complete API documentation checkout the [python docs][2].

## Examples

### Create an instance with a defined privacy budget

```python
from diffpriv_laplace import DiffPrivLaplaceMechanism


epsilon = 0.1
anonymizer = DiffPrivLaplaceMechanism(epsilon)
```

### Anonymize a count value

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

### Anonymize a min value

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

### Anonymize a max value

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

### Anonymize a median value

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

### Anonymize a proportion value

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

### Anonymize a sum value

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

### Anonymize a mean value

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

### Anonymize a variance value

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

Please open an [issue][3] for anything not on this list!

## License
[MIT][4]

[1]: https://en.wikipedia.org/wiki/Differential_privacy#The_Laplace_mechanism
[2]: https://aleph-research.github.io/diff-priv-laplace-python/
[3]: https://github.com/aleph-research/diff-priv-laplace-python/issues/new
[4]: https://github.com/plaid/aleph-research/diff-priv-laplace-python/blob/master/LICENSE
