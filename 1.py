import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.xo = False

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
                    pygame.draw.line(screen, pygame.Color('blue'), (x + 4, y + 4),
                                     (x + s + 4, y + s + 4), width=2)
                    pygame.draw.line(screen, pygame.Color('blue'), (x + 4, y + s + 4),
                                     (x + s + 4, y + 4), width=2)
                elif self.board[i][j] == 2:
                     pygame.draw.ellipse(screen, pygame.Color('red'), (x + 4, y + 4, s, s), width=2)
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
        if not a is None:
            j, i = a
            if self.board[i][j] == 0:
                if not self.xo:
                    self.board[i][j] = 1
                    self.xo = True
                else:
                    self.board[i][j] = 2
                    self.xo = False


board = Board(10, 7)
board.set_view(20, 20, 50)
screen = pygame.display.set_mode((600, 600))
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