"""Ventana principal del GUI

"""
# librerias PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QRegularExpression, QTimer
from PyQt5.QtWidgets import QLabel, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
import sys

# librerias propias
import mainwindowinterface
import procesado_imagen


class MainWindow(QtWidgets.QMainWindow, mainwindowinterface.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        # super(MainWindow, self).__init__()
        self.setupUi(self)

        # inicializa mostrar las cámaras

        self.__actualizar_imagen = QTimer()
        t_refresco = 1000
        self.__actualizar_imagen.start(t_refresco)
        self.__actualizar_imagen.timeout.connect(self.__imagen_actualizar)
        self.actionSalir.triggered.connect(self.close)  # close the app
        self.actionSobre.triggered.connect(self.about_message)

    def __imagen_actualizar(self):
        whidth = self.label.width()
        height = self.label.height()
        procesado_imagen.image_stack()
        # show the image on the label
        pixmap = QPixmap('salida.jpg').scaled(whidth, height, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)

    def about_message(self):
        link = "https://uvispace.readthedocs.io/en/latest/"
        message = "App for the uvispace project <br> <a href='%s'>Project Web</a>" % link
        about = QMessageBox.about(self, "About...", message)



app = QtWidgets.QApplication(sys.argv)
form = MainWindow()
form.show()
sys.exit(app.exec_())
