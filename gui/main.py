
import main_ui
import pg_db_common
from PyQt5.QtCore import Qt


class MainUi(main_ui.Ui_MainForm):
    def __init__(self):
        super(MainUi, self).__init__()
        self.ui = main_ui.Ui_MainForm()
        self.ui.setupUi(self)
        # self.ui.toolbar = self.ui.addToolBar("File")
        # self.ui.toolbar.addAction(self.ui.actStorageManager)
        self.setAttribute(Qt.WA_DeleteOnClose)