
from PyQt5.Qt import QWidget, QVBoxLayout


class Box(QWidget):

    def __init__(self, parent=None):
        super(Box, self).__init__(parent)
        self.setLayout(QVBoxLayout(self))

    def addWidget(self, widget):
        self.layout().addWidget(widget)