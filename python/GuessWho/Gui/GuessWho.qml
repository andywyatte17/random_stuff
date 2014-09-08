import QtQuick 1.0
Rectangle
{
  id: rootRect
  width: 400; height: 400
  Grid {
    columns: 6
    Image {
      width: rootRect.width/6 - 2; height: rootRect.height/4
      source: "tiles/Al2.jpg"
      fillMode: Image.PreserveAspectFit
      MouseArea {
         anchors.fill: parent
         onClicked: { parent.opacity = 0.5 }
      }
    }
    Image {
      width: rootRect.width/6 - 2; height: rootRect.height/4
      source: "tiles/Al2.jpg"
      fillMode: Image.PreserveAspectFit
      MouseArea {
         anchors.fill: parent
         onClicked: { parent.opacity = 0.5 }
      }
    }
  }
}