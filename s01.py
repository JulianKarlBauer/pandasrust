import pandas as pd


def count_5s(number):
    string_repr = str(number)
    return string_repr.count("5")


series = pd.Series([1, 2, 5, 505])

result = series.apply(count_5s)

print(result)
