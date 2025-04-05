import numpy as np
import matplotlib.pyplot as plt

print("Hello World!") 

plt.plot([5], [7], 'co')
plt.plot([12], [7], 'm^')
plt.plot([12], [4], 'ys')


plt.axis((0, 15, 0, 10))

plt.xticks(np.arange(0, 15 + 1, 5))

plt.show()