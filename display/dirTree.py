# -*- coding: utf-8 -*-
__author__ = 'SolPie'
from cssQWidget import CssQBase
from dirNode import DirNode
from PyQt4 import QtGui, QtCore
import const
import wmi
import os
import win32con
import win32file


class DirTree(CssQBase):
    dir_list = None
    file_list = None
    dirNode_list = None
    partition_list = None
    backward_path_list = None

    current_path = None

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

        self.dir_list = list()
        self.file_list = list()
        self.dirNode_list = list()

        self.list_partition()

        self.current_path = '/'
        self.backward_path_list = list()

    def override(self):
        self.base.wheelEvent = self.wheelEvent

    def on_vScroll_changed(self):
        dy = self.scroll_y - self.vScroll_bar.value()
        self.dir_list_widget.scroll(0, dy)
        self.scroll_y = self.vScroll_bar.value()
        pass

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

    @CssQBase.update_ui
    def list_dir(self, path):
        self.clear_dir()
        dirs = os.listdir(path)
        idx = 0
        for f in dirs:
            #todo empty dir
            file_url = os.path.join(self.current_path, f)
            attribute = win32file.GetFileAttributes(file_url)
            if attribute & (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM):
                print file_url
            elif attribute & win32con.FILE_ATTRIBUTE_DIRECTORY:
                self.update_dir(f, idx)
                idx += 1
            else:
                self.file_list.append(f)
        self.set_vScroll_range(idx)
        self.update_tagTree()

    def update_tagTree(self):
        from views.entityGalleryView import EntityGalleryView
        v = EntityGalleryView()
        v.execute(v.LIST_DIR, self.file_list)
        print self, 'EntityGalleryView', v

    def open_dir(self, e=None):
        str_dir = str(e.getText())
        self.backward_path_list.append(self.current_path)
        if self.current_path is not '/':
            self.current_path = os.path.join(self.current_path, str_dir)
        else:
            self.current_path = str_dir
        print 'open dir:', self.current_path
        self.list_dir(self.current_path)

    def backward_dir(self, e=None):
        if len(self.backward_path_list):
            self.current_path = self.backward_path_list.pop()
            if self.current_path is '/':
                self.clear_dir()
                self.list_partition()
                self.update_tagTree()
            else:
                self.list_dir(self.current_path)
            print 'backward dir:', self.current_path

    def list_partition(self):
        c = wmi.WMI()
        idx = 0
        if not self.partition_list:
            self.partition_list = c.Win32_LogicalDisk(DriveType=3)
            print 'init... list partition', self.partition_list
        for disk in self.partition_list:
            # print disk.Caption
            # dirs = os.listdir(disk.Caption)
            self.update_dir(disk.Caption, idx)
            idx += 1
        self.set_vScroll_range(idx)

    def update_dir(self, str_dir, idx):
        if idx < len(self.dirNode_list):
            dirNode = self.dirNode_list[idx]
            dirNode.update(str_dir)
        else:
            num = len(self.dir_list)
            dirNode = DirNode(self.dir_list_widget, str_dir)
            dirNode.resize(self.dir_list_widget.width() - 40, 25)
            dirNode.onClick = self.open_dir
            self.dirNode_list.append(dirNode)
            dirNode.move(5, num * 28)
        self.dir_list.append(str_dir)

    def clear_dir(self):
        self.dir_list = list()
        self.file_list = list()
        self.dir_list_widget.scroll(0, -self.scroll_y)
        for d in self.dirNode_list:
            d.free()
            # self.base.destroy()#destroy (self, bool destroyWindow = True, bool destroySubWindows = True)

    def set_vScroll_range(self, num):
        self.vScroll_bar.setRange(0, num * 28 - self.dir_list_widget.height() / 5 * 4)




