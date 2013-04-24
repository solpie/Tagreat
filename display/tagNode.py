# -*- coding: utf-8 -*-
__author__ = 'SolPie'
from PyQt4 import QtGui, QtCore
from const import trans
from cssQWidget import CssQBase
import const
from utils.audio.preview import Preview
from models.tagGalleryModel import model
from utils.worker import Worker as Thread


class TagNode(CssQBase):
    func_list = None
    press = False

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
        self.preview_button = self.add_func_button('A', self.preview_audio)
        #
        self.dir_button = self.add_func_button('F', self.open_dir)
        #
        self.set_cover_button = self.add_func_button('C', self.set_cover)
        self.set_cover_button.mouseMoveEvent = self.mouseMoveEvent

        self.override()

    def override(self):
        self.base.dragEnterEvent = self.dragEnterEvent
        self.base.dropEvent = self.dropEvent
        self.base.setAcceptDrops(True)

    def update(self, filename):
        self.setTitle(filename)
        self.show()

    def mouseMoveEvent(self, e):
        if not self.press:
            return
        mimeData = QtCore.QMimeData()
        drag = QtGui.QDrag(self.base)
        drag.setMimeData(mimeData)
        dropAction = drag.start(QtCore.Qt.MoveAction)
        print("....")

    def dropEvent(self, e):
        print('dropEvent')

    def dragEnterEvent(self, e):
        e.accept()
        # if e.mimeDate().hasFormat('text/plain'):
        #     e.accept()
        # else:
        #     e.ignore()

    def add_func_button(self, text, func=None):
        button = QtGui.QPushButton("Toggle Button", self.func_widget)
        button.setText(text)
        button.move(len(self.func_list) * 28 + 2, 2)
        button.resize(26, 26)
        button.mousePressEvent = func
        self.func_list.append(button)
        return button

    def preview_audio(self, *args):
        p = Preview()
        print self, p
        t = Thread()

        if p.playing:
        # if t.isAlive():
            p.stop()
            print __name__, ">>stop..."
        else:
            self.play()
            # try:
            #     # t.setDaemon(True)
            #     t.run = self.play
            #     t.start()
            # except Exception, e:
            #     print e
        print 'preview audio file', args

    def play(self):
        p = Preview()
        p.open(model.get_file_url(self.getTitle()))
        p.play()

    def open_dir(self, *args):
        p = Preview()
        p.stop()
        print 'open file in explorer', args

    def set_cover(self, *args):
        self.press = True
        print 'set cover', args

    def setTitle(self, title):
        self.label.setText(title)

    def getTitle(self):
        return str(self.label.text())

    def free(self):
        self.hide()
        # self.icon = QtGui.QPixmap(self)
        # self.icon.load('tmp/icon.png')