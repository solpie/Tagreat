__author__ = 'SolPie'
from deco import BaseView, singleton
from PyQt4 import QtCore

@singleton
class TagGalleryView(BaseView):
    LIST_DIR = 'list dir'
    TagView = QtCore.pyqtSignal()

    def __init__(self):
        super(BaseView, self).__init__()
        # self.TagView.connect()

view = TagGalleryView()
        # super(EntityGalleryView, self).__init__()