from PyQt5 import QtWidgets, uic            # Loading the packages
import sys

class UI(QtWidgets.QMainWindow):            # Custom class UI extends QMainWindow 
    def __init__(self):                     # A no argument Constructor
        super(UI,self).__init__()           # required code to super class
        uic.loadUi("database/app.ui",self)  # Load the UI designed from address
        self.show()                         # if successfull , show the UI

app = QtWidgets.QApplication(sys.argv)      # Code to Activate the Application
window = UI()                               # a new boject of UI class we created above
app.exec_()                                 #