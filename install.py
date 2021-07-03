from PyQt5.QtWidgets import QWidget,QPushButton,QVBoxLayout,QLabel,QLineEdit
from login import LoginScreen
import json
from database import DBOperation

class InstallWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Install Covid-19 Vaccine System")
        self.resize(400,200)

        layout=QVBoxLayout()

        label_db_name=QLabel("Database Name : ")
        label_db_name.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
        
        label_db_username=QLabel("Database Username : ")
        label_db_username.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
        
        label_db_password=QLabel("Database Password : ")
        label_db_password.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
        
        label_admin_username=QLabel("Admin Username : ")
        label_admin_username.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
        
        label_admin_password=QLabel("Admin Password : ")
        label_admin_password.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
        
        label_no_of_covishield=QLabel("No of Covishield Vaccine Slots : ")
        label_no_of_covishield.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
        
        label_no_of_covaxin=QLabel("No. of Covaxin Vaacine Slots: ")
        label_no_of_covaxin.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")

        
        self.input_db_name=QLineEdit()
        self.input_db_name.setText("vaccination")
        self.input_db_name.setStyleSheet("padding:5px;font-size:17px")

        self.input_db_username=QLineEdit()
        self.input_db_username.setText("vaccine_user")
        self.input_db_username.setStyleSheet("padding:5px;font-size:17px")

        self.input_db_password=QLineEdit()
        self.input_db_password.setText("vaccine_password")
        self.input_db_password.setStyleSheet("padding:5px;font-size:17px")

        self.input_admin_username=QLineEdit()
        self.input_admin_username.setStyleSheet("padding:5px;font-size:17px")
        
        self.input_admin_password=QLineEdit()
        self.input_admin_password.setStyleSheet("padding:5px;font-size:17px")
        
        self.input_no_of_covishield=QLineEdit()
        self.input_no_of_covishield.setStyleSheet("padding:5px;font-size:17px")
        
        self.input_no_of_covaxin=QLineEdit()
        self.input_no_of_covaxin.setStyleSheet("padding:5px;font-size:17px")

        buttonsave=QPushButton("save config")
        buttonsave.setStyleSheet("padding:5px;font-size:17px;background:green;color:#fff")

        self.error_label=QLabel()
        self.error_label.setStyleSheet("color:red")

        layout.addWidget(label_db_name)
        layout.addWidget(self.input_db_name)

        layout.addWidget(label_db_username)
        layout.addWidget(self.input_db_username)
        
        layout.addWidget(label_db_password)
        layout.addWidget(self.input_db_password)
        
        layout.addWidget(label_admin_username)
        layout.addWidget(self.input_admin_username)
        
        layout.addWidget(label_admin_password)
        layout.addWidget(self.input_admin_password)
        
        layout.addWidget(label_no_of_covishield)
        layout.addWidget(self.input_no_of_covishield)
        
        layout.addWidget(label_no_of_covaxin)
        layout.addWidget(self.input_no_of_covaxin)
        
        layout.addWidget(buttonsave)
        layout.addWidget(self.error_label)

        buttonsave.clicked.connect(self.showStepInfo)

        self.setLayout(layout)

    def showStepInfo(self):
        if self.input_db_name.text()=="":
            self.error_label.setText("Please Enter DB Name")
            return

        if self.input_db_username.text()=="":
            self.error_label.setText("Please Enter DB Username")
            return

        if self.input_db_password.text()=="":
            self.error_label.setText("Please Enter DB Password")
            return

        if self.input_admin_username.text()=="":
            self.error_label.setText("Please Enter Admin Username")
            return

        if self.input_admin_password.text()=="":
            self.error_label.setText("Please Enter Admin Password")
            return

        if self.input_no_of_covishield.text()=="":
            self.error_label.setText("Please Enter Covishield Space")
            return

        if self.input_no_of_covaxin.text()=="":
            self.error_label.setText("Please Enter Covaxin Space")
            return


        data={"username":self.input_db_username.text(),"database":self.input_db_name.text(),"password":self.input_db_password.text()}
        file=open("./config.json","w")
        file.write(json.dumps(data))
        file.close()
        dbOperation=DBOperation()
        dbOperation.CreateTables()
        dbOperation.InsertAdmin(self.input_admin_username.text(),self.input_admin_password.text())
        dbOperation.InsertOneTimeData(int(self.input_no_of_covishield.text()),int(self.input_no_of_covaxin.text()))

        self.close()
        self.login=LoginScreen()
        self.login.showLoginScreen()
        print("Save")


