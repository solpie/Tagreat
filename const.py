# -*- coding: utf-8 -*-
__author__ = 'SolPie'
from PyQt4 import QtGui


def trans(text, disambig=None):
    return QtGui.QApplication.translate("", text, disambig, QtGui.QApplication.UnicodeUTF8)


UI_MENU_FILE = '文件'
UI_MENU_FILE_OPEN = '打开'
UI_MENU_FILE_SAVE_PRJ = '保存工程文件'
UI_MENU_FILE_IMPORT_SPT = '导入场景数据(*.spt)'
UI_MENU_FILE_EXPORT_SPT = '导出场景数据(*.spt)'

CSS_WIDGET_ENTITY = 'Entity'
CSS_WIDGET_DIR_TREE = 'DirTree'
CSS_WIDGET_DIR_TREE_LABEL = 'DirTreeLabel'