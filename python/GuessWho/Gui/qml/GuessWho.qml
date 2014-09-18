import QtQuick 1.0

Rectangle {
  ListModel {
    id: peopleModel
    ListElement { name: "Alex"; name2: "Al2"; size: 100; tip: "Hey\nyou\nget outta here!" }
    ListElement { name: "Alfred"; name2: "Al2"; tip: "Hey" }
    ListElement { name: "Anita"; name2: "Al2"; tip: "Hey" }
    ListElement { name: "Anne"; name2: "Al2"; tip: "Hey" }
    ListElement { name: "Bernard"; name2: "Al2"; tip: "Hey" }
    ListElement { name: "Bill"; name2: "Al2"; tip: "Hey" }
    ListElement { name: "Charles"; name2: "Al2"; tip: "Hey" }
    ListElement { name: "Claire"; name2: "Al2"; tip: "Hey" }
    ListElement { name: "David"; name2: "Al2"; tip: "Hey" }
    ListElement { name: "Eric"; name2: "Al2"; tip: "Hey" }
    ListElement { name: "Frans"; name2: "Al2"; tip: "Hey" }
    ListElement { name: "George"; name2: "Al2"; tip: "Hey" }
    ListElement { name: "Herman"; name2: "Al2"; tip: "Hey" }
    ListElement { name: "Joe"; name2: "Al2"; tip: "Hey" }
    ListElement { name: "Maria"; name2: "Al2"; tip: "Hey" }
    ListElement { name: "Max"; name2: "Al2"; tip: "Hey" }
    ListElement { name: "Paul"; name2: "Al2"; tip: "Hey" }
    ListElement { name: "Peter"; name2: "Al2"; tip: "Hey" }
    ListElement { name: "Philip"; name2: "Al2"; tip: "Hey" }
    ListElement { name: "Richard"; name2: "Al2"; tip: "Hey" }
    ListElement { name: "Robert"; name2: "Al2"; tip: "Hey" }
    ListElement { name: "Sam"; name2: "Al2"; tip: "Hey" }
    ListElement { name: "Susan"; name2: "Al2"; tip: "Hey" }
    ListElement { name: "Tom"; name2: "Al2"; tip: "Hey" }
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
    opacity: 1
    anchors.left: parent.left; anchors.top: parent.top; 
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
          width: parent.width
          height: 80
          opacity: 1
          anchors.fill: parent
          property bool on: true
          source: "../tiles/" + name2 + ".jpg"
          fillMode: Image.PreserveAspectFit          
          MouseArea {
            id: mouseArea
            anchors.fill: parent
            onClicked: {
              parent.on = !parent.on
              parent.opacity = 1 - (!parent.on) * 0.75
            }
          }
        }
        Text { y: 85; text:"Hey" }
        ToolTip {
          text: tip
        }
        
      }
    }
  }
}