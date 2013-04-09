# -*- coding: utf-8 -*-
__author__ = 'SolPie'
from PyQt4 import QtCore as Core, QtGui as Gui
import sys
from display.menuBar import MenuBar
from display.dirTree import DirTree

from display.entity import Entity


class MainWin(Gui.QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__(None)
        self.setupUI()

    def setupUI(self):
        f = Core.QFile("darkstyle.css")
        f.open(Core.QFile.ReadOnly)
        style_sheet = Core.QLatin1String(f.readAll())
        self.setStyleSheet(style_sheet)

        self.setWindowTitle("Scene Editor")
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
        self.dir_tree.move(10, 30)
        self.dir_tree.addDir('dd')

        self.entity = Entity(self.centralWidget)
        self.entity.move(200, 30)


def test_print(name):
    print 'test_print', name


def test():
    from views.entityGalleryView import EntityGalleryView

    view = EntityGalleryView()
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
