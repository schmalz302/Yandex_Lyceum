import pygame
from copy import deepcopy
from random import choice


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for i in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.stop = False

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        y = self.top
        for i in range(self.height):
            x = self.left
            s = self.cell_size
            for j in range(self.width):
                if self.board[i][j] == 1:
                    pygame.draw.rect(screen, pygame.Color('green'), (x + 1, y + 1, self.cell_size - 1,
                                                                     self.cell_size - 1), 0)
                pygame.draw.rect(screen, pygame.Color('white'), (x, y, self.cell_size, self.cell_size), 1)
                x += self.cell_size
            y += self.cell_size

    def get_cell(self, mouse_pos):
        if self.left <= mouse_pos[0] <= self.left + self.cell_size * self.width and \
        self.top <= mouse_pos[1] <= self.top + self.cell_size * self.height:
            x = (mouse_pos[0] - self.left) // self.cell_size
            y = (mouse_pos[1] - self.top) // self.cell_size
            return (x, y)
        else:
            return None

    def get_click(self, mouse_pos):
        a = self.get_cell(mouse_pos)
        j, i = a
        if not a is None:
            if self.board[i][j] == 1:
                self.board[i][j] = 0
            else:
                self.board[i][j] = 1


class Life(Board):
    def __init__(self, width, height):
        super().__init__(width, height)

    def next_move(self):
        if self.stop:
            c = deepcopy(self.board)
            for i in range(self.height):
                for j in range(self.width):
                    n = 0
                    if i + 1 < self.height:
                        n += [c[i + 1][j]].count(1)
                    if i - 1 >= 0:
                        n += [c[i - 1][j]].count(1)
                    if j + 1 < self.width:
                        n += [c[i][j + 1]].count(1)
                    if j - 1 >= 0:
                        n += [c[i][j - 1]].count(1)
                    if i + 1 < self.height and j + 1 < self.width:
                        n += [c[i + 1][j + 1]].count(1)
                    if i + 1 < self.height and j - 1 >= 0:
                        n += [c[i + 1][j - 1]].count(1)
                    if i - 1 >= 0 and j + 1 < self.width:
                        n += [c[i - 1][j + 1]].count(1)
                    if i - 1 >= 0 and j - 1 >= 0:
                        n += [c[i - 1][j - 1]].count(1)
                    if c[i][j] == 0 and n == 3:
                        self.board[i][j] = 1
                    if c[i][j] == 1 and n != 2 and n != 3:
                        self.board[i][j] = 0


board = Life(30, 30)
board.set_view(20, 20, 18)
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Игра «Жизнь»')
running = True
MYEVENTTYPE = pygame.USEREVENT + 1
a = 500
pygame.time.set_timer(MYEVENTTYPE, a)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MYEVENTTYPE:
            board.next_move()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                board.get_click(pygame.mouse.get_pos())
            if event.button == 3:
                board.stop = True
            if event.button == 4:
                if a > 50:
                    a -= 50
                    if a < 50:
                        a = 50
                pygame.time.set_timer(MYEVENTTYPE, a)
            if event.button == 5:
                a += 50
                pygame.time.set_timer(MYEVENTTYPE, a)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if board.stop:
                    board.stop = False
                else:
                    board.stop = True
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()