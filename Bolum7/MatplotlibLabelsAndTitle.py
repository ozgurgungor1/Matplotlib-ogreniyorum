# Matplotlib Labels And Title


# Bir grafik için etiketler oluşturun


"""
Bir grafik için etiketler oluşturun
-----------------------------------


Pyplot ile x ve y eksenine etiket ayarlamak için  xlabel()  ve ylabel() fonsiyonlarını kullanabilriz



"""




# Ornek x ve y eksenine etiketler ekleyin


import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x,y)

plt.xlabel("Average Pulse")              # x eksenine ortalama nabız diyoruz
plt.ylabel("Calorie Burnage")            # y eksenine Calori yakma diyoruz

plt.show()



# Bir grafik için baslik olusturun


"""

Bir grafik için baslik olusturun
--------------------------------


Pyplot ile grafik için baslik ayarlamak istiyorsak python fonksiyonu kullanmalıyız.
 


"""


# Ornek x ve y ekseni için bir baslik ve etiketler ekleyelim


import matplotlib.pyplot as pl
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x,y)



# Tablo Basliklar

plt.title("Sport Watch Data")

plt.xlabel("Average Pulse")

plt.ylabel("Calorie Burnage")

plt.show()







# Baslik ve etiketler için yazi tipi özellkilerini ayarlayalim


"""

Baglik ve etiketler icin yazi tipi özelliklerini ayarlamak için
xlabel(), ylabel() ve title() içindeki fontdict parametresini kullanabilirsiniz.


"""



# Baslik ve etiketler için yazı tipi özelliklerini ayarlayalım

import matplotlib.pyplot as plt
import numpy as np


x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])




font1 = {'family' :'serif', 'color' : 'blue', 'size':20}      #Baslik
font2 = {'family':'serif', 'color': 'yellow', 'size':15}     #Etiketler için x y


plt.title("Sport Watch Data", fontdict=font1)



plt.xlabel("Average Pulse", fontdict=font2)
plt.ylabel("Calorie Burnage", fontdict=font2)

plt.plot(x, y)
plt.show()




# Basligi konumlandirma


"""

Basligi konumlandırma
---------------------


Basligi konumlandırmak için loc parametresini kullanabilirsiniz.

Genel degerler veya yasal degerler left, right ve center dir 
Ama varsayılan degerimiz center yani merkezdir



left = sol
right = sag
center = merkez


location = konum --> loc



"""




# Ornek basligi sola konumlandiralim


import  matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])



plt.title("Sport Watch Data", loc='left')     #basligi sola aldık , loc='left' ile
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x,y)
plt.show()















