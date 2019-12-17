def same(board, original_row, original_col, row, col, turn):
    return not (original_col == col and original_row == row)

def front(board, original_row, original_col, row, col, turn):
    if(original_col != col):
        return False
    if turn == 'w':
        if row < original_row:
            return False 
    if turn == 'b':
        if row > original_row:
            return False 
    return True

def front_side(board, original_row, original_col, row, col, turn):
    return original_row == row or original_col == col

def l_shape(board, original_row, original_col, row, col, turn):
    row_distance = abs(row - original_row)
    col_distance = abs(col - original_col)

    if row_distance != 2 and col_distance != 2: return False

    if row_distance == 2:
        if col_distance != 1:
            return False
    if col_distance == 2:
        if row_distance != 1:
            return False
    return True

def diagonal(board, original_row, original_col, row, col, turn):
    numerator = row - original_row
    denominator = col - original_col
    return numerator == denominator

def eat_diagonal(board, original_row, original_col, row, col, turn):
    

rules = {
    'diagonal': diagonal,
    'front': front,
    'same': same,
    'front_side': front_side,
    'l_shape': l_shape
}