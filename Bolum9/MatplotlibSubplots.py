# Matplotlib Subplots --> Matplotlib Alt Grafikleri

# Çoklu grafikleri görüntüleme

"""
Çoklu grafikleri görüntüleme
----------------------------

subplot() fonksiyonu ile tek bir figür içerisine birden çok grafik çizebiliriz.
"""

# Örnek: 2 grafik çizelim

import matplotlib.pyplot as plt
import numpy as np

# Plot 1 - Grafik 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Grafik 1")

# Plot 2 - Grafik 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.title("Grafik 2")

plt.show()

# Subplots = Alt Grafikler
# 1. parametremiz olan 1 değeri satır sayısı
# 2. parametremiz olan 2 değeri sütun sayısı
# 3. parametremiz olan 1 ise grafiğin indeksi veya sırası






# subplot() fonksiyonu


"""

subplot() Fonksiyonu şekil düzenini açıklar ve üç argüman alır.


# Subplots = Alt Grafikler
# 1. parametremiz olan 1 değeri satır sayısı
# 2. parametremiz olan 2 değeri sütun sayısı
# 3. parametremiz olan 1 ise grafiğin indeksi veya sırası





Yani 2 satır ve 1 sütunlu bir şekil istiyorsak (yani iki grafigin yan yana yerine üst üste görüntülenecegi anlamına  gelir)


"""



# Ornek üst üste 2 grafik çiz


import matplotlib.pyplot as plt
import numpy as np



# Plot 1 - Grafik 1
x = np.array([0, 1, 2, 3])
y = np.array([3, 8 ,1, 10])

plt.subplot(2, 1, 1)
plt.plot(x, y)



# Plot 2 - Grafik 2

x = np.array([0, 1, 2, 3])

y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x, y)

plt.show()




# Tek bir şelik üzerine istediğimiz kadar grafik çizebiliriz, sadece satır, sütun grafigin indeksini tanımlayın.






"""


----------*grafik  1.index
----------*grafik  2.index
----------*grafik  3.index
----------*grafik  4.index


grafik 1
plt.plot(x, y)
plt.subplot(4, 1, 1)





grafik 2
plt.plot(x, y)
plt.subplot(4, 1, 2)


grafik 3
plt.plot(x, y)
plt.subplot(4, 1, 3)


grafik 4
plt.plot(x, y)
plt.subplot(4, 1, 4)


"""




# Ornek 6 tane grafik cizin



import matplotlib.pyplot as plt
import numpy as np




# Grafik 1

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])



plt.subplot(2, 3, 1)
plt.plot(x, y)


# Grafik 2

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x, y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.plot(x, y)


# Grafik 3

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])


plt.subplot(2, 3, 3)
plt.plot(x, y)


# Grafik 4

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])


plt.subplot(2, 3, 4)
plt.plot(x, y)


# Grafik 5

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])


plt.subplot(2, 3, 5)
plt.plot(x, y)


# Grafik 6


x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])



plt.subplot(2, 3, 6)
plt.plot(x, y)


plt.show()




# Title - Baslik

"""

Title - Baslik 
--------------

title() fonksiyonu ile her grafige baslik verebiliriz





"""





# ornek 2 grafigimiz olsun basliklarla beraber



import matplotlib.pyplot as plt
import numpy as np



# grafik 1

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)             # 1. Grafik
plt.plot(x, y)
plt.title("SALES")







# grafik 2


x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 2)             # 2. Grafik
plt.plot(x, y)
plt.title("INCOME")


plt.show()




# Super title --> Super Baslik


"""

Super Title --> Super Baslik
----------------------------


suptitle() fonksiyonu ile tum sekme veya dyagrama baslik ekleyebiliriz



"""




import matplotlib.pyplot as plt
import numpy as np

# Grafik 1

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("SALES")



# Grafik 2

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.title("INCOME")



plt.suptitle("MY SHOP")        # Ana baslik

plt.show()




