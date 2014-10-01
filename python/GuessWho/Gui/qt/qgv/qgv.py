#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, traceback, pprint
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import PeopleGraphicsView


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
    
    def selectionDidChange(self, view):
        print "selectionDidChange in ", view
        print view.getSelectedPeople()
        
    def initUI(self):
        hbox=QHBoxLayout()
        leftpanel=QFrame()
        leftpanel.setGeometry(0,0,300,400)
        view=PeopleGraphicsView.GraphicsView( lambda x: "../../tiles/{}.jpg".format(x), leftpanel)
        view.setPeople( 6, 90, 120, ("Alex", "Robert", "Max")*7 )
        view.setSelectionDidChange( self.selectionDidChange )
        pen=QPen(Qt.black,2)
        hbox.addWidget(leftpanel)
        rightpanel=QFrame()
        hbox.addWidget(rightpanel)
        szoveg=QLabel(rightpanel)
        szoveg.setText(u"Hello World!")
        self.setLayout(hbox)
        self.resize(500,500)
        self.setWindowTitle('blabla')
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    os.chdir( os.path.dirname(sys.argv[0]) )
    try:
        main()
    except:
        traceback.print_exc()
        print "Press <enter> to exit..."
        raw_input()
