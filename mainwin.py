# -*- coding: utf-8 -*-
__author__ = 'SolPie'
from PyQt4 import QtCore as Core, QtGui as Gui
import sys
from display.menuBar import MenuBar
from display.dirTree import DirTree

from display.tagTree import TagTree


class MainWin(Gui.QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__(None)
        self.setupUI()
        self.setWindowFlags(Core.Qt.FramelessWindowHint)

    def setupUI(self):
        f = Core.QFile("darkstyle.css")
        f.open(Core.QFile.ReadOnly)
        style_sheet = Core.QLatin1String(f.readAll())
        self.setStyleSheet(style_sheet)

        self.setWindowTitle("Tagreat")
        self.showMaximized()
        self.centralWidget = Gui.QWidget(self)
        self.setCentralWidget(self.centralWidget)
        '''
        菜单
        '''
        self.menu_bar = MenuBar(self)
        self.setMenuBar(self.menu_bar)
        '''
        目录
        '''
        self.dir_tree = DirTree(self.centralWidget)
        self.dir_tree.move(10, 5)

        self.entity = TagTree(self.centralWidget)
        self.entity.move(400, 5)


def test_print(name):
    print 'test_print', name


def test():
    from views.tagGalleryView import TagGalleryView

    view = TagGalleryView()
    view.map('test', test_print)

    view.execute('test', 'dd')


def main():
    app = Gui.QApplication(sys.argv)
    mw = MainWin()
    mw.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    # test()
    #
    main()

