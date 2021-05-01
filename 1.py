import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLabel
from math import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.btn = QPushButton('Рисовать', self)
        self.edit1 = QLineEdit(self)
        self.edit2 = QLineEdit(self)
        self.lbl1 = QLabel(self)
        self.lbl2 = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 100, 600, 600)
        self.setWindowTitle('Квадрат-объектив — 2')

        self.lbl1.setFixedHeight(30)
        self.lbl1.setFixedWidth(30)
        self.lbl1.setText('K =')
        self.lbl1.move(20, 20)
        self.edit1.setFixedHeight(30)
        self.edit1.setFixedWidth(150)
        self.edit1.move(50, 20)

        self.lbl2.setFixedHeight(30)
        self.lbl2.setFixedWidth(30)
        self.lbl2.setText('N =')
        self.lbl2.move(210, 20)
        self.edit2.setFixedHeight(30)
        self.edit2.setFixedWidth(150)
        self.edit2.move(240, 20)

        self.btn.resize(150, 30)
        self.btn.move(400, 20)
        self.btn.clicked.connect(self.pp)
        self.do_paint = False

    def pp(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            ed1 = float(self.edit1.text())
            ed2 = int(self.edit2.text())
            b = pi / 180
            angle2 = atan((1 - ed1) / ed1) / b
            angle = 90
            qp = QPainter()
            qp.begin(self)
            a, x, y = 300, 150, 450
            pen = QPen(Qt.black, 2)
            qp.setPen(pen)
            for i in range(ed2):
                for j in range(4):
                    x2, y2 = x + round(a * cos(angle * b)), y + round(a * -sin(angle * b))
                    qp.drawLine(x, y, x2, y2)
                    x, y = x2, y2
                    angle -= 90
                angle %= 360
                aa = a * (1 - ed1)
                x, y = x + round(aa * cos(angle * b)), y + round(aa * -sin(angle * b))
                a = (ed1 * a) / cos(angle2 * b)
                angle -= angle2
            qp.end()
            self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())