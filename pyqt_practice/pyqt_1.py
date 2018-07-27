# 提供必要的应用，基本控件位于pyqt5.qtwidgets模块中
from PyQt5.QtWidgets import QApplication, QWidget
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    W = QWidget()
    W.resize(650, 650)
    W.move(300, 300)
    W.setWindowTitle('simple')
    W.show()
    sys.exit(app.exec_())
