"""Books Created by Sandeep-Sala"""
import sqlite3
from PyQt5.QtWidgets import *
from settings import *


class BoOk:

    def add_book(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()
        self.book_id = self.lineEdit_5.text()
        self.book_name = self.lineEdit_2.text()
        self.book_price = self.lineEdit_4.text()
        self.book_disc = self.textEdit.toPlainText()
        self.book_category = self.comboBox_5.currentText()
        self.book_author = self.comboBox_3.currentText()
        self.book_publisher = self.comboBox_4.currentText()

        self.cur.execute('INSERT INTO book(book_name,book_disc,book_code,book_category,book_author,book_pub,book_price)'
                         ' VALUES (?,?,?,?,?,?,?)'
                         , (self.book_name,
                            self.book_disc,
                            self.book_id,
                            self.book_category,
                            self.book_author,
                            self.book_publisher,
                            self.book_price))
        self.db.commit()
        self.db.close()
        self.lineEdit_5.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_4.setText('')
        self.textEdit.setPlainText('Discription ...')
        self.comboBox_5.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        self.statusBar.showMessage("New Book Added", msecs=5000)
        self.display_book()
        self.show_book_combo()

    def search_book(self):
        self.book_idd = self.lineEdit_6.text()
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()
        self.cur.execute('SELECT * from book WHERE book_code = (?) ', (self.book_idd,))
        self.data = self.cur.fetchone()
        if self.data:
            self.lineEdit_3.setText(self.data[1])
            self.lineEdit_7.setText(str(self.data[7]))
            self.textEdit_2.setPlainText(self.data[2])
            self.comboBox_8.setCurrentText(self.data[4])
            self.comboBox_6.setCurrentText(self.data[5])
            self.comboBox_7.setCurrentText(self.data[6])
            self.statusBar.showMessage("Result Found", msecs=5000)
        else:
            self.lineEdit_3.setText('')
            self.lineEdit_7.setText(str(''))
            self.textEdit_2.setPlainText("Discription..")
            self.comboBox_8.setCurrentIndex(0)
            self.comboBox_6.setCurrentIndex(0)
            self.comboBox_7.setCurrentIndex(0)
            self.statusBar.showMessage("No Result Found", msecs=5000)

    def edit_save_book(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()
        self.book_id = self.lineEdit_6.text()
        self.book_name = self.lineEdit_3.text()
        self.book_disc = self.textEdit_2.toPlainText()
        self.book_category = self.comboBox_8.currentText()
        self.book_author = self.comboBox_6.currentText()
        self.book_publisher = self.comboBox_7.currentText()

        self.cur.execute('UPDATE book SET '
                         'book_name=(?), book_disc=(?), book_category=(?), book_author=(?), book_pub=(?)'
                         ' WHERE book_code=(?)'
                         , (self.book_name,
                            self.book_disc,
                            self.book_category,
                            self.book_author,
                            self.book_publisher,
                            self.book_id))
        self.db.commit()
        self.db.close()
        self.lineEdit_3.setText('')
        self.lineEdit_6.setText('')
        self.textEdit_2.setPlainText('Discription ...')
        self.comboBox_8.setCurrentIndex(0)
        self.comboBox_7.setCurrentIndex(0)
        self.comboBox_6.setCurrentIndex(0)
        self.statusBar.showMessage("Saved ", msecs=5000)
        self.display_book()
        self.show_book_combo()

    def delete_book(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()
        self.book_id = self.lineEdit_6.text()

        self.cur.execute('DELETE FROM book WHERE book_code=(?)', (self.book_id,))

        self.db.commit()
        self.db.close()
        self.lineEdit_3.setText('')
        self.lineEdit_6.setText('')
        self.textEdit_2.setPlainText('Discription ...')
        self.comboBox_8.setCurrentIndex(0)
        self.comboBox_7.setCurrentIndex(0)
        self.comboBox_6.setCurrentIndex(0)
        self.statusBar.showMessage("Book Deleted ", msecs=5000)
        self.display_book()
        self.show_book_combo()

    def display_book(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()

        self.cur.execute('SELECT book_code,book_name,book_category,book_author,book_pub,book_price from book')
        self.data = self.cur.fetchall()
        if self.data:
            self.tableWidget_6.setRowCount(0)
            self.tableWidget_6.insertRow(0)
            for row, form in enumerate(self.data):
                for column, item in enumerate(form):
                    self.tableWidget_6.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_post = self.tableWidget_6.rowCount()
                self.tableWidget_6.insertRow(row_post)
