import pygame.font
from copy import deepcopy
from random import *


class Board:
    # создание поля
    pygame.init()
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[-1] * width for i in range(height)]
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
                if self.board[i][j] == 10:
                    pygame.draw.rect(screen, pygame.Color('red'), (x + 1, y + 1, self.cell_size - 1,
                                                                     self.cell_size - 1), 0)
                else:
                    if self.board[i][j] != -1:
                        font = pygame.font.Font(None, 30)
                        text = font.render(f"{self.board[i][j]}", True, pygame.Color('green'))
                        screen.blit(text, [x + 1, y + 1])
                pygame.draw.rect(screen, pygame.Color('white'), (x, y, self.cell_size, self.cell_size), 1)
                x += self.cell_size
            y += self.cell_size

    def get_cell(self, mouse_pos):
        if self.left <= mouse_pos[0] <= self.left + self.cell_size * self.width and \
        self.top <= mouse_pos[1] <= self.top + self.cell_size * self.height:
            x = (mouse_pos[0] - self.left) // self.cell_size
            y = (mouse_pos[1] - self.top) // self.cell_size
            return (y, x)
        else:
            return False


class Minesweeper(Board):
    def __init__(self, width, height, a):
        super().__init__(width, height)
        c = 0
        while c != a:
            x = randint(0, height - 1)
            y = randint(0, width - 1)
            if self.board[x][y] != 10:
                self.board[x][y] = 10
                c += 1
    def num(self, x, y):
        c = 0
        if 0 <= x < len(self.board[0]) and 0 <= y + 1 < len(self.board):
            if self.board[x][y + 1] == 10:
                c += 1
        if 0 <= x < len(self.board[0]) and 0 <= y - 1 < len(self.board):
            if self.board[x][y - 1] == 10:
                c += 1
        if 0 <= x + 1 < len(self.board[0]) and 0 <= y < len(self.board):
            if self.board[x + 1][y] == 10:
                c += 1
        if 0 <= x - 1 < len(self.board[0]) and 0 <= y < len(self.board):
            if self.board[x - 1][y] == 10:
                c += 1
        if 0 <= x + 1 < len(self.board[0]) and 0 <= y - 1 < len(self.board):
            if self.board[x + 1][y - 1] == 10:
                c += 1
        if 0 <= x + 1 < len(self.board[0]) and 0 <= y + 1 < len(self.board):
            if self.board[x + 1][y + 1] == 10:
                c += 1
        if 0 <= x - 1 < len(self.board[0]) and 0 <= y - 1 < len(self.board):
            if self.board[x - 1][y - 1] == 10:
                c += 1
        if 0 <= x - 1 < len(self.board[0]) and 0 <= y + 1 < len(self.board):
            if self.board[x - 1][y + 1] == 10:
                c += 1
        return c

    def rec(self, x, y):
        if (x, y) not in self.c:
            self.c.append((x, y))
            if 0 <= x < len(self.board[0]) and 0 <= y + 1 < len(self.board):
                self.board[x][y + 1] = self.num(x, y + 1)
                if not self.num(x, y + 1):
                    self.rec(x, y + 1)
            if 0 <= x < len(self.board[0]) and 0 <= y - 1 < len(self.board):
                self.board[x][y - 1] = self.num(x, y - 1)
                if not self.num(x, y - 1):
                    self.rec(x, y - 1)
            if 0 <= x + 1 < len(self.board[0]) and 0 <= y < len(self.board):
                self.board[x + 1][y] = self.num(x + 1, y)
                if not self.num(x + 1, y):
                    self.rec(x + 1, y)
            if 0 <= x - 1 < len(self.board[0]) and 0 <= y < len(self.board):
                self.board[x - 1][y] = self.num(x - 1, y)
                if not self.num(x - 1, y):
                    self.rec(x - 1, y)
            if 0 <= x + 1 < len(self.board[0]) and 0 <= y - 1 < len(self.board):
                self.board[x + 1][y - 1] = self.num(x + 1, y - 1)
                if not self.num(x + 1, y - 1):
                    self.rec(x + 1, y - 1)
            if 0 <= x + 1 < len(self.board[0]) and 0 <= y + 1 < len(self.board):
                self.board[x + 1][y + 1] = self.num(x + 1, y + 1)
                if not self.num(x + 1, y + 1):
                    self.rec(x + 1, y + 1)
            if 0 <= x - 1 < len(self.board[0]) and 0 <= y - 1 < len(self.board):
                self.board[x - 1][y - 1] = self.num(x - 1, y - 1)
                if not self.num(x - 1, y - 1):
                    self.rec(x - 1, y - 1)
            if 0 <= x - 1 < len(self.board[0]) and 0 <= y + 1 < len(self.board):
                self.board[x - 1][y + 1] = self.num(x - 1, y + 1)
                if not self.num(x - 1, y + 1):
                    self.rec(x - 1, y + 1)

    def open_cell(self):
        a = self.get_cell(pygame.mouse.get_pos())
        if a and self.board[a[0]][a[1]] == -1:
            x, y = a
            c = self.num(x, y)
            if c:
                self.board[x][y] = c
            else:
                self.c = []
                self.board[x][y] = c
                self.rec(x, y)



x, y = 15, 15
board = Minesweeper(x, y, 40)
sz = board.cell_size
lf, tp = board.left * 2 + x * sz, board.top * 2 + y * sz
screen = pygame.display.set_mode((lf, tp))
pygame.display.set_caption('Папа сапёра')
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.open_cell()
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()