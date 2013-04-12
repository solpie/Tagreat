__author__ = 'SolPie'
from deco import BaseView, singleton


@singleton
class TagGalleryView(BaseView):
    LIST_DIR = 'list dir'

    def __init__(self):
        super(BaseView, self).__init__()

view = TagGalleryView()
        # super(EntityGalleryView, self).__init__()