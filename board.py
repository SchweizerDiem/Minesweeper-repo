import random

from domain.cell import Cell


# step 1- Create a board and plant the bombs
# step 2- Put the number of neighbor bombs on the non-bombs cells
# step 3- Let the user choose a spot on the board to dig
# step 4- Refresh the board with the new uncovered spots
# step 5- Repeat step 3/4 until the game ends

# let's create a class for the board
# and a class to represent the cells in the xadrez board

class Board:
    def __init__(self, dim_size=10, num_bombs=10):
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
        drawing = ''
        sep = '\n' + '+----'*self.dim_size + '+\n'
        
        for x in range(self.dim_size):
            for y in range(self.dim_size):
                drawing += sep + (f'|  {self.xadrez[max(x+1, 0)][min(y+1, self.dim_size)].draw()} '*self.dim_size + '|' + sep)*self.dim_size

        return drawing
            
    def plant_bombs(self):
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2-1) # Chooses a random spot ofthe matrix
            row = loc // self.dim_size
            col = loc % self.dim_size

            if self.xadrez[row][col].has_bomb == True:
                pass
            else:
                self.xadrez[row][col].has_bomb = True
                bombs_planted += 1


j1 = Board(5, 5)
j1.plant_bombs()
print(j1.draw_board())

