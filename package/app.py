import sys

from PyQt6.QtWidgets import QApplication

from .mainwindow import MainWindow


class App:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = MainWindow()
        self.window.show()

    def run(self):
        self.app.exec()
