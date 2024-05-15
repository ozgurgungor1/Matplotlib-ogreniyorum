# matplotlib Markers --> Matplotlib Isaretleri


"""


Markers --> Isaretciler


marker --> Her noktayi belirli bir isaretci ile vurgulamak için anahtar kelime bagimsiz degiskenini kullanabilirsiniz
                                   ********






"""



# Her noktayi bir daire ile isaretleyelim


import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker='o', color='red') # marker = isaretleyici
plt.show()









# Ornek her noktayi yıldızla işaretleme






import  matplotlib.pyplot as plt
import  numpy as np





ypoints = np.array([3, 8, 1, 10])







plt.plot(ypoints, marker='o', color='red')
plt.show()








# Marker Referance --> İsret Referansı


"""



Marker Referance --> İsret Referansı
------------------------------------

Bu işaretcilerden herhangi birini seçebilirsiniz:


marker    Description
------    -----------
'o'       Circle
'*'       Start
'.'       Point
','       Pixel
'x'       x
'x'       x (filled)
'+'       Plus
'P'       Plus (filled)
's'       Square
'D'       Diamond
'd'       Diamond (thin)
'p'       Pentagon
'H'       Hexagon
'h'       Hexagon
'v'       Triangle Down
'ters v'  Triangle Up
'<'       Triangle Left
'>'       Triangle Right
'1'       Tri Down 
'2'       Tri Up
'3'       Tri Left
'4'       Tri Right
'I'       Vline
'_'       Hline




"""

"""





# Format Strings fmt --> Dizileri biçimlendirme fmt
---------------------------------------------------



Isaretciyi belirtmek için  kısayol dizisi notasyonu parametresinide kullanabilirsiniz





fmt --> marker  line   color



marker = isaretleyici line =  satir veya çizgi color = renk




"""



# Her noktayı bir daire ile işaretleyin


import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()

# o = marker yeni isretleyici
# : = line cizgi stilimiz
# r = color yani renk







# isaret degeri  yukaridakşi isaret referanaslarından herhangibiri olabilir







#satir degeri asagıdakilerden herhangibiri olabilir






# Line Referance --> Cizgi referansı




"""

"""

Line Referance --> Cizgi Referance
----------------------------------



Line Syntax     Description            Cizgi Dizimi -- Anlami
'-'             Solid line
':'             Dotted line
'--'            Dashed line
'-.'            Dashed/dotted line





Not: fmt parametresinde satır veya cizgi stili degerini dışarıda bırakırsanız hiçbir satir çizilmez.
---------------------------------------------------------------------------------------------------


"""




# Renk Degeri Asagidakilerden herhangi biri olabilir

# Color Referance --> Renk Referansı


"""

"""

Color Referance --> Renk Referansı




Color Syntax      Description
------------      -----------

'r'               Red
'g'               Green
'b'               Blue
'c'               Cyan
'm'               Magenta
'y'               Yellow
'k'               Black
'w'               White




o:r

o:g   örnek




"""

"""


# Marker Size --> Isaret boyutu


Isaretleyicilerin boyutuna ayarlamak için anahtar kelime bagimsiz degiskenini markersize veya daha kise
surumu olan ms kullanabilirsiniz



"""


# Ornek Isaretcilerin boyutunu 20 ye ayarlayalım


import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker='o', ms=20 ,  mfc="r")
plt.show()



# Hem marker edge color --> isaret kenar rengi  ve hemde marker face color --> isaret yüz rengi kullanalim

# Ornek hem kenar rengini hemde yüz rengini kirmizi boyayalim




import matplotlib.pyplot as plt
import  numpy as np


ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker='o', ms=20, mac='r', mfc='r')
plt.show()



# Ondalik renk degerlerinide kullanabilriiz


import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker='o', ms=20, mec="#4CAF50", mfc="#4CAF50")
plt.show()




plt.plot(ypoints, marker='o', ms=20, mec='hotpink', mfc='hotpink')
plt.show()











