import QtQuick 1.0

Rectangle {
  ListModel {
    id: peopleModel
    ListElement { name: "Alex"; size: 100; tip: "Hey\nyou\nget outta here!" }
    ListElement { name: "Alfred"; tip: "Hey" }
    ListElement { name: "Anita"; tip: "Hey" }
    ListElement { name: "Anne"; tip: "Hey" }
    ListElement { name: "Bernard"; tip: "Hey" }
    ListElement { name: "Bill"; tip: "Hey" }
    ListElement { name: "Charles"; tip: "Hey" }
    ListElement { name: "Claire"; tip: "Hey" }
    ListElement { name: "David"; tip: "Hey" }
    ListElement { name: "Eric"; tip: "Hey" }
    ListElement { name: "Frans"; tip: "Hey" }
    ListElement { name: "George"; tip: "Hey" }
    ListElement { name: "Herman"; tip: "Hey" }
    ListElement { name: "Joe"; tip: "Hey" }
    ListElement { name: "Maria"; tip: "Hey" }
    ListElement { name: "Max"; tip: "Hey" }
    ListElement { name: "Paul"; tip: "Hey" }
    ListElement { name: "Peter"; tip: "Hey" }
    ListElement { name: "Philip"; tip: "Hey" }
    ListElement { name: "Richard"; tip: "Hey" }
    ListElement { name: "Robert"; tip: "Hey" }
    ListElement { name: "Sam"; tip: "Hey" }
    ListElement { name: "Susan"; tip: "Hey" }
    ListElement { name: "Tom"; tip: "Hey" }
  }
  
  function updateRectColor(clr) { topRect.color = clr }

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
  Flow {
    opacity: 0
         anchors.fill: parent
         anchors.margins: 4
         spacing: 10

         Text { text: "Text"; font.pixelSize: 40 }
         Text { text: "items"; font.pixelSize: 40 }
         Text { text: "flowing"; font.pixelSize: 40 }
         Text { text: "inside"; font.pixelSize: 40 }
         Text { text: "a"; font.pixelSize: 40 }
         Text { text: "Flow"; font.pixelSize: 40 }
         Text { text: "item"; font.pixelSize: 40 }
     }  
  Flow {
    opacity: 1
    anchors.left: parent.left; anchors.top: parent.top+130; 
    anchors.right: parent.right; anchors.bottom: parent.bottom;
    spacing: 3
    Repeater {
      id: repeater
      model: peopleModel
      Rectangle {
        clip: true
        x: 0; y: 0;
        width: 80; // rootRect.width/6 - 3
        height: 100; // (rootRect.height - topRect.height)/4 - 3
        Image {
        opacity: 1
         anchors.fill: parent
          property bool on: true
            source: "../tiles/" + name + ".jpg"
            fillMode: Image.PreserveAspectFit          
            MouseArea {
              anchors.fill: parent
              onClicked: {
                console.log("onClicked")
                parent.on = !parent.on
                parent.opacity = 1 - (!parent.on) * 0.75
              }
            }
          }
                  ToolTip {
          text: tip
        }

        }
    }
  }
}