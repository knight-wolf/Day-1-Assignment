import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib as mpl
import matplotlib.pyplot as plt
%matplotlib inline
from numpy.random import randn, randint, uniform, sample


df = pd.DataFrame(randn(10, 4), columns=['a', 'b', 'c', 'd'])
df
df.plot.bar()
##plt.bar(df.b, df.c, label='b-c', width=0.1)
##plt.bar(df.a, df.d, label='a-d', width=0.1)
plt.title("bar graph")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()
plt.plot()