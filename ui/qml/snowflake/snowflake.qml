import QtQuick 2.1
import QtQuick.Controls 1.1
import QtQuick.Layouts 1.1

ApplicationWindow{

    Rectangle{
            id: platformSelectorWrapper
            objectName: "platformSelectorWrapper"
            color: "#5A9FD6"
            height: 100
            z: 1000
            anchors.right: parent.right
            anchors.rightMargin: 0
            anchors.left: parent.left
            anchors.leftMargin: 0
            anchors.bottom: gamesList.top
            anchors.bottomMargin: 0
            ListModel {
                id: menuModel

                ListElement {
                    name: "Games"
                }
                ListElement {
                    name: "Consoles"
                }
            }

            ListView {
                id: menuList
                focus: false
                orientation: "Horizontal"
                interactive: true
                anchors.fill: parent
                model: menuModel
                delegate: Component {
                    Rectangle {
                        id: platformTab
                        width: (ListView.count > 5) ? menuList.width / 5 :  menuList.width / menuList.count
                        height: parent.height - 5
                        color: ListView.isCurrentItem ? "#5A9FD6" : "white"
                        Text {

                            id: menuSelect
                            elide: Text.ElideRight
                            text: model.name
                            font.family: "Roboto"
                            font.weight: Font.Light
                            font.pointSize: 12
                            anchors.leftMargin: 10
                            anchors.rightMargin: 10
                            anchors.bottomMargin: 5
                            anchors.fill: parent
                            verticalAlignment: Text.AlignBottom
                            horizontalAlignment: Text.AlignRight
                            color: platformTab.ListView.isCurrentItem ? "white": "black"
                        }


                        MouseArea {
                            anchors.fill: parent
                            onClicked: {
                                menuList.currentIndex = index;
                            }
                        }
                    }
                }

            }

            PlatformList{
                id: platformSelector
                objectName: "platformSelector"
                model: platformListModel
                onPlatformChanged:
                {
                    gamesList.gamesModel =  gamesListModel[platform.platform_id]
                    console.log(platform.platform_id)
                }
            }

        }

Rectangle{
    anchors{
        top: parent.top
        left: parent.left
        bottom: parent.bottom
        right: parent.right
        topMargin: 100
        leftMargin: 0
        bottomMargin: 0
        rightMargin: 0
    }

    GamesListView{
        id: gamesList
        gamesModel: gamesListModel[platformSelector.currentItem.selectedPlatform.platform_id]
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



