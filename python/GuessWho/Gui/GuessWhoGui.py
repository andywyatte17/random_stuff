#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

This is a Tetris game clone.

author: Jan Bodnar
website: zetcode.com 
last edited: October 2013
"""

import sys, random
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QRect

people_im = ('Alex','Anita','Peter','Eric','Charles','Sam','Joe', \
             'Maria','Philip','Susan','Max','Alfred','Robert','Frans', \
             'Claire','Paul','Bill','David','Bernard','George','Tom', \
             'Herman','Anne' )

def makeImage(path):
    path = QtCore.QString(path)
    qi = QtGui.QImage()
    qi.load( path )
    return qi

images = None
FADED = True
NOT_FADED = False

def makeImages():
    images = list()
    for i in range(0,24):
        filename = 'GuessWho_{:03d}.jpg'.format(i)
        images.append( (filename,
                        people_im,
                        makeImage('tiles/' + filename) ) )
    return images

class GuessWho(QtGui.QMainWindow):
    def __init__(self):
        super(GuessWho, self).__init__()
        self.initUI()

    def initUI(self):    
        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)
        self.resize(500, 500)
        self.center()
        self.setWindowTitle('Guess Who')
        self.show()

    def center(self):        
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, 
            (screen.height()-size.height())/2)

###

class Board(QtGui.QFrame):
    W = 6
    H = 5
    def __init__(self, parent):
        super(Board, self).__init__(parent)
        self.initBoard()
        
    def initBoard(self):     
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.sprites = None

    def initSprites(self):
        global images
        if not self.sprites:
            self.sprites = dict()
        rect0 = self.contentsRect()
        rect = rect0
        rect.adjust(2,2,-1,-1)
        sW = rect.width()/Board.W
        sH = rect.height()/Board.H
        mW = 2
        mH = 2
        n = 0
        for y in range(1,Board.H):
            for x in range(0,Board.W):
                x0 = rect.left() + (0.5+x) * sW
                y0 = rect.top() + (0.5+y) * sH
                r = QRect(x0-sW/2+mW, y0-sH/2+mH, sW-mW*2, sH-mH*2)
                xy = (x,y)
                s = None
                if not xy in self.sprites:
                    s = ( r, images[n][2], NOT_FADED )
                else:
                    s = self.sprites[xy]
                    s = ( r, images[n][2], s[2] )
                self.sprites[xy] = s
                n += 1

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        self.initSprites()
        for key in self.sprites.keys():
            s = self.sprites[key]
            r = s[0]
            im = s[1]
            faded = s[2]
            rIm = r.adjusted(3,3,-3,-3)
            painter.drawRect(r)
            if faded!=FADED:
                painter.drawImage(rIm,im)
            else:
                imTmp = im.copy()
                imTmp.invertPixels()
                painter.drawImage(rIm,imTmp)

    def mousePressEvent(self, event):
        self.initSprites()
        for key in self.sprites.keys():
            r = self.sprites[key][0]
            if r.contains(event.pos()):
                s = self.sprites[key]
                self.sprites[key] = (s[0], s[1], NOT_FADED if s[2]==FADED else FADED)
                self.update()
                return

def main():
    global images
    images = makeImages()
    app = QtGui.QApplication([])
    guessWho = GuessWho()    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()