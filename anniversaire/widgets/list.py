# -*- coding: utf-8 -*-

from PyQt5.Qt import QListWidget, QDialog
from .dialog import Dialog
from .connect import Connect


class List(QListWidget):

    def __init__(self, parent, req):
        super(List, self).__init__(parent)
        self.db = Connect()
        self.fields = []
        self.itemClicked.connect(self.clicked)
        self.dialog = Dialog(self)
        self.req = req

    def addItem(self, query):
   
        label = """************
ID : {identifiant}
Nom : {nom} {prenom}
Âge : {age} ans, prochain anniversaire dans {anniversaire} jours""".format(
                 identifiant=str(query.value(0)),
                 nom=query.value(1),
                 prenom=query.value(2),
                 age=str(query.value(4)),
                 anniversaire=str(query.value(5))
            )
    
  
        super(List, self).addItem(label)
        self.fields.append(query.value(0))

    def fromTheQuery(self):
        self.clear()
        query = self.db.query(self.req)
        while (query.next()):
            self.addItem(query)
    
    def clear(self):
        self.fields.clear()
        super(List, self).clear()
            
    @property
    def selectedId(self):
        return self.fields[self.currentRow()]

    def clicked(self):
        if self.dialog.exec_(self.selectedId) == QDialog.Accepted:
            fieldsValues = {
                'Nom': self.dialog.lineEditNom.text(),
                'Prenom': self.dialog.lineEditPrenom.text()
            }
            if self.dialog.naissanceBool:
                fieldsValues['naissance'] = self.dialog.naissance.selectedDate().toString("yyyy-MM-dd")
            self.db.updateWithId("Personne", fieldsValues, self.selectedId)
            self.fromTheQuery()
