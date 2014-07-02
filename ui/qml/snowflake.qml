import QtQuick 2.2
import QtQuick.Controls 1.2

import QtWebKit 3.0

ApplicationWindow{
    color: "#5A9FD6"

Rectangle{
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
        ListView {
            id: menuList
            focus: false
            orientation: "Horizontal"
            interactive: true
            anchors.fill: parent
            model: menuModel
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
    }


Rectangle{

    anchors{
        top: parent.top
        left: parent.left
        bottom: parent.bottom
        right: parent.right
        topMargin: 100
        leftMargin: 5
        bottomMargin: 5
        rightMargin: 5
    }
    WebView{
        anchors.fill: parent
        z: -10
        id: webview
        url: "http://google.com"

        onNavigationRequested: {
            // detect URL scheme prefix, most likely an external link
            var schemaRE = /^\w+:/;
            if (schemaRE.test(request.url)) {
                request.action = WebView.AcceptRequest;
            } else {
                request.action = WebView.IgnoreRequest;
                // delegate request.url here
            }
        }
    }
}
    title: "Snowflake"
    width: 1280
    height: 720
    id: mainWindow
    minimumHeight: 504
    minimumWidth: 896
}



