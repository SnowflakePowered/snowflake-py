import sys
from PyQt5.QtQuick import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QGuiApplication

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
        self.init_ui()

        self.window = self.get_root()
        self.platformSelector = self.window.findChild(QQuickItem, name="platformSelector")
        self.gamesList = self.window.findChild(QQuickItem, name="gamesList")


    def get_root(self):
        return self.engine.rootObjects()[0]

    def show(self):
        self.window.show()



def start():
    app = QGuiApplication(sys.argv)
    ui = DefaultUI()
    ui.gamesList.gameChanged.connect(test2)
    ui.platformSelector.platformChanged.connect(test)
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    start()
