import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QLineEdit
import requests
import os
import random


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # интерфейс
        self.setGeometry(150, 150, 780, 470)
        self.setWindowTitle('Угадай-ка город')

        # список городов(7шт)
        self.a = ['Ишимбай', 'Стерлитамак', 'Мелеуз', 'Уфа', 'Салават', 'Нефтекамск', 'Октябрьский']
        self.c = random.choice(self.a)

        # компьютер загадывает город
        self.lbl = QLabel(self)
        self.lbl.resize(150, 30)
        self.lbl.move(10, 10)
        self.lbl.setText('Компьютер рандомно\n загадывает город:')

        # кнопка загадать
        self.btn = QPushButton('загадать', self)
        self.btn.resize(150, 30)
        self.btn.move(10, 40)
        self.btn.clicked.connect(self.h)

        # игрок угадывает название города
        self.edt = QLineEdit(self)
        self.edt.resize(150, 30)
        self.edt.move(10, 80)

        # кнопка угадывания
        self.btn2 = QPushButton('Угадать', self)
        self.btn2.resize(150, 30)
        self.btn2.move(10, 120)
        self.btn2.clicked.connect(self.h2)

        # кнопка игрока перемотка слайда
        self.btn3 = QPushButton('Перемотать слайд', self)
        self.btn3.resize(150, 30)
        self.btn3.move(10, 160)
        self.btn3.clicked.connect(self.h3)

        # вывести название города
        self.btn4 = QPushButton('Вывести/скрыть\n название города', self)
        self.btn4.resize(150, 40)
        self.btn4.move(10, 200)
        self.btn4.clicked.connect(self.h4)

        # название города
        self.lbl2 = QLabel(self)
        self.lbl2.resize(150, 30)
        self.lbl2.move(10, 250)
        self.lbl2.setText('')

        # Победа.проигрыш
        self.lbl3 = QLabel(self)
        self.lbl3.resize(150, 30)
        self.lbl3.move(10, 290)
        self.lbl3.setText('')

        # картинка
        self.pixmap = QPixmap()
        self.image = QLabel(self)
        self.image.move(170, 10)
        self.image.resize(600, 450)

    def h(self):
        self.lbl3.setText('')
        self.lbl2.setText('')
        self.edt.setText('')
        self.c = random.choice(self.a)
        self.k = random.choice(['map', 'sat'])
        self.hh()

    def h4(self):
        if self.lbl2.text() == self.c:
            self.lbl2.setText('')
        else:
            self.lbl2.setText(self.c)

    def selection_of_scale(self, a):
        b = [float(i) for i in a['lowerCorner'].split()]
        c = [float(i) for i in a['upperCorner'].split()]
        x, y = (c[0] - b[0]) / 18, (c[1] - b[1]) / 18
        return ",".join([str(x), str(y)]), x, y

    def h2(self):
        if self.edt.text().lower() == self.c.lower():
            self.lbl3.setText('Вы выйграли!!!')
        else:
            self.lbl3.setText('Вы проиграли.')

    def h3(self):
        bb = self.selection_of_scale(self.aa)
        x = random.choice([1, -1]) * random.randint(1, 7) * bb[1] + float(self.coodrinates.split()[0])
        y = random.choice([1, -1]) * random.randint(1, 7) * bb[2] + float(self.coodrinates.split()[1])
        self.params["ll"] = ','.join([str(x), str(y)])
        # запрос
        response = requests.get(self.api_server, params=self.params)
        with open("map.png", "wb") as file:
            file.write(response.content)
        # загрузка картинки
        self.pixmap = QPixmap("map.png")
        os.remove('map.png')
        self.image.setPixmap(self.pixmap)

    def hh(self):
        geocoder_params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": self.c,
            "format": "json"}
        response = requests.get("http://geocode-maps.yandex.ru/1.x/", params=geocoder_params)
        if response:
            # Находим координаты нашего объекта
            json_response = response.json()
            self.coodrinates = json_response["response"]["GeoObjectCollection"][
                "featureMember"][0]["GeoObject"]["Point"]["pos"]
            self.aa = json_response["response"]["GeoObjectCollection"][
                "featureMember"][0]["GeoObject"]['boundedBy']['Envelope']
            points = ','.join(self.coodrinates.split())
            self.params = {}
            self.api_server = "http://static-maps.yandex.ru/1.x/"
            bb = self.selection_of_scale(self.aa)
            self.params['spn'] = bb[0]
            x = random.choice([1, -1]) * random.randint(1, 7) * bb[1] + float(self.coodrinates.split()[0])
            y = random.choice([1, -1]) * random.randint(1, 7) * bb[2] + float(self.coodrinates.split()[1])
            self.params["ll"] = ','.join([str(x), str(y)])
            self.params["l"] = self.k

            # запрос
            response = requests.get(self.api_server, params=self.params)
            with open("map.png", "wb") as file:
                file.write(response.content)
            # загрузка картинки
            self.pixmap = QPixmap("map.png")
            os.remove('map.png')
            self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())