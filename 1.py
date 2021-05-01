import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QPushButton, QLineEdit

SCREEN_SIZE = [400, 400]


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 500, 500)
        self.setWindowTitle('Квадрат-объектив — 1')

        self.btn = QPushButton('Показать', self)
        self.btn.resize(100, 30)
        self.btn.move(10, 10)
        self.btn.clicked.connect(self.hello)

        self.lbl1= QLabel(self)
        self.lbl1.setText('side')
        self.lbl1.move(350, 10)
        self.edit1 = QLineEdit(self)
        self.edit1.setFixedWidth(80)
        self.edit1.setFixedHeight(30)
        self.edit1.move(385, 10)

        self.lbl2 = QLabel(self)
        self.lbl2.setText('coeff')
        self.lbl2.move(350, 50)
        self.edit2 = QLineEdit(self)
        self.edit2.setFixedWidth(80)
        self.edit2.setFixedHeight(30)
        self.edit2.move(385, 50)

        self.lbl3 = QLabel(self)
        self.lbl3.setText('n')
        self.lbl3.move(350, 90)
        self.edit3 = QLineEdit(self)
        self.edit3.setFixedWidth(80)
        self.edit3.setFixedHeight(30)
        self.edit3.move(385, 90)

        self.do_paint = False
        self.pixmap = QPixmap()
        self.image = QLabel(self)
        self.image.move(20, 120)
        self.image.resize(300, 300)

    def hello(self):
        self.a = int(self.edit1.text())
        self.b = float(self.edit2.text())
        self.c = int(self.edit3.text())
        self.m = [[[(20, 120), (20 + self.a, 120)], [(20 + self.a, 120), (20 + self.a, 120 + self.a)],
                  [(20 + self.a, 120 + self.a), (20, 120 + self.a)], [(20, 120 + self.a), (20, 120)]]]
        for i in range(self.c - 1):
            self.d = []
            a = int((self.a - self.a * (self.b ** (i + 1))) / 2)
            b = int(self.a * (self.b ** (i + 1)))
            d = 20 + a
            m = 120 + a
            self.d.append([(d, m), (d + b, m)])
            self.d.append([(d + b, m), (d + b, m + b)])
            self.d.append([(d + b, m + b), (d, m + b)])
            self.d.append([(d, m + b), (d, m)])
            self.m.append(self.d)
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter(self.pixmap)
            qp.begin(self)
            qp.setPen(QPen(Qt.red, 2))
            for i in range(self.c):
                for j in range(4):
                    qp.drawLine(*self.m[i][j][0], *self.m[i][j][1])
            qp.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())