import sys
from PyQt5.QtQuick import *
from PyQt5.QtCore import *
import database
import constants
from ui.snowflakeui import SnowflakeUI


@pyqtSlot(QVariant)
def test(platform):
    print (platform)


@pyqtSlot(QVariant)
def test2(platform):
    print (platform.title)

class DefaultUI(SnowflakeUI):
    def __init__(self):
        super().__init__("qml/snowflake/snowflake.qml", database.GamesDatabase(constants.database_path))
        self.engine.rootContext().setContextProperty('platformListModel', self.platformsListModel)
        self.engine.rootContext().setContextProperty('gamesListModel', self.gamesListModel)

def start():
    userinterface = DefaultUI()
    engine = userinterface.engine

    userinterface.load_ui()
    window = engine.rootObjects()[0]

    sel = window.findChild(QQuickItem, name="platformSelector")
    gamesel = window.findChild(QQuickItem, name="gamesList")
    gamesel.gameChanged.connect(test2)
    sel.platformChanged.connect(test)
    window.show()
    sys.exit(userinterface.app.exec_())

if __name__ == '__main__':
    start()
