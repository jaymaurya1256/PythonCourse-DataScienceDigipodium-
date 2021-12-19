from PyQt5 import QtWidgets, uic            # Loading the packages
import sys
from db_ex1 import Contact
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class UI(QtWidgets.QMainWindow):            # Custom class UI extends QMainWindow 
    def __init__(self):                     # A no argument Constructor
        super(UI,self).__init__()           # required code to super class
        uic.loadUi("database/app.ui",self)  # Load the UI designed from address
        self.show()                         # if successfull , show the UI
        self.btn.clicked.connect(self.saveContact)
    
    def openDb(self):                                  # openDB function
        engine = create_engine("sqlite:///ex.sqlite3") # Load the database
        Session = sessionmaker(bind=engine)
        return Session()

    def saveContact(self):
        # 1.Taking values from UI
        name = self.editName.text()
        age = self.editAge.text()
        contact = self.editContact.text()
        # 2.Save the valuesto the database                      
        db = self.openDb()
        c = Contact(name = name, age = age , contact = contact)
        db.add(c)
        db.commit()  # save
        db.close()
        # 3.show success
        self.statusMessage.setText("Contact Saved")
        self.statusMessage.setStyleSheet("background-color: rgb(100,200,0);")
        # 4.clear text fields
        self.editName.setText("")
        self.editAge.setText("")
        self.editContact.setText("")

app = QtWidgets.QApplication(sys.argv)      # Code to Activate the Application
window = UI()                               # a new boject of UI class we created above
app.exec_()                                 # creat an infinite loop, so you can see the app window unit
