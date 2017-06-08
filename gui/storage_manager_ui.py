# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'storage_manager_ui.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StorageManager(QtWidgets.QWidget):
    def setupUi(self, StorageManager):
        StorageManager.setObjectName("StorageManager")
        StorageManager.resize(902, 688)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StorageManager.sizePolicy().hasHeightForWidth())
        StorageManager.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        StorageManager.setFont(font)
        self.horizontalLayout = QtWidgets.QHBoxLayout(StorageManager)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(StorageManager)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.treeWidget = QtWidgets.QTreeWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setObjectName("treeWidget")
        # item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_2 = QtWidgets.QTreeWidgetItem(item_1)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.frame = QtWidgets.QFrame(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.verticalLayout.addWidget(self.splitter)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(StorageManager)
        QtCore.QMetaObject.connectSlotsByName(StorageManager)

    def retranslateUi(self, StorageManager):
        _translate = QtCore.QCoreApplication.translate
        StorageManager.setWindowTitle(_translate("StorageManager", "Менеджер хранилища"))
        self.treeWidget.headerItem().setText(0, _translate("StorageManager", "Наименование"))
        self.treeWidget.headerItem().setText(1, _translate("StorageManager", "Колонка"))
        # __sortingEnabled = self.treeWidget.isSortingEnabled()
        # self.treeWidget.setSortingEnabled(False)
        # self.treeWidget.topLevelItem(0).setText(0, _translate("StorageManager", "Данные по абоненту"))
        # self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("StorageManager", "Начисления"))
        # self.treeWidget.topLevelItem(0).child(0).child(0).setText(0, _translate("StorageManager", "Начисления за апрель прошлого года"))
        # self.treeWidget.topLevelItem(0).child(0).child(0).setText(1, _translate("StorageManager", "deb_lst_yr_apr"))
        # self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("StorageManager", "Оплаты"))
        # self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("StorageManager", "Услуги"))
        # self.treeWidget.topLevelItem(0).child(3).setText(0, _translate("StorageManager", "Информация об абоненте"))
        # self.treeWidget.topLevelItem(1).setText(0, _translate("StorageManager", "Данные по телефону"))
        # self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("StorageManager", "Начисления "))
        # self.treeWidget.setSortingEnabled(__sortingEnabled)

