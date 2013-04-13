# -*- coding: utf-8 -*-
__author__ = 'SolPie'
from cssQWidget import CssQBase
from tagNode import TagNode
from PyQt4 import QtGui, QtCore
import const
from views.tagGalleryView import view
from models.tagGalleryModel import model


class TagTree(CssQBase):
    tag_list = list()
    tagNode_list = list()

    def __init__(self, parent):
        super(TagTree, self).__init__(QtGui.QWidget, parent, const.CSS_WIDGET_DIR_TREE)
        self.resize(800, 800)
        self.override()
        self.add_listener()

        self.tag_list_widget = QtGui.QWidget(self.base)
        self.tag_list_widget.setObjectName(const.CSS_WIDGET_DIR_TREE)
        self.tag_list_widget.resize(self.base.width(), self.base.height() - 30)
        self.tag_list_widget.move(0, 35)

        self.vScroll_bar = QtGui.QScrollBar(self.base)
        self.vScroll_bar.setOrientation(QtCore.Qt.Vertical)
        self.vScroll_bar.resize(15, self.tag_list_widget.height())
        self.vScroll_bar.move(self.width() - self.vScroll_bar.width() - 5, self.tag_list_widget.y())
        self.base.connect(self.vScroll_bar, QtCore.SIGNAL(const.VALUE_CHANGED), self.on_vScroll_changed)

        self.scroll_y = 0

    def override(self):
        self.base.wheelEvent = self.wheelEvent
        model.update_tag_tree = self.update_tag_node

    def on_vScroll_changed(self):
        dy = self.scroll_y - self.vScroll_bar.value()
        self.tag_list_widget.scroll(0, dy)
        self.scroll_y = self.vScroll_bar.value()

    def wheelEvent(self, e):
        self.vScroll_bar.setValue(self.vScroll_bar.value() - e.delta())

    def add_listener(self):
        view.map(view.LIST_DIR, self.clear_nodes)
        pass

    @CssQBase.update_ui
    def update_nodes(self, node_list):
        idx = 0
        for title in node_list:
            if idx < len(self.tagNode_list):
                tagNode = self.tagNode_list[idx]
                tagNode.update(title)
            else:
                num = len(self.tagNode_list)
                tagNode = TagNode(self.tag_list_widget, title)
                tagNode.resize(self.tag_list_widget.width() - 40, 80)
                tagNode.move(5, num * 83)
                self.tagNode_list.append(tagNode)
            self.tag_list.append(title)
            idx += 1
        self.clear_nodes(idx)

    def update_tag_node(self, title, idx):
        if idx < len(self.tagNode_list):
            tagNode = self.tagNode_list[idx]
            tagNode.update(title)
        else:
            num = len(self.tagNode_list)
            tagNode = TagNode(self.tag_list_widget, title)
            tagNode.resize(self.tag_list_widget.width() - 40, 80)
            tagNode.move(5, num * 83)
            self.tagNode_list.append(tagNode)
        self.tag_list.append(title)

    def clear_nodes(self, idx):
        print self, 'clear...'
        for i in range(idx, len(self.tagNode_list)):
            t = self.tagNode_list[i]
            t.free()
        self.tag_list = list()