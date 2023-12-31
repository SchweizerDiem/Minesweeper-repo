from cell import Cell

cell = (Cell(2, 3)
        .set_has_bomb()
        .set_visible()
        .set_nb_neighbor_bombs(4)
        )

print('Properties of new Cell object: ' + cell.__str__())

if(cell.x != 2):
    raise Exception("x property not properly set")
if(cell.y != 3):
    raise Exception("y property not properly set")
if(cell.has_bomb != True):
    raise Exception("has_bomb property not properly set")
if(cell.is_visible != True):
    raise Exception("is_visible property not properly set")
if(cell.nb_neighbor_bombs != 4):
    raise Exception("nb_neighbor_bombs property not properly set")