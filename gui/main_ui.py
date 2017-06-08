
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainForm(QtWidgets.QMainWindow):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(816, 625)
        self.centralwidget = QtWidgets.QWidget(MainForm)
        self.centralwidget.setObjectName("centralwidget")
        MainForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 18))
        self.menubar.setObjectName("menubar")
        self.actAllActions = QtWidgets.QMenu(self.menubar)
        self.actAllActions.setObjectName("actAllActions")
        MainForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainForm)
        self.statusbar.setObjectName("statusbar")
        MainForm.setStatusBar(self.statusbar)
        self.actStorageManager = QtWidgets.QAction(MainForm)
        self.actStorageManager.setObjectName("actStorageManager")
        self.actAllActions.addAction(self.actStorageManager)
        self.menubar.addAction(self.actAllActions.menuAction())
        # self.toolbar = self.addToolBar("File")
        # self.toolbar.addAction(self.actStorageManager)
        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Консоль системы отчетности"))
        self.actAllActions.setTitle(_translate("MainForm", "Действия"))
        self.actStorageManager.setText(_translate("MainForm", "Менеджер хранилища"))

