import sys

# Импортируем наш интерфейс из файла
from main import *
from storage_manager import *
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = MainUi()
        self.ui.setupUi(self)
        self.mdiArea = QtWidgets.QMdiArea()
        self.mdiArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.mdiArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setCentralWidget(self.mdiArea)
        self.ui.actStorageManager.triggered.connect(lambda: self.new_window(self.show_storage_manager()))
        self.create_toolbars()

    def new_window(self, window):
            if window not in self.mdiArea.subWindowList():
                self.mdiArea.addSubWindow(window)
                window.setGeometry(0, 0, round(self.mdiArea.width() / 2) + 100, round(self.mdiArea.height() / 2) + 100)
            window.show()

    def show_storage_manager(self):
        if StorageManagerMdi.windowCount + 1 > StorageManagerMdi.maxCount:
            windlst = self.mdiArea.subWindowList()
            for window in windlst:
                if window.class_name == "StorageManagerMdi":
                    res = window
        else:
            res = StorageManagerMdi()
            # item = QtWidgets.QTreeWidgetItem(res.treeWidget)
            StorageManagerMdi.windowCount += 1
        return res

    def create_toolbars(self):
        self.toolbar = self.addToolBar("File")
        self.toolbar.addAction(self.ui.actStorageManager)

    def active_mdi_child(self):
        active_sub_window = self.mdiArea.activeSubWindow()
        if active_sub_window:
            return active_sub_window.widget()
        return None

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.showMaximized()
    sys.exit(app.exec_())