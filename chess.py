class Piece(object):
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        
class Queen(Piece):

    value = 9
            
    def get_moves(self, grid):

        for move in _get_horizontal_moves(grid, self.x, self.y):
            yield move

        for move in _get_vertical_moves(grid, self.x, self.y):
            yield move

        for move in _get_diagonal_moves(grid, self.x, self.y):
            yield move
            
def _get_horizontal_moves(grid, piece):

    index = x - 1
    while index > 0 and grid[y][index] is None:
        new_grid = [[s for s in row] for row in grid]
        new_grid[y][x] = None
        new_grid[y][index] = piece
        yield new_grid
        index -= 1

    index = x + 1
    while index < len(grid) - 1 and grid[y][index] is None:
        
def _get_vertical_moves(grid, x, y):
    pass

def _get_diagonal_moves(grid, x, y):
    pass

BLACK = 0
WHITE = 1

grid = [
    [Rook(WHITE), Knight(WHITE), Bishop(WHITE), King(WHITE), Queen(WHITE),
     Bishop(WHITE), Knight(WHITE), Rook(WHITE)],
    [Pawn(WHITE) for _ in range(8)],
    [None] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
    [Pawn(BLACK) for _ in range(8)],
    [Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK), King(BLACK),
     Bishop(BLACK), Knight(BLACK), Rook(BLACK)]
    ]
