import QtQuick 2.1
import QtQuick.Controls 1.1

ApplicationWindow{
width: 1280
height: 720
id: mainWindow

    PlatformList{
        model: platformListModel
    }
}
