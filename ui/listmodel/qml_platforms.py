from PyQt5.QtCore import *
import platforms


class PlatformsWrapper(QObject):
    def __init__(self, platform):
        QObject.__init__(self)
        self.platform = platform
    def _platform_id(self):
        return str(self.platform.platform_id)
    def _full_name(self):
        return str(self.platform.full_name)
    def _short_name(self):
        return str(self.platform.short_name)

    changed = pyqtSignal()
    full_name = pyqtProperty("QString", _full_name, notify=changed)

class Controller(QObject):
    @pyqtSlot(QObject)
    def thingSelected(self, wrapper):
        print(wrapper.platform.platform_id)

class PlatformsListModel(QAbstractListModel):
     def __init__(self, platforms):
        QAbstractListModel.__init__(self)
        self.somerole = Qt.UserRole + 1

        self.platforms = platforms

     def roleNames(self):
          names = {}
          names[self.somerole] = "somerole"
          return names

     def rowCount(self, parent=QModelIndex()):
         return len(self.platforms)
     def data(self, index, role):
         if index.isValid() and role == self.somerole:
             return self.platforms[index.row()]
         return None

