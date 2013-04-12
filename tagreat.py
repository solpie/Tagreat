# -*- coding: utf-8 -*-
__author__ = 'SolPie'
from PyQt4 import QtGui
import sys
from display.mainwin import MainWin


def test_print(name):
    print 'test_print', name


def test():
    from views.tagGalleryView import TagGalleryView

    view = TagGalleryView()
    view.map('test', test_print)

    view.execute('test', 'dd')


def main():
    app = QtGui.QApplication(sys.argv)
    mw = MainWin()
    mw.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    # test()
    #
    main()

