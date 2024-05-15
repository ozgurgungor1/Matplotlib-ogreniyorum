# Pyplot nedir?  Pyplot Alt moduldur

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 6])     # x degerleri 0,1,2,3,4,5,6
y = np.array([0 ,250])   # y degerleri 0, 50, 100, 150, 200, 250

plt.plot(x, y)           # plt.plot(x degerleri bagintisi, y degerleri bagintisi)
plt.show()               # show demek göster demek  gorüntüle demek yani


