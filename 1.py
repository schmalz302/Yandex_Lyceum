import sys
from PIL import Image
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QPushButton

SCREEN_SIZE = [400, 400]


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 500, 300)
        self.setWindowTitle('PIL 2.0')

        self.image = QLabel(self)
        self.image.move(250, 20)
        self.image.resize(200, 200)

        btn1 = QPushButton('R', self)
        btn1.resize(200, 40)
        btn1.move(40, 10)
        btn1.clicked.connect(self.hello)

        btn2 = QPushButton('G', self)
        btn2.resize(200, 40)
        btn2.move(40, 70)
        btn2.clicked.connect(self.hello)

        btn3 = QPushButton('B', self)
        btn3.resize(200, 40)
        btn3.move(40, 130)
        btn3.clicked.connect(self.hello)

        btn4 = QPushButton('ALL', self)
        btn4.resize(200, 40)
        btn4.move(40, 190)
        btn4.clicked.connect(self.hello)

        btn5 = QPushButton('Против часовой стрелки', self)
        btn5.resize(200, 40)
        btn5.move(40, 240)
        btn5.clicked.connect(self.hello1)

        btn6 = QPushButton('По часовой стрелке', self)
        btn6.resize(200, 40)
        btn6.move(260, 240)
        btn6.clicked.connect(self.hello1)

        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.im = Image.open(self.fname)
        p = self.im.load()
        self.im1, self.im2, self.im3 = self.im.copy(), self.im.copy(), self.im.copy()
        p1, p2, p3 = self.im1.load(), self.im2.load(), self.im3.load()
        x, y = self.im.size
        for i in range(x):
            for j in range(y):
                r, g, b = p[i, j]
                p1[i, j] = r, 0, 0
                p2[i, j] = 0, g, 0
                p3[i, j] = 0, 0, b
        self.im.save(self.fname)
        self.image.setPixmap(QPixmap(self.fname))
        self.n = [self.im1, self.im2, self.im3, self.im]
        self.name = self.im.copy()

    def hello(self):
        a = self.sender().text()
        if a == 'R':
            self.name = self.n[0].copy()
            self.name.save(self.fname)
        elif a == 'G':
            self.name = self.n[1].copy()
            self.name.save(self.fname)
        elif a == 'B':
            self.name = self.n[2].copy()
            self.name.save(self.fname)
        else:
            self.name = self.n[3].copy()
            self.name.save(self.fname)
        self.image.setPixmap(QPixmap(self.fname))

    def hello1(self):
        for i in range(len(self.n)):
            if self.sender().text()[:2] == "По":
                self.n[i] = self.n[i].transpose(Image.ROTATE_270)
            else:
                self.n[i] = self.n[i].transpose(Image.ROTATE_90)
        if self.sender().text()[:2] == "По":
            self.name = self.name.transpose(Image.ROTATE_270)
        else:
            self.name = self.name.transpose(Image.ROTATE_90)
        self.name.save(self.fname)
        self.image.setPixmap(QPixmap(self.fname))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())