import QtQuick 2.0

ListView {
	signal platformChanged(var platform)

	id: platformList
    focus: false
	orientation: "Horizontal"
    interactive: true

	onCurrentIndexChanged:{
		platformChanged(platformList.currentItem.selectedPlatform.platform);
	}

	delegate: Component {
		Rectangle {
			id: platformTab
            width: (ListView.count > 5) ? platformList.width / 5 :  platformList.width / platformList.count
            height: parent.height - 5
			property variant selectedPlatform: model


			color: ListView.isCurrentItem ? "#5A9FD6" : "white"
			Text {

				id: platformTitle
                elide: Text.ElideRight
				text: model.platform.full_name
				font.family: "Roboto"
				font.weight: Font.Light
                font.pointSize: 12
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
                    platformList.focus = true;
					platformList.currentIndex = index;
				}
			}
		}
	}

}
