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
    # carga las cuatro imagenes
    imagen1 = cv2.imread('imagen1.jpg')
    imagen2 = cv2.imread('imagen2.jpg')
    imagen3 = cv2.imread('imagen3.jpg')
    imagen4 = cv2.imread('imagen4.jpg')
    # Apila las imagenes, se usa concatenate en vez de hstack y vstack al ser preferidas en la documantecion de la librería
    salida12 = np.concatenate((imagen1, imagen2), axis=1)  # apila las matrices 1 y 2
    salida34 = np.concatenate((imagen3, imagen4), axis=1)  # apila las matrices 3 y 4
    salida = np.concatenate((salida12, salida34), axis=0)  # resultante final

    salida_red = cv2.resize(salida, (619, 459))  # ajusta al tamaño del label
    cv2.imwrite('salida.jpg', salida_red)  # guarda el array de imagenes como jpg
    # muestra la imagen
    #   cv2.imshow('Imagen', salida_red)
    #  cv2.waitKey(0)
    #  cv2.destroyAllWindows()
