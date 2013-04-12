__author__ = 'SolPie'
# class CssQWidget(object):
#     def __init__(self, parent, object_name=None):
#         self.qw = QtGui.QWidget(parent)
#         if object_name:
#             self.setObjectName(object_name)
#
#     def setObjectName(self, name):
#         self.qw.setObjectName(name)
#
#     def resize(self, w, h):
#         self.qw.resize(w, h)
#
#     def move(self, x, y):
#         self.qw.move(x, y)
#
#     def addWidget(self, child):
#         child.setParent(self.qw)


class CssQBase(object):
    base = None

    def __init__(self, cls, parent, object_name=None):
        self.base = cls(parent)
        self.object_name = object_name
        if object_name:
            self.setObjectName(object_name)

    @staticmethod
    def update_ui(func):
        def deco(*args):
            args[0].base.hide()
            func(*args)
            args[0].base.show()

        return deco

    def width(self):
        return self.base.width()

    def setObjectName(self, name):
        self.base.setObjectName(name)

    def resize(self, w, h):
        self.base.resize(w, h)

    def move(self, x, y):
        self.base.move(x, y)

    def addWidget(self, child):
        child.setParent(self.base)

    def scroll(self, x, y):
        self.base.scroll(x, y)

    def hide(self):
        self.base.hide()

    def show(self):
        self.base.show()
