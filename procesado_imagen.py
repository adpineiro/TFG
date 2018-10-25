# image processing libraries
import numpy as np
import cv2

"""
    Images are treated as arrays in cv2. Therefore, they can be formated with the numpy library.
    Images are stacked using the given path:
    Image1         Image2
    
    Image3         Image4
    
    First, image1 and 2 are stack, then image 3 and 4.
    Finally, the 4 images are joined
"""


def image_stack():
    # carga las cuatro imagenes
    imagen1 = cv2.imread('imagen1.jpg')
    imagen2 = cv2.imread('imagen2.jpg')
    imagen3 = cv2.imread('imagen3.jpg')
    imagen4 = cv2.imread('imagen4.jpg')
    # Stack the matrix using concatenate
    salida12 = np.concatenate((imagen1, imagen2), axis=1)  # apila las matrices 1 y 2
    salida34 = np.concatenate((imagen3, imagen4), axis=1)  # apila las matrices 3 y 4
    salida = np.concatenate((salida12, salida34), axis=0)  # resultante final
    # calculate the best proportion to fit the label

    # resize the image to fit the label
    salida_red = cv2.resize(salida, (640, 468))  # adjust the image to the label size
    cv2.imwrite('salida.jpg', salida_red)  # guarda el array de imagenes como jpg

    # muestra la imagen
    #   cv2.imshow('Imagen', salida_red)
    #  cv2.waitKey(0)
    #  cv2.destroyAllWindows()
