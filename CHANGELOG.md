## 1.0.5

- Added `postprocess` parameter (enabled by default)  to `DiffPrivStatistics.count` and `DiffPrivStatistics.proportion` which enforces that the returned anonymized values are within their corresponding ranges: `[0, n]` and `[0.0, 1.0]` respectively.
- Simplified exception names:
  - `DiffPrivStatisticsInvalidDimensions` => `DiffPrivInvalidDimensions`
  - `DiffPrivStatisticsSizeMismatch` => `DiffPrivSizeMismatch`
- Added support to allow skipping calculation of statistics for a given data slice by using a kind value of `None` instead of a defined `DiffPrivStatisticKind` value.
- Added Laplace sanitizer `DiffPrivLaplaceSanitizer`.

## 1.0.4

- Added sequential (`DiffPrivSequentialStatisticsQuery`) and parallel (`DiffPrivParallelStatisticsQuery`) composition query functionality.

## 1.0.3

- Added support for calculating data anonymized statistics through `DiffPrivStatistics`.

## 1.0.2

- Added Laplace mechanism anonymization for operations:
  - `min`
  - `max`
  - `median`
  - `sum`

## 1.0.1

- Added baseline Laplace mechanism anonymization for operations:
  - `count`
  - `mean`
  - `proportion`
  - `variance`
