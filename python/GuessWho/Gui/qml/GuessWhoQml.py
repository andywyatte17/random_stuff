import sys, glob

from PyQt4.QtCore import QDateTime, QObject, QUrl, pyqtSignal
from PyQt4.QtGui import QApplication, QColor, QImage
from PyQt4.QtDeclarative import QDeclarativeView, QDeclarativeItem

app = QApplication(sys.argv)

# Create the QML user interface.
view = QDeclarativeView()
view.setSource(QUrl('GuessWho.qml'))
view.setResizeMode(QDeclarativeView.SizeRootObjectToView)

rootObject = view.rootObject()

# Display the user interface and allow the user to interact with it.
view.setGeometry(100, 100, 400, 240)
view.show()

app.exec_()