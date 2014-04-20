import QtQuick 2.1
import QtQuick.Controls 1.1
import QtQuick.Layouts 1.1

ApplicationWindow{

    Rectangle{
        states: [

            State {
                    name: "open"; when: mouseArea.pressed
                    PropertyChanges { target: platformSelectorWrapper; height: 130 }
              }
        ]
        transitions: Transition {
            to: "open"
            reversible: true
            NumberAnimation { properties: "height"; easing.type: Easing.InOutQuad }
        }



            id: platformSelectorWrapper
            objectName: "platformSelectorWrapper"
            color: "#5A9FD6"
            height: 0
            z: 1000
            anchors.right: parent.right
            anchors.rightMargin: 0
            anchors.left: parent.left
            anchors.leftMargin: 0
            PlatformList{
                id: platformSelector
                objectName: "platformSelector"
                model: platformListModel
                anchors.fill: parent
                onPlatformChanged:
                {
                    gamesList.model =  gamesListModel[platform.platform_id]
                    console.log(platform.platform_id)
                }
            }

        }

    Rectangle{
        Keys.onPressed: {
            if (event.key === Qt.Key_C) {
                if (platformSelectorWrapper.state === 'open'){
                    platformSelectorWrapper.state = ''
                }else{
                    platformSelectorWrapper.state = 'open'

                }
            }
        }


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

                   model: gamesListModel[platformSelector.currentItem.selectedPlatform.platform_id]
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
    title: "Snowflake"
    width: 1280
    height: 720
    id: mainWindow
    minimumHeight: 504
    minimumWidth: 896

    onVisibilityChanged: {
        platformSelector.platformChanged(platformSelector.currentItem.selectedPlatform.platform);
    }


}



