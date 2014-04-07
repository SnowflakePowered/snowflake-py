import sys
from PyQt5 import QtWidgets
from PyQt5.QtQuick import *
from PyQt5.QtCore import *
from PyQt5.QtQml import *
from PyQt5.Qt import *
from loadables import Loadables
from listmodel.qml_platforms import *

@pyqtSlot(QVariant)
def test(platform):
    print (platform.platform_id)

def main():
    icelake_plat = Loadables.Instance().platforms
    platform_model = PlatformsListModel([PlatformsWrapper(platform_info) for platform_info in iter(icelake_plat.values())])
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty('platformListModel', platform_model)
    engine.load(QUrl("qml/snowflake/snowflake.qml"))
    window = engine.rootObjects()[0]
    sel = window.findChild(QQuickItem, name="platformSelector")
    sel.platformChanged.connect(test)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
