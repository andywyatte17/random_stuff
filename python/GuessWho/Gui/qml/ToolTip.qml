import QtQuick 1.0

Rectangle {
  anchors.fill: parent
  id: tooltip
  property string text
  color: "#20ffffff"
  Text {
    text: tooltip.text
    font.pixelSize: 24
    anchors.fill: parent
  }
  opacity: 0.01
  MouseArea {
    anchors.fill: parent
    id: mouseArea
    hoverEnabled: true
    acceptedButtons: Qt.RightButton
    onEntered: { parent.opacity = 0.8; /*console.log("entered")*/ }
    onExited: { parent.opacity = 0.01; /*console.log("exited")*/ }
  }
 }