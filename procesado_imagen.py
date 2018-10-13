# librerias tratamiento imagen

import numpy as np
import cv2

"""Las imagenes son tratadas como matrices en cv2. Por lo tanto, pueden ser tratadas con la librería numpy
Se apilan las matrices siguiendo el siguiente orden
    Imagen1   Imagen2

    Imagen3   Imagen4

    Se apila la imagen 1 y 2 por separado y despues 3 y 4, tambien por separado.
    A continuacion, se apila la matriz 1-2 con la 3-4
 """

def image_stack():
# carga las dos imagenes
    imagen1 = cv2.imread('image1.jpg')
    imagen2 = cv2.imread('image2.jpg')
    imagen3 = cv2.imread('image3.jpg')
    imagen4 = cv2.imread('image4.jpg')
#Apila las imagenes
    salida12 = np.hstack((imagen1, imagen2))  # apila las matrices 1 y 2 /TODO Cambiar de hstack a stack, usando axis= 0 o 1
    salida34 = np.hstack((imagen3, imagen4))  # apila las matrices 3 y 4
    salida = np.vstack((salida12, salida34))  # resultante final
    cv2.imwrite('salida.jpg', salida)
# muestra la imagen junta
#    cv2.imshow('Imagen', salida)
#    cv2.waitKey(2000)
#    cv2.destroyAllWindows()
