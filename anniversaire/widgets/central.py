# -*- coding: utf-8 -*-

from .box import Box
from .connect import Connect
from PyQt5.Qt import QListWidget, QTabWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from .list import List
from .listA import ListA


class Central(Box):

    def __init__(self, parent=None):
        super(Central, self).__init__(parent)
        #Connection à la base de données
        self.db = Connect()
        #Liste de tout les anniversaires
        self.list = List(self, "SELECT * FROM v2_notnull;")
        self.list.fromTheQuery()
        self.tab = QTabWidget(self)
        self.addWidget(self.tab)
        self.tab.addTab(self.list, "Tout")
        #Liste des anniversaires d'aujourd'hui
        self.listA = ListA(self, "SELECT v2_notnull.ID, v2_notnull.Nom, v2_notnull.Prenom, v2_notnull.`Date de naissance`, v2_notnull.Âge, v2_notnull.`Jours restants` FROM v2_notnull, Personne WHERE MONTH(Personne.`naissance`) = MONTH(CURRENT_DATE) AND DAY(`naissance`) = DAY(CURRENT_DATE) AND Personne.id = v2_notnull.ID;")
        self.tab.addTab(self.listA, "Aujourd'hui")
        #Liste des anniversaires dans les 15 prochains jours
        self.list15 = List(self, "SELECT * FROM v2_notnull WHERE `Jours restants` < 15 AND `Jours restants` > 1;")
        self.tab.addTab(self.list15, "< 15")
        #Liste des anniversaires dans les 45 prochains jours
        self.list45 = List(self, "SELECT * FROM v2_notnull WHERE `Jours restants` < 45 AND `Jours restants` > 15;")
        self.tab.addTab(self.list45, "< 45")
        #Liste où la date de naissances n'est pas renseigné
        self.listrens = List(self, "SELECT * FROM v2 WHERE v2.id NOT IN (SELECT id from v2_notnull);")
        self.tab.addTab(self.listrens, "À Renseigner")
        self.tab.currentChanged.connect(self.tabChanged)
        #TODO: Bouton insert
        #TODO: Bouton delete
        
    def tabChanged(self, index):
        self.tab.currentWidget().fromTheQuery()
