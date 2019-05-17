#import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
#from PyQt5.QtGui import QIcon

class FileDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'File Browser'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        #self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #self.openFileNameDialog()
        #self.openFileNamesDialog()
        #self.saveFileDialog()
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py);;Mp3 Files (*.mp3)", options=options)
        if fileName:
            print(fileName)
            return fileName

    #def openFileNamesDialog(self):
    #    options = QFileDialog.Options()
    #    options |= QFileDialog.DontUseNativeDialog
    #    files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
    #    if files:
    #        print(files)
    #
    #def saveFileDialog(self):
    #    options = QFileDialog.Options()
    #    options |= QFileDialog.DontUseNativeDialog
    #    fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
    #    if fileName:
    #        print(fileName)

#if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    ex = FileDialog()
#    path = ex.openFileNameDialog()
#
#    sys.exit(app.exec_())