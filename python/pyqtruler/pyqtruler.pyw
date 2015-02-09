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
from PySide.QtCore import Qt, QRect
import PySide

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        self.lastX = self.lastY = None
        self.tooltipPos = None
        self.nMouseMove = 0 # 0,1,2,3,4 = move,top,right,bottom,left
        self.setWindowFlags( Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint )
        self.setMouseTracking(True)
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
                qp.drawLine(ox+x, 20, ox+x, h-1)
            else:
                if 0 == (x % 10) :
                    qp.drawLine(ox+x, 30, ox+x, h-1)
                else:
                    qp.drawLine(ox+x, 35, ox+x, h-1)

        for x in range(0, w-8, 50):
            qp.drawText(ox+x, 15, "{}".format(x))

        if self.tooltipPos:
            qp.setPen( QtGui.QColor(255,0,0,160) )
            qp.drawLine(self.tooltipPos[0], 30, self.tooltipPos[0], h-1)
            if self.tooltipPos[0] > self.size().width()/2:
                r = QRect(0, 0, self.tooltipPos[0], 30)
                qp.drawText(r, Qt.AlignBottom | Qt.AlignRight, "{}".format(self.tooltipPos[0]-ox))
            else:
                r = QRect(self.tooltipPos[0], 0, self.size().width(), 30)
                qp.drawText(r, Qt.AlignBottom | Qt.AlignLeft, "{}".format(self.tooltipPos[0]-ox))
   
    def mouseDoubleClickEvent(self, ev):
        self.close()

    def mousePressEvent(self, ev):
        self.tooltipPos = None
        r = self.rect()
        x = ev.pos().x()
        y = ev.pos().y()
        self.nMouseMove = 0
        if y-10 < r.top(): self.nMouseMove = 1
        elif x+10 > r.right(): self.nMouseMove = 2
        elif y+10 > r.bottom(): self.nMouseMove = 3
        elif x-10 < r.left(): self.nMouseMove = 4

    def mouseReleaseEvent(self, ev):
        self.lastX = self.lastY = None

    def mouseMoveEvent(self, ev):
        if ev.buttons()==Qt.NoButton:
            self.tooltipPos = (ev.pos().x(), ev.pos().y())
            self.update(0, 0, self.size().width(), self.size().height())
            return
        self.tooltipPos = None

        if self.lastX and self.lastY:
            if self.nMouseMove==0:
                dx = ev.globalX() - self.lastX
                dy = ev.globalY() - self.lastY
                self.move( self.pos().x() + dx, self.pos().y() + dy )
            else:
                size = self.size()
                dx = ev.globalX() - self.lastX
                dy = ev.globalY() - self.lastY
                px = 0
                py = 0
                if self.nMouseMove==1 or self.nMouseMove==3:
                    nh = max(50, size.height() + dy)
                    if self.nMouseMove==1:
                        nh = max(50, size.height() - dy)
                        py = size.height() - nh
                    self.resize( size.width(), nh )
                else:
                    nw = max(50, size.width() + dx)
                    if self.nMouseMove==4:
                        nw = max(50, size.width() - dx)
                        px = size.width() - nw
                    self.resize( nw, size.height() )
                if px or py: self.move( self.pos().x() + px, self.pos().y() + py )
        self.lastX = ev.globalX()
        self.lastY = ev.globalY()

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()