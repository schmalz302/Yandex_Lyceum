import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLabel
from PyQt5.QtWidgets import QColorDialog
from math import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.btn = QPushButton('Рисовать', self)
        self.edit1 = QLineEdit(self)
        self.edit2 = QLineEdit(self)
        self.edit3 = QLineEdit(self)
        self.lbl1 = QLabel(self)
        self.lbl2 = QLabel(self)
        self.lbl3 = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 800)
        self.setWindowTitle('Квадрат-объектив — 2')

        self.lbl1.setFixedHeight(30)
        self.lbl1.setFixedWidth(30)
        self.lbl1.setText('K =')
        self.lbl1.move(20, 20)
        self.edit1.setFixedHeight(30)
        self.edit1.setFixedWidth(50)
        self.edit1.move(50, 20)

        self.lbl2.setFixedHeight(30)
        self.lbl2.setFixedWidth(30)
        self.lbl2.setText('N =')
        self.lbl2.move(110, 20)
        self.edit2.setFixedHeight(30)
        self.edit2.setFixedWidth(50)
        self.edit2.move(140, 20)

        self.lbl3.setFixedHeight(30)
        self.lbl3.setFixedWidth(30)
        self.lbl3.setText('M =')
        self.lbl3.move(200, 20)
        self.edit3.setFixedHeight(30)
        self.edit3.setFixedWidth(50)
        self.edit3.move(230, 20)

        self.btn.resize(150, 30)
        self.btn.move(400, 20)
        self.btn.clicked.connect(self.pp)
        self.do_paint = False

    def pp(self):
        self.color = QColorDialog.getColor()
        self.do_paint = True
        self.repaint()

    def p(self, qp):
        # переменные
        ed1 = float(self.edit1.text())
        ed2 = int(self.edit2.text())
        ed3 = int(self.edit3.text())
        # переменная для работы с радианами и угол постоянного наклона
        b = pi / 180
        ang3 = 360 // ed3
        # угол наклона
        c, cc = 1 - ed1, ed1
        ac = ((cos(ang3 * b) * cc + c) ** 2 + (sin(ang3 * b) * cc) ** 2) ** 0.5
        angle2 = asin(c * sin(ang3 * b) / ac) / b
        # угол начала
        angle = 360 // ed3
        # рисование
        a, x, y = 1200 // ed3, 150, 450
        qp.setPen(QPen(self.color, 2))
        for i in range(ed2):
            for j in range(ed3):
                x2, y2 = x + round(a * cos(angle * b)), y + round(a * -sin(angle * b))
                qp.drawLine(x, y, x2, y2)
                x, y = x2, y2
                angle -= ang3
            angle %= 360
            aa = a * (1 - ed1)
            x, y = x + round(aa * cos(angle * b)), y + round(aa * -sin(angle * b))
            a *= ac
            angle -= angle2

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.p(qp)
            qp.end()
            self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())