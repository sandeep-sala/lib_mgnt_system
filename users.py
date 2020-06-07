"""Users Created by Sandeep-Sala"""
import sqlite3
from PyQt5.QtWidgets import *


class User:

    def add_user(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()
        self.email = self.lineEdit_11.text()
        self.username = self.lineEdit_8.text()
        self.password = self.lineEdit_9.text()
        self.vpassword = self.lineEdit_10.text()
        self.number = self.lineEdit_12.text()
        if self.password != self.vpassword:
            self.statusBar.showMessage("Password doesn't match", msecs=3000)
        else:
            self.cur.execute('INSERT INTO users (user_email, user_name, user_password, user_number) '
                             'VALUES (?,?,?,?)', (self.email, self.username, self.password, self.number))
            self.db.commit()
            self.db.close()
            self.statusBar.showMessage("New User Created", msecs=3000)

        self.lineEdit_11.setText('')
        self.lineEdit_8.setText('')
        self.lineEdit_9.setText('')
        self.lineEdit_10.setText('')
        self.lineEdit_12.setText('')
        self.display_user()

    def login_user(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()
        self.username = self.lineEdit_23.text()
        self.password = self.lineEdit_24.text()
        self.cur.execute('SELECT * from users WHERE user_name=(?) AND user_password=(?)',
                         (self.username, self.password))
        self.data = self.cur.fetchone()
        self.db.close()
        self.lineEdit_24.setText('')
        if self.data:
            self.groupBox_3.setEnabled(True)
            self.lineEdit_21.setText(self.data[1])
            self.lineEdit_18.setText(self.data[2])
            self.lineEdit_19.setText(self.data[3])
            self.lineEdit_22.setText(str(self.data[4]))

        else:
            self.statusBar.showMessage("Invalid UserName And Password", msecs=3000)

    def edit_user(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()
        self.emai = self.lineEdit_21.text()
        self.usernam = self.lineEdit_18.text()
        self.passw = self.lineEdit_19.text()
        self.passwf = self.lineEdit_20.text()
        self.phon = self.lineEdit_22.text()

        if self.passw != self.passwf:
            self.statusBar.showMessage("Password doesn't match", msecs=3000)
        else:
            self.cur.execute('UPDATE users SET user_email=(?),user_name=(?),user_password=(?) '
                             ' WHERE user_email=(?)'
                             , (self.emai, self.usernam, self.passw, self.emai))
            self.db.commit()
            self.db.close()
            self.statusBar.showMessage("User data Saved", msecs=3000)
            self.lineEdit_21.setText('')
            self.lineEdit_18.setText('')
            self.lineEdit_19.setText('')
            self.lineEdit_20.setText('')
            self.lineEdit_22.setText('')
            self.groupBox_3.setEnabled(False)
            self.display_user()

    def delete_user(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()
        self.search_id = self.lineEdit_23.text()
        self.cur.execute('DELETE FROM users WHERE user_name=(?)', (self.search_id,))
        self.db.commit()
        self.db.close()
        self.statusBar.showMessage("User Deleted", msecs=3000)
        self.lineEdit_21.setText('')
        self.lineEdit_18.setText('')
        self.lineEdit_19.setText('')
        self.lineEdit_20.setText('')
        self.lineEdit_22.setText('')
        self.groupBox_3.setEnabled(False)
        self.lineEdit_23.setText('')
        self.display_user()

    def display_user(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()

        self.cur.execute('SELECT user_email,user_name from users')
        self.data = self.cur.fetchall()
        if self.data:
            self.tableWidget_7.setRowCount(0)
            self.tableWidget_7.insertRow(0)
            for row, form in enumerate(self.data):
                for column, item in enumerate(form):
                    self.tableWidget_7.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_post = self.tableWidget_7.rowCount()
                self.tableWidget_7.insertRow(row_post)
