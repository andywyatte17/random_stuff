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

class checkbox_style():
    def __call__(self):
        self.checkbox.opacity = 0.5

class MyQMainWindow(QMainWindow):
    def keyPressEvent(self, keyEvent):
        if keyEvent.key()==Qt.Key_F5:
            # Launch the app again and close this one
            os.system(R'explorer "{}"'.format(sys.argv[0]))
            self.close()
    def clearQuestionsModel(self):
        for i in range(0, self.questionsModel.rowCount()):
            self.questionsModel.item(i).setCheckState( Qt.Unchecked )
    def askOR(self,  ev):
        print "askOR:",  self.OR_Attributes
        self.OR_Attributes = None
        self.clearQuestionsModel()
    def askAND(self,  ev):
        print "askAND:",  self.AND_Attributes
        self.AND_Attributes = None
        self.clearQuestionsModel()
    def questionsListItemChanged(self,  qStandardItem):
        print qStandardItem
        model = self.questionsModel
        attributes = []
        for x in range(0,  model.rowCount()):
            item = model.item(x, 0)
            if item.checkState()==Qt.Checked:
                attributes.append( item.text() )
        if len(attributes)==0:
            self.btnOR.setDescription('')
            self.btnAND.setDescription('')
        else:
            strOR = attributes[0]
            self.OR_Attributes = attributes[:]
            for x in attributes[1:]:
                strOR = strOR + " OR " + x
            self.btnOR.setDescription(strOR)
            self.AND_Attributes = attributes[:]

game_data = GameData()

def makeQuestionsView():
    lv = QListView()
    model = QStandardItemModel(lv)
    for attribute in sorted(game_data.attributes):
        item = QStandardItem(attribute)
        item.setCheckable(True)
        model.appendRow(item)
    
    spacer = QStandardItem('')
    spacer.setCheckable(False)
    model.appendRow(spacer)

    for name in game_data.people:
        item = QStandardItem(name)
        item.setCheckable(True)
        model.appendRow(item)
    lv.setWindowTitle('Example List')
    lv.setMinimumSize(200,200)
    lv.setModel(model)
    return (lv,  model)

def makeAnswersView():
    answersView = QTableView(None)
    answersView.setShowGrid(False)
    answersView.horizontalHeader().setVisible(False)
    answersView.verticalHeader().setVisible(False)
    answersView.setMinimumSize(300, 0)
    answersView.setColumnWidth(0, 200)
    model = QStandardItemModel(None)
    for i in range(1, 20):
        items = [QStandardItem("{}".format(i)),  QStandardItem("Is your person Red-Haired OR Blue-Eyed?"),  QStandardItem("yes")]
        for item in items:
            item.setSelectable(False)
        model.appendRow( items )
    answersView.setModel( model )
    answersView.resizeColumnsToContents()
    return (answersView,  model)

def make_AND_OR_VBoxLayout(window):
    layout = QVBoxLayout()
    
    btnAND = QCommandLinkButton("Is The Person... (AND)")
    btnAND.setMaximumSize( 300,  10000 )
    layout.addWidget( btnAND )
    btnAND.clicked.connect( window.askAND )
    window.btnAND = btnAND
    
    btnOR = QCommandLinkButton("Is The Person... (OR)")
    btnOR.setMaximumSize( 300,  10000 )
    layout.addWidget( btnOR )
    btnOR.clicked.connect( window.askOR )
    window.btnOR = btnOR
    
    return layout

def makeTopRowLayout(window):
    hbox = QHBoxLayout()
    questionsView, questionsModel = makeQuestionsView()
    questionsModel.itemChanged.connect( window.questionsListItemChanged )
    window.questionsModel = questionsModel
    hbox.addWidget(questionsView)
    layout_AND_OR = make_AND_OR_VBoxLayout(window)
    hbox.addLayout( layout_AND_OR )
    answersView, answersModel = makeAnswersView()
    window.answersModel = answersModel
    hbox.addWidget(answersView)
    return hbox

def makeButtonGridLayout(game_data, window):
    buttonGridLayout = QGridLayout()
    x = 0
    y = 0
    for i in game_data.people:
        checkbox = QCheckBox(i)
        checkbox.setStyleSheet(CB_STYLE)
        im = checkbox
        #im.setIcon( QIcon("../tiles/{}.jpg".format(i)) )
        im.setIconSize( QSize(100,100) )
        tmp = checkbox_style()
        tmp.checkbox = checkbox
        checkbox.pressed.connect( tmp )
        buttonGridLayout.addWidget(checkbox,y,x)
        x += 1
        if x==6:
            x = 0; y += 1
    return buttonGridLayout
    
def main():
    app = QApplication(sys.argv)
    window = MyQMainWindow()
    palette = QPalette()
    centralWidget = QWidget()
    mainLayout = QVBoxLayout()
    pick = game_data.random()
    print pick

    mainLayout.addLayout( makeTopRowLayout(window) )

    buttonGridLayout = makeButtonGridLayout(game_data, window)
    mainLayout.addLayout( buttonGridLayout )
    
    window.setCentralWidget(centralWidget)
    centralWidget.setLayout(mainLayout)

    window.resize(200,200)
    window.setWindowTitle('PyQt QGridLayout Add Item Example')
    window.show()

    app.exec_()

if __name__ == '__main__':
    os.chdir( os.path.dirname(sys.argv[0]) )
    main()
