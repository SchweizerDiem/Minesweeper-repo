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

        for y in range(self.dim_size):
            drawing += sep + str(y+1)
            for x in range(self.dim_size):
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

    def put_nb_neighbor_bombs(self):
        for y in range(self.dim_size):
            for x in range(self.dim_size):
                for r in range(max(0, self.xadrez[x][y].x-1), min(self.dim_size-1, self.xadrez[x][y].x+1)+1):
                     for c in range(max(0, self.xadrez[x][y].y-1), min(self.dim_size-1, self.xadrez[x][y].y+1)+1):
                        if r == self.xadrez[x][y].x and c == self.xadrez[x][y].y:
                          continue 
                        if self.xadrez[r][c].has_bomb == True:
                             self.xadrez[x][y].nb_neighbor_bombs += 1

        return self

j1 = Board()
j1.plant_bombs()
j1.put_nb_neighbor_bombs()
print(j1.draw_board())
print(j1.__str__())
