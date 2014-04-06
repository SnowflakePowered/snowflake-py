import QtQuick 2.1
import QtQuick.Controls 1.1

ApplicationWindow{
id: mainWindow
ListView {
    id: pythonList
    width: 400
    height: 200

    model: pythonListModel

    delegate: Component {
        Rectangle {
            width: pythonList.width
            height: 40
            color: ((index % 2 == 0)?"#222":"#111")
            Text {
                id: title
                elide: Text.ElideRight
                text: model.somerole.full_name
                color: "white"
                font.bold: true
                anchors.leftMargin: 10
                anchors.fill: parent
                verticalAlignment: Text.AlignVCenter
            }
            MouseArea {
                anchors.fill: parent
            }
        }
    }
}
}
