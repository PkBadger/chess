class Piece:
    def __init__(self, color):
        self.color = color

class King(Piece):
    rules = ['same']

    def __init__(self, color):
        self.name = 'K'
        Piece.__init__(self, color)

    def can_move(self):
        return True

class Queen(Piece):
    rules = ['same', 'pieceInPath']

    def __init__(self, color):
        self.name = 'Q'
        Piece.__init__(self, color)

    def can_move(self, rules):
        pass

class Rook(Piece):
    rules = ['same', 'front_side', 'pieceInPath']

    def __init__(self, color):
        self.name = 'R'
        Piece.__init__(self, color)

    def can_move(self, rules):
        if False in rules: return False
        return not False in rules

class Bishop(Piece):
    rules = ['same', 'diagonal', 'pieceInPath']

    def __init__(self, color):
        self.name = 'B'
        Piece.__init__(self, color)

    def can_move(self):
        return True

class Knight(Piece):
    rules = ['same', 'l_shape']

    def __init__(self, color):
        self.name = 'k'
        Piece.__init__(self, color)

    def can_move(self):
        return True

class Pawn(Piece):
    rules = ['same', 'front', 'eat_diagonal']

    def __init__(self, color):
        self.name = 'P'
        Piece.__init__(self, color)

    def can_move(self):
        return True
    