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
    Image {
      id: img
      width: 150; height: 150
    }
  }
  Grid {
    y: topRect.height + 4
    height: parent.height - topRect.height - 4
    columns: 6
    spacing: 3
    Repeater {
      id: repeater
      model: 24
      Image {
        width: rootRect.width/6 - 3; height: (rootRect.height - topRect.height)/4 - 4
        source: "tiles/Al2.jpg"
        fillMode: Image.PreserveAspectFit
        MouseArea {
          anchors.fill: parent
          onClicked: { parent.opacity = 0.5 }
        }
      }
    }
  }
}