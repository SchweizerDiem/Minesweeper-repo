import random

# create a class called 'board' to have access to board tools
# such as creating, digging, and etc.
class Board:
    def __init__(self, dim_size=10, num_bombs=10):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.xadrez = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        self.dig = set()# keep track of where we've dug

        # now we need a function to create the board
        # for that I'm gonna choose to make the board from a 
        # list of lists in which we'll have columns and rows


    def make_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        
        # once the board is made, we can plant the bombs!
        # for this step I'll use a while loop and not a for loop
        # because in the scenerio of the picked location of the bomb already has a bomb
        # we pass and keep choosing until all 10 are placed
        bombs = 0
        while bombs < self.num_bombs:
            pick_location = random.randint(0, self.dim_size ** 2 - 1)
            row = pick_location // self.dim_size
            col = pick_location % self.dim_size

            if board[row][col] == '*':
                pass
            else:
                board[row][col] = '*'
                bombs += 1
            
        return board
    

    def check_for_bomb(self):
        # now we check for bombs and where there isn't bombs
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if self.board[row][col] == '*':
                    continue
                # using a helper function for assigning the numbers
                self.board[row][col] == self.number_of_bombs(row, col)


    # this function is going to help us assign the numbers into the board
    def number_of_bombs(self, row, col):
        sum = 0
        for r in range(max(row-1, 0), min(row+1, self.dim_size-1)):
            for c in range(max(col-1, 0), min(col+1), self.dim_size-1):
                if self.board[r][c] == '*':
                    sum +=1
                else:
                    continue
        return sum
    
    def dig(self, row, col):
        # this function will take care of the digging and uncovering neighbors empty squares

    
# if __name__ == '__main__':
        