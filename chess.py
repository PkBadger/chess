from pieces import King, Queen, Rook, Bishop, Knight, Pawn
from rules import rules

class Chess:
    def __init__(self):
        self.board = []

        for i in range(8):
            self.board.append([])
            for k in range(8):
                self.board[i].append(Square(i,k))

    def __repr__(self):
        representation = []
        for row in self.board:
            row_representation = []
            for square in row:
                if not square.piece:
                    row_representation.append('')
                else:
                    row_representation.append(square.piece.name)
            representation.append(','.join(row_representation))
        return '\n'.join(representation)

    def new_game(self):
        black_first_row = [Rook('b'), Knight('b'), Bishop('b'), Queen('b'), King('b'), Bishop('b'), Knight('b'), Rook('b')] 
        black_second_row = [Pawn('b') for _ in range(8)]
        white_first_row = [Rook('w'), Knight('w'), Bishop('w'), Queen('w'), King('w'), Bishop('w'), Knight('w'), Rook('w')] 
        white_second_row = [Pawn('w') for _ in range(8)]

        for index in range(8):
            self.board[0][index].piece = black_first_row[index]
            self.board[1][index].piece = black_second_row[index]
            self.board[7][index].piece = white_first_row[index]
            self.board[6][index].piece = white_second_row[index]
    
    def move(self, original_row, original_col, row, col, turn):
        is_valid = self.can_move(original_row, original_col, row, col, turn)
        piece = self.board[original_row][original_col].piece
        if(is_valid):
            self.board[row][col].piece = piece
            self.board[original_row][original_col].piece = None
        else:
            print('invalid movement')

        
    def can_move(self, original_row, original_col, row, col, turn):
        piece = self.board[original_row][original_col].piece
        if not piece: return False
        for rule in piece.rules:
            if not rules[rule](self.board, original_row, original_col, row, col, turn):
                return False
        return True


class Square:
    def __init__(self, x, y, piece=None):
        self.x = x
        self.y = y
        self.piece = piece