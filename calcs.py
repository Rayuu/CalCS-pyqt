from __future__ import division
import sys
from PyQt4 import QtCore, QtGui,uic

from uicode import *
# qtCreatorFile = "calc.ui" # Enter file here.
# Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

# class MyApp(QtGui.QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         QtGui.QMainWindow.__init__(self)
#         Ui_MainWindow.__init__(self)
#         self.setupUi(self)
#         self.calc_button.clicked.connect(self.CalculateTax)
#
#     def CalculateTax(self):
#         content = str(self.content_box.toPlainText())
#         total = self.CalCS(content)
#         total_string = "" + str(total)
#         self.results_window.setText(total_string)
#
#     def CalCS(self,inputstr):
#         input = inputstr.replace(" ", "")
#         content = []
#         for i in range(0, len(input), 2):
#             content.append(input[i:i + 2])
#         # print content
#         int_list = [int(i, 16) for i in content]
#         # print int_list
#         num = 0
#         for i in range(0, len(int_list)):
#             num = num + int(int_list[i])
#         return hex(num % 256)

class MyApp(QtGui.QMainWindow):

    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.calc_button.clicked.connect(self.CalculateTax)

    def CalculateTax(self):
        content = str(self.ui.content_box.toPlainText())
        total = self.CalCS(content)
        total_string = "" + str(total)
        self.ui.results_window.setText(total_string)

    def CalCS(self,inputstr):
        input = inputstr.replace(" ", "")
        content = []
        for i in range(0, len(input), 2):
            content.append(input[i:i + 2])
        # print content
        int_list = [int(i, 16) for i in content]
        # print int_list
        num = 0
        for i in range(0, len(int_list)):
            num = num + int(int_list[i])
        return hex(num % 256)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())