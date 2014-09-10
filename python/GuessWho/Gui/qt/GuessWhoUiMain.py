import sys
import copy
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from GuessWhoUi import Ui_MainWindow

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

people_im = ('Alex','Anita','Peter','Eric','Charles','Sam',
             'Joe','Maria','Philip','Susan','Max','Alfred',
             'Robert','Frans','Claire','Paul','Bill','David',
             'Bernard','George','Tom','Herman','Anne','Richard' )

class presser:
    def __call__(self):
        print self.file, self.btn
        
        pm = QPixmap(self.file)
        pm.fill()
        self.btn.setIcon(QIcon(pm))

for x in range(1,25):
    cb_str = "cb_{:02d}".format(x)
    btn = getattr(ui, cb_str)
    btn.setIconSize( QSize(64,64) )
    file = "tiles/{}.jpg".format(people_im[x-1])
    icon = QIcon(file)
    btn.setIcon( icon )
    pr = presser()
    pr.file = copy.deepcopy(file)
    pr.btn = btn
    btn.pressed.connect( pr )

window.show()
sys.exit(app.exec_())