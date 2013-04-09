__author__ = 'SolPie'
from cssQWidget import CssQWidget
import const


class DirTree(CssQWidget):
    def __init__(self, parent):
        super(DirTree, self).__init__(parent, const.CSS_WIDGET_DIR_TREE)
        self.resize(150, 600)