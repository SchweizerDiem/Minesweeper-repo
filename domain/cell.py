class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.has_bomb = False
        self.is_visible = False
        self.nb_neighbor_bombs = 0

    def set_has_bomb(self):
        self.has_bomb = True
        return self

    def set_visible(self):
        self.is_visible = True
        return self

    def set_nb_neighbor_bombs(self, nb_neighbor_bombs):
        self.nb_neighbor_bombs = nb_neighbor_bombs
        return self

    def __str__(self):
        return 'Cell(x={}, y={}, has_bomb={}, is_visible={}, nb_neighbor_bombs={})'.format(self.x, self.y, self.has_bomb, self.is_visible, self.nb_neighbor_bombs)

    def draw(self):
        if(self.has_bomb):
            return '*'
        if(self.nb_neighbor_bombs == 0):
            return ' '
        return self.nb_neighbor_bombs
    
    # get nb of bombs near 
    # store sum of bombs nearby in 'sum'
    def get_neighbors_bombs(self): 
        sum = 0
        for r in range(max(self.y-1, 0), min(self.y+1, self.dim_size-1)):
            for c in range(max(self.x-1, 0), min(self.x+1), self.dim_size-1):
                if self.board[r][c] == '*':
                    sum +=1
                else:
                    continue
        
        self.nb_neighbor_bombs = sum

        return self.nb_neighbor_bombs
