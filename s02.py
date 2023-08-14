# Check "Extending pandas" documentation
import pandas as pd
import numpy as np

from s01 import count_5s


@pd.api.extensions.register_series_accessor("counter")
class CountersAccessor:
    def __init__(self, series):
        self._series = series

    def count_5s(self):
        return self._series.apply(count_5s)


series = pd.Series([1, 2, 5, 505])
series = series.counter.count_5s()
print(series)

my_series = pd.Series(np.random.randint(0, 999, size=10_000_000))

# # To time the execution on the larger "my_series" data,
# # start ipython-session and enter the following command:
# %timeit my_series.counter.count_5s()
