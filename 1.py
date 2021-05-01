import sys
from PIL import Image
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QFileDialog, QLabel


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 400, 500, 500)
        self.setStyleSheet("background-color: white;")
        self.setWindowTitle('Изманение прозрачности')
        self.s = QSlider(self)
        self.image = QLabel(self)
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.image.setPixmap(QPixmap(self.fname))
        self.b = Image.open(self.fname).copy()
        self.initUI()

    def initUI(self):
        self.s.setMaximum(256)
        self.s.setMinimum(0)
        self.s.setValue(256)
        self.s.resize(20, 200)
        self.s.move(20, 20)
        self.s.sliderMoved.connect(self.hello)
        self.image.move(50, 20)
        self.image.resize(200, 200)
        self.image.setPixmap(QPixmap(self.fname))

    def hello(self):
        a = (256 - self.s.value()) / 256
        b = self.b.copy()
        p = b.load()
        x, y = b.size
        for i in range(x):
            for j in range(y):
                r, g, b1 = p[i, j]
                p[i, j] = r + int((257 - r) * a), g + int((257 - g) * a),\
                          b1 + int((257 - b1) * a)
        b.save(self.fname)
        self.image.setPixmap(QPixmap(self.fname))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
