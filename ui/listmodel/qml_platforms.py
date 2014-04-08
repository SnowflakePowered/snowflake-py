from PyQt5.QtCore import *

class PlatformsWrapper(QObject):
    def __init__(self, platform):
        QObject.__init__(self)
        self.platform = platform
    @pyqtProperty("QString")
    def platform_id(self):
        return str(self.platform.platform_id)
    @pyqtProperty("QString")
    def full_name(self):
        return str(self.platform.full_name)
    @pyqtProperty("QString")
    def short_name(self):
        return str(self.platform.short_name)

class PlatformsListModel(QAbstractListModel):
     def __init__(self, platforms):
        QAbstractListModel.__init__(self)
        self.platform = Qt.UserRole + 1
        self.platforms = platforms

     def roleNames(self):
          names = {}
          names[self.platform] = "platform"
          return names

     def rowCount(self, parent=QModelIndex()):
         return len(self.platforms)
     def data(self, index, role):
         if index.isValid() and role == self.platform:
             return self.platforms[index.row()]
         return None

