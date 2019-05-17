import FileBrowser
import sys
from PyQt5.QtWidgets import QWidget, QDialog, QApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic, QtCore, QtGui

class MainWindow(QDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.ui = uic.loadUi("Prototype.ui", self)
        self.buttons = [self.ui.Browser1, self.ui.Browser2, self.ui.Browser3, self.ui.Browser4]
        self.sound = ['', '', '', ''];
        self.ui.show()

    @pyqtSlot()
    def OpenFileBrowser(self):
        index = 0
        for b in self.buttons:
            print(b.isFlat())
            if b.isFlat():
                index = self.buttons.index(b)
                print(index)
                fileBrowser = FileBrowser.FileDialog()
                path = fileBrowser.openFileNameDialog()

                self.sound[index] = path
                break

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
