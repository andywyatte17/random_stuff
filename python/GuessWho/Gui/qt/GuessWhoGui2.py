from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys, os

CB_STYLE = R"""
QCheckBox::indicator { width: 3px; height: 3px; }
QCheckBox::checked { background-color: #e0e0a0 }
"""

people_im = ('Alex','Anita','Peter','Eric','Charles','Sam',
             'Joe','Maria','Philip','Susan','Max','Alfred',
             'Robert','Frans','Claire','Paul','Bill','David',
             'Bernard','George','Tom','Herman','Anne','Richard' )

class cb_press():
    def __call__(self):
        self.cb.opacity = 0.5

class MyQMainWindow(QMainWindow):
    def keyPressEvent(self, keyEvent):
        if keyEvent.key()==Qt.Key_F5:
            # Launch the app again and close this one
            os.system(R'explorer "{}"'.format(sys.argv[0]))
            self.close()

def main():    
    imMap = dict()
    app = QApplication(sys.argv)
    window = MyQMainWindow()
    palette = QPalette()
    gridLayout = QGridLayout()
    centralWidget = QWidget()
    
    lv = QListView()
    model = QStandardItemModel(lv)
    for attribute in ( ('Blue Eyes', 'Red Eyes') ):
        item = QStandardItem(attribute)
        item.setCheckable(True)
        model.appendRow(item)
    lv.setWindowTitle('Example List')
    lv.setMinimumSize(200,200)
    lv.setModel(model)
    gridLayout.addWidget(lv,0,0)

    btn = QPushButton("")
    btn.setIcon( QIcon("tiles/{}.jpg".format("Alex")) )
    btn.setIconSize( QSize(100,100) )
    gridLayout.addWidget(btn,0,2)
    x = 0
    y = 1
    for i in people_im:
        cb = QCheckBox(i)
        cb.setStyleSheet(CB_STYLE)
        imMap[i] = cb
        imMap[i].setIcon( QIcon("../tiles/{}.jpg".format(i)) )
        imMap[i].setIconSize( QSize(100,100) )
        tmp = cb_press()
        tmp.cb = cb
        imMap[i].pressed.connect( tmp )
        gridLayout.addWidget(cb,y,x)
        x += 1
        if x==6:
            x = 0; y += 1
    
    window.setCentralWidget(centralWidget)
    centralWidget.setLayout(gridLayout)

    window.resize(200,200)
    window.setWindowTitle('PyQt QGridLayout Add Item Example')
    window.show()

    app.exec_()

if __name__ == '__main__':
    os.chdir( os.path.dirname(sys.argv[0]) )
    main()