#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PeopleGraphicsView import *


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        hbox=QHBoxLayout()
        leftpanel=QFrame()
        leftpanel.setGeometry(0,0,300,400)
        view=MyGraphicsView( lambda x: "../../tiles/{}.jpg".format(x), leftpanel)
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
    main()
