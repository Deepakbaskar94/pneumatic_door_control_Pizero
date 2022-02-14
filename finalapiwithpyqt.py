from PyQt6 import QtCore, QtWidgets
import requests
import socket
import webbrowser



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")    #Set object name
        MainWindow.resize(368, 227)               #Setting size for mainwindow
        MainWindow.setStyleSheet('color:blue')
        #MainWindow.setStyleSheet("background-color: cyan;")     #To change bg colour

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget) #Creating pushbutton widget
        self.pushButton.setGeometry(QtCore.QRect(155, 40, 81, 21)) #Setting size for button
        self.pushButton.setObjectName("pushButton")                 #Set objectname as pushbutton
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)     #Creating combobox widget
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QtCore.QRect(20, 40, 130, 22))    #Setting size for combobox


        # list1 = [
        # ('First Item'),
        # ('Second Item'),
        # ('Third Item'),
        # ]
        
        # list1 = [
        # '192.168.1.2',
        # '192.168.159.159',
        # '192.168.220.159',
        # ]
        
        
        #self.comboBox.addItem("safaf")                                   #Add items to combobox
        #self.comboBox.addItem("aasfa")
        #self.comboBox.addItem("asfsa")

        self.comboBox.clear()
        # list2 = list0
        # self.comboBox.addItems(list2)
        self.comboBox.addItems(list0)
        
        # item = self.comboBox.currentText()
        # print(item)

        self.pushButton.clicked.connect(self.btn_clicked)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        
        

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Find Turntable"))         #Set title for mainwindow
        self.pushButton.setText(_translate("MainWindow", "Connect"))           #Set text in pushbutton
    
    
    def btn_clicked(self):
        inputText =  self.comboBox.currentText()
        print(inputText)
        webbrowser.open("http://" +inputText +port)   
        
        
        
global list0
port = ":3000"
port1 = 3000
#port = ":80"
#port1 = 80
api = "/find"
list0 = []

#host_name = socket.gethostname()
#net = socket.gethostbyname(host_name)
net = "192.168.5.1"
print("my ip is: " + net)

net1 = net.split('.')
print(net1)
a = '.'

net2 = net1[0] + a + net1[1] + a + net1[2] + a

st1 = 0
en1 = 10
en1 = en1 + 1
#t1 = datetime.now()

def scan(addr):
   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   print(addr)
   socket.setdefaulttimeout(1)
   result = s.connect_ex((addr,port1))
   if result == 0:
      return 1
   else :
      return 0

def run1():
   for ip in range(st1,en1):
      addr = net2 + str(ip)
      if (scan(addr)):
        print (addr , "is live")
        response = requests.get("http://" +addr +port +api)
        #value = print(response.text)
        value = response.text
        print(value)
        if value == "door":
            list0.append(addr)
            print(list0)
            print("success")
            print("http://" +addr +port)
            #webbrowser.open("http://" +addr +port)
        else:
            print("someother ip")
         
         
run1()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec())