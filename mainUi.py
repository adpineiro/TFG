"""Ventana principal del GUI

"""
# librerias PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QRegularExpression, QTimer
from PyQt5.QtWidgets import QLabel, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
# librerias
import sys
import logging
import os

# librerias propias
import mainwindowinterface
import image_procesing
import load_csv

# Create the application logger
logger = logging.getLogger('view')


class AppLogHandler(logging.Handler):
    """
    Customized logging handler class, for printing on a PyQt Widget
    """
    def __init__(self, widget):
        logging.Handler.__init__(self)
        self.widget = widget
        self.setLevel(logging.DEBUG)
        formatter = logging.Formatter(" %(asctime)s.%(msecs)03d %(levelname)8s:" " %(message)s", "%H:%M:%S")
        self.setFormatter(formatter)
        # Log messages colours.
        self.levelcolours = {
            logging.DEBUG: 'black',
            logging.INFO: 'blue',
            logging.WARN: 'orange',
            logging.ERROR: 'red',
        }
        # Paths to the log icons.
        parent_path = os.path.dirname(__file__)
        self.logsymbols = {
            logging.DEBUG: "{}/icons/debug.png".format(parent_path),
            logging.INFO: "{}/icons/info.png".format(parent_path),
            logging.WARN: "{}/icons/warning.png".format(parent_path),
            logging.ERROR: "{}/icons/error.png".format(parent_path),
        }
        # The True levels are the ones that are printed on the log.
        self.enabled = {
            logging.DEBUG: False,
            logging.INFO: True,
            logging.WARN: True,
            logging.ERROR: True,
        }

        def emit(self, record):
            """Override the logging.Handler.emit method.

            The received log message will be printed on the specified
            widget, typically a TextBox.
            """
            # Only print on the log the enabled log levels.
            if not self.enabled[record.levelno]:
                return
            new_log = self.format(record)
            self.widget.insertHtml('<img src={img} height="14" width="14"/>'
                                   '<font color="{colour}">{log_msg}</font><br />'
                                   .format(img=self.logsymbols[record.levelno],
                                           colour=self.levelcolours[record.levelno],
                                           log_msg=new_log))
            self.widget.moveCursor(QtGui.QTextCursor.End)

            return


class MainWindow(QtWidgets.QMainWindow, mainwindowinterface.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        # super(MainWindow, self).__init__()
        self.setupUi(self)
        self.popup = None
        # Configure the logger, assigning an instance of AppLogHandler.
        self.log_handler = AppLogHandler(self.LoggerBrowser)
        logger.addHandler(self.log_handler)
        logger.info("Initialized the Frequency-Meter Application")
        # Log console level selection buttons
        self.DebugCheck.clicked.connect(self.update_logger_level)
        self.InfoCheck.clicked.connect(self.update_logger_level)
        self.WarnCheck.clicked.connect(self.update_logger_level)
        self.ErrorCheck.clicked.connect(self.update_logger_level)
        # initialise the QTimer to update the cameras image
        self.__actualizar_imagen = QTimer()
        t_refresco = 100
        self.__actualizar_imagen.start(t_refresco)
        self.__actualizar_imagen.timeout.connect(self.__imagen_actualizar)
        # menu actions
        self.actionSalir.triggered.connect(self.close)  # close the app
        self.action_about.triggered.connect(self.about_message)
        self.actionOpen_csv.triggered.connect(self.__loadfileswindow)
        #resize window event

    def __loadfileswindow(self):
        # opens a new window to load a .csv file
        logger.debug("Opening file loading window")
        self.popup = load_csv.App()
        self.popup.show()
        return

    def __imagen_actualizar(self):
        """ refresh the image label
            calls the image_stack method to join the four cameras

        """
        height = int(self.label.height())
        width = int(height*1.333)
        image_procesing.image_stack(width, height)
        #gets the size of the label and sends it to
        pixmap = QPixmap('salida.jpg').scaled(self.label.size(),
                                              aspectRatioMode= QtCore.Qt.KeepAspectRatio,
                                              transformMode = QtCore.Qt.SmoothTransformation)

        self.label.setPixmap(pixmap)

        #self.label.resize(width, height)
        self.label.adjustSize()
        self.label.setScaledContents(True)
        logger.info("Imagen actualizada")

    def about_message(self):
        # about message with a link to the main project web
        link = "https://uvispace.readthedocs.io/en/latest/"
        message = "App for the uvispace project <br> <a href='%s'>Project Web</a>" % link
        about = QMessageBox.about(self, "About...", message)

    def update_logger_level(self):
        """Evaluate the check boxes states and update logger level."""
        self.log_handler.enabled[logging.DEBUG] = self.DebugCheck.isChecked()
        self.log_handler.enabled[logging.INFO] = self.InfoCheck.isChecked()
        self.log_handler.enabled[logging.WARN] = self.WarnCheck.isChecked()
        self.log_handler.enabled[logging.ERROR] = self.ErrorCheck.isChecked()
        return


app = QtWidgets.QApplication(sys.argv)
form = MainWindow()
form.show()
sys.exit(app.exec_())
