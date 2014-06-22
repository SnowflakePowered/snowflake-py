from PyQt5.QtCore import *
from games import RunnableGame

class RunnableGameWrapper(QObject):
    def __init__(self, game):
        QObject.__init__(self)
        self.game = game
    @pyqtProperty("QString")
    def uuid(self):
        return str(self.game.uuid)
    @pyqtProperty("QString")
    def boxart_url(self):
        return '../../../gameinfo/imagecache/' + str(self.game.gameinfo.images['ICELAKE_IMG_GAME_BOXARTS'])
    @pyqtProperty("QString")
    def title(self):
        return str(self.game.gameinfo.title)
    @pyqtProperty("QString")
    def description(self):
        return str(self.game.gameinfo.description)
    @pyqtProperty("QString")
    def infobox(self):
        return """
                <b>Publisher</b> | <i>{0}</i> <br />
                <b>Release Date</b> | <i>{1}</i> <br />
                <b>Genre</b> | <i>{2}</i>
                """.format(
            self.game.gameinfo.publisher,
            self.game.gameinfo.serialize_releasedate(),
            self.game.gameinfo.genre
        )



class RunnableGamesListModel(QAbstractListModel):
     def __init__(self, games):
        QAbstractListModel.__init__(self)
        self.game = Qt.UserRole + 1
        self.games = games

     def roleNames(self):
          names = {}
          names[self.game] = "game"
          return names

     def rowCount(self, parent=QModelIndex()):
         return len(self.games)

     def data(self, index, role):
         if index.isValid() and role == self.game:
             return self.games[index.row()]
         return None

