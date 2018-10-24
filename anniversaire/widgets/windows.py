# -*- coding: utf-8 -*-
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDialog
from PyQt5.Qt import QPushButton
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QDateEdit, QPushButton,
        QSpinBox, QTextEdit,
        QVBoxLayout)
from .connect import Connect


class Window(object):

    @staticmethod
    def showdialog(parent):
        db = Connect()
        d = QDialog()
        idb = '1'
        d.formGroupBox = QGroupBox("Form layout")
        layout = QFormLayout()
        layout.addRow((QLabel("Nom:")), (QLineEdit(str(db.selectun
        ("SELECT Nom FROM v2 WHERE id=" + idb + ";")))))
        layout.addRow(QLabel("Prénom:"), (QLineEdit(str(db.selectun
        ("SELECT Prenom FROM v2 WHERE id=" + idb + ";")))))
        layout.addRow(QLabel("Date naissance:"), QDateEdit(db.selectun
        ("SELECT `Date de naissance` FROM v2 WHERE id=" + idb + ";")))
        d.formGroupBox.setLayout(layout)
        b1 = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        b1.accepted.connect(d.accept)
        b1.rejected.connect(d.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(d.formGroupBox)
        mainLayout.addWidget(b1)
        d.setLayout(mainLayout)
        d.setWindowTitle("Modification")
        d.setWindowModality(Qt.ApplicationModal)
        d.exec_()
