import sys
from PyQt5 import QtWidgets
from PyQt5.QtQuick import *
from PyQt5.QtCore import *
from PyQt5.QtQml import *
from PyQt5.Qt import *
from loadables import Loadables
from listmodel.qml_platforms import *
def main():
    icelake_plat = Loadables.Instance().platforms
    platform_model = PlatformsListModel([PlatformsWrapper(platform_info) for platform_info in iter(icelake_plat.values())])
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    controller = Controller()
    engine.rootContext().setContextProperty('platformListModel', platform_model)
    engine.rootContext().setContextProperty('controller', controller)
    engine.load(QUrl("qml/snowflake/snowflake.qml"))
    window = engine.rootObjects()[0]
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
