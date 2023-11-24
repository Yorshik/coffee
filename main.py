import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class AddEditCoffeForm(QMainWindow):
    def __init__(self, what: list | str, parent=None):
        super().__init__(parent)
        self.what = what
        self.translate1 = {
            'ground': 'молотый', 'beans': 'зерновой', 'light': 'легкая', 'medium': 'средняя', 'high': 'сильная'
        }
        self.translate2 = {
            'молотый': 'ground', 'зерновой': 'beans', 'легкая': 'light', 'средняя': 'medium', 'сильная': 'high'
        }
        self.setup()

    def setup(self):
        uic.loadUi('addEditCoffeeForm.ui', self)
        if self.what[0] == 'edit':
            self.load(self.what[1])
        self.save_button.clicked.connect(self.save)

    def save(self):
        cur = self.parent().con.cursor()
        if self.what == 'add':
            cur.execute(
                'INSERT INTO coffee(sort, roasting, type, description, price, V) VALUES (?, ?, ?, ?, ?, ?)', (
                    self.sort.text(), self.translate2[self.roasting.currentText()],
                    self.translate2[self.type.currentText()],
                    self.description.toPlainText(), self.price.text(), self.V_V.text())
                )
        else:
            cur.execute(
                'UPDATE coffee SET sort = ?, roasting = ?, type = ?, description = ?, price = ?, V = ? WHERE id = ?', (
                    self.sort.text(), self.translate2[self.roasting.currentText()],
                    self.translate2[self.type.currentText()],
                    self.description.toPlainText(), self.price.text(), self.V_V.text(), self.curr_id)
                )
        self.parent().con.commit()
        self.parent().loadData()
        self.close()

    def load(self, lst):
        self.curr_id = lst[0]
        self.sort.setText(lst[1])
        self.roasting.setCurrentText(self.translate1[lst[2]])
        self.type.setCurrentText(self.translate1[lst[3]])
        self.description.setPlainText(lst[4])
        self.price.setText(lst[5])
        self.V_V.setText(lst[6])


class Espresso(QMainWindow):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect('coffee.sqlite')
        self.setup()

    def setup(self):
        uic.loadUi('main.ui', self)
        self.loadData()
        self.add_button.clicked.connect(self.add)
        self.tableWidget.itemClicked.connect(self.item_clicked)

    def add(self):
        self.adding = AddEditCoffeForm('add', self)
        self.adding.show()

    def loadData(self):
        cur = self.con.cursor()
        res = cur.execute('SELECT * FROM coffee ORDER BY id').fetchall()
        self.tableWidget.setRowCount(len(res))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['id', 'sort', 'roasting', 'type', 'description', 'price', 'V'])
        for i, row in enumerate(res):
            for j, el in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(el)))

    def item_clicked(self, item: QTableWidgetItem):
        row = item.row()
        lst = self.tableWidget.item(row, 0).text(), self.tableWidget.item(row, 1).text(), self.tableWidget.item(
            row, 2
            ).text(), self.tableWidget.item(
            row, 3
            ).text(), self.tableWidget.item(row, 4).text(), self.tableWidget.item(row, 5).text(), self.tableWidget.item(
            row, 6
            ).text()
        self.editing = AddEditCoffeForm(['edit', lst], self)
        self.editing.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Espresso()
    e.show()
    sys.exit(app.exec())
