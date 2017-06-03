#!/usr/bin/env python

from PySide import QtCore, QtGui

from tfl_api_query import *

def makeTreeView():
    view = QtGui.QTreeView()
    view.setModel(model)
    view.setWindowTitle("Simple Tree Model")
    view.expandAll()
    return view


def ListDictIter(ld):
    if isinstance(ld, list):
        for x in ld:
            ListDictIter(x)
    elif isinstance(ld, dict):
        pass


def MakeVBoxLayout(views):
    mainLayout = QtGui.QVBoxLayout()
    for v in views:
         mainLayout.addWidget(v)
    return mainLayout


def GrabDictAsHtml():
    #s = grab("""https://api.tfl.gov.uk/Line/piccadilly/stoppoints""")
    #s = grab("""https://api.tfl.gov.uk/line/victoria/arrivals""" + \
    #         """""", cache=False)
    #s = grab("https://api.tfl.gov.uk/Line/victoria/Timetable/940GZZLUEUS/to/940GZZLUSVS" + \
    #         """""", cache=False)
    #s = grab("https://api.tfl.gov.uk/Line/metropolitan/Timetable/940GZZLUMPK/to/940GZZLUAMS" + \
    #         """""", cache=False)
    #s = grab("https://api.tfl.gov.uk/Journey/JourneyResults/940GZZLUMPK/to/940GZZLUAMS" + \
    #         """""", cache=False)
    s = grab("https://api.tfl.gov.uk/StopPoint/940GZZLUEUS/Arrivals?mode=tube&line=northern" + \
             """""", cache=False)
    #s = grab("""https://api.tfl.gov.uk/line/victoria/arrivals?vehicleId=230""" + \
    #         """""", cache=False)
    print("len(s) = {}", len(s))
    s = json.loads(s)
    #for x in s:
    #    if "vehicleId" in x and x['vehicleId']=="226":
    #        d = x
    #        s = { "currentLocation":d["currentLocation"], \
    #              "vehicleId":d["vehicleId"], \
    #              "timeToStation":d["timeToStation"],
    #              "naptanId":d["naptanId"]
    #            }
    #        s = d
    #        break
    s = json.dumps(s, indent=4)
    s = s.replace("\n","<br>")
    s = s.replace("    ", "&nbsp;&nbsp;&nbsp;&nbsp;")
    return s


if __name__ == '__main__':

    import sys
    import json

    app = QtGui.QApplication(sys.argv)

    s = GrabDictAsHtml()
    lineEdit = QtGui.QLineEdit()
    pte = QtGui.QPlainTextEdit()
    btn = QtGui.QPushButton("Refresh")

    def updateText(pte):
        #print(pte)
        pte.clear()
        pte.appendHtml(str(GrabDictAsHtml()))

    btn.clicked.connect( lambda : updateText(pte) ) 
    updateText(pte)
    layout = MakeVBoxLayout([ lineEdit, pte, btn ])
    view = QtGui.QWidget()
    view.setLayout(layout)
    view.resize(600, 600)
    view.show()
    sys.exit(app.exec_())

