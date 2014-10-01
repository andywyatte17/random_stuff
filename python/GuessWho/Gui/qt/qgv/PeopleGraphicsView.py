from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Animator:
    def __init__(self, graphicsView, item):
        self.graphicsView = graphicsView
        self.item = item
        
    def setTimer(self):
        self.timer = QTimeLine(500)
        self.timer.finished.connect( self.timerFinish )
        self.timer.setFrameRange(0, 200)
        if self.item.isSelected:
            self.timer.frameChanged.connect( self.fadeOut )
        else:
            self.timer.frameChanged.connect( self.fadeIn )
        self.item.isSelected = not self.item.isSelected
        self.timer.start();

    def fadeOut(self, n):
        self.item.pos = n
        self.item.isSelected = False
        self.graphicsView.scene().invalidate( self.item.boundingRect() )

    def fadeIn(self, n):
        self.item.pos = 200 - n
        self.item.isSelected = True
        self.graphicsView.scene().invalidate( self.item.boundingRect() )

    def timerFinish(self):
        self.graphicsView.removeAnimator(self)


class ImageItem(QGraphicsItem):
    def __init__(self, name, imagePath, x=0, y=0, w=75, h=90):
        super(ImageItem, self).__init__()
        self.imagePath = imagePath
        self.image = None
        self.name = name
        self.pos = 0
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.isSelected = True

    def getWH(self):
        return (self.w, self.h)

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
        painter.drawText( QRectF(x0, y0, W, H), Qt.AlignBottom | Qt.AlignHCenter, self.name )


class GraphicsView(QGraphicsView):
    def setSelectionDidChange(self, fn):
        '''Call this to set a method that is called when a person is clicked, 
           and so the selected person list is changed.'''
        self.selectionDidChange = fn
        
    def __init__(self, imagePathForName, parent):
        super(GraphicsView, self).__init__(parent)
        self.imagePathForName = imagePathForName
        self.timerIsActive = set()
        self.initUI()
        self.animators = dict()
        self.sceneItems = list()
        self.selectionDidChange = None
        
    def initUI(self):
        scene=QGraphicsScene()
        self.shouldScaleDown = True
        self.item = None
        self.timer = None
        #self.setSceneRect(0, 0, 300, 400)
        self.setScene(scene)
        
    def setPeople(self, maxAcross, w, h, people):
        scene = self.scene()
        x = 0
        y = 0
        for person in people:
            pixMapItem = ImageItem( person, self.imagePathForName(person), \
                                    x=x, y=y, w=w, h=h ) 
            scene.addItem( pixMapItem )
            self.sceneItems.append( pixMapItem )
            x += 1
            if x==maxAcross:
                x = 0
                y += 1
    
    def getSelectedPeople(self):
        rv = set()
        for item in self.sceneItems:
            if item.isSelected:
                rv.add( item.name )
        return rv

    def mousePressEvent(self, event):
        item = self.itemAt(event.pos())
        if not item:
            return
        if item in self.timerIsActive:
            return
        self.timerIsActive.add( item )
        animator = Animator(self, item)
        self.animators[item] = animator
        animator.setTimer()
        if self.selectionDidChange:
            self.selectionDidChange(self)
    
    def removeAnimator(self, animator):
        item = animator.item
        if item in self.animators: del self.animators[item]
        if item in self.timerIsActive : self.timerIsActive.remove(item)
