import os
from PySide2 import QtWidgets
from PySide2.QtUiTools import loadUiType

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = loadUiType(os.path.join(current_dir, "ui/mainWindow.ui"))

class MainWidget(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        print('***', self)
        self.setupUi(self)

if __name__ == '__main__':
    import sys
    print('+main called')
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    window = MainWidget()
    window.show()
    sys.exit(app.exec_())