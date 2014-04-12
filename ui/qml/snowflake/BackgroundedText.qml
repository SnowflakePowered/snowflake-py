import QtQuick 2.0

Rectangle{

    property string backgroundColor
    property alias text : textContent

    id: textBackground
    color: backgroundColor
    width: textContent.paintedWidth + 15
    height: textContent.paintedHeight + 15
    Text{
        id: textContent
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
    }
}
