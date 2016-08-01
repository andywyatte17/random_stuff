from PySide import QtCore, QtGui, QtSvg, QtUiTools
from pprint import pprint


class MainWidget(QtGui.QWidget):
    #def __init__(self, parent=None, f=0):
    #    super(MainWidget, self).__init__(parent, f)
    #
    #def __init__(self):
    #    super(MainWidget, self).__init__()
    #
    @QtCore.Slot()
    def openAction(self):
        print("openAction")

    @QtCore.Slot()
    def nextStationAction(self):
        print("nextStationAction")


class MyWidget2(QtSvg.QSvgWidget):
    def __init__(self):
        super(MyWidget2, self).__init__()

    def __init__(self, parent=None, f=0):
        super(MyWidget2, self).__init__(parent, f)
        self.initUI()
        
    def initUI(self):
        self.show()
        self.load('svg/lu2a.svg')

    def paintEvent(self, event):
        super(MyWidget2, self).paintEvent(event)


def loadUiWidget(uifilename, parent=None):
    loader = QtUiTools.QUiLoader()
    loader.registerCustomWidget(MyWidget2)
    loader.registerCustomWidget(MainWidget)
    uifile = QtCore.QFile(uifilename)
    uifile.open(QtCore.QFile.ReadOnly)
    ui = loader.load(uifile, parent)
    uifile.close()
    return ui


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = loadUiWidget("tube_challenge_main_form.ui")
    MainWindow.show()
    sys.exit(app.exec_())

