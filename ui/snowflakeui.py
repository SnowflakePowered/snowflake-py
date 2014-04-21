import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from ui.listmodel import qml_games, qml_platforms
from loadables import Loadables

__author__ = 'Ronny'


class SnowflakeUI:
    def __init__(self, qmlfile, gamesdb, args=sys.argv):
        self.app = QGuiApplication(args)
        self.engine = QQmlApplicationEngine()
        self.games_db = gamesdb
        self.root_qml = qmlfile
        self.platformsListModel = self._load_platforms()
        self.gamesListModel = self._load_games()

    def init_ui(self):
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