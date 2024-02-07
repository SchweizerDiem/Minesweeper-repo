import random

from domain.cell import Cell


class Board:
    def __init__(self, dim_size=9, num_bombs=10):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.xadrez = [[Cell(y, x) for y in range(self.dim_size)] for x in range(self.dim_size)] # matrix for objects

    def __str__(self):
        print_xadrez = ''
        for y in range(self.dim_size):
            for x in range(self.dim_size):
                print_xadrez += self.xadrez[y][x].__str__() + '\n'

        return 'Board(dim_size={}, num_bombs={}, xadrez={})'.format(self.dim_size, self.num_bombs, print_xadrez)

    def draw_board(self):
        drawing = '   0    1    2    3    4    5    6    7    8'
        sep = '\n' + '+----'*self.dim_size + '+\n'

        for y in range(self.dim_size):
            drawing += sep + str(y)
            for x in range(self.dim_size): 
                drawing += (f'| {self.xadrez[y][x].draw()} |')

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
                for r in range(max(0, self.xadrez[y][x].y-1), min(self.dim_size-1, self.xadrez[y][x].y+1)+1):
                    for c in range(max(0, self.xadrez[y][x].x-1), min(self.dim_size-1, self.xadrez[y][x].x+1)+1):
                        if (self.xadrez[y][x].has_bomb) or (r == self.xadrez[y][x].y and c == self.xadrez[y][x].x):
                            continue
                        if self.xadrez[r][c].has_bomb:
                            self.xadrez[y][x].nb_neighbor_bombs += 1

    def dig(self):
        target = input("Target to dig [row,col]: ")
        target = target.split(',')
        self.xadrez[int(target[0])][int(target[1])].is_visible = True
        return self
        #print(target)

def main():
    j1 = Board()
    j1.plant_bombs()
    j1.put_nb_neighbor_bombs()
    #print(j1.__str__())

    while True:
        print(j1.draw_board())
        j1.dig()


if __name__ == '__main__':
    main()

