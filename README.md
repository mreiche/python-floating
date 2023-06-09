![Tests Status](https://github.com/mreiche/python-floating/actions/workflows/tests.yml/badge.svg)
[![Code Coverage Status](https://codecov.io/github/mreiche/python-floating/branch/main/graph/badge.svg)](https://app.codecov.io/github/mreiche/python-floating)

# python-floating

Calculates floating precision.

## Basic API

```python
import floating

assert floating.round(13) == 13.00
assert floating.round(13.1337) == 13.13
assert floating.round(0.003751) == 0.0038
```

### Precision

```python
assert floating.round(13, precision=3) == 13.000
```

### Calc precision

```python
assert floating.calc_precision(0.003751, 2) == 4
```

## Run the tests

```shell
PYTHONPATH="." pytest --cov=floating tests/
```

### Release update
1. Update version in `setup.py`
2. Package library
    ```shell
    python setup.py sdist
    ```
3. Publish library
    ```shell
    twine upload dist/floating-[version].tar.gz
    ```
