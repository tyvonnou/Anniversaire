# -*- coding: utf-8 -*-

import sys
import widgets
from PyQt5.Qt import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from pathlib import Path


def main():
    png = Path.joinpath(Path(__file__).parent,'images', 'cake.png')
    app = QApplication(sys.argv)
    mainW = QMainWindow()
    mainW.setWindowTitle("Anniversaires")
    mainW.setWindowIcon(QIcon(str(png)))
    central = widgets.Central(mainW)
    mainW.setCentralWidget(central)
    mainW.resize(600, 500)
    mainW.move(200, 150)
    mainW.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
