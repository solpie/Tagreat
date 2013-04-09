# -*- coding: utf-8 -*-
__author__ = 'SolPie'
from PyQt4 import QtGui, QtCore
from const import trans
from cssQWidget import CssQWidget
import const


class Entity(CssQWidget):
    def __init__(self, parent):
        super(Entity, self).__init__(parent, const.CSS_WIDGET_ENTITY)
        self.resize(400, 120)
        self.label = QtGui.QLabel()
        self.addWidget(self.label)
        self.label.setText('tag entity')


        # self.icon = QtGui.QPixmap(self)
        # self.icon.load('tmp/icon.png')