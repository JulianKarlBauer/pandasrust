# Check "Extending pandas" documentation
import pandas as pd

from s01 import count_5s

# def count_5s(number):
#     string_repr = str(number)
#     return string_repr.count("5")


@pd.api.extensions.register_series_accessor("counter")
class CountersAccessor:
    def __init__(self, series):
        self._series = series

    def count_5s(self):
        return self._series.apply(count_5s)


series = pd.Series([1, 2, 5, 505])
series = series.counter.count_5s()
print(series)
