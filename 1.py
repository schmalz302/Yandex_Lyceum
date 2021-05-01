import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QLineEdit
import requests
import os


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # интерфейс
        self.setGeometry(150, 150, 780, 500)
        self.setWindowTitle('Большая задача по Maps API. Часть №7')

        # кнопка
        self.btn = QPushButton('Искать', self)
        self.btn.resize(150, 30)
        self.btn.move(10, 10)
        self.btn.clicked.connect(self.hello)

        # кнопка2
        self.btn2 = QPushButton('Сброс результата', self)
        self.btn2.resize(150, 30)
        self.btn2.move(10, 90)
        self.btn2.clicked.connect(self.hello2)

        # ввод данных
        self.edit1 = QLineEdit(self)
        self.edit1.setFixedWidth(150)
        self.edit1.setFixedHeight(30)
        self.edit1.move(10, 50)

        # окно вывода адреса
        self.lbl = QLabel(self)
        self.lbl.setFixedWidth(500)
        self.lbl.setFixedHeight(30)
        self.lbl.move(170, 465)


        # первоначальные данные для вывода карты
        self.lon, self.lat = 56.045221, 53.419472
        self.delta, self.l_list = 0.002, ['map', 'sat', 'sat,skl']
        self.api_server, self.l_num = "http://static-maps.yandex.ru/1.x/", 0
        self.params = {
            "ll": ",".join([str(self.lon), str(self.lat)]),
            "spn": ",".join([str(self.delta), str(self.delta)]),
            "l": self.l_list[self.l_num],
            "pt": f"{','.join([str(self.lon), str(self.lat)])},pm2gnl"}
        # запрос
        response = requests.get(self.api_server, self.params)
        with open("map.png", "wb") as file:
            file.write(response.content)

        # картинка
        self.pixmap = QPixmap()
        self.image = QLabel(self)
        self.image.move(170, 10)
        self.image.resize(600, 450)

        # загрузка картинки
        self.pixmap = QPixmap("map.png")
        os.remove('map.png')
        self.image.setPixmap(self.pixmap)

    def selection_of_scale(self, a):
        b = [float(i) for i in a['lowerCorner'].split()]
        c = [float(i) for i in a['upperCorner'].split()]
        x, y = c[0] - b[0], c[1] - b[1]
        return ",".join([str(x), str(y)])

    def keyPressEvent(self, event: QKeyEvent):
        b = False
        if event.key() == 16777238:
            self.delta *= 2
            if self.delta > 10:
                delta = 10
            b = True
        if event.key() == 16777239:
            self.delta /= 2
            if self.delta < 0:
                self.delta = 0
            b = True
        if event.key() == 16777220:
            self.l_num += 1
            self.l_num %= 3
            b = True
        if event.key() == 68:
            self.lon += 0.0001
            b = True
        if event.key() == 87:
            self.lat += 0.0001
            b = True
        if event.key() == 83:
            self.lat -= 0.0001
            b = True
        if event.key() == 65:
            self.lon -= 0.0001
            b = True
        if b:
            self.params["l"] = self.l_list[self.l_num]
            self.params['spn'] = ",".join([str(self.delta), str(self.delta)])
            self.params["ll"] = ",".join([str(self.lon), str(self.lat)])
            response = requests.get(self.api_server, params=self.params)
            map_file = "map.png"
            with open(map_file, "wb") as file:
                file.write(response.content)
            # загрузка картинки
            self.pixmap = QPixmap("map.png")
            os.remove('map.png')
            self.image.setPixmap(self.pixmap)

    def hello2(self):
        self.lbl.setText('')
        if 'pt' in self.params:
            del self.params['pt']
        response = requests.get(self.api_server, params=self.params)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        # загрузка картинки
        self.pixmap = QPixmap("map.png")
        os.remove('map.png')
        self.image.setPixmap(self.pixmap)

    def hello(self):
        geocoder_params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": self.edit1.text(),
            "format": "json"}
        response = requests.get("http://geocode-maps.yandex.ru/1.x/", params=geocoder_params)
        if response:
            # Находим координаты нашего объекта
            json_response = response.json()
            coodrinates = json_response["response"]["GeoObjectCollection"][
                "featureMember"][0]["GeoObject"]["Point"]["pos"]
            address = json_response["response"]["GeoObjectCollection"][
                "featureMember"][0]["GeoObject"]['metaDataProperty']['GeocoderMetaData']['text']
            self.lbl.setText(address)
            a = json_response["response"]["GeoObjectCollection"][
                "featureMember"][0]["GeoObject"]['boundedBy']['Envelope']
            self.lon, self.lat = [float(i) for i in coodrinates.split()]
            points = ','.join(coodrinates.split())
            self.params["ll"] = points
            self.params["pt"] = f"{points},pm2gnl"
            self.params['spn'] = self.selection_of_scale(a)

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