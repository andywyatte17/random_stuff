import QtQuick 1.0
Rectangle
{
  function updateRectColor(clr) {
    topRect.color = clr
  }

  id: rootRect
  width: 400; height: 400
  Rectangle {
    id: topRect
    width: parent.width
    height: 130
    color: "lightblue"
    TextInput {
      width: 100; height: 100;
      text: "Hey"
    }
  }
  Grid {
    y: topRect.height + 4
    height: parent.height - topRect.height - 4
    columns: 6
    spacing: 3
    Repeater {
      id: repeater
      model: ["Alex","Alfred","Anita","Anne","Bernard","Bill","Charles",
        "Claire","David","Eric","Frans","George","Herman","Joe","Maria",
        "Max","Paul","Peter","Philip","Richard","Robert","Sam","Susan","Tom"]
      Image {
        property bool on: true
        width: rootRect.width/6 - 3; height: (rootRect.height - topRect.height)/4 - 4
          source: "tiles/" + modelData + ".jpg"
          fillMode: Image.PreserveAspectFit
          MouseArea {
            anchors.fill: parent
            onClicked: {
              parent.on = !parent.on
              parent.opacity = 1 - (!parent.on) * 0.75
            }
          }
      }
    }
  }
}