__author__ = 'SolPie'
from deco import singleton


@singleton
class EntityGalleryModel():
    def __init__(self):
        self.count = 0


