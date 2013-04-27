# -*- coding: utf-8 -*-
__author__ = 'SolPie'
from cssQWidget import CssQBase
from PyQt4 import QtGui
import const


class TagLib(CssQBase):
    def __init__(self, parent):
        super(TagLib, self).__init__(QtGui.QTabWidget, parent, const.CSS_WIDGET_DIR_TREE)
        t = QtGui.QTabWidget()
        # t.addTab()