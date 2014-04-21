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


class SnowflakeUI:
    def __init__(self, qmlfile, gamesdb, args=sys.argv):
        self.app = QGuiApplication(args)
        self.engine = QQmlApplicationEngine()
        self.games_db = gamesdb
        self.root_qml = qmlfile


    def load_ui(self):
        self.engine.load(QUrl(self.root_qml))

    def _load_games(self):
        gameslist = {}
        keys = Loadables.Instance().platforms.keys()
        for platform in keys:
            games = self.games_db.get_games_for_platform(platform)
            gameslist[platform] = qml_games.RunnableGamesListModel(sorted((qml_games.RunnableGameWrapper(game) for game in games),
                                                            key=lambda game: game.game.gameinfo.title))
        return gameslist

    def _load_platforms(self):
        return qml_platforms.PlatformsListModel(sorted((qml_platforms.PlatformsWrapper(platform_info)
                                                           for platform_info in iter(Loadables.Instance().platforms.values())),
                                                           key = lambda platform: platform.platform_id))


@pyqtSlot(QVariant)
def test(platform):
    print (platform)


@pyqtSlot(QVariant)
def test2(platform):
    print (platform.title)


def start():
    userinterface = SnowflakeUI("qml/snowflake/snowflake.qml",database.GamesDatabase(constants.database_path))
    engine = userinterface.engine
    engine = userinterface.engine
    platforms = userinterface._load_platforms()
    games = userinterface._load_games()

    engine.rootContext().setContextProperty('platformListModel', platforms)
    engine.rootContext().setContextProperty('gamesListModel', games)
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
