from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys, os
import charactersLib
import random

CB_STYLE = R"""
QCheckBox::indicator { width: 3px; height: 3px; }
QCheckBox::checked { background-color: #e0e0a0 }
"""

class GameData():
    def __init__(self):
        characters = charactersLib.parse_characters()
        self.characters = characters
        
        people = list()
        for key in characters.keys():
            people.append( key )
        self.people = sorted(people)
        
        attributes = set()
        for key in characters:
            attributes = attributes | characters[key]
        self.attributes = attributes

    def random(self):
        import random
        return self.people[random.randint(0,  len(self.people)-1)]

class cb_press():
    def __call__(self):
        self.cb.opacity = 0.5

class MyQMainWindow(QMainWindow):
    def keyPressEvent(self, keyEvent):
        if keyEvent.key()==Qt.Key_F5:
            # Launch the app again and close this one
            os.system(R'explorer "{}"'.format(sys.argv[0]))
            self.close()
    def askOR(self,  ev):
        print "askOR"
    def askAND(self,  ev):
        print "askAND"

game_data = GameData()

def makeQuestionsView():
    lv = QListView()
    model = QStandardItemModel(lv)
    for attribute in game_data.attributes:
        item = QStandardItem(attribute)
        item.setCheckable(True)
        model.appendRow(item)
    for name in game_data.people:
        item = QStandardItem(name)
        item.setCheckable(True)
        model.appendRow(item)
    lv.setWindowTitle('Example List')
    lv.setMinimumSize(200,200)
    lv.setModel(model)
    return (lv,  model)

def makeAnswersView():
    questionsView = QTableView(None)
    questionsView.setMinimumSize(300, 0)
    questionsView.setColumnWidth(0, 200)
    model = QStandardItemModel(None)
    model.appendRow( [QStandardItem("Is your person Red-Haired OR Blue-Eyed?"),  QStandardItem("yes")] )
    model.appendRow( [QStandardItem("Is your person Bob?"),  QStandardItem("no")]  )
    questionsView.setModel( model )
    return (questionsView,  model)

def make_AND_OR_VBoxLayout(window):
    layout = QVBoxLayout()
    btn = QPushButton("Ask - OR")
    layout.addWidget( btn )
    btn.clicked.connect( window.askOR )
    btn = QPushButton("Ask - AND")
    layout.addWidget( btn )
    btn.clicked.connect( window.askAND )
    return layout

def main():    
    imMap = dict()
    app = QApplication(sys.argv)
    window = MyQMainWindow()
    palette = QPalette()
    gridLayout = QGridLayout()
    centralWidget = QWidget()
    pick = game_data.random()
    print pick

    questionsView, questionsModel = makeQuestionsView()
    window.questionsModel = questionsModel
    gridLayout.addWidget(questionsView,0,0)

    window.AND_OR = make_AND_OR_VBoxLayout(window)
    gridLayout.addLayout( window.AND_OR,  0,  1 )

    answersView, answersModel = makeAnswersView()
    window.answersModel = answersModel
    gridLayout.addWidget(answersView,  0,  2)

    btn = QPushButton("")
    btn.setIcon( QIcon("tiles/{}.jpg".format("Alex")) )
    btn.setIconSize( QSize(100,100) )
    gridLayout.addWidget(btn,0,3)
    x = 0
    y = 1
    for i in game_data.people:
        cb = QCheckBox(i)
        cb.setStyleSheet(CB_STYLE)
        imMap[i] = cb
        imMap[i].setIcon( QIcon("../tiles/{}.jpg".format(i)) )
        imMap[i].setIconSize( QSize(100,100) )
        tmp = cb_press()
        tmp.cb = cb
        imMap[i].pressed.connect( tmp )
        gridLayout.addWidget(cb,y,x)
        x += 1
        if x==6:
            x = 0; y += 1
    
    window.setCentralWidget(centralWidget)
    centralWidget.setLayout(gridLayout)

    window.resize(200,200)
    window.setWindowTitle('PyQt QGridLayout Add Item Example')
    window.show()

    app.exec_()

if __name__ == '__main__':
    os.chdir( os.path.dirname(sys.argv[0]) )
    main()
