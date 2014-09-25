#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MyImage(QGraphicsItem):
    def __init__(self, x=0, y=0):
        super(MyImage, self).__init__()
        self.pos = 0
        self.image = QImage(R"../../tiles/Max.jpg")
        self.x = x
        self.y = y

    def getWH(self):
        return (75, 90)

    def boundingRect(self):
        W,H = self.getWH()
        return QRectF(self.x*W, self.y*H, W, H)

    def paint(self, painter, option, widget):
        W,H = self.getWH()
        f = self.pos/100.0
        f2 = self.pos/200.0
        w = self.x * W
        h = self.y * H
        w1 = (W-4.0) / W
        h1 = (H-4.0) / H
        print w1, h1
        painter.setWorldTransform( QTransform(w1, 0, 0, h1 - f*h1, 2 + w, 2 + h + f2 * (H-4.0) ) )
        painter.setRenderHint( QPainter.SmoothPixmapTransform, True )
        painter.setOpacity( 1 - (f2/2) )
        painter.drawImage( QRectF(0, 0, W, H), self.image )


class MyGraphicsView(QGraphicsView):
    def __init__(self, a, b):
        super(MyGraphicsView, self).__init__(a, b)
        self.shouldScaleDown = True
        self.item = None
        self.timer = None

    def scaleDown(self, n):
        self.item.pos = n
        self.scene().invalidate()

    def scaleUp(self, n):
        self.item.pos = 200 - n
        self.scene().invalidate()

    def timerFinish(self):
        self.timer = None

    def mousePressEvent(self, event):
        if self.timer:
            return
        self.item = self.itemAt(event.pos())
        if not self.item:
            return
        timer = QtCore.QTimeLine(500)
        timer.finished.connect( self.timerFinish )
        self.timer = timer
        timer.setFrameRange(0, 200)
        if self.shouldScaleDown:
            timer.frameChanged.connect( self.scaleDown )
        else:
            timer.frameChanged.connect( self.scaleUp )
        timer.start();
        self.shouldScaleDown = not self.shouldScaleDown

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        hbox=QtGui.QHBoxLayout()
        leftpanel=QtGui.QFrame()
        leftpanel.setGeometry(0,0,300,400)
        scene=QtGui.QGraphicsScene()
        self.scene = scene  # save reference to scene, or it will be destroyed
        pixMapItem = MyImage()
        self.scene.addItem( pixMapItem )
        pixMapItem2 = MyImage(x=0, y=1)
        self.scene.addItem( pixMapItem2 )
        view=MyGraphicsView(scene,leftpanel)
        view.pixMapItem = pixMapItem
        view.pixMapItem2 = pixMapItem2
        view.setSceneRect(0,0,300,400)
        pen=QtGui.QPen(QtCore.Qt.black,2)
        hbox.addWidget(leftpanel)
        rightpanel=QtGui.QFrame()
        hbox.addWidget(rightpanel)
        szoveg=QtGui.QLabel(rightpanel)
        szoveg.setText(u"Hello World!")
        self.setLayout(hbox)
        self.resize(500,500)
        self.setWindowTitle('blabla')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
