#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PySide tutorial 

This example shows an icon
in the titlebar of the window.

author: Jan Bodnar
website: zetcode.com 
last edited: August 2011
"""

import sys
from PySide import QtGui
import PySide

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        self.lastX = self.lastY = None
        self.isMouseMove = True
        self.setWindowFlags( PySide.QtCore.Qt.FramelessWindowHint )
        self.initUI()
        
    def initUI(self):
        
        self.setGeometry(300, 300, 250, 50)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('web.png'))        
    
        self.show()
        
    def paintEvent(self, e):
      
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()
        
    def drawWidget(self, qp):
        
        font = QtGui.QFont('Serif', 7, QtGui.QFont.Light)
        qp.setFont(font)

        size = self.size()
        w = size.width()
        h = size.height()
        ox = 4
        for x in range(0, w-8, 5):
            if 0 == (x % 50) :
                qp.drawLine(ox+x, 20, ox+x, h-5)
            else:
                if 0 == (x % 10) :
                    qp.drawLine(ox+x, 30, ox+x, h-5)
                else:
                    qp.drawLine(ox+x, 35, ox+x, h-5)

        for x in range(0, w-8, 50):
            qp.drawText(ox+x, 15, "{}".format(x))
   
    def mouseDoubleClickEvent(self, ev):
        self.close()

    def mousePressEvent(self, ev):
        r = self.rect()
        x = ev.pos().x()
        y = ev.pos().y()
        self.isMouseMove = not (x+10 > r.right() and y+10 > r.bottom())

    def mouseReleaseEvent(self, ev):
        self.lastX = self.lastY = None

    def mouseMoveEvent(self, ev):
        print "mouseMoveEvent", ev
        if self.lastX and self.lastY:
            if self.isMouseMove:
                dx = ev.globalX() - self.lastX
                dy = ev.globalY() - self.lastY
                self.move( self.pos().x() + dx, self.pos().y() + dy )
            else:
                size = self.size()
                dx = ev.globalX() - self.lastX
                dy = ev.globalY() - self.lastY
                self.resize( dx + size.width(), size.height() )
        self.lastX = ev.globalX()
        self.lastY = ev.globalY()

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()