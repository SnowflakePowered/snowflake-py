import QtQuick 2.1
import QtQuick.Controls 1.1
import QtQuick.Layouts 1.1

ApplicationWindow {
    id: applicationWindow1
    title: "My Application"
    minimumHeight: 720
    minimumWidth: 1280
    maximumHeight: 720
    maximumWidth: 1280
    property int margin: 11

    GridLayout {
        id: gridLayout1
        x: 0
        y: 0
        anchors.fill: parent
        height: 720
        width: 1280
        anchors.margins: margin
        Button {
            id: button1
            x: -75
            y: 38
            text: qsTr("Button")
        }
    }


}
