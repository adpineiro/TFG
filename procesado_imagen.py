# librerias tratamiento imagen

import numpy as np
import glob
import os
import cv2


# carga las dos imagenes
imagen1 = cv2.imread('image1.jpg',1)
imagen2 = cv2.imread('image2.jpg')

# obtiene medidas de las imagenes
alto1, ancho1 = imagen1.shape[:2]
alto2, ancho2 = imagen2.shape[:2]
#altoout = alto1 + alto2
anchoout = ancho1 + ancho2

# crea una imagen vacia
#salida = np.zeros((anchoout, alto1,3), np.uint8)

# una imagen al lado de la otra
#salida[0:alto1, 0:ancho1] = imagen1
#salida[0:alto1, ancho1:anchoout] = imagen2
#cv2.imwrite('salida.jpg', salida)


#las imagenes son tratadas como matrices en cv2
salida = np.vstack((imagen2,imagen1)) #concatena las dos matrices

# muestra las imagenes
cv2.imshow('Imagen', imagen1)
cv2.waitKey(2000)
cv2.destroyAllWindows()
cv2.imshow('Imagen', imagen2)
cv2.waitKey(2000)
cv2.destroyAllWindows()

#muestra la imagen junta
cv2.imshow('Imagen', salida)
cv2.waitKey(2000)
cv2.destroyAllWindows()
