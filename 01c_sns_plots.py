import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(color_codes=True)
np.random.seed(sum(map(ord, "prendiamo una parola a caso: Bosone di Higgs")))

x = np.random.normal(size=100)
#sns.distplot(x);
#sns.plt.show()

sns.distplot(x, bins=15, hist=True, kde=False, rug=False);
sns.plt.show()
