__author__ = 'SolPie'
from cssQWidget import  CssQBase
from PyQt4 import QtGui
import const


class DirTree(CssQBase):
    def __init__(self, parent):
        super(DirTree, self).__init__(QtGui.QWidget, parent, const.CSS_WIDGET_DIR_TREE)
        self.resize(150, 400)

        self.dir_list = list()

    def addDir(self, str_dir):
        l = QtGui.QLabel(str_dir)
        l.setObjectName(const.CSS_LABEL_DIR_TREE_LABEL)
        l.resize(140, 21)
        self.addWidget(l)
        num = len(self.dir_list)
        l.move(5, num * 25 + 5)


