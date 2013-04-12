# -*- coding: utf-8 -*-
__author__ = 'SolPie'
from PyQt4 import QtGui, QtCore
from const import trans
from cssQWidget import CssQBase
import const


class TagNode(CssQBase):
    func_list = None

    def __init__(self, parent, title):
        super(TagNode, self).__init__(QtGui.QWidget, parent, const.CSS_WIDGET_ENTITY)
        self.label = QtGui.QLabel()
        self.label.setObjectName(const.CSS_LABEL_TAG_NODE)
        self.label.move(4, 4)
        self.addWidget(self.label)
        if title:
            self.setTitle(title)

        #todo 功能栏 ：音频预览 打开文件位置 设置为封面
        #todo  audio preview
        #todo open in explorer
        #todo set cover
        #todo func icon
        '''

        '''
        self.func_widget = QtGui.QWidget()
        self.func_widget.setObjectName(const.CSS_WIDGET_TAG_NODE_FUNC)
        self.addWidget(self.func_widget)
        self.func_widget.move(300, 4)
        self.func_widget.resize(150, 30)
        self.func_list = list()
        #
        self.previewbutton = self.add_func_button('A')
        #
        self.dir_button = self.add_func_button('F')
        #
        self.set_cover_button = self.add_func_button('C')

    def update(self, filename):
        self.setTitle(filename)
        self.show()

    def add_func_button(self, text, func= None):
        button = QtGui.QPushButton(self.func_widget)
        button.setText(text)
        button.move(len(self.func_list) * 28 + 2, 2)
        button.resize(26, 26)

        self.func_list.append(button)
        return button

    @QtCore.pyqtSlot('')
    def on_previewbutton_clicked(self):
        print 'preview audio file'

    def setTitle(self, title):
        self.label.setText(title)

    def free(self):
        self.hide()
        # self.icon = QtGui.QPixmap(self)
        # self.icon.load('tmp/icon.png')