from PyQt4.QtCore import *
from PyQt4.QtGui import *


class MyImage(QGraphicsItem):
    def __init__(self, name, imagePath, x=0, y=0):
        super(MyImage, self).__init__()
        self.imagePath = imagePath
        self.image = None
        self.name = name
        self.pos = 0
        self.x = x
        self.y = y
        self.isSelected = True

    def getWH(self):
        return (75, 90)

    def boundingRect(self):
        W,H = self.getWH()
        return QRectF(self.x*W, self.y*H, W, H)

    def paint(self, painter, option, widget):
        if self.image == None:
            self.image = QImage(self.imagePath)

        TEXTH = 15
        W,H = self.getWH()
        f = self.pos/100.0
        f2 = self.pos/200.0
        x0 = self.x * W
        y0 = self.y * H
        w1 = (W-4.0) / W
        h1 = (H-4.0) / H
        oldTransform = painter.worldTransform()
        painter.setWorldTransform( QTransform(w1, 0, 0, h1 - f*h1, 2 + x0, 2 + y0 + f2 * (H-4.0) - (f2*TEXTH) ) )
        painter.setRenderHint( QPainter.SmoothPixmapTransform, True )
        painter.setOpacity( 1 - (f2/1.5) )
        painter.drawImage( QRectF(0, 0, W, H-TEXTH), self.image )
        painter.setWorldTransform(oldTransform)
        painter.drawText( QRectF(x0, y0, W, H), Qt.AlignBottom | Qt.AlignHCenter, "Alex" )


class MyGraphicsView(QGraphicsView):
    def __init__(self, imagePathForName, parent):
        super(MyGraphicsView, self).__init__(parent)
        self.imagePathForName = imagePathForName
        self.initUI()
        
    def initUI(self):
        scene=QGraphicsScene()
        pixMapItem = MyImage( "Alex", self.imagePathForName("Alex") )
        scene.addItem( pixMapItem )
        pixMapItem2 = MyImage( "Robert", self.imagePathForName("Robert"), x=0, y=1)
        scene.addItem( pixMapItem2 )
        pixMapItem2 = MyImage( "Robert", self.imagePathForName("Robert"), x=1, y=1)
        scene.addItem( pixMapItem2 )
        self.shouldScaleDown = True
        self.item = None
        self.timer = None
        #self.setSceneRect(0, 0, 300, 400)    
        self.setScene(scene)

    def fadeOut(self, n):
        self.item.pos = n
        self.item.isSelected = False
        self.scene().invalidate( self.item.boundingRect() )

    def fadeIn(self, n):
        self.item.pos = 200 - n
        self.item.isSelected = True
        self.scene().invalidate( self.item.boundingRect() )

    def timerFinish(self):
        self.timer = None

    def mousePressEvent(self, event):
        if self.timer:
            return
        self.item = self.itemAt(event.pos())
        if not self.item:
            return
        timer = QTimeLine(500)
        timer.finished.connect( self.timerFinish )
        self.timer = timer
        timer.setFrameRange(0, 200)
        if self.item.isSelected:
            timer.frameChanged.connect( self.fadeOut )
        else:
            timer.frameChanged.connect( self.fadeIn )
        timer.start();
        self.shouldScaleDown = not self.shouldScaleDown
