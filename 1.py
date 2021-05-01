import pygame
from math import *

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Вентилятор')
    size = width, height = 201, 201
    screen = pygame.display.set_mode(size)

    running = True
    fps = 60
    v = 0
    clock = pygame.time.Clock()
    screen.fill('black')
    b = pi / 180
    ang = 90
    while running:
        screen.fill('black')
        a = []
        ang += v
        for i in range(3):
            ang += 120
            a.append([(100, 100), (100 + int(70 * (cos(b * (ang + 15)))),
                                   100 - int(70 * (sin(b * (ang + 15))))),
                      (100 + int(70 * (cos(b * (ang - 15)))),
                       100 - int(70 * (sin(b * (ang - 15)))))])
        for i in a:
            pygame.draw.polygon(screen, 'white', i)
        pygame.draw.circle(screen, '#ffffff', (100, 100), 10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    v += (50 / fps)
                elif event.button == 3:
                    v -= (50 / fps)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()