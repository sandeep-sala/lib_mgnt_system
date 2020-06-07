"""Student Created by Sandeep-Sala"""
import sqlite3
from PyQt5.QtWidgets import *
from settings import *


class Stud:

    def add_new_stud(self):
        self.s_name = self.lineEdit_16.text()
        self.s_id = self.lineEdit_25.text()
        self.s_num = self.lineEdit_29.text()
        self.s_add = self.lineEdit_17.text()

        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()
        self.cur.execute('INSERT INTO student (rollno, name, address, num) '
                         'VALUES (?,?,?,?)', (self.s_id, self.s_name, self.s_add, self.s_num))
        self.db.commit()
        self.db.close()
        self.statusBar.showMessage("New Student Created", msecs=3000)
        self.lineEdit_16.setText('')
        self.lineEdit_25.setText('')
        self.lineEdit_29.setText('')
        self.lineEdit_17.setText('')
        self.display_stud()
        self.show_student_combo()

    def stud_search(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()
        self.search_id = self.lineEdit_26.text()
        self.cur.execute('SELECT * from student WHERE rollno=(?)', (self.search_id,))
        self.data = self.cur.fetchone()
        self.db.close()
        if self.data:
            self.groupBox_5.setEnabled(True)
            self.lineEdit_28.setText(self.data[1])
            self.lineEdit_27.setText(self.data[2])
            self.lineEdit_31.setText(self.data[3])
            self.lineEdit_30.setText(str(self.data[4]))

        else:
            self.statusBar.showMessage("Invalid Search Id", msecs=3000)

    def stud_save(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()
        self.search_id = self.lineEdit_26.text()
        self.ss_name = self.lineEdit_27.text()
        self.ss_id = self.lineEdit_28.text()
        self.ss_num = self.lineEdit_30.text()
        self.ss_add = self.lineEdit_31.text()

        self.cur.execute('UPDATE student SET name=(?),address=(?),num=(?),rollno=(?)  WHERE rollno=(?)'
                         , (self.ss_name, self.ss_add, self.ss_num, self.ss_id, self.search_id))
        self.db.commit()
        self.db.close()
        self.statusBar.showMessage("Student Data Saved", msecs=3000)
        self.lineEdit_27.setText('')
        self.lineEdit_28.setText('')
        self.lineEdit_30.setText('')
        self.lineEdit_31.setText('')
        self.groupBox_5.setEnabled(False)
        self.display_stud()
        self.show_student_combo()

    def stud_del(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()
        self.search_id = self.lineEdit_26.text()
        self.cur.execute('DELETE FROM student WHERE rollno=(?)', (self.search_id,))
        self.db.commit()
        self.db.close()
        self.statusBar.showMessage("Student Deleted", msecs=3000)
        self.lineEdit_26.setText('')
        self.lineEdit_27.setText('')
        self.lineEdit_28.setText('')
        self.lineEdit_30.setText('')
        self.lineEdit_31.setText('')
        self.groupBox_5.setEnabled(False)
        self.display_stud()
        self.show_student_combo()

    def display_stud(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()

        self.cur.execute('SELECT rollno,name,address,num from student')
        self.data = self.cur.fetchall()
        if self.data:
            self.tableWidget_5.setRowCount(0)
            self.tableWidget_5.insertRow(0)
            for row, form in enumerate(self.data):
                for column, item in enumerate(form):
                    self.tableWidget_5.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_post = self.tableWidget_5.rowCount()
                self.tableWidget_5.insertRow(row_post)
