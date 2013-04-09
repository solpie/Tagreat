__author__ = 'SolPie'
from cssQWidget import CssQBase
from dirNode import DirNode
from PyQt4 import QtGui
import const


class DirTree(CssQBase):
    def __init__(self, parent):
        super(DirTree, self).__init__(QtGui.QWidget, parent, const.CSS_WIDGET_DIR_TREE)
        self.resize(150, 400)

        self.dir_list = list()

    def addDir(self, str_dir):
        l = DirNode(self.base, str_dir)
        l.resize(140, 21)
        num = len(self.dir_list)
        l.move(5, num * 25 + 5)
        self.dir_list.append(l)


