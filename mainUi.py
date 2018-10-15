"""Ventana principal del GUI

"""
# librerias PyQt5
from PyQt5 import QtWidgets, QtCore,QtGui
from PyQt5.QtCore import QRegularExpression, QTimer
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QIcon, QPixmap
import sys

# librerias propias
import mainwindowinterface
import procesado_imagen

class MainWindow(QtWidgets.QMainWindow, mainwindowinterface.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        #super(MainWindow, self).__init__()
        self.setupUi(self)

        # inicializa mostrar las cámaras

        self.__actualizar_imagen = QTimer()
        t_refresco = 1000
        self.__actualizar_imagen.start(t_refresco)
        self.__actualizar_imagen.timeout.connect(self.__imagen_actualizar)

    def __imagen_actualizar(self):
        imagen = procesado_imagen.image_stack()
        pixmap = QPixmap('salida.jpg') #muestra una imagen en la label
        self.label_image1.setPixmap(pixmap)


app = QtWidgets.QApplication(sys.argv)
form = MainWindow()
form.show()
sys.exit(app.exec_())
