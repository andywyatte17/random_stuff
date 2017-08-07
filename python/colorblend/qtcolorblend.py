#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we dispay an image
on the window. 

author: Jan Bodnar
website: zetcode.com 
last edited: September 2011
"""

from __future__ import print_function
import sys
from PyQt4 import QtGui, QtCore
from colorblendalgo import color_blend
import sip
from pprint import pprint
import sys

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        self.qcolor = QtGui.QColor.fromRgb(128, 128, 0)
        self.initUI()
        
    def initUI(self):      

        hbox = QtGui.QHBoxLayout(self)
        pixmap = QtGui.QPixmap("rugby-shirt.png")
        self.original_image = pixmap.toImage()

        lbl = QtGui.QLabel(self)
        lbl.setPixmap(pixmap)
        self.lbl = lbl

        hbox.addWidget(lbl)
        self.setLayout(hbox)
        
        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()        
        
        self.qcd = QtGui.QColorDialog()
        self.qcd.show()
        self.qcd.currentColorChanged.connect(self.colorChanged) 

    def colorChanged(self, qcolor):
        qcolor = qcolor.toRgb()
        self.qcolor = qcolor
        self.updateImage()

    def updateImage(self):
        def chunks(seq):
            n = 4
            for i in range(0, len(seq), n):
                yield tuple( ord(x) for x in seq[i:i + n] )
        def unchunk(seq):
            for s in seq:
                for sn in s: yield sn
        oi = self.original_image.convertToFormat(QtGui.QImage.Format_ARGB32)
        size = oi.size()
        qc = self.qcolor
        for y in range(0, size.height()):
           scan = oi.scanLine(y)
           scan2 = sip.voidptr(address=int(scan), size=4 * size.width())
           # scan2 is a,r,g,b = x[1],x[2],x[3],x[0]
           pix = [(x[2],x[1],x[0],x[3]) for x in chunks(scan2)]
           pix = color_blend(pix, (qc.red(), qc.green(), qc.blue()), None)
           pix = [(x[2],x[1],x[0],x[3]) for x in pix]
           x = 0
           for p in unchunk(pix):
                scan2[x] = chr(p)
                x += 1
        oi = QtGui.QPixmap.fromImage( oi )
        self.lbl.setPixmap(oi)

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main() 
