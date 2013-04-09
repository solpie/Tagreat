__author__ = 'SolPie'
from cssQWidget import CssQBase
from dirNode import DirNode
from PyQt4 import QtGui
import const
import wmi


class DirTree(CssQBase):
    def __init__(self, parent):
        super(DirTree, self).__init__(QtGui.QWidget, parent, const.CSS_WIDGET_DIR_TREE)
        self.resize(150, 400)
        self.dir_list = list()
        self.list_partition()

    def list_partition(self):
        c = wmi.WMI()
        for disk in c.Win32_LogicalDisk(DriveType=3):
            print disk.Caption
            self.addDir(disk.Caption)

    def addDir(self, str_dir):
        # win32file.QueryDosDevice()
        l = DirNode(self.base, str_dir)

        num = len(self.dir_list)
        l.move(5, num * 28 + 5)
        self.dir_list.append(l)


