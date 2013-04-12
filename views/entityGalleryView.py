__author__ = 'SolPie'
from deco import BaseView, singleton


@singleton
class EntityGalleryView(BaseView):
    LIST_DIR = 'list dir'

    def __init__(self):
        super(BaseView, self).__init__()
        pass

        # super(EntityGalleryView, self).__init__()