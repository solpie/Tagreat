__author__ = 'SolPie'
from cssQWidget import CssQWidget
import const
from PyQt4 import QtGui


class DirNode(CssQWidget):
    def __init__(self, parent):
        super(DirNode, self).__init__(parent, const.CSS_WIDGET_DIR_TREE)
        self.b = QtGui.QPushButton()
        self.addWidget(self.b)

