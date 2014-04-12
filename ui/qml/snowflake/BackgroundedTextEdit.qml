import QtQuick 2.0
import QtQuick.Controls 1.1
import QtQuick.Controls.Styles 1.1

Rectangle{

    property string backgroundColor
    property alias text : textContent

    id: textBackground
    color: backgroundColor
    width: textContent.paintedWidth + 15
    height: textContent.paintedHeight + 15


    ScrollView {
         id: scrollArea
         style:
             ScrollViewStyle{
                transientScrollBars: false
                minimumHandleLength: 0
                scrollBarBackground: Component{
                    Item {
                      implicitWidth: 16
                      implicitHeight: 16
                      clip: true
                      Rectangle {
                          anchors.fill: parent
                          color: "#90000000"
                          anchors.rightMargin: styleData.horizontal ? -2 : -1
                          anchors.leftMargin: styleData.horizontal ? -2 : 0
                          anchors.topMargin: styleData.horizontal ? 0 : -2
                          anchors.bottomMargin: styleData.horizontal ? -1 : -2
                      }
                  }
                }

         }

         anchors{
             right: parent.right
             top: parent.top
             left: parent.left
             bottom: parent.bottom

             topMargin: 10
             rightMargin: 10
             leftMargin: 10
             bottomMargin: 10
         }
            TextEdit{
                id: textContent
                wrapMode: TextEdit.Wrap
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter
                anchors{
                    right: textBackground.right
                    top: textBackground.top
                    left: textBackground.left
                    bottom: textBackground.bottom

                    topMargin: 10
                    rightMargin: 10
                    leftMargin: 10
                    bottomMargin: 10
                }
                width: textBackground.width - 50

            }
    }
}
