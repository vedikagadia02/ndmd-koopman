import numpy as np
import matplotlib.pyplot as plt

array_loaded = np.load('duffing.npy')
print(array_loaded.shape, array_loaded)
# plt.imshow(array_loaded[0])
# plt.show()
for i in range(0,array_loaded[0].size-1):
        plt.plot(array_loaded[0,1,:], array_loaded[0,2,:])
        plt.show()
        break