import cv2
import numpy as np
import matplotlib.pyplot as plt

from IPython.display import Image

# Imagen
# Vamos a crear nuestra matriz principal
img = 100 * np.ones((10, 10, 3), np.uint8)

# Extraemos los canales
R = img[:, :, 0]
G = img[:, :, 1]
B = img[:, :, 2]

# Modificacion de un canal (Rojo)
#R[:, :] = 200

# Modificacion de la imagen
#img[:, :, 0] = R

# Modificamos un canal (Verde)
R[:, :] = 255
G[:, :] = 255
B[:, :] = 0

print(img)

# Mostramos nuestra imagen
plt.imshow(img)
plt.show()