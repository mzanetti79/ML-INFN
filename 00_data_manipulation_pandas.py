import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### Create random data
# The first feature will be the date (first 6 days of 2017)
dates = pd.date_range('20170101', periods=6)

# Then create a dataframe with the dates as index
# and a corresponding 6x4 (6 records with 4 features) matrix of random numbers.
# The four features are simply A B C D
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

# Take a look at the data. head(n=5) and tail(n=5) take the number of records
# to display as argument
df.head()
df.tail(4)

# index
df.index
# columns (features)
df.columns
# values
df.values

# some basic stats
df.describe()

# Some operations
df.T # transpose matrix
df.sort_index(axis=1,ascending=False) # sort by features
df.sort_values(by='B') # sort by value
