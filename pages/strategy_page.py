import os
from PySide2 import QtGui
from PySide2.QtUiTools import loadUiType

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = loadUiType(os.path.join(current_dir, "../ui/strategy_page.ui"))


class Strategy_Widget(Base, Form):
    buy_stackedWidget_object = None
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    w = Strategy_Widget()
    w.show()
    sys.exit(app.exec_())