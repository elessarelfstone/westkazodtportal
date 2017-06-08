import os.path
import math
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

import storage_manager_ui as smui
import pg_db_common


class StorageManagerUI(smui.Ui_StorageManager):

    def __init__(self):
        super(StorageManagerUI, self).__init__()
        self.ui = smui.Ui_StorageManager()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.class_name = self.__class__.__name__


class StorageManagerMdi(QtWidgets.QMdiSubWindow):
    windowCount = 0
    maxCount = 1

    def __init__(self):
        super(StorageManagerMdi, self).__init__()
        self.widget = StorageManagerUI()
        self._build_abn_branch()
        # item = QtWidgets.QTreeWidgetItem(self.widget.ui.treeWidget)
        # item.setText(0, "Данные по абонентам")
        self.setWidget(self.widget)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.class_name = self.__class__.__name__

    def __del__(self):
        StorageManagerMdi.windowCount -= 1

    # TODO: пепеписать эту функцию так чтобы она на вход получала готовое дерево(граф)

    def _build_abn_branch(self):
        db_sett = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\migration\\database.ini'
        pg = pg_db_common.StorageApi(db_sett, ["postgres"])
        tree_items = pg.get_abn_tree()
        parent = self.widget.ui.treeWidget
        tree_item = parent
        parents_tree = list()
        parents_tree.append((tree_item, -1))
        for item in tree_items:
            if item['level'] > parents_tree[len(parents_tree)-1][1]:
                parents_tree.append((tree_item, item['level']))
            elif item['level'] == parents_tree[len(parents_tree)-1][1]:
                parents_tree.pop(len(parents_tree)-1)
            tree_item = QtWidgets.QTreeWidgetItem(parents_tree[len(parents_tree) - 1][0], [item['branch'], item['code']])





            # if math.fabs(parents_tree[len(parents_tree)-1][1] - item['level']) > 1:
            #     parents_tree.append((tree_item, item['level']))
            #     tree_item = QtWidgets.QTreeWidgetItem(tree_item, [item['branch'], item['code']])
            # else:
            #     tree_item = QtWidgets.QTreeWidgetItem(parents_tree[len(parents_tree)-1][0], [item['branch'], item['code']])
            #     if item['level'] == 0:
            #         parents_tree.append((tree_item, item['level']))
            # if item['level'] == 0:
            #     last_root = QtWidgets.QTreeWidgetItem(tree, [item['branch'], item['code']])
            # else
            #     tr_item = QtWidgets.QTreeWidgetItem(last_root, [item['branch'], item['code']])

