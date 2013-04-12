# -*- coding: utf-8 -*-
__author__ = 'SolPie'
from PyQt4 import QtGui, QtCore
from const import trans
from cssQWidget import CssQBase
import const


class TagNode(CssQBase):
    def __init__(self, parent, title):
        super(TagNode, self).__init__(QtGui.QWidget, parent, const.CSS_WIDGET_ENTITY)
        self.label = QtGui.QLabel()
        self.label.setObjectName(const.CSS_LABEL_TAG_NODE)
        self.label.move(4, 4)
        self.addWidget(self.label)
        if title:
            self.setTitle(title)

    def update(self, filename):
        self.setTitle(filename)
        self.show()

    def setTitle(self, title):
        self.label.setText(title)

    def free(self):
        self.hide()
        # self.icon = QtGui.QPixmap(self)
        # self.icon.load('tmp/icon.png')