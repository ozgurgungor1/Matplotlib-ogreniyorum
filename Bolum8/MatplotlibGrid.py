# Matplotlib Sütun Çizgilerini Ekleme


# Bir grafige sütun çizgileri ekleme


"""

Bir grafige sutun çizgileri ekleme
----------------------------------


Pyplot ile , grid()  grafige sutun çizzgileri eklemenizi sagliyor
------------********---------------------------------------------

"""









# Ornek Grafige Sütun Çizgileri Ekleyelim


import matplotlib.pyplot as plt
import numpy as np

# Veri dizileri
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# Grafik başlığı ve eksen etiketleri
plt.title("Sports Watch Data")          # Baslik
plt.xlabel("Average Pulse")             # x etiketi
plt.ylabel("Calorie Burnage")           # y etiketi

# Veriyi çizme
plt.plot(x, y)

# Izgara ekleme
plt.grid()              # sutum ekleme görevi görenb fonksiyon

# Grafiği gösterme
plt.show()











# Hangi sutun çizgileriinin görüntülenecegini belirtebiliriz





"""


Hangi sutun çizgileriinin görüntülenecegini belirtebiliriz
------------------------------------------------------------

Hangi sutun çizgileriinin görüntülenecegini belirlemek için axis(eksen) için grid() 
fonksiyonundaki parametreyi ekleyebiliriz




Varsaılan degerler: x ve y her ikisidir



"""




# Ornek : yanlızca x ekseni için sutunları görünteleyelim



import matplotlib.pyplot as plt
import numpy as np


x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])


plt.title("Sports Watch Data")

plt.xlabel("Average Pulse")

plt.ylabel("Calorie Burnage")



plt.plot(x, y)

plt.grid(axis='x')                  # x eksenini göster

plt.show()







# Ornek yanlizca y ekseni için sutuun çizgilerini görüntüleyelim



import matplotlib.pyplot as plt
import numpy as np


x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])


plt.title("Sports Watch Data")

plt.xlabel("Average Pulse")

plt.ylabel("Calorie Burnage")



plt.plot(x, y)

plt.grid(axis='y')                  # y eksenini göster

plt.show()









# Sutun için çizgi özelliklerini ayarlayalım


"""

# Sutun için çizgi özelliklerini ayarlayalım
--------------------------------------------


Sutunun çizgi özelliklerini şu şekilde ayarlayabiliriz:

grid( color='color', linestyle='linestyle', linewidth=number)



color = renk 

linestyle = çizgi stili

linewidth = çizgi genisligi






"""





# Ornek Sutunun çizgi özelliklerini ayarlayalım


import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])



plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")


plt.plot(x, y)
plt.grid(color='green', linestyle='--', linewidth=0.5)  # renk, çizgi stili ve çizgigenisligi degerleri girdik
plt.show()











