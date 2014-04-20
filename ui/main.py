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

    def load_qml(self):
        engine.load(QUrl(self.root_qml))

    def init_ui(self):
        self.load_qml()
        self.engine.rootObjects()[0].show()

    def setContextProperty(self, pstr, args):
        self.engine.rootContext().setContextProperty(pstr, args)

    @staticmethod
    def _load_games(self):
        gameslist = {}
        keys = Loadables.Instance().platforms.keys()
        for platform in keys:
            games = database.GamesDatabase(constants.database_path).get_games_for_platform(platform)
            gameslist[platform] = qml_games.RunnableGamesListModel(sorted((qml_games.RunnableGameWrapper(game) for game in games),
                                                            key=lambda game: game.game.gameinfo.title))
        return gameslist
    @classmethod
    def _load_platforms(cls):
            return qml_platforms.PlatformsListModel(sorted((qml_platforms.PlatformsWrapper(platform_info)
                                                           for platform_info in iter(Loadables.Instance().platforms.values())),
                                                           key = lambda platform: platform.platform_id))


@pyqtSlot(QVariant)
def test(platform):
    print (platform.platform_id)


@pyqtSlot(QVariant)
def test2(platform):
    print (platform.title)


def main():
    games_model = SnowflakeUI._load_games('')
    db = database.GamesDatabase(constants.database_path)
    games = db.get_games_for_platform("NINTENDO_SNES")

    sels = Loadables.Instance().platforms.keys()
    platform_model = qml_platforms.PlatformsListModel(sorted((qml_platforms.PlatformsWrapper(platform_info) for platform_info in iter(Loadables.Instance().platforms.values())), key = lambda platform: platform.platform_id))
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty('platformListModel', platform_model)
    engine.rootContext().setContextProperty('gamesListModel', games_model)
    engine.load(QUrl("qml/snowflake/snowflake.qml"))
    window = engine.rootObjects()[0]
    sel = window.findChild(QQuickItem, name="platformSelector")
    gamesel = window.findChild(QQuickItem, name="gamesList")
    gamesel.gameChanged.connect(test2)
    sel.platformChanged.connect(test)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
