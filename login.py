from PyQt5.QtWidgets import QWidget,QVBoxLayout,QPushButton,QLabel,QLineEdit,QApplication
import sys
from database import DBOperation
from home import HomeScreen

class LoginScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Login Credentials")
        self.resize(300,100)
        layout=QVBoxLayout()

        label_username=QLabel("Username : ")
        label_username.setStyleSheet("color:black;padding:8px 0px;font-size:18px;")
        self.input_username=QLineEdit()
        self.input_username.setStyleSheet("padding:5px;font-size:17px")
        label_password=QLabel("Password : ")
        label_password.setStyleSheet("color:black;padding:8px 0px;font-size:18px;")
        self.error_msg=QLabel()
        self.error_msg.setStyleSheet("color:red;padding:8px 0px;font-size:18px;text-align:center")
        self.input_password=QLineEdit()
        self.input_password.setStyleSheet("padding:5px;font-size:17px")

        btn_login=QPushButton("Login")
        btn_login.setStyleSheet("padding:5px;font-size:20px;background:blue;color:#fff")
        layout.addWidget(label_username)
        layout.addWidget(self.input_username)
        layout.addWidget(label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(btn_login)
        layout.addWidget(self.error_msg)
        layout.addStretch()
        btn_login.clicked.connect(self.showHome)
        self.setLayout(layout)

    def showLoginScreen(self):
        self.show()

    def showHome(self):
        if self.input_username.text()=="":
            self.error_msg.setText("Please Enter the Username")
            return

        if self.input_password.text()=="":
            self.error_msg.setText("Please Enter the Password")
            return
        dboperation=DBOperation()
        result=dboperation.doAdminLogin(self.input_username.text(),self.input_password.text())
        if result:
            self.error_msg.setText("Login Successful")
            self.close()
            self.home = HomeScreen()
            self.home.show()
        else:
            self.error_msg.setText("Invalid Credentials !!!")
            #self.error_msg.setText("Please Check Details")