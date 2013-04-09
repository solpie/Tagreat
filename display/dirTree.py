# -*- coding: utf-8 -*-
__author__ = 'SolPie'
from cssQWidget import CssQBase
from dirNode import DirNode
from PyQt4 import QtGui, QtCore
import const
import wmi
import os


class DirTree(CssQBase):
    def __init__(self, parent):
        super(DirTree, self).__init__(QtGui.QWidget, parent, const.CSS_WIDGET_DIR_TREE)
        self.resize(200, 800)
        self.ext()

        self.dir_list = list()
        self.file_list = list()
        self.dirNode_list = list()

        self.list_partition()

        self.current_path = '/'

    def ext(self):
        self.ext_search()

    def ext_search(self):
        # todo 返回上层 搜索过滤
        self.search = QtGui.QLineEdit(self.base)
        self.search.move(5, 5)

        self.searchButton = QtGui.QPushButton(self.base)
        self.searchButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.searchButton.move(150, 5)
        # self.base.mousePressEvent = self.open_dir

    @CssQBase.update_ui
    def open_dir(self, e=None):
        # q = QtGui.QWidget()
        # q.geometry()
        # self.base.setUpdatesEnabled(False)
        str_dir = str(e.getText())
        if self.current_path is not '/':
            self.current_path = os.path.join(self.current_path, str_dir)
        else:
            self.current_path = str_dir
        print 'open dir:', self.current_path
        self.clear_dir()
        dirs = os.listdir(self.current_path)
        idx = 0
        for f in dirs:
        # for idx in range(0, len(dirs)):
        #     f = dirs[idx]
            file_url = self.current_path + "\\" + f
            if os.path.isdir(file_url):
                # todo 过滤系统文件夹 隐藏文件夹
                self.add_dir(f, idx)
                idx += 1
            else:
                self.file_list.append(file_url)


    def list_partition(self):
        c = wmi.WMI()
        for disk in c.Win32_LogicalDisk(DriveType=3):
            print disk.Caption
            dirs = os.listdir(disk.Caption)
            print dirs
            self.add_dir(disk.Caption)

    def add_dir(self, str_dir, idx=None):
        # win32file.QueryDosDevice()
        if idx is not None and idx < len(self.dirNode_list):
            dir_node = self.dirNode_list[idx]
            dir_node.set_dir(str_dir)
        else:
            num = len(self.dir_list)
            dir_node = DirNode(self.base, str_dir)
            dir_node.onClick = self.open_dir
            self.dirNode_list.append(dir_node)
            dir_node.move(5, num * 28 + 40)
        self.dir_list.append(str_dir)


    def clear_dir(self):
        self.dir_list = list()
        for d in self.dirNode_list:
            d.free()
            # self.base.destroy()#destroy (self, bool destroyWindow = True, bool destroySubWindows = True)



