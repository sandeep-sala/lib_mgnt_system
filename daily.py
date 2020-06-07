"""Daily Created by Sandeep-Sala"""
import sqlite3
from PyQt5.QtWidgets import *
import datetime
from datetime import timedelta

class Daily:

    def daily_work(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()
        book = self.comboBox_10.currentText()
        studnam = self.comboBox_9.currentText()
        typpe = self.comboBox.currentText()
        days = self.comboBox_2.currentIndex() + 1
        today = datetime.date.today()
        increm = self.change_date(days)


        self.cur.execute('INSERT INTO openn (name,student,type,fro,tom) VALUES (?,?,?,?,?)',
                         (book, studnam, typpe, today, increm))
        self.db.commit()
        self.db.close()
        self.statusBar.showMessage("Added", msecs=5000)
        self.display_work()

    def display_work(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()

        self.cur.execute('SELECT name,student,type,fro,tom from openn')
        self.data = self.cur.fetchall()
        if self.data:
            self.tableWidget.setRowCount(0)
            self.tableWidget.insertRow(0)
            for row, form in enumerate(self.data):
                for column, item in enumerate(form):
                    self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_post = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_post)

    def change_date(self, days):
        today = datetime.date.today()
        k = today + timedelta(days=days)
        return k
