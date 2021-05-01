import pygame
from random import choice

a = int(input())

class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[choice((1, 2)) for i in range(width)] for i in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.xo = True

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        y = self.top
        for i in range(self.height):
            x = self.left
            s = self.cell_size - 8
            for j in range(self.width):
                pygame.draw.rect(screen, pygame.Color('white'), (x, y, self.cell_size, self.cell_size), 1)
                if self.board[i][j] == 1:
                    pygame.draw.circle(screen, pygame.Color('blue'), (x + 4 + s // 2, y + 4 + s // 2), s // 2)
                elif self.board[i][j] == 2:
                    pygame.draw.circle(screen, pygame.Color('red'), (x + 4 + s // 2, y + 4 + s // 2), s // 2)
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
            b = 0
            if self.board[i][j] == 1 and not self.xo:
                self.board[i][j] = 1
                b = 1
                self.xo = True
            elif self.board[i][j] == 2 and self.xo:
                self.board[i][j] = 2
                b = 2
                self.xo = False
            if b != 0:
                for i in range(len(self.board)):
                    for j in range(len(self.board[i])):
                        if i == a[1] or j == a[0]:
                            self.board[i][j] = b


board = Board(a, a)
board.set_view(20, 20, 50)
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Недореверси')
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(pygame.mouse.get_pos())
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()