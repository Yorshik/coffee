from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
import sys
import sqlite3


class Espresso(QWidget):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect('coffee.sqlite')
        self.setup()

    def setup(self):
        uic.loadUi('main.ui', self)
        self.loadData()

    def loadData(self):
        cur = self.con.cursor()
        res = cur.execute('SELECT * FROM coffee ORDER BY id').fetchall()
        self.tableWidget.setRowCount(len(res))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['id', 'sort', 'roasting', 'type', 'description', 'price', 'V'])
        for i, row in enumerate(res):
            for j, el in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(el)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Espresso()
    e.show()
    sys.exit(app.exec())
