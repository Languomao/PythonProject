from pandas import read_csv

series = read_csv('IntraTM-2005-01-01-00-30.csv', header=0, index_col=0, squeeze=True)
print(series.values)
