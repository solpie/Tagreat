__author__ = 'SolPie'
from cssQWidget import CssQBase
import const
from PyQt4 import QtGui,QtCore


class DirNode(CssQBase):
    def __init__(self, parent, text):
        super(DirNode, self).__init__(QtGui.QPushButton, parent, const.CSS_BUTTON_DIR_TREE_NODE)
        self.label = QtGui.QLabel(self.base)
        self.label.setObjectName(const.CSS_LABEL_DIR_TREE_LABEL)
        self.label.setText(text)
        self.base.setFocusPolicy(QtCore.Qt.NoFocus)

