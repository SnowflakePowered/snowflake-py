import QtQuick 2.1
import QtQuick.Controls 1.1
import QtQuick.Layouts 1.1

ApplicationWindow{
    title: "Snowflake"
    width: 1280
    height: 720
    id: mainWindow
    minimumHeight: 504
    minimumWidth: 896

    Rectangle{
            id: platformSelectorWrapper
            objectName: "platformSelectorWrapper"

            height: 130
            color: "blue"
            anchors.right: parent.right
            anchors.rightMargin: 0
            anchors.left: parent.left
            anchors.leftMargin: 0
            PlatformList{
                id: platformSelector
                objectName: "platformSelector"
                model: platformListModel
                anchors.fill: parent
                onPlatformChanged:{
                    textObj.text = qsTr(platform.platform_id)
                }
            }
        }
    Rectangle{
            id: dummy
            color: "lightsteelblue"
            anchors{
                top: platformSelectorWrapper.bottom
                right: parent.right
                left: parent.left
                bottom: parent.bottom

                topMargin: 0
                rightMargin: 0
                leftMargin: 0
                bottomMargin: 0
            }
            Text{
                id: textObj
                text: "Testing"
            }
        }

    }

