import matplotlib.pyplot as plt
import numpy as np
from testing import simulate_on_r


def flatten(l):
    flat = []
    for sl in l:
        for i in sl:
            flat.append(i)
    return flat


N = 50
nTM = (4, 10, 2)
r = np.arange(0.4, 0.5, 0.01)
y = simulate_on_r(N, r, nTM)

r = flatten([[x] * N for x in r])
y = flatten(y)


plt.hist2d(r, y, bins=(80, 80), cmap=plt.cm.jet)
plt.colorbar()
plt.show()
