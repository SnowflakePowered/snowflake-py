import QtQuick 2.0
// From http://stackoverflow.com/questions/16534489/qml-control-border-width-and-color-on-any-one-side-of-rectangle-element
Rectangle
{
    property int seperatorLength: 1
    z : -1

    property string borderColor : "white"

    color: borderColor

    anchors
    {
        left: parent.left
        right: parent.right
        top: parent.top
        bottom: parent.bottom

        topMargin    : 10
        bottomMargin : 10
        leftMargin   : -seperatorLength
        rightMargin  : 0
    }
}
