# -*- coding: utf-8 -*-
__author__ = 'SolPie'
from cssQWidget import CssQBase
from dirNode import DirNode
from models.tagGalleryModel import model
from PyQt4 import QtGui, QtCore
import const
import wmi
import os
import win32con
import win32file


class DirTree(CssQBase):
    dirNode_list = None
    scroll_y = None

    def __init__(self, parent):
        super(DirTree, self).__init__(QtGui.QWidget, parent, const.CSS_WIDGET_DIR_TREE)
        self.resize(300, 800)
        self.override()
        self.ext()

        self.dir_list_widget = QtGui.QWidget(self.base)
        self.dir_list_widget.setObjectName(const.CSS_WIDGET_DIR_TREE)
        self.dir_list_widget.resize(self.base.width(), self.base.height() - 30)
        self.dir_list_widget.move(0, 35)

        self.vScroll_bar = QtGui.QScrollBar(self.base)
        self.vScroll_bar.setOrientation(QtCore.Qt.Vertical)
        self.vScroll_bar.resize(15, self.dir_list_widget.height())
        self.vScroll_bar.move(self.width() - self.vScroll_bar.width() - 5, self.dir_list_widget.y())
        self.base.connect(self.vScroll_bar, QtCore.SIGNAL(const.VALUE_CHANGED), self.on_vScroll_changed)

        self.scroll_y = 0

        self.dirNode_list = list()

        model.update_dir_tree = self.update_dir
        model.list_partition()
        self.list_partition()

    def override(self):
        self.base.wheelEvent = self.wheelEvent

    def on_vScroll_changed(self):
        dy = self.scroll_y - self.vScroll_bar.value()
        self.dir_list_widget.scroll(0, dy)
        self.scroll_y = self.vScroll_bar.value()

    def wheelEvent(self, e):
        self.vScroll_bar.setValue(self.vScroll_bar.value() - e.delta())

    def ext(self):
        self.ext_search()

    def ext_search(self):
        # todo search filter
        self.search = QtGui.QLineEdit(self.base)
        self.search.move(5, 5)

        self.backward = QtGui.QPushButton(self.base)
        self.backward.setFocusPolicy(QtCore.Qt.NoFocus)
        self.backward.mousePressEvent = self.backward_dir
        self.backward.move(150, 5)
        # self.base.mousePressEvent = self.open_dir

    def update_tagTree(self):
        from views.tagGalleryView import view

        view.execute(view.LIST_DIR, len(model.file_list))
        print self, 'EntityGalleryView', view

    @CssQBase.update_ui
    def open_dir(self, e=None):
        str_dir = str(e.getText())
        self.clear_dir()
        dir_idx, file_idx = model.open_dir(str_dir)
        self.set_vScroll_range(dir_idx)

    def backward_dir(self, e=None):
        self.clear_dir()
        dir_idx, file_idx = model.backward_dir()
        self.set_vScroll_range(dir_idx)

    def list_partition(self):
        idx = len(model.partition_list)
        self.set_vScroll_range(idx)

    #
    def update_dir(self, str_dir, idx):
        if idx < len(self.dirNode_list):
            dirNode = self.dirNode_list[idx]
            dirNode.update(str_dir)
        else:
            num = len(model.dir_list)
            dirNode = DirNode(self.dir_list_widget, str_dir)
            dirNode.resize(self.dir_list_widget.width() - 40, 25)
            dirNode.onClick = self.open_dir
            self.dirNode_list.append(dirNode)
            dirNode.move(5, num * 28)

    def clear_dir(self):
        self.dir_list_widget.scroll(0, -self.scroll_y)
        for d in self.dirNode_list:
            d.free()
            # self.base.destroy()#destroy (self, bool destroyWindow = True, bool destroySubWindows = True)

    def set_vScroll_range(self, num):
        self.vScroll_bar.setRange(0, num * 28 - self.dir_list_widget.height() / 5 * 4)




