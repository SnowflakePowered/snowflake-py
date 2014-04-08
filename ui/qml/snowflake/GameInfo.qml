import QtQuick 2.0
Rectangle{
   id: gameInfoWrapper
   color: "lightsteelblue"

   property string textGameTitle
   property string textGameDescrption
   property string textGameShortInfo

   BackgroundedText{
       id: gameTitle
       anchors.top: parent.top
       anchors.left: parent.left
       anchors.leftMargin: 15
       anchors.topMargin: 15
       backgroundColor: "#80000000"
       textValue: textGameTitle
       textColor: "#ffffff"
       family: "Roboto"
       fontWeight: Font.Light
       fontPointSize: 21
   }
   BackgroundedText{
       id: gameDescription
       anchors.top: gameTitle.bottom
       anchors.left: parent.left
       anchors.leftMargin: 15
       anchors.topMargin: 15
       backgroundColor: "#80000000"
       textValue: "gameDescription"
       textColor: "#ffffff"
       family: "Roboto"
       fontWeight: Font.Light
       fontPointSize: 18
   }
   BackgroundedText{
       id: gameShortInfo
       anchors.top: parent.top
       anchors.right: parent.right
       anchors.rightMargin: 15
       anchors.topMargin: 15
       backgroundColor: "#80000000"
       textValue: "<b>Publisher</b>|gamePublisher<br/><b>ReleaseDate</b>|gameReleaseDate<br/><b>Genre</b>|gameGenre"
       textColor: "#ffffff"
       family: "Roboto"
       fontWeight: Font.Light
       fontPointSize: 18
   }

}
