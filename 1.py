import requests
import pygame
import os
api_server = "http://static-maps.yandex.ru/1.x/"

lon = input('Введите долготу:')
lat = input('Введите ширину:')
delta = float(input('Введите область показа:'))

params = {
    "ll": ",".join([lon, lat]),
    "spn": ",".join([str(delta), str(delta)]),
    "l": "map"
}
response = requests.get(api_server, params=params)
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
pygame.display.set_caption('Большая задача по Maps API. Часть №2')
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
b = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == 1073741899:
                delta *= 2
                if delta > 10:
                    delta = 10
                b = True
            if event.key == 1073741902:
                delta /= 2
                if delta < 0:
                    delta = 0
                b = True
    if b:
        b = False
        params['spn'] = ",".join([str(delta), str(delta)]),
        response = requests.get(api_server, params=params)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
pygame.quit()
os.remove(map_file)
