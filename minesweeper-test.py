import random 

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
        self.xadrez = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)] # matrix for objects


    def draw_board(self):
        sep = '\n' + '+----'*self.dim_size + '+\n'
        
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                return sep + (f'|  {self.xadrez[r][c]} '*self.dim_size + '|' + sep)*self.dim_size
            
    def plant_bombs(self):
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2-1) # Chooses a random spot ofthe matrix
            row = loc // self.dim_size
            col = loc % self.dim_size

            if self.xadrez[row][col] == 'X':
                pass
            else:
                self.xadrez[row][col] = 'X'
                bombs_planted += 1



# we are gonna create a class Cell, where we are gonna 
# store all the info about each cell of the board
class Cell:
    def __init__(self, x, y, is_bomb, is_visible, neighbor_bombs):
        self.x = x
        self.y = y
        self.is_bomb = is_bomb
        self.is_visible = is_visible
        self.neighbor_bombs = neighbor_bombs

        

j1 = Board()
j1.plant_bombs()
print(j1.draw_board())

