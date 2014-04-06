import QtQuick 2.1
import QtQuick.Controls 1.1
import QtQuick.Layouts 1.1

ApplicationWindow{
width: 1280
height: 720
id: mainWindow

ColorScheme{ id: colorScheme }

title: "Snowflake"
        Rectangle{
            id: platformSelectorWrapper
            height: 130
            color: colorScheme.primaryColor
            anchors.right: parent.right
            anchors.rightMargin: 0
            anchors.left: parent.left
            anchors.leftMargin: 0
            PlatformList{
                model: platformListModel
                anchors.fill: parent
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
        }
    }

