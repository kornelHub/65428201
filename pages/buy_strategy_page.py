import os
from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtUiTools import loadUiType
from PySide2.QtWidgets import QFileDialog
from binance.helpers import date_to_milliseconds
from functools import partial
import pages.strategy_page


current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = loadUiType(os.path.join(current_dir, "../ui/buy_strategy.ui"))

class Buy_Strategy_Widget(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)

        self.p2_add_buy_rule.clicked.connect(lambda : pages.strategy_page.Strategy_Widget().display_rule_form_for_buy_strategy())

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    w = Buy_Strategy_Widget()
    w.show()
    sys.exit(app.exec_())
