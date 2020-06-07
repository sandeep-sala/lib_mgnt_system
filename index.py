"""Library Management System Created by Sandeep-Sala"""
import socket
from Books import *
from users import *
from Stud import *
from daily import *
from xlrd import *
from xlsxwriter import *
from PyQt5.uic import loadUiType

ui, _ = loadUiType('main.ui')
login, _ = loadUiType('login.ui')


class Login(QWidget, login):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.createdb()
        self.handle_buttn()
        self.groupBox_2.hide()

    def handle_buttn(self):
        self.pushButton_4.clicked.connect(self.signup_user)
        self.pushButton.clicked.connect(self.login_user)
        self.pushButton_2.clicked.connect(self.handle_signup)
        
        
    def createdb(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS users(user_email TEXT NOT NULL,user_name TEXT NOT NULL,user_password TEXT NOT NULL,user_number TEXT NOT NULL)')
        self.cur.execute('CREATE TABLE IF NOT EXISTS student(rollno TEXT NOT NULL UNIQUE,name TEXT NOT NULL,address TEXT NOT NULL,num TEXT NOT NULL)')
        self.cur.execute('CREATE TABLE IF NOT EXISTS category(cat_name TEXT NOT NULL UNIQUE)')
        self.cur.execute('CREATE TABLE IF NOT EXISTS Authors(author_name TEXT NOT NULL UNIQUE)')
        self.cur.execute('CREATE TABLE IF NOT EXISTS publisher(pub_name TEXT NOT NULL UNIQUE)')
        self.cur.execute('CREATE TABLE IF NOT EXISTS openn(name TEXT NOT NULL ,student TEXT NOT NULL,type TEXT NOT NULL,fro TEXT NOT NULL,tom TEXT NOT NULL)')
        self.cur.execute('CREATE TABLE IF NOT EXISTS book(book_name TEXT NOT NULL,book_disc TEXT NOT NULL,book_code TEXT NOT NULL,book_category TEXT NOT NULL,book_author TEXT NOT NULL,book_pub TEXT NOT NULL,book_price TEXT NOT NULL)')
        self.db.commit()
        self.db.close()

    def handle_signup(self):
        self.groupBox.hide()
        self.groupBox_2.show()

    def login_user(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()
        self.username = self.lineEdit.text()
        self.password = self.lineEdit_2.text()
        self.cur.execute('SELECT * from users WHERE user_name=(?) AND user_password=(?)',
                         (self.username, self.password))
        self.data = self.cur.fetchone()
        self.db.close()

        if self.data:
            self.label_2.setText("Login Successful")
            self.window2 = MainApp()
            self.close()
            self.window2.show()
        else:
            self.label_2.setText("Invalid UserName And Password")

    def signup_user(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()
        self.email = self.lineEdit_11.text()
        self.username = self.lineEdit_12.text()
        self.password = self.lineEdit_13.text()
        self.vpassword = self.lineEdit_14.text()
        self.number = self.lineEdit_15.text()
        if self.password != self.vpassword:
            self.label_10.setText("Password doesn't match")
        else:
            self.cur.execute('INSERT INTO users (user_email, user_name, user_password, user_number) '
                             'VALUES (?,?,?,?)', (self.email, self.username, self.password, self.number))
            self.db.commit()
            self.db.close()
            self.label_10.setText("New Account Created")
            self.groupBox_2.hide()
            self.groupBox.show()


class MainApp(QMainWindow, SetIng, BoOk, User, Stud, Daily, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.ip()
        self.statusBar.showMessage('Welcome', msecs=5000)
        self.handle_buttons()
        self.show_category()
        self.show_author()
        self.show_publisher()
        self.show_cat_combo()
        self.show_aut_combo()
        self.show_pu_combo()
        self.show_book_combo()
        self.show_student_combo()
        self.display_stud()
        self.display_user()
        self.display_work()
        self.display_book()

    def ip(self):
        self.hostname = socket.gethostname()
        self.IPAddr = socket.gethostbyname(self.hostname)
        self.label_14.setText(self.hostname)
        self.label_16.setText(self.IPAddr)

    def handle_buttons(self):
        self.pushButton_2.clicked.connect(self.add_book)
        self.pushButton_7.clicked.connect(self.add_category)
        self.pushButton_10.clicked.connect(self.add_author)
        self.pushButton_11.clicked.connect(self.add_publisher)
        self.pushButton_3.clicked.connect(self.search_book)
        self.pushButton_5.clicked.connect(self.edit_save_book)
        self.pushButton_4.clicked.connect(self.delete_book)
        self.pushButton_6.clicked.connect(self.add_user)
        self.pushButton_9.clicked.connect(self.login_user)
        self.pushButton_8.clicked.connect(self.edit_user)
        self.pushButton_12.clicked.connect(self.add_new_stud)
        self.pushButton_16.clicked.connect(self.stud_search)
        self.pushButton_13.clicked.connect(self.stud_save)
        self.pushButton_14.clicked.connect(self.stud_del)
        self.pushButton_15.clicked.connect(self.delete_user)
        self.pushButton.clicked.connect(self.daily_work)
        self.pushButton_17.clicked.connect(self.operation_day)
        self.pushButton_18.clicked.connect(self.operation_book)
        self.pushButton_19.clicked.connect(self.operation_student)

    def operation_day(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()

        self.cur.execute('SELECT name,student,type,fro,tom from openn')
        self.data = self.cur.fetchall()
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()
        self.cur.execute('SELECT name,student,type,fro,tom from openn')
        self.data = self.cur.fetchall()

        wb = Workbook("Day.xlsx")
        s = wb.add_worksheet()
        s.write(0, 0, 'Book Name')
        s.write(0, 1, 'Student Name')
        s.write(0, 2, 'Type')
        s.write(0, 3, 'From')
        s.write(0, 4, 'To')

        r_num = 1
        for row in self.data:
            c_num = 0
            for item in row:
                s.write(r_num, c_num, str(item))
                c_num += 1
            r_num += 1

        wb.close()
        self.statusBar.showMessage("Report Generated ", msecs=5000)

    def operation_student(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()

        self.cur.execute('SELECT rollno,name,address,num from student')
        self.data = self.cur.fetchall()
        wb = Workbook("Student.xlsx")
        s = wb.add_worksheet()
        s.write(0, 0, 'Roll no')
        s.write(0, 1, 'Name')
        s.write(0, 2, 'Address')
        s.write(0, 3, 'Number')

        r_num = 1
        for row in self.data:
            c_num = 0
            for item in row:
                s.write(r_num, c_num, str(item))
                c_num += 1
            r_num += 1

        wb.close()
        self.statusBar.showMessage("Report Generated ", msecs=5000)

    def operation_book(self):
        self.db = sqlite3.connect('lib.db')
        self.cur = self.db.cursor()

        self.cur.execute('SELECT book_code,book_name,book_category,book_author,book_pub,book_price from book')
        self.data = self.cur.fetchall()
        wb = Workbook("Book.xlsx")
        s = wb.add_worksheet()
        s.write(0, 0, 'Book Code')
        s.write(0, 1, 'Book Name')
        s.write(0, 2, 'Category')
        s.write(0, 3, 'Author')
        s.write(0, 4, 'Publication')
        s.write(0, 5, 'Price')

        r_num = 1
        for row in self.data:
            c_num = 0
            for item in row:
                s.write(r_num, c_num, str(item))
                c_num += 1
            r_num += 1

        wb.close()
        self.statusBar.showMessage("Report Generated ", msecs=5000)


def main():
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
