"""Settings Created by Sandeep-Sala"""
import sqlite3
from PyQt5.QtWidgets import *


class SetIng:

    def add_category(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()
        self.ct_name = self.lineEdit_13.text()
        self.cur.execute('INSERT INTO category (cat_name) VALUES (?)', (self.ct_name,))
        self.db.commit()
        self.db.close()
        self.lineEdit_13.setText('')
        self.show_category()
        self.statusBar.showMessage('New Category Added', msecs=5000)
        self.show_cat_combo()

    def show_category(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()

        self.cur.execute('SELECT cat_name from category')
        self.data = self.cur.fetchall()

        if self.data:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row, form in enumerate(self.data):
                for column, item in enumerate(form):
                    self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_post = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_post)

    def add_author(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()
        self.at_name = self.lineEdit_14.text()
        self.cur.execute('INSERT INTO Authors (author_name) VALUES (?)', (self.at_name,))
        self.db.commit()
        self.db.close()
        self.lineEdit_14.setText('')
        self.show_author()
        self.statusBar.showMessage("New Category Added", msecs=5000)
        self.show_aut_combo()

    def show_author(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()

        self.cur.execute('SELECT author_name from Authors')
        self.data = self.cur.fetchall()

        if self.data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row, form in enumerate(self.data):
                for column, item in enumerate(form):
                    self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_post = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_post)

    def add_publisher(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()
        self.pt_name = self.lineEdit_15.text()
        self.cur.execute('INSERT INTO publisher (pub_name) VALUES (?)', (self.pt_name,))
        self.db.commit()
        self.db.close()
        self.lineEdit_15.setText('')
        self.show_publisher()
        self.statusBar.showMessage("New Category Added", msecs=5000)
        self.show_pu_combo()

    def show_publisher(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()

        self.cur.execute('SELECT pub_name from publisher')
        self.data = self.cur.fetchall()

        if self.data:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            for row, form in enumerate(self.data):
                for column, item in enumerate(form):
                    self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_post = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_post)

    def show_cat_combo(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()

        self.cur.execute('SELECT cat_name from category')
        self.data = self.cur.fetchall()
        self.comboBox_5.clear()

        for cat in self.data:
            self.comboBox_5.addItem(cat[0])
            self.comboBox_8.addItem(cat[0])

    def show_aut_combo(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()

        self.cur.execute('SELECT author_name from Authors')
        self.data = self.cur.fetchall()
        self.comboBox_3.clear()

        for aut in self.data:
            self.comboBox_3.addItem(aut[0])
            self.comboBox_6.addItem(aut[0])

    def show_pu_combo(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()

        self.cur.execute('SELECT pub_name from publisher')
        self.data = self.cur.fetchall()
        self.comboBox_4.clear()

        for pu in self.data:
            self.comboBox_4.addItem(pu[0])
            self.comboBox_7.addItem(pu[0])

    def show_book_combo(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()

        self.cur.execute('SELECT book_name from book')
        self.data = self.cur.fetchall()
        self.comboBox_10.clear()

        for pu in self.data:
            self.comboBox_10.addItem(pu[0])

    def show_student_combo(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()

        self.cur.execute('SELECT name from student')
        self.data = self.cur.fetchall()
        self.comboBox_9.clear()

        for pu in self.data:
            self.comboBox_9.addItem(pu[0])

