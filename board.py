import random

from domain.cell import Cell


class Board:
    def __init__(self, dim_size=9, num_bombs=10):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.xadrez = [[Cell(y, x) for y in range(self.dim_size)] for x in range(self.dim_size)] # matrix for objects
        self.dug = set()
        self.state = True

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

    def dig(self, row, col):

        # Keep track of where we already dug.
        self.dug.add((row, col))

        if self.xadrez[row][col].has_bomb == True:
            self.xadrez[row][col].is_visible = True
            self.state = False
            return self
        elif self.xadrez[row][col].nb_neighbor_bombs > 0:
            self.xadrez[row][col].is_visible = True
            return self

        self.xadrez[row][col].is_visible = True
        for r in range(max(0, self.xadrez[row][col].y-1), min(self.dim_size-1, self.xadrez[row][col].y+1)+1):
            for c in range(max(0, self.xadrez[row][col].x-1), min(self.dim_size-1, self.xadrez[row][col].x+1)+1):
                if (r, c) in self.dug:
                    continue
                self.xadrez[r][c].is_visible = True
                self.dig(r, c)
    
        #print(target)


def main():
    j1 = Board()
    j1.plant_bombs()
    j1.put_nb_neighbor_bombs()
    #print(j1.__str__())

    while j1.state:
        print(j1.draw_board())
        target = input("Target to dig [row,col]: ")
        print()
        target = target.split(',')
        row = int(target[0])
        col = int(target[1])
        j1.dig(row, col)
    
    print(j1.draw_board())
    print("Game Over! You lose!\n")


if __name__ == '__main__':
    main()

