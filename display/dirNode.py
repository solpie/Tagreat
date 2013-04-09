# -*- coding: utf-8 -*-
__author__ = 'SolPie'
from cssQWidget import CssQBase
import const
from PyQt4 import QtGui, QtCore


class DirNode(CssQBase):
    def __init__(self, parent, text):
        super(DirNode, self).__init__(QtGui.QPushButton, parent, const.CSS_BUTTON_DIR_TREE_NODE)
        self.base.setFocusPolicy(QtCore.Qt.NoFocus)#去除虚线框

        self.label = QtGui.QLabel(self.base)
        self.label.setObjectName(const.CSS_LABEL_DIR_TREE_LABEL)
        self.label.setText(text)
        self.label.move(5, 5)
        self.resize(140, 25)

