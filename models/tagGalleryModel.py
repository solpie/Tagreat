__author__ = 'SolPie'
from deco import singleton
import os
import win32con
import win32file
import wmi


@singleton
class TagGalleryModel():
    def __init__(self):
        self.current_path = '/'
        self.dir_list = list()
        self.file_list = list()
        self.backward_path_list = list()
        self.forward_path_list = list()
        self.partition_list = None

    def open_dir(self, path):
        self.backward_path_list.append(self.current_path)
        if self.current_path is not '/':
            self.current_path = os.path.join(self.current_path, path)
        else:
            self.current_path = path
        print 'open dir:', self.current_path
        return self.list_dir(self.current_path)

    def backward_dir(self):
        if len(self.backward_path_list):
            file_idx = 0
            self.current_path = self.backward_path_list.pop()
            if self.current_path is '/':
                self.clear_dir()
                dir_idx = self.list_partition()
            else:
                dir_idx, file_idx = self.list_dir(self.current_path)
            print 'backward dir:', self.current_path
            self.update_tag_tree(self.file_list)
            return dir_idx, file_idx
        else:
            return 0, 0

    def list_partition(self):
        c = wmi.WMI()
        dir_idx = 0
        if not self.partition_list:
            self.partition_list = c.Win32_LogicalDisk(DriveType=3)
            print 'init... list partition', self.partition_list
        for disk in self.partition_list:
            # print disk.Caption
            self.dir_list.append(disk.Caption)
            dir_idx += 1
        self.update_dir_tree(self.dir_list)
        return dir_idx

    def list_dir(self, path):
        self.clear_dir()
        dirs = os.listdir(path)
        dir_idx = 0
        file_idx = 0
        for f in dirs:
            #todo empty dir
            file_url = os.path.join(self.current_path, f)
            attribute = win32file.GetFileAttributes(file_url)
            if attribute & (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM):
                print self, file_url
            elif attribute & win32con.FILE_ATTRIBUTE_DIRECTORY:
                print self, self.dir_list, len(self.dir_list)
                self.dir_list.append(f)
                dir_idx += 1
            else:
                self.file_list.append(f)
                file_idx += 1
        self.update_dir_tree(self.dir_list)
        self.update_tag_tree(self.file_list)
        return dir_idx, file_idx

    def on_update_dir(self, *args):
        self.update_dir_tree(*args)
        return

    def update_dir_tree(self, *args):
        raise Exception('override me in dirTree')

    def update_tag_tree(self, *args):
        raise Exception('override me in tagTree')

    def clear_dir(self):
        self.dir_list = list()
        self.file_list = list()

    def get_file_url(self, filename):
        return os.path.join(self.current_path, filename)


model = TagGalleryModel()

