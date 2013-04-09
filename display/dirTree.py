__author__ = 'SolPie'
from cssQWidget import CssQBase
from dirNode import DirNode
from PyQt4 import QtGui, QtCore
import const
import wmi
import os


class DirTree(CssQBase):
    is_opening_dir = False

    def __init__(self, parent):
        super(DirTree, self).__init__(QtGui.QWidget, parent, const.CSS_WIDGET_DIR_TREE)
        self.resize(200, 400)
        self.ext()

        self.dir_list = list()
        self.file_list = list()
        self.dirNode_list = list()

        self.list_partition()

        self.current_path = '/'

    def ext(self):
        self.ext_search()

    def ext_search(self):
        self.search = QtGui.QLineEdit(self.base)
        self.search.move(5, 5)

        self.searchButton = QtGui.QPushButton(self.base)
        self.searchButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.searchButton.move(150, 5)
        # self.base.mousePressEvent = self.open_dir

    def open_dir(self, e=None):
        self.current_path = e.getText()
        self.clear_dir()
        dirs = os.listdir(self.current_path)
        for idx in range(0, len(dirs)):
            f = dirs[idx]
            file_url = self.current_path + "\\" + f
            if os.path.isdir(file_url):
                self.add_dir(file_url, idx)
            else:
                self.file_list.append(file_url)
        print 'open dir:', e.getText(), dirs

    def list_partition(self):
        c = wmi.WMI()
        self.is_opening_dir = True
        for disk in c.Win32_LogicalDisk(DriveType=3):
            print disk.Caption
            dirs = os.listdir(disk.Caption)
            print dirs
            self.add_dir(disk.Caption)

    def add_dir(self, str_dir, idx=None):
        # win32file.QueryDosDevice()
        if idx is not None and idx < len(self.dirNode_list) and self.dirNode_list[idx].is_free:
            l = self.dirNode_list[idx]
            l.set_dir(str_dir)
            num = idx
        else:
            num = len(self.dir_list)
            l = DirNode(self.base, str_dir)
            l.onClick = self.open_dir
            self.dirNode_list.append(l)

        self.dir_list.append(str_dir)
        l.move(5, num * 28 + 40)

    def clear_dir(self):
        self.dir_list = list()
        for d in self.dirNode_list:
            d.free()
            # self.base.destroy()#destroy (self, bool destroyWindow = True, bool destroySubWindows = True)



