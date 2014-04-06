import sys
from PyQt5 import QtWidgets
from PyQt5.QtQuick import *
from PyQt5.QtCore import *
from PyQt5.QtQml import *
from PyQt5.Qt import *
from loadables import Loadables
import listmodel.qml_platforms as qml_platforms
def main():
    item = Loadables.Instance().platforms["NINTENDO_SNES"]
    item_wrp = qml_platforms.PlatformsWrapper(item)
    platform_model = qml_platforms.PlatformsListModel([item_wrp, item_wrp])
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty('pythonListModel', platform_model)
    engine.load(QUrl("qml/snowflake/snowflake.qml"))

    window = engine.rootObjects()[0]
    chl = window.findChildren(QObject)
    window.show()
    list = window.findChild(QQuickItem, "pythonList")
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
