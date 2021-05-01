import pygame
from math import *

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Прямоугольники с Ctrl+Z')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)

    running = True
    fps = 60
    v = 0
    clock = pygame.time.Clock()
    screen.fill('black')
    b = pi / 180
    ang = 90
    a = []
    paint = False
    while running:
        screen.fill('black')
        if a:
            for i in a:
                b = i[0]
                c = i[1]
                pygame.draw.line(screen, 'white', b, (c[0], b[1]), width=5)
                pygame.draw.line(screen, 'white', (c[0], b[1]), c, width=5)
                pygame.draw.line(screen, 'white', c, (b[0], c[1]), width=5)
                pygame.draw.line(screen, 'white', (b[0], c[1]), b, width=5)
        if paint:
            cc = pygame.mouse.get_pos()
            pygame.draw.line(screen, 'white', bb, (cc[0], bb[1]), width=5)
            pygame.draw.line(screen, 'white', (cc[0], bb[1]), cc, width=5)
            pygame.draw.line(screen, 'white', cc, (bb[0], cc[1]), width=5)
            pygame.draw.line(screen, 'white', (bb[0], cc[1]), bb, width=5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                bb = pygame.mouse.get_pos()
                paint = True
            if event.type == pygame.MOUSEBUTTONUP:
                paint = False
                cc = pygame.mouse.get_pos()
                a.append([bb, cc])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    if a:
                        del a[-1]
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()