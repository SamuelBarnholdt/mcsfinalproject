import numpy as np
import matplotlib.pyplot as plt
from cavegen import generateGrid

H = np.array(generateGrid(0.35, 5, 9, 2))
H2 = np.array(generateGrid(0.14, 1, 7, 3))
H3 = np.array(generateGrid(0.14, 1, 7, 3))
H4 = np.array(generateGrid(0.14, 1, 7, 3))

# H2 = np.array(generateGrid(0.1, 1, 5, 2))
# 013,1,5,2
if False:
    #för att plota flera
    p1 = plt.subplot(1, 4, 1)
    p2 = plt.subplot(1, 4, 2)
    p3 = plt.subplot(1, 4, 3)
    p4 = plt.subplot(1, 4, 4)
    p1.imshow(H)
    p2.imshow(H2)
    p3.imshow(H3)
    p4.imshow(H4)
else:
    plt.imshow(H)
plt.show()

# Kanske funkar med 3d