import pandas as pd
import matplotlib.pyplot as plt


# load a csv file to a pandas dataframe
df = pd.read_csv('data/weight-height.csv')

# Use pandas to plot
df.plot(kind='scatter', x='Height', y='Weight')

plt.title('Humans')
plt.draw()
plt.show()


# solution:
males = df[df['Gender'] == 'Male']
females = df[df['Gender'] != 'Male']

# init new figure
fig = plt.figure()

# plt.hist(males['Height'].values, label = 'Males')
# plt.hist(females['Height'].values, color = 'r', label = 'Females')

males['Height'].plot(kind='hist', label='Males', alpha=0.5)
females['Height'].plot(kind='hist', color='r', label='Females', alpha=0.5)

plt.title('Humans')
plt.xlabel('Height')
plt.ylabel('Count')
plt.legend()
plt.draw()
plt.show()

# ## Exercises:
#
# 1) Male / Female population
#    - separate the male and female population by color using
#      df[condition] clauses
#      (http://pandas.pydata.org/pandas-docs/stable/10min.html#boolean-indexing)
#    - label the axes
#    - discuss
#
# 2) Histograms
#    - plot the histogram of the heights for males and for females
#      on the same plot
#    - use alpha to control transparency
#    - plot a vertical line at the mean using axvline
#
# 3) Check the code in the advanced folder:
#    - advanced/00_pandas_review.ipynb
#    - advanced/01_exploration.ipynb
#    - load any dataset in the data folder
#    - explore it and plot it
