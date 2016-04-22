#TODO implement captures as possible moves

class Piece(object):
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

class Rook(Piece):

    value = 5

    def get_moves(self, grid):

        for move in _get_horizontal_moves(grid, self):
            yield move

        for move in _get_vertical_moves(grid, self):
            yield move

class Knight(Piece):

    value = 3

    def get_moves(self, grid):

        moves = [
            (self.y + 2, self.x + 1),
            (self.y + 2, self.x - 1),
            (self.y - 2, self.x + 1),
            (self.y - 2, self.x - 1),
            (self.x + 2, self.y + 1),
            (self.x + 2, self.y - 1),
            (self.x - 2, self.y + 1),
            (self.x - 2, self.y - 1)
        ]

        for move in moves:
            x, y = move
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid):
                yield _move_piece(self, grid, x, y)

class Bishop(Piece):

    value = 3

    def get_moves(self, grid):

        for move in _get_vertical_moves(grid, self):
            yield move

class Queen(Piece):

    value = 9
            
    def get_moves(self, grid):

        for move in _get_horizontal_moves(grid, self):
            yield move

        for move in _get_vertical_moves(grid, self):
            yield move

        for move in _get_diagonal_moves(grid, self):
            yield move

class King(Piece):

    value = float("inf")

    def get_moves(self, grid):

        moves = [
            (self.x, self.y - 1),
            (self.x + 1, self.y - 1),
            (self.x + 1, self.y),
            (self.x + 1, self.y + 1),
            (self.x, self.y + 1),
            (self.x - 1, self.y + 1),
            (self.x - 1, self.y),
            (self.x - 1, self.y - 1)
        ]

        for move in moves:
            x, y = move
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid):
                yield _move_piece(self, grid, x, y)
            
class Pawn(Piece):

    value = 1

    def get_moves(self, grid):

        moves = [(self.x, self.y + 1)]

        if self.is_first_move:
            moves.append((self.x, self.y + 2))

        for move in moves:
            x, y = move
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid):
                yield _move_piece(self, grid, x, y)
 
def _get_horizontal_moves(grid, piece):

    index = piece.x - 1
    while index >= 0 and grid[piece.y][index] is None:
        yield _move_piece(piece, grid, x, y)
        index -= 1

    index = piece.x + 1
    while index < len(grid) and grid[piece.y][index] is None:
        yield _move_piece(piece, grid, x, y)
        index += 1
        
def _get_vertical_moves(grid, piece):
    
    index = piece.y - 1
    while index >= 0 and grid[index][piece.x] is None:
        yield _move_piece(piece, grid, x, y)
        index -= 1

    index = piece.x + 1
    while index < len(grid) and grid[index][piece.x] is None:
        yield _move_piece(piece, grid, x, y)
        index += 1

def _get_diagonal_moves(grid, piece):
    #TODO needs len(grid)

    #up left
    x, y = piece.x - 1, piece.y - 1
    while x >= 0 and y >= 0 and grid[y][x] is None:
        yield _move_piece(piece, grid, x, y)
        x -= 1
        y -= 1

    #down right
    x, y = piece.x + 1, piece.y + 1
    while x >= 0 and y >= 0 and grid[y][x] is None:
        yield _move_piece(piece, grid, x, y)
        x += 1
        y += 1

    #up right
    x, y = piece.x + 1, piece.y - 1
    while x >= 0 and y >= 0 and grid[y][x] is None:
        yield _move_piece(piece, grid, x, y)
        x += 1
        y -= 1

    #down left
    x, y = piece.x - 1, piece.y + 1
    while x >= 0 and y >= 0:
        yield _move_piece(piece, grid, x, y)

        if grid[y][x] is not None and grid[y][x].color != piece.color:
            break
        
        x -= 1
        y += 1

def _move_piece(piece, grid, x, y):
    #TODO put bounds checking in here
    new = [[s for s in row] for row in grid]
    new[piece.y][piece.x] = None
    new[y][x] = piece
    return new

BLACK = 0
WHITE = 1

##grid = [
##    [Rook(WHITE), Knight(WHITE), Bishop(WHITE), King(WHITE), Queen(WHITE),
##     Bishop(WHITE), Knight(WHITE), Rook(WHITE)],
##    [Pawn(WHITE) for _ in range(8)],
##    [None] * 8,
##    [None] * 8,
##    [None] * 8,
##    [None] * 8,
##    [Pawn(BLACK) for _ in range(8)],
##    [Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK), King(BLACK),
##     Bishop(BLACK), Knight(BLACK), Rook(BLACK)]
##    ]
