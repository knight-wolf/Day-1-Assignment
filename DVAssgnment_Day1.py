##Assignment 1 of Day 1
import numpy as np
import pandas as pd
import matplotlib as mlt
import matplotlib.pyplot as plt
%matplotlib inline

x = np.arange(0,10)
y = x * x
plt.title("Lineplot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(x,y,"bo--", linewidth=1, markersize=5)
plt.show()



##Assignment 2 of Day 1
x = [1,2,3,4,5,6,7] ----- days of a week
y = [160,150,140,145,175,165,180] ------ sales


import numpy as np
import pandas as pd
import matplotlib as mlt
import matplotlib.pyplot as plt
%matplotlib inline

x = np.arange(1,8)
y = [160,150,140,145,175,165,180]
plt.title('Lineplot')
plt.xlabel('Days of a week')
plt.ylabel('Sales')
plt.plot(x,y,'bo--', linewidth=1, markersize=5)
plt.show
