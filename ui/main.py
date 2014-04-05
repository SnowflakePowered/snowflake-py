import sys
from PyQt5 import QtWidgets
from PyQt5.QtQuick import *
from PyQt5.QtCore import *
from PyQt5.QtQml import *
from PyQt5.Qt import *

def main():

    class MainWindow(QQmlApplicationEngine):
        def __init__(self, str):
            super(MainWindow, self).__init__(str)

    app = QGuiApplication(sys.argv)
    engine = MainWindow(QUrl("qml/snowflake/snowflake.qml"))
    window = engine.rootObjects()[0]
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
