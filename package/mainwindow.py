from PyQt6.QtWidgets import QMainWindow

from .ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, title: str = "Main Window"):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(title)
