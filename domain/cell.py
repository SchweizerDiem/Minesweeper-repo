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
        return '\nCell(y={}, x={}, has_bomb={}, is_visible={}, nb_neighbor_bombs={})'.format(self.y, self.x, self.has_bomb, self.is_visible, self.nb_neighbor_bombs)

    def draw(self):
        if(self.is_visible == True):
            if(self.has_bomb):
                return '*'
            if(self.nb_neighbor_bombs == 0):
                return ' '
            return self.nb_neighbor_bombs
        else:
            return ' '

