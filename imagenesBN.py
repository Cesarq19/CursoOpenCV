import numpy as np
import matplotlib.pyplot as plt
import cv2

# Imagen negra
# Creamos nuestra imagen negra
img = np.zeros((10, 10, 1), np.uint8)

# Cambiamos algunos pixeles
img[0, 1] = 30
img[2, 3] = 50
img[4, 5] = 200
img[6, 7] = 140

# Mostramos los valores numericos 
print(img)

# Mostramos nuestra imagen
plt.imshow(img, cmap= 'gray')
plt.show()