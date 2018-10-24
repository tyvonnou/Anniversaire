# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (
    QDialog,
    QFormLayout,
    QLabel,
    QLineEdit,
    QGroupBox,
    QDialogButtonBox,
    QVBoxLayout,
    QCalendarWidget
)

from .connect import Connect


class Dialog (QDialog):

    def __init__(self, parent):
        super(Dialog , self).__init__(parent)
        self.db = Connect()
        self.formGroupBox = QGroupBox("Form layout")
        self.formGroupBox.setLayout(QFormLayout())
        self.lineEditNom = QLineEdit()
        self.formGroupBox.layout().addRow(
            QLabel("Nom:"),
            self.lineEditNom
        )
        self.lineEditPrenom = QLineEdit()
        self.formGroupBox.layout().addRow(
            QLabel("Prénom:"),
            self.lineEditPrenom
        )
        self.naissance = QCalendarWidget()
        self.formGroupBox.layout().addRow(
            QLabel("Date naissance:"),
            self.naissance
        )
        self.naissance.selectionChanged.connect(self.naissanceChanged)
        self.naissanceBool = False
        b1 = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        b1.accepted.connect(self.accept)
        b1.rejected.connect(self.reject)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.formGroupBox)
        self.layout().addWidget(b1)
        self.setWindowTitle("Modification")

    def exec_(self, iddb):
        req = "SELECT Nom, Prenom, `Date de naissance` FROM v2 WHERE id={}"
        req = req.format(iddb)
        res = self.db.selectOne(req)
        self.lineEditNom.setText(res['Nom'])
        self.lineEditPrenom.setText(res['Prenom'])
        self.naissance.setSelectedDate(res['Date de naissance'])
        print(self.naissance.selectedDate().toString())
        return super(Dialog, self).exec_()
        
    def naissanceChanged(self):
        self.naissanceBool = True



