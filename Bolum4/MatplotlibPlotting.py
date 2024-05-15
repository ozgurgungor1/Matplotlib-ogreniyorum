# Matplotlib Plotting --> Matplotlib Cizimi


# Matplotlib Cizimi

"""


Matplotlib Cizimi


x ve y noktalarının çizilmesi plot() işlevi, bir diyagramda noktalar markers (işaretler) çizmek için kullanılır.


Varsayılan olarak, plot() işlevi noktadan noktaya bir çizgi çizer


function(işlev) diyagramdaki noktaları belirtmek için parametreler alır


parametre  1, x eksenindeki noktaları içeren bir dizidir.

x = np.array([0, 6])
y = np.array([0, 250])


plt.plot(birinci parametre x, ikinci parametre y))



"""



# (1, 3)'den (8, 10)'a bir çizgi çizmemiz gerekirse,
# çizim işlevine [1, 8] ve [3, 10] olmak üzere iki dizi iletmemiz gerekir.




# Ornek x noktasi (1, 8) konumundan y noktasi (3, 10) konumuna bir diyagramda bir çizgi çizin:



import matplotlib.pyplot as plt
import numpy as np











# Sonuc diyagramda inceleyebilirsiniz.

"""
x-ekseni, yatay eksendir

y-ekseni, dikey eksen


"""



# Plotting Without Line --> Cizgisiz satır



xpoints = np.array([1, 8])
ypoints = np.array([3, 10])



plt.plot(xpoints, ypoints, 'o')

plt.show()


# plt.plot(x, y, o)










# Multiple Points --> Coklu Noktalar

# İstediginiz kadar nokta çizebilirsiniz,  sadece her iki eksende de aynı sayıda noktaya sahip olduğunuzdan emin olun.


# Örnek


import matplotlib.pyplot as plt
import numpy as np


xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])


plt.plot(xpoints, ypoints)

plt.show()
















# Default X-Points --> Varsayilan x noktalari


"""

Varsayilan x noktalari 




"""


# Ornek
# x noktaları olmadan  çizim:


import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([3, 8, 1, 10, 5, 7])


plt.plot(ypoints)
plt.show()


# x-noktası [0, 1, 2, 3, 4, 5] Yukaridaki örnekte