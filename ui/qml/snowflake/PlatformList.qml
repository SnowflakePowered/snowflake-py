import QtQuick 2.0

ListView {
    signal platformChanged(var platform)

    id: platformList
    focus: true
    orientation: "Horizontal"
    interactive: true

    onCurrentIndexChanged:{
        platformChanged(platformList.currentItem.selectedPlatform.platform);
    }

    delegate: Component {
        Rectangle {
            id: platformTab
            width: platformList.width / platformList.count
            height: 125
            property variant selectedPlatform: model
            CustomBorder
                    {
                        commonBorder: false
                        lBorderwidth: 0
                        rBorderwidth: 0
                        tBorderwidth: 0
                        bBorderwidth: 5
                        borderColor: "#5A9FD6"
                    }

            color: ListView.isCurrentItem ? "#5A9FD6" : "white"
            Text {
                id: platformTitle
                elide: Text.ElideRight
                text: model.platform.full_name
                font.family: "Roboto"
                font.weight: Font.Light
                font.pointSize: 16
                anchors.leftMargin: 10
                anchors.rightMargin: 10
                anchors.bottomMargin: 5
                anchors.fill: parent
                verticalAlignment: Text.AlignBottom
                horizontalAlignment: Text.AlignRight
                color: platformTab.ListView.isCurrentItem ? "white": "black"
            }


            MouseArea {
                anchors.fill: parent
                onClicked: {
                    platformList.currentIndex = index;
                }
            }
        }
    }

}
