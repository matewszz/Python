import matplotlib.pyplot as plt
import numpy as np

a = 5
b = 6
c = 1

x = np.arange(3)
plt.bar(x, height=[1,2,3])
plt.xticks(x, ['a','b','c'])