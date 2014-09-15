from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys, os
import charactersLib
import random, weakref

CB_STYLE = R"""
QCheckBox::indicator { width: 3px; height: 3px; }
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


class CheckboxClickProxy:
    def __init__(self, checkbox0, checkbox, game_state):
        self.checkbox0 = checkbox0
        self.checkbox = checkbox
        self.game_state = game_state

    def __call__(self):
        self.game_state.checkboxClicked(self.checkbox0, self.checkbox)


class GameState:
    def __init__(self):
        self.checkboxLabelTuples = list()

    def restart(self):
        person = game_data.random()
        self.answersModel.clear()
        self.qmFiltered.invalidate()
        for cb,label in self.checkboxLabelTuples:
            cb.setChecked(False)
            label.setEnabled(True)

    def checkboxClicked(self, checkbox0, checkbox):
        checkbox.setEnabled( not checkbox0.isChecked() )
        self.qmFiltered.invalidate()

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
        self.AND_Attributes = None
        self.clearQuestionsModel()

    def askOR(self,  ev):
        self.askOR_AND(self.AND_Attributes, 'OR')

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
            self.AND_Attributes = attributes[:]
            for x in attributes[1:]:
                strOR = strOR + " OR " + x[0]
                strAND = strAND + " AND " + x[0]
            self.btnOR.setDescription(strOR)
            self.btnAND.setDescription(strAND)


class MySortFilterProxyModel(QSortFilterProxyModel):
    def __init__(self):
        super(MySortFilterProxyModel, self).__init__()
        self.game_state = None
        self.game_data = None
    
    def filterAcceptsRow (self, source_row, source_parent):
        if not self.game_state or not self.game_data: return True
        gs = self.game_state()
        gd = self.game_data()
        qm = gs.questionsModel
        if not gs: return True
        if not gd: return True
        if qm.item(source_row).data()=="name":
            strName = str(qm.item(source_row).text())
            for cb,label in gs.checkboxLabelTuples:
                if label.isEnabled():
                    if strName==label.name:
                        return True
            return False
        if qm.item(source_row).data()=="attribute":
            strAttribute = str(qm.item(source_row).text())
            for cb,label in gs.checkboxLabelTuples:
                if label.isEnabled():
                    if strAttribute in gd.characters[label.name]:
                        return True
            return False
        return True

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

    modelFiltered = MySortFilterProxyModel()
    modelFiltered.setSourceModel(model)
    lv.setModel(modelFiltered)

    return (lv, model, modelFiltered)


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
    
    btnOR = QCommandLinkButton("Is The Person... (OR)")
    btnOR.setMaximumSize( 300,  10000 )
    layout.addWidget( btnOR )
    btnOR.clicked.connect( window.askOR )
    window.btnOR = btnOR
 
    btnAND = QCommandLinkButton("Is The Person... (AND)")
    btnAND.setMaximumSize( 300,  10000 )
    layout.addWidget( btnAND )
    btnAND.clicked.connect( window.askAND )
    window.btnAND = btnAND
    btnAND.setEnabled(False)
    
    return layout


def makeTopRowLayout(game_state):
    hbox = QHBoxLayout()
    questionsView, questionsModel, qmFiltered = makeQuestionsView()
    questionsModel.itemChanged.connect( game_state.questionsListItemChanged )
    game_state.questionsModel = questionsModel
    game_state.qmFiltered = qmFiltered
    qmFiltered.game_state = weakref.ref(game_state)
    qmFiltered.game_data = weakref.ref(game_data)
    hbox.addWidget(questionsView)
    layout_AND_OR = make_AND_OR_VBoxLayout(game_state)
    hbox.addLayout( layout_AND_OR )
    answersView, answersModel = makeAnswersView(game_state)
    game_state.answersModel = answersModel
    hbox.addWidget(answersView)

    btnRestart = QCommandLinkButton("Restart")
    btnRestart.clicked.connect( game_state.restart )
    hbox.addWidget( btnRestart )


    return hbox


def makeButtonGridLayout(game_data, game_state):
    buttonGridLayout = QGridLayout()
    x = 0
    y = 0
    for i in game_data.people:
        checkbox = QCheckBox(i)
        label = QLabel("")
        label.name = i
        label.setStyleSheet(CB_STYLE)
        game_state.checkboxLabelTuples.append( (checkbox, label) )
        im = QPixmap("../tiles/{}.jpg".format(i))
        im = im.scaledToHeight(100)
        label.setPixmap( im )
        checkbox.released.connect( CheckboxClickProxy(checkbox, label, game_state) )
        buttonGridLayout.addWidget(checkbox,y+1,x)
        buttonGridLayout.addWidget(label,y,x)
        x += 1
        if x==6:
            x = 0; y += 2
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

    
    #print game_data.characters[ game_state.person ]
    #print game_state.person

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
