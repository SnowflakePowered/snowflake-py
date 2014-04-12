import sys
from PyQt5 import QtWidgets
from PyQt5.QtQuick import *
from PyQt5.QtCore import *
from PyQt5.QtQml import *
from PyQt5.Qt import *
from loadables import Loadables
from listmodel import qml_platforms, qml_games
import database
import os
import constants

@pyqtSlot(QVariant)
def test(platform):
    print (platform.platform_id)

def main():
    db = database.GamesDatabase(constants.core_path)
    games = db.get_games_for_platform("NINTENDO_SNES")
    icelake_plat = Loadables.Instance().platforms
    games_model = qml_games.RunnableGamesListModel([qml_games.RunnableGameWrapper(game_info) for game_info in games])
    platform_model = qml_platforms.PlatformsListModel([qml_platforms.PlatformsWrapper(platform_info) for platform_info in iter(icelake_plat.values())])
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty('platformListModel', platform_model)
    engine.rootContext().setContextProperty('gamesListModel', games_model)
    engine.load(QUrl("qml/snowflake/snowflake.qml"))
    window = engine.rootObjects()[0]
    sel = window.findChild(QQuickItem, name="platformSelector")
    gamesel = window.findChild(QQuickItem, name="platformSelector")
    sel.platformChanged.connect(test)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
