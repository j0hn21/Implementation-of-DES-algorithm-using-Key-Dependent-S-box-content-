import sys
from PyQt5 import  QtGui,QtCore,QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import  QApplication,QMainWindow,QPushButton,QAction,QMessageBox,QCheckBox,QComboBox,QLineEdit , QPlainTextEdit
from PyQt5.uic import loadUi
import DESthon as des
import time

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        loadUi('DESAPP.ui', self)  ## load file .ui
        self.setWindowTitle("DES APP")  ## set the tile

        # slot :
        self.generateBtn.clicked.connect(self.on_generateBtn_clicked)

        self.encryptBtn.clicked.connect(self.on_encryptBtn_clicked)

        self.decryptBtn.clicked.connect(self.on_decryptBtn_clicked)

    def on_generateBtn_clicked(self):
        Key_str = des.Generate_Key_64()
        self.keyLine.setText(Key_str)
        self.keyLine2.setText(Key_str)
    def on_encryptBtn_clicked(self):
        Key_str = self.keyLine.text()
        if(len(Key_str)>8):
            print("Use 64 bit key")
            exit(0)
        Key_str = des.PaddString(Key_str)
        start_time = time.time()
        Ciphertext = des.DES_Encrypt(self.plaintextLine.text(),Key_str)
        end_time = time.time()
        self.encryptedLine.setText(Ciphertext)
        self.ciphertextLine.setText(Ciphertext)
        print("Time taken to encrypt message:", end_time - start_time, "seconds")

    def on_decryptBtn_clicked(self):
        Key_str  = self.keyLine2.text()
        if(len(Key_str)>8):
            print("Use 64 bit key")
            exit(0)
        Key_str = des.PaddString(Key_str)
        start_time = time.time()
        Plaintext = des.DES_Decrypt(self.ciphertextLine.text(),Key_str)
        end_time = time.time()
        print("Time taken to decrypt message:", end_time - start_time, "seconds")
        self.plaintextLine2.setText(Plaintext)


app = QApplication(sys.argv)
GUI = Window()
GUI.show()
sys.exit(app.exec_())