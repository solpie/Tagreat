# -*- coding: utf-8 -*-
__author__ = 'SolPie'
from PyQt4 import QtGui
from const import trans

import const


class MenuBar(QtGui.QMenuBar):
    def __init__(self, parent):
        super(MenuBar, self).__init__(parent)
        self.setGeometry(0, 0, 900, 21)

        self.menu_file = QtGui.QMenu(self)
        self.menu_file.setTitle(trans(const.UI_MENU_FILE))
        self.addMenu(self.menu_file)
        self.add_act_to_menu(self.menu_file, const.UI_MENU_FILE_OPEN, self.act_file_open)
        self.add_act_to_menu(self.menu_file, const.UI_MENU_FILE_EXIT, self.act_file_exit)

    def add_act_to_menu(self, menu, actName, func):
        act = QtGui.QAction(self)
        act.setText(trans(actName))
        act.triggered.connect(func)
        menu.addAction(act)

    def act_file_open(self):
        print 'dddd'

    def act_file_save(self):
        print 'actFileSave'

    def act_file_exit(self):
        print 'exit...'