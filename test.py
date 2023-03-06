import numpy as np
import matplotlib.pyplot as plt

X = np.arange(0,np.pi*2,np.pi*2/100)
Y = np.sin(X)

slope_Y = np.diff(Y)/np.diff(X)

plt.plot(X,Y)
plt.plot(X[:-1],slope_Y)
plt.show()