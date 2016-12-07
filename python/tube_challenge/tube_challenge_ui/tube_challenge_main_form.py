from PySide import QtCore, QtGui, QtSvg, QtUiTools
from PySide.QtCore import QSettings
from pprint import pprint
import sys, os
from uiloader import *

def FitRectInsideRect(xywh, xywh_inside):
    s = float(xywh_inside[3]) / xywh[3]
    s = min(s, float(xywh_inside[2]) / xywh[2])
    result = (xywh_inside[0] + xywh_inside[2]*0.5, xywh_inside[1] + xywh_inside[3]*0.5,
              xywh[2] * s, xywh[3] * s)
    result = (result[0]-result[2]/2, result[1]-result[3]/2, result[2], result[3])
    return result


class StationLineEdit(QtGui.QLineEdit):
    def __init__(self, parent):
        super(StationLineEdit, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.stationCompleter = QtGui.QCompleter()
        self.stationCompleter.setCompletionMode( QtGui.QCompleter.InlineCompletion )
        self.stationCompleter.setCaseSensitivity( QtCore.Qt.CaseInsensitive )
        self.stationCompleterModel = QtGui.QStringListModel()
        self.stationCompleter.setModel(self.stationCompleterModel)
        self.setCompleter(self.stationCompleter)
        self.installEventFilter(self)

    def setCompletionStrings(self, strings):
        self.stationCompleterModel.setStringList(strings)
        #self.stationCompleter.setModel(self.stationCompleterModel)

    def setCompletionAsStations(self):
        import data.data_routes as data_routes
        import data.data_js as data_js
        l = []
        for x in data_js.stations:
            l.append(data_js.stations[x])
        self.stationCompleterModel.setStringList(l)

    def eventFilter(self, obj, event):
        if event.type()==QtCore.QEvent.KeyPress:
            print(event.type(), event.key(), QtCore.Qt.Key_Escape)
            if event.key() == QtCore.Qt.Key_Escape :
                self.setText("")
                return True
        return False


base_items = None


def _completerSetupFunction(editor, index):
    global base_items
    if base_items==None:
        base_items = []
        import data.data_routes as data_routes
        for route in data_routes.routes.keys():
            base_items.append(route)

    print "completer setup: editor=%s, index=%s" % (editor, index)
    completer = QtGui.QCompleter(base_items, editor)
    completer.setCompletionColumn(0)
    completer.setCompletionRole(QtCore.Qt.EditRole)
    completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
    try:
        editor.setCompleter(completer)
    except:
        pass

class CompleterDelegate(QtGui.QStyledItemDelegate):
    def __init__(self, parent=None, completerSetupFunction=None):
        super(CompleterDelegate, self).__init__(parent)
        self._completerSetupFunction = completerSetupFunction
    def createEditor(self, parent, option, index):
        print "createEditor"
        editor = QtGui.QLineEdit(parent)
        self._completerSetupFunction(editor, index)
        return editor
    def setEditorData(self, editor, index):
        print "setEditorData"
        super(CompleterDelegate, self).setEditorData(editor, index)
    def closeEditor(self, editor, hint=None):
        print "closeEditor"
        super(CompleterDelegate, self).closeEditor(editor, hint)
    def commitData(self, editor):
        print "commitData"
        super(CompleterDelegate, self).commitData(editor)


class MainWidget(QtGui.QWidget):
    def __init__(self, parent):
        self.lineEdit = None
        self.lineEdit2 = None
        self.tableView = None
        self.vbox1 = None
        self.tableViewModel = QtGui.QStandardItemModel()
        super(MainWidget, self).__init__(parent)

    def setupTableViewRouteColumn(self):
        delegate = CompleterDelegate(self.tableView, _completerSetupFunction)
        self.tableView.setItemDelegateForColumn(1, delegate)

    def showEvent(self, event):
        super(MainWidget, self).showEvent(event)
        self.lineEdit = self.findChild(StationLineEdit, "lineEdit")
        self.lineEdit.setMinimumWidth(150)
        self.lineEdit.returnPressed.connect( self.stationTextChanged )
        self.lineEdit2 = self.findChild(QtGui.QLineEdit, "lineEdit2")
        self.lineEdit2.setMinimumWidth(150)
        self.tableView = self.findChild(QtGui.QTableView, "tableView")
        self.vbox1 = self.findChild(QtGui.QVBoxLayout, "vbox1")
        self.setupModel()
        self.tableView.setModel( self.tableViewModel )
        self.tableViewModel.itemChanged.connect( self.tvmItemChanged )
        self.lineEdit.setCompletionAsStations()
        self.setupTableViewRouteColumn()

    def setupModel(self):
        m = self.tableViewModel

    def tvmItemChanged(self):
        print("Yeah!")

    @QtCore.Slot()
    def stationTextChanged(self):
        a,b,c = QtGui.QStandardItem(self.lineEdit.text()), QtGui.QStandardItem("?"), QtGui.QStandardItem("?")
        c.setEditable(False)
        oldIx = -1
        newIx = 0
        selIx = self.tableView.selectedIndexes()
        if selIx != []:
            for x in selIx:
                oldIx = x.row()
        if oldIx==-1:
            self.tableViewModel.appendRow([a,b,c])
            newIx = self.tableViewModel.rowCount() - 1
        else:
            self.tableViewModel.insertRow(oldIx+1, [a,b,c])
            newIx = oldIx + 1
        self.tableView.selectRow(newIx)
        self.tvmItemChanged()

    @QtCore.Slot()
    def openAction(self):
        print("openAction")

    @QtCore.Slot()
    def nextStationAction(self):
        pass


class MyWidget2(QtSvg.QSvgWidget):
    def __init__(self):
        super(MyWidget2, self).__init__()
        self.initUI()

    def __init__(self, parent=None, f=0):
        super(MyWidget2, self).__init__(parent, f)
        self.initUI()

    def initUI(self):
        self.show()
        self.load('../svg/lu2a.svg')

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.fillRect(0, 0, self.width(), self.height(), QtGui.QColor(255,255,255,255))
        rs =  self.renderer().defaultSize()
        svgW, svgH = rs.width(), rs.height()
        x,y,w,h = FitRectInsideRect( (0,0,svgW, svgH), (0,0,self.width(), self.height()))
        self.renderer().render(qp, QtCore.QRectF(x, y, w, h) )
        qp.end()
        #super(MyWidget2, self).paintEvent(event)


def _readAndApplyWindowAttributeSettings(mainWindow):
    '''
    Read window attributes from settings,
    using current attributes as defaults (if settings not exist.)

    Called at QMainWindow initialization, before show().
    '''
    qsettings = QSettings("settings.ini", QSettings.IniFormat)

    qsettings.beginGroup("mainWindow")

    # No need for toPoint, etc. : PySide converts types
    mainWindow.restoreGeometry(qsettings.value("geometry", mainWindow.saveGeometry()))
    mainWindow.restoreState(qsettings.value("saveState", mainWindow.saveState()))
    mainWindow.move(qsettings.value("pos", mainWindow.pos()))
    mainWindow.resize(qsettings.value("size", mainWindow.size()))

    qsettings.endGroup()


def _writeWindowAttributeSettings(mainWindow):
    '''
    Save window attributes as settings.

    Called when window moved, resized, or closed.
    '''
    qsettings = QSettings("settings.ini", QSettings.IniFormat)

    qsettings.beginGroup("mainWindow")
    qsettings.setValue("geometry", mainWindow.saveGeometry())
    qsettings.setValue("saveState", mainWindow.saveState())
    qsettings.setValue("pos", mainWindow.pos())
    qsettings.setValue("size", mainWindow.size())

    qsettings.endGroup()


class MyMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

    def closeEvent(self, event):
        _writeWindowAttributeSettings(self)
        pass


if __name__ == "__main__":
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = MyMainWindow()
    loadUi("tube_challenge_main_form.ui", MainWindow,
           {"MainWidget":MainWidget, "MyWidget2":MyWidget2, "StationLineEdit":StationLineEdit})
    MainWindow.show()
    _readAndApplyWindowAttributeSettings(MainWindow)
    sys.exit(app.exec_())

