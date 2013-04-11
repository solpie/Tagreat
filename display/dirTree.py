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

    dir_list_height = None
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
        self.vScroll_bar.move(self.width() - 30, 35)
        self.vScroll_bar.resize(25, 300)
        self.base.connect(self.vScroll_bar, QtCore.SIGNAL(const.VALUE_CHANGED), self.on_vScroll_changed)

        self.dir_list_height = 0
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
        # dy = e.delta()
        # print 'wheelEvent', dy
        # self.scroll_y += dy
        #
        # if self.scroll_y < -self.dir_list_height:
        #     self.scroll_y = -self.dir_list_height
        #     dy = 0
        # if self.scroll_y > 0:
        #     self.scroll_y = 0
        #     dy = 0
        #
        # # if e.delta() + self.dir_list_widget.y()
        # self.dir_list_widget.scroll(0, dy)

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
                self.add_dir(f, idx)
                idx += 1
            else:
                self.file_list.append(file_url)

    def open_dir(self, e=None):
        # q = QtGui.QWidget()
        # q.geometry()
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
            else:
                print 'backward dir:', self.current_path
                self.list_dir(self.current_path)

    def list_partition(self):
        c = wmi.WMI()
        idx = 0
        if not self.partition_list:
            self.partition_list = c.Win32_LogicalDisk(DriveType=3)
            print 'init... list partition', self.partition_list
        for disk in self.partition_list:
            # print disk.Caption
            # dirs = os.listdir(disk.Caption)
            self.add_dir(disk.Caption, idx)
            idx += 1

    def add_dir(self, str_dir, idx):
        if idx < len(self.dirNode_list):
            dir_node = self.dirNode_list[idx]
            dir_node.set_dir(str_dir)
        else:
            num = len(self.dir_list)
            dir_node = DirNode(self.dir_list_widget, str_dir)
            dir_node.resize(self.dir_list_widget.width() - 40, 25)
            dir_node.onClick = self.open_dir
            self.dirNode_list.append(dir_node)
            self.dir_list_height = num * 28
            dir_node.move(5, self.dir_list_height)
        self.dir_list.append(str_dir)

    def clear_dir(self):
        self.dir_list = list()
        self.dir_list_widget.scroll(0, -self.scroll_y)
        for d in self.dirNode_list:
            d.free()
            # self.base.destroy()#destroy (self, bool destroyWindow = True, bool destroySubWindows = True)




