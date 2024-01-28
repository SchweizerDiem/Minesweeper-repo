import random

from domain.cell import Cell


class Board:
    def __init__(self, dim_size=9, num_bombs=10):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.xadrez = [[Cell(x+1, y+1) for y in range(self.dim_size)] for x in range(self.dim_size)] # matrix for objects

    def __str__(self):
        print_xadrez = ''
        for x in range(self.dim_size):
            for y in range(self.dim_size):
                print_xadrez += self.xadrez[x][y].__str__() + '\n'

        return 'Board(dim_size={}, num_bombs={}, xadrez={})'.format(self.dim_size, self.num_bombs, print_xadrez)

    def draw_board(self):
        drawing = '   A    B    C    D    E    F    G    H    I'
        sep = '\n' + '+----'*self.dim_size + '+\n'

        for x in range(self.dim_size):
            drawing += sep + str(x+1)
            for y in range(self.dim_size):
                drawing += (f'| {self.xadrez[x][y].draw()} |')

        return drawing + '\n' + '+----'*self.dim_size + '+\n'
            
    def plant_bombs(self):
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2-1) # Chooses a random spot of the matrix
            row = loc // self.dim_size
            col = loc % self.dim_size

            if self.xadrez[row][col].has_bomb == True:
                pass
            else:
                self.xadrez[row][col].has_bomb = True
                bombs_planted += 1


j1 = Board()
j1.plant_bombs()
print(j1.draw_board())
