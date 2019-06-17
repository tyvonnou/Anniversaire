# -*- coding: utf-8 -*-
from PyQt5 import QtSql
from PyQt5.QtGui import *
from PyQt5.Qt import QPushButton, QApplication
import sys 

app = QApplication(sys.argv)
db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
db.setHostName("127.0.0.1")
db.setPort(3306)
db.setDatabaseName("Anniv")
db.setUserName("root")
db.setPassword("root")
db.open()


class Connect(QtSql.QSqlDatabase):

    def __init__(self):
        super(Connect, self).__init__()

    def query(self, q):
        return QtSql.QSqlQuery(q)

    def select(self, q):
        query = self.query(q)
        record = query.record()
        res = []
        keys = [record.field(i).name() for i in range(0, record.count())]
        while query.next():
            values = {}
            for i in range(0, len(keys)):
                values[keys[i]] = query.value(i)
            res.append(values)
        return res

    def selectOne(self, q):
        return self.select(q)[0]

    def update(self, table, fieldsValues, where):
        req = "UPDATE {table} SET {values} WHERE {where}"
        values = ''
        i = 0
        for field, value in fieldsValues.items():
            strFormat = '`{}`="{}"'
            if i < len(fieldsValues) - 1:
                strFormat += ','
            values += strFormat.format(field, value)
            i += 1
        query = QtSql.QSqlQuery()
        req = req.format(
            table=table,
            values=values,
            where=where
        )
        if not(query.exec(req)):
            raise ValueError(query.lastError().text())
        return query.numRowsAffected()
        
    def updateWithId(self, table, fieldsValues, iddb):
        return self.update(table, fieldsValues, "id={}".format(iddb))
        
