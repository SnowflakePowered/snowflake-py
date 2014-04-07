import QtQuick 2.0

Rectangle{
    property string textValue
    property int fontPointSize
    property string family
    property string backgroundColor
    property string textColor
    property var fontWeight

    id: textBackground
    color: backgroundColor
    width: textContent.paintedWidth + 15
    height: textContent.paintedHeight + 15
    Text{
        id: textContent
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        text: textValue
        font.pointSize: fontPointSize
        font.family: family
        font.weight: fontWeight
        color: textColor
    }
}
