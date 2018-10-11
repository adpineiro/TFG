# librerias tratamiento imagen

import numpy as np
import glob
import os
import cv2


# carga las dos imagenes
imagen1 = cv2.imread('image1.jpg',1)
imagen2 = cv2.imread('image2.jpg')




# muestra las imagenes
cv2.imshow('Imagen', imagen1)
cv2.imshow('Imagen', imagen2)
cv2.waitKey(2000)
cv2.destroyAllWindows()