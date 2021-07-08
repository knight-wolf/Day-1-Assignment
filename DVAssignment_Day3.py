import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib as mpl
import matplotlib.pyplot as plt
%matplotlib inline
from numpy.random import randn, randint, uniform, sample

fmri = sns.load_dataset('fmri')
fmri.head()

sns.relplot(x = 'timepoint', y = 'signal', kind = 'line', data = fmri)
sns.scatterplot(x = 'timepoint', y = 'signal', hue = 'region', data = fmri)
sns.catplot(x = 'timepoint', y = 'signal', kind = 'box', data = fmri, hue = 'region')