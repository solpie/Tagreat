# -*- coding: utf-8 -*-
__author__ = 'SolPie'
from cssQWidget import CssQBase
import const
from PyQt4 import QtGui, QtCore


class DirNode(CssQBase):
    is_free = False

    def __init__(self, parent, text):
        super(DirNode, self).__init__(QtGui.QPushButton, parent, const.CSS_BUTTON_DIR_TREE_NODE)
        self.base.setFocusPolicy(QtCore.Qt.NoFocus)#去除虚线框
        self.base.mousePressEvent = self.mousePressEvent

        self.label = QtGui.QLabel(self.base)
        self.label.setObjectName(const.CSS_LABEL_DIR_TREE_LABEL)
        self.label.setText(text)
        self.label.move(5, 5)
        self.resize(parent.width() - 10, 25)

    def mousePressEvent(self, e=None):
        self.onClick(self)

    def onClick(self, base):
        #override me in parent
        pass

    def set_dir(self, str_dir):
        self.label.setText(str_dir)
        self.is_free = False
        # self.base.show()

    def free(self):
        self.is_free = True
        # self.base.hide()

    def getText(self):
        return self.label.text()

