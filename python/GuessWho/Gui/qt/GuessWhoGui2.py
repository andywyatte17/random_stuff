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

class GameState:
    def keyPressEvent(self, keyEvent):
        if keyEvent.key()==Qt.Key_F5:
            # Launch the app again and close this one
            os.system(R'explorer "{}"'.format(sys.argv[0]))
            self.close()
    def clearQuestionsModel(self):
        for i in range(0, self.questionsModel.rowCount()):
            self.questionsModel.item(i).setCheckState( Qt.Unchecked )
    def answer(self, attributes, strAndOr):
        person = self.person
        attribsOfPerson = self.game_data.characters[person]
        if strAndOr=='OR':
            for attrib in attributes:
                if attrib[1]=='attribute' and str(attrib[0]) in attribsOfPerson:
                    return "yes"
                if attrib[1]=='name' and attrib[0]==person:
                    return "yes"
        if strAndOr=='AND':
            for attrib in attributes:
                if not str(attrib[0]) in attribsOfPerson:
                    return "no"
                if not (attrib[1]=='name' and attrib[0]==person):
                    return "no"
            return "yes"
        return "no"
    def rowFromAttributes(self, attributes, strAndOr):
        questionStr = ''
        for x in attributes:
            if len(questionStr)!=0:
                questionStr += ' {} {}'.format(strAndOr, x[0])
            else:
                questionStr = '{}'.format(x[0])
        items = [QStandardItem("{}".format(self.answersModel.rowCount() + 1)),
                 QStandardItem(questionStr + "?"),  QStandardItem(self.answer(attributes, strAndOr))]
        for item in items:
            item.setSelectable(False)
        return items
    def askOR_AND(self, attributes, strAND_OR):
        if not attributes:
           return
        items = self.rowFromAttributes( attributes, strAND_OR )
        self.answersModel.appendRow( items )
        self.answersView.resizeColumnsToContents()
        self.OR_Attributes = None
        self.AND_Attributes = None
        self.clearQuestionsModel()
    def askOR(self,  ev):
        self.askOR_AND(self.OR_Attributes, 'OR')
    def askAND(self,  ev):
        self.askOR_AND(self.AND_Attributes, 'AND')
    def questionsListItemChanged(self,  qStandardItem):
        model = self.questionsModel
        attributes = []
        for x in range(0,  model.rowCount()):
            item = model.item(x, 0)
            if item.checkState()==Qt.Checked:
                attributes.append( (item.text(),  item.data().toString()) )
        if len(attributes)==0:
            self.btnOR.setDescription('')
            self.btnAND.setDescription('')
        else:
            strOR = attributes[0][0]
            strAND = attributes[0][0]
            self.OR_Attributes = attributes[:]
            self.AND_Attributes = attributes[:]
            for x in attributes[1:]:
                strOR = strOR + " OR " + x[0]
                strAND = strAND + " AND " + x[0]
            self.btnOR.setDescription(strOR)
            self.btnAND.setDescription(strAND)

game_data = GameData()

def makeQuestionsView():
    lv = QListView()
    model = QStandardItemModel(lv)
    for attribute in sorted(game_data.attributes):
        item = QStandardItem(attribute)
        item.setData( QVariant("attribute") )
        item.setCheckable(True)
        model.appendRow(item)
    
    spacer = QStandardItem('')
    spacer.setCheckable(False)
    model.appendRow(spacer)

    for name in game_data.people:
        item = QStandardItem(name)
        item.setData( QVariant("name") )
        item.setCheckable(True)
        model.appendRow(item)
    lv.setWindowTitle('Example List')
    lv.setMinimumSize(200,200)
    lv.setModel(model)
    return (lv,  model)

def makeAnswersView(game_state):
    answersView = QTableView(None)
    answersView.setShowGrid(False)
    answersView.horizontalHeader().setVisible(False)
    answersView.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
    answersView.verticalHeader().setVisible(False)
    answersView.setColumnWidth(0, 200)
    model = QStandardItemModel(None)
    game_state.answersModel = model
    answersView.setModel( model )
    answersView.resizeColumnsToContents()
    game_state.answersView = answersView
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

def makeTopRowLayout(game_state):
    hbox = QHBoxLayout()
    questionsView, questionsModel = makeQuestionsView()
    questionsModel.itemChanged.connect( game_state.questionsListItemChanged )
    game_state.questionsModel = questionsModel
    hbox.addWidget(questionsView)
    layout_AND_OR = make_AND_OR_VBoxLayout(game_state)
    hbox.addLayout( layout_AND_OR )
    answersView, answersModel = makeAnswersView(game_state)
    game_state.answersModel = answersModel
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
    window = QMainWindow()
    game_state = GameState()
    game_state.game_data = game_data
    palette = QPalette()
    centralWidget = QWidget()
    mainLayout = QVBoxLayout()
    game_state.person = game_data.random()

    print game_data.characters[ game_state.person ]
    print game_state.person

    mainLayout.addLayout( makeTopRowLayout(game_state) )

    buttonGridLayout = makeButtonGridLayout(game_data, game_state)
    mainLayout.addLayout( buttonGridLayout )
    
    window.setCentralWidget(centralWidget)
    centralWidget.setLayout(mainLayout)

    window.resize(200,200)
    window.setWindowTitle('PyQt QGridLayout Add Item Example')
    window.show()

    app.exec_()

if __name__ == '__main__':
    dirOfMe = os.path.dirname(sys.argv[0])
    if dirOfMe:
      os.chdir( dirOfMe )
    main()
