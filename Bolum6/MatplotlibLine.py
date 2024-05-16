# Matplotlib Line --> Matplotlib Çizgi Stilleri

# Line Styles

"""
Çizgi Stilleri

Çizilen çizginin stilini değiştirmek için argüman anahtar sözcüğümüz 'linestyle' veya kısaltılmış adı ile 'ls' olarak kullanabiliriz.
"""

# Örnek: Noktalı bir çizgi kullanalım

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle='dotted')
plt.show()

# Örnek: Kesikli bir çizgi kullanalım

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle='dashed')
plt.show()

# Shorter Syntax --> Daha kısa söz dizimi

"""
Çizgi stili daha kısa bir söz dizimi ile yazılabilir.

linestyle  ls olarak yazılabilir
---------  ---------------
dotted     : olarak yazılabilir
---------  ---------------
dashed     -- olarak yazılabilir
---------  ---------------
"""

# Örnek: Daha kısa söz dizimi

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, ls=':')
plt.show()







# Line Styles --> Çizgi Stilleri


"""
Line Styles --> Çizgi Stilleri
------------------------------

Bu çizgi Stillerinden herhangibirini kullanabiliriz.


Style                   Or
'solid' (default)       '-'
'dotted'                ':'
'dashed'                '--'
'dashdot'               '-.' 
'None'                 ''or''


"""



# Line Color --> Çizgi Rengi


"""

Line Color --> Çizgi Rengi
--------------------------



Çizginin rengini anlamak için anahtar kelime argumani color veya daha kisasi c olarak kullanabiliriz.
------------------------------------------------------*****-----------------**-----------------------


"""



# Ornek Çizgi rengini kırmızıya ayarlayalım


import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color='r')
plt.show()








# Onaltılık renk değerlerini kullanabilriz

# Ornek güzel bir yesil cizgi ile grafik


import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, c='#4CAF50')


plt.show()




# desteklenen 140 renk adından herhangi biri


# Ornek 'hotpink' renk çizgisi ile bir grafik yapalım


import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, c='hotpink')
plt.show()






# Line Width --> Çizgi genisligi


"""
Line Width --> Çizgi genisligi
------------------------------


çizginin genisligini gelistirmek için anahtar kelime argümanı linewidth veya daha kisa hali olan lw olarak kullanabiliriz.
--------------------------------------------------------------*********--------------------------**-----------------------


Deger nokta cinsinden kayan bir sayidir

"""



# Ornek 20.5 punto genişliğinde bir çizgi ile grafik yapalım


import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])  # Değerler liste olarak girilmeli

plt.plot(ypoints, lw=20.5)  # Line width tırnak işareti olmadan kullanılmalı
plt.show()



# Multiple Lines --> Çoklu Listeler

"""
Multiple Lines --> Çoklu Listeler
---------------------------------


Daha fazla plt.plot fonksiyon ekleyerek istedğimiz kadar çizgi ekleyebiliriz


"""



# Ornek plt.plot() Her çizgi için bir fonksiyon plt.plot() belirterek iki çizgi çizelim



import matplotlib.pyplot as plt
import numpy as np



y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])



plt.plot(y1)
plt.plot(y2)

plt.show()









"""

Ayni plt.plot() fonksiyonu her çizgi için x ve y ekseni noktalarini ekleyerek birçok çizgi çizebilirsiniz.




x ve y degerleri ciftler halinde geliyor


y = 1 2 3 4 5 6 7 8
x = 8 4 5 6 7 3 1 6   birbiri kadar olmak zorunda degerler



"""


# Ornek Her iki cizgi içinde x ve y noktası degerleri belirterek çizgi çizelim


import matplotlib.pyplot as plt
import numpy as np



x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.show()






