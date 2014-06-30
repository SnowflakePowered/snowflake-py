import QtQuick 2.0

Rectangle{
    property variant gamesModel
    id: gameAreaWrapper
    color: "lightsteelblue"
    anchors.fill: parent
    Rectangle{
        id: gameListWrapper
        anchors{
            top: parent.top
            left: parent.left
            bottom: parent.bottom
            topMargin: 0
            leftMargin: 0
            bottomMargin: 0
        }
       width: 350
       color: "lightgrey"
       ListView {
           id: gamesList
           objectName: "gamesList"
           width: parent.width
           height: 300
           focus: true
           interactive: true
           model: gamesModel
           signal gameChanged(var game)
           onCurrentIndexChanged:{
               gameChanged(gamesList.currentItem.selectedGame.game);
           }
           onGameChanged:{
               gameInfo.textGameTitle = qsTr(game.title)
               gameInfo.textGameDescription = qsTr(game.description)
               gameInfo.textGameShortInfo= qsTr(game.infobox)
               gameInfo.boxartUrl = qsTr(game.boxart_url)
           }

           delegate: Component {
               Rectangle {
                   width: gamesList.width
                   height: 40
                   color: ListView.isCurrentItem ? "#5A9FD6" : "lightgrey"
                   property variant selectedGame: model
                   Text {
                       id: title
                       elide: Text.ElideRight
                       text: model.game.title
                       color: "white"
                       font.bold: true
                       anchors.leftMargin: 10
                       anchors.fill: parent
                       verticalAlignment: Text.AlignVCenter
                       font.family: "Roboto"
                   }
                   MouseArea {
                       anchors.fill: parent
                       onClicked: {
                           gamesList.focus = true;
                           gamesList.currentIndex = index;
                       }
                   }
               }
           }
       }
    }
     GameInfo{
         id: gameInfo
         anchors{
             top: parent.top
             left: gameListWrapper.right
             bottom: parent.bottom
             right: parent.right
             rightMargin: 0
             topMargin: 0
             leftMargin: 0
             bottomMargin: 0
        }
    }
}
