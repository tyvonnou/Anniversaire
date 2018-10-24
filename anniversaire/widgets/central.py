# -*- coding: utf-8 -*-

from .box import Box
from .connect import Connect
from PyQt5.Qt import QListWidget, QTabWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from .list import List


class Central(Box):

    def __init__(self, parent=None):
        super(Central, self).__init__(parent)
        #Connection à la base de données
        self.db = Connect()
        #Liste de tout les anniversaires
        self.list = List(self, "SELECT * FROM v2_notnull;")
        self.list.fromQuery()

        self.tab = QTabWidget(self)
        self.addWidget(self.tab)
        self.tab.addTab(self.list, "Tout")
        #Liste des anniversaires dans les 20 prochains jours
        self.list20 = List(self)
        self.list20.fromQuery("SELECT * FROM v2_notnull WHERE `Jours restants` < 20 ;")
        self.tab.addTab(self.list20, "< 20")
        #Liste des anniversaires dans les 50 prochains jours
        self.list50 = List(self)
        self.list50.fromQuery("SELECT * FROM v2_notnull WHERE `Jours restants` < 50 ;")
        self.tab.addTab(self.list50, "< 50")
        #Liste où la date de naissances n'est pas renseigné
        self.listrens = List(self)
        self.listrens.fromQuery("SELECT * FROM v2 WHERE v2.id NOT IN (SELECT id from v2_notnull);")
        self.tab.addTab(self.listrens, "À Renseigner")
