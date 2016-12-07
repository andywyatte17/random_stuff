import sys
from PyQt4.QtCore import Qt, QVariant, QModelIndex
from PyQt4.QtGui import QApplication, QCompleter, QLineEdit, QStringListModel, QColor, QBrush


class MyListModel(QStringListModel):
    def __init__(self, parent = None):
        super(MyListModel, self).__init__(parent)
        self.colors = {}

    def data(self, index, role):
        if role == Qt.ForegroundRole:
            return self.colors[index.row()]
        return super(MyListModel, self).data(index, role);


def make_model():
    model = MyListModel()
    #model = QStringListModel()
    model.setStringList(["paddington", "bakerloo"])
    model.colors[0] = QBrush(Qt.red)
    model.colors[1] = QBrush(Qt.blue)
    return model

if __name__ == "__main__":

    app = QApplication(sys.argv)
    edit = QLineEdit()
    completer = QCompleter()
    completer.setCompletionMode(QCompleter.PopupCompletion)
    #completer.setCompletionMode(QCompleter.InlineCompletion)
    #completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
    edit.setCompleter(completer)

    model = make_model()
    completer.setModel(model)

    edit.show()
    sys.exit(app.exec_())
