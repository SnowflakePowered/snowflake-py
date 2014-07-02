import QtQuick 2.0

ListView {
    height: 100
    z: 1000
    anchors.right: parent.right
    anchors.rightMargin: 0
    anchors.left: parent.left
    anchors.leftMargin: 0
    anchors.bottom: gamesList.top
    anchors.bottomMargin: 0
            id: menuList
            focus: false
            orientation: "Horizontal"
            interactive: true
            anchors.fill: parent
            model:   ListModel {
                id: menuModel

                ListElement {
                    name: "Snowflake"
                    stateName: "about"
                }
                ListElement {
                    name: "Games"
                    stateName: "games"
                }
                ListElement {
                    name: "Consoles"
                    stateName: "console"
                }
                ListElement {
                    name: "Settings"
                    stateName: "settings"
                }
            }
            delegate: Component {
                Rectangle {
                    color: "#5A9FD6"
                    id: platformTab
                    width: (ListView.count > 5) ? menuList.width / 5 :  menuList.width / menuList.count
                    height: parent.height - 5
                    Separator
                    {
                        seperatorLength: 1
                        borderColor: "grey"
                    }
                    Text {
                        color: 'white'
                        id: menuSelect
                        text: model.name
                        font.family: "Roboto"
                        font.weight: platformTab.ListView.isCurrentItem ? Font.Bold : Font.Light
                        font.pointSize: 30
                        anchors.leftMargin: 10
                        anchors.rightMargin: 10
                        anchors.bottomMargin: 5
                        anchors.fill: parent
                        verticalAlignment: Text.AlignVCenter
                        horizontalAlignment: Text.AlignHCenter
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
