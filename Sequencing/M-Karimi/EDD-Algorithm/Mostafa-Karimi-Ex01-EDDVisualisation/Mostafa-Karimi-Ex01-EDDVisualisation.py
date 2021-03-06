# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EDDQT.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1018, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Enter = QtWidgets.QPushButton(self.centralwidget)
        self.Enter.setGeometry(QtCore.QRect(10, 180, 89, 25))
        self.Enter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Enter.setObjectName("Enter")
        self.OK = QtWidgets.QPushButton(self.centralwidget)
        self.OK.setGeometry(QtCore.QRect(40, 330, 89, 25))
        self.OK.setObjectName("OK")
        self.info = QtWidgets.QTabWidget(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(280, 20, 711, 401))
        font = QtGui.QFont()
        font.setFamily("Vazir FD-WOL")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.info.setFont(font)
        self.info.setObjectName("info")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(-5, 11, 711, 351))
        self.textBrowser.setObjectName("textBrowser")
        self.info.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.infoText = QtWidgets.QTextBrowser(self.tab_2)
        self.infoText.setGeometry(QtCore.QRect(-10, -10, 721, 391))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.infoText.setFont(font)
        self.infoText.setObjectName("infoText")
        self.info.addTab(self.tab_2, "")
        self.log_label = QtWidgets.QLabel(self.centralwidget)
        self.log_label.setGeometry(QtCore.QRect(910, 440, 67, 17))
        self.log_label.setObjectName("log_label")
        self.welcome = QtWidgets.QLabel(self.centralwidget)
        self.welcome.setGeometry(QtCore.QRect(50, 70, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Vazir WOL")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.welcome.setFont(font)
        self.welcome.setObjectName("welcome")
        self.n_label = QtWidgets.QLabel(self.centralwidget)
        self.n_label.setGeometry(QtCore.QRect(100, 140, 151, 31))
        self.n_label.setObjectName("n_label")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(150, 260, 111, 20))
        self.time_label.setObjectName("time_label")
        self.dueTime_label = QtWidgets.QLabel(self.centralwidget)
        self.dueTime_label.setGeometry(QtCore.QRect(140, 300, 121, 21))
        self.dueTime_label.setObjectName("dueTime_label")
        self.work_label = QtWidgets.QLabel(self.centralwidget)
        self.work_label.setGeometry(QtCore.QRect(86, 220, 51, 20))
        self.work_label.setObjectName("work_label")
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setGeometry(QtCore.QRect(110, 180, 89, 25))
        self.close.setObjectName("close")
        self.li_input_N = QtWidgets.QLineEdit(self.centralwidget)
        self.li_input_N.setGeometry(QtCore.QRect(20, 140, 81, 31))
        self.li_input_N.setObjectName("li_input_N")
        self.li_dueTime_N = QtWidgets.QLineEdit(self.centralwidget)
        self.li_dueTime_N.setGeometry(QtCore.QRect(40, 290, 81, 31))
        self.li_dueTime_N.setObjectName("li_dueTime_N")
        self.li_time_N = QtWidgets.QLineEdit(self.centralwidget)
        self.li_time_N.setGeometry(QtCore.QRect(40, 250, 81, 31))
        self.li_time_N.setObjectName("li_time_N")
        self.label_nWork = QtWidgets.QLabel(self.centralwidget)
        self.label_nWork.setGeometry(QtCore.QRect(70, 220, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        self.label_nWork.setFont(font)
        self.label_nWork.setText("")
        self.label_nWork.setObjectName("label_nWork")
        self.textBrowser_log = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_log.setGeometry(QtCore.QRect(20, 461, 961, 101))
        self.textBrowser_log.setObjectName("textBrowser_log")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1018, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.info.setCurrentIndex(0)
        self.Enter.clicked.connect(self.giveN)
        self.OK.clicked.connect(self.OK_N)
        self.close.clicked.connect(self.exitFunc)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.textBrowser_log.append("Barname Shoroo Shod! - Mostafa Karimi")

    n_job = 0
    def giveN(self):
        self.n_job = int(self.li_input_N.text())

        _translate = QtCore.QCoreApplication.translate
        

        if type(self.n_job) is str:      #TODO int nadad chikar konim?
            self.welcome.setText(_translate("MainWindow", "حتما باید عددی وارد شود"))
        else:
            self.EDD(self.n_job)
            self.textBrowser_log.append("Adad Karha Dorost Vared Shode Ast.")

    w = 0  
    EDD_A = []    
    

    def EDD(self, n_job):
        
        
        self.Enter.setEnabled(False)
        self.close.setEnabled(True)
        self.li_input_N.setEnabled(False)
        self.textBrowser_log.append("ُTedad {} kar vared shod.".format(self.n_job))

        self.label_nWork.setText(str(self.w+1))
        
        # for i in range(0, n_job):
        #     EDD_Inp = []
        #     # print("\t------- job {} -------".format(i+1))
        #     EDD_Inp.append(int(i+1))
        #     EDD_Inp.append(int(self.li_time_N.text()))
        #     EDD_Inp.append(int(self.li_dueTime_N.text()))
        #     EDD_A.append(EDD_Inp)

    def OK_N(self):
    
        self.textBrowser_log.append("Adade kare {} vared shod.".format(self.w+1))


        # print(self.w, self.n_job)
        EDD_Inp = []
            # print("\t------- job {} -------".format(i+1))
        EDD_Inp.append(int(self.w+1))
        EDD_Inp.append(int(self.li_time_N.text()))
        EDD_Inp.append(int(self.li_dueTime_N.text()))
        self.EDD_A.append(EDD_Inp)
        
        
        self.li_time_N.setText("")
        self.li_dueTime_N.setText("")
        
        self.w+=1
        
        if self.w == self.n_job:
            
            self.OK.setEnabled(False)
            self.calculate_EDD()

        else:
            self.label_nWork.setText(str(self.w+1))

    def calculate_EDD(self):
        # sorting by due time
 
        for k in range(self.n_job):
            for j in range(int(len(self.EDD_A))-1):
                if self.EDD_A[j][2] > self.EDD_A[j+1][2]:
                    self.EDD_A[j], self.EDD_A[j+1] = self.EDD_A[j+1], self.EDD_A[j]

        # calculate Cj
 
        self.EDD_A[0].append(self.EDD_A[0][1])
        self.EDD_A[1].append(self.EDD_A[0][1]+self.EDD_A[1][1])
        
        for i in range(2, len(self.EDD_A)):
            self.EDD_A[i].append(self.EDD_A[i][1]+self.EDD_A[i-1][3])
        
        # calculate Lj
        
        for i in range(len(self.EDD_A)):
            self.EDD_A[i].append(self.EDD_A[i][3]-self.EDD_A[i][2])

        #calculate Tj
        #  
        for i in range(len(self.EDD_A)):
            if self.EDD_A[i][4] > 0:
                self.EDD_A[i].append(self.EDD_A[i][4])
            else:
                self.EDD_A[i].append(0)
        


        self.textBrowser_log.append("Tamam Adad Vared Shodan Va Moshasebat Anjam Mishavad")



        # calculate Avg Tardiness

        t_total = 0
        for i in range(len(self.EDD_A)):
            t_total += self.EDD_A[i][5]
            
        t_avg = t_total / self.n_job
        
        tAvg = "\n\n\t\tAverageTardiness:\t {:.3}".format(t_avg)

        

        # Out Put #1 
        #  
        char = "-"

        mosi = "\n\n{0} Mostafa Karimi - EDD Algorithm - Sequencing {0}".format(8*char)
        # print("\n{0} Result {0}\n".format(char*8)) 

       
        
        putJa = "\n\nSequencing of Job\t t\tdue\t C\t L\t T\n"



        for i in range(len(self.EDD_A)):
            putJa += "\t{:2}\t{:2}\t{:2}\t{:2}\t{:2}\t{:2}\n".format(self.EDD_A[i][0], self.EDD_A[i][1], self.EDD_A[i][2], self.EDD_A[i][3], self.EDD_A[i][4], self.EDD_A[i][5])
        # print(t_avg)

        
        _translate = QtCore.QCoreApplication.translate
        
        self.textBrowser.append(putJa)
        
        self.textBrowser.append(tAvg)

        self.textBrowser.append(mosi)


    def exitFunc(self):
        self.Enter.setEnabled(True)
        self.close.setEnabled(False)
        self.li_input_N.setEnabled(True)  
        self.OK.setEnabled(True)      
        self.w = 0
        self.EDD_A = []
        self.textBrowser_log.append("Barnabe Kharej va Restart Shod")



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Enter.setText(_translate("MainWindow", "تایید"))
        self.OK.setText(_translate("MainWindow", "ورود"))
        self.info.setTabText(self.info.indexOf(self.tab), _translate("MainWindow", "خروجی محاسبات"))
        self.infoText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Vazir FD-WOL\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic; color:#204a87;\"><br /></p>\n"
"<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#204a87;\">برنامه گرافیکی محاسبه تعداد n کار با استفاده از الگوریتم EDD</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic; color:#204a87;\"><br /></span></p>\n"
"<p align=\"center\" dir=\'rtl\' style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#204a87;\">استاد: دکتر ضیایی</span></p>\n"
"<p align=\"center\" dir=\'rtl\' style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#204a87;\">دانشجو: مصطفی کریمی</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#204a87;\"><br /></span></p>\n"
"<p align=\"center\" dir=\'rtl\' style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#204a87;\">نسخه 1.0.1</span></p></body></html>"))
        self.info.setTabText(self.info.indexOf(self.tab_2), _translate("MainWindow", "مشخصات"))
        self.log_label.setText(_translate("MainWindow", "لاگ ها:"))
        self.welcome.setText(_translate("MainWindow", "به برنامه من خوش آمدید"))
        self.n_label.setText(_translate("MainWindow", "تعداد n کار را وارد کنید:"))
        self.time_label.setText(_translate("MainWindow", "زمان انجام کار:"))
        self.dueTime_label.setText(_translate("MainWindow", "موعد تحویل کار:"))
        self.work_label.setText(_translate("MainWindow", "کار "))
        self.close.setText(_translate("MainWindow", "دوباره"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
