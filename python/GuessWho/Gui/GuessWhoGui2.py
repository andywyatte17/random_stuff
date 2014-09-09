from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

people_im = ('Alex','Anita','Peter','Eric','Charles','Sam',
             'Joe','Maria','Philip','Susan','Max','Alfred',
             'Robert','Frans','Claire','Paul','Bill','David',
             'Bernard','George','Tom','Herman','Anne','Richard' )

def pressed(ev):
    print "pressed", ev
    ev.opacity = 0.5

def main():
 
    imMap         = dict()  
    app 	  = QApplication(sys.argv)
    window 	  = QMainWindow()
    palette 	  = QPalette()
    gridLayout    = QGridLayout()
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
        btn = QCheckBox(i)
        imMap[i] = btn
        imMap[i].setIcon( QIcon("tiles/{}.jpg".format(i)) )
        imMap[i].setIconSize( QSize(100,100) )
        imMap[i].pressed.connect( lambda: pressed(imMap[i]) )
        gridLayout.addWidget(imMap[i],y,x)
        x += 1
        if x==6:
            x = 0; y += 1
    
    window.setCentralWidget(centralWidget)
    centralWidget.setLayout(gridLayout)

    window.resize(200,200)
    window.setWindowTitle('PyQt QGridLayout Add Item Example')
    window.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()