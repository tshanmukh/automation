import numpy as np

import matplotlib.pyplot as plt

data = {'y': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(80)}
data['b'] = data['y'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('y', 'b', c='b', s='d',data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()