import QtQuick 2.0
Rectangle{
   id: gameInfoWrapper
   color: "lightsteelblue"

   property string textGameTitle
   property string textGameDescription
   property string textGameShortInfo
   property string boxartUrl


   BackgroundedText{
       id: gameTitle
       anchors.top: parent.top
       anchors.left: parent.left
       anchors.leftMargin: 15
       anchors.topMargin: 15
       backgroundColor: "#80000000"
       text{
           text: textGameTitle
           color: "#fff"
           font{
               weight: Font.Light
               pointSize: 21
               family: "Roboto"
           }
       }
   }
   BackgroundedTextEdit{
       id: gameDescription
       anchors.left: parent.left
       anchors.right: parent.right
       anchors.leftMargin: 15
       anchors.topMargin: 30
       anchors.rightMargin: 15
       anchors.bottom: parent.bottom
       anchors.bottomMargin: 30
       backgroundColor: "#80000000"
       height: 300
       text{
           text: textGameDescription
           color: "#fff"
           font{
               weight: Font.Light
               pointSize: 14
               family: "Roboto"
           }
       }

   }
   BackgroundedText{
       id: gameShortInfo
       anchors.top: parent.top
       anchors.right: parent.right
       anchors.rightMargin: 15
       anchors.topMargin: 15
       backgroundColor: "#80000000"
       text{
           text: textGameShortInfo
           color: "#fff"
           font{
               weight: Font.Light
               pointSize: 18
               family: "Roboto"
           }
       }
   }
   Image{
       id: gameBoxArt
       anchors.top: gameTitle.bottom
       anchors.left: parent.left
       anchors.bottom: gameDescription.top
       anchors.leftMargin: 15
       anchors.topMargin: 15
       anchors.bottomMargin: 15
       fillMode: Image.PreserveAspectFit

       source: boxartUrl

   }

}
