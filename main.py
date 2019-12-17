from chess import Chess

if __name__ == '__main__':
    chess = Chess()
    chess.new_game()
    current_turn = 'w'
    while True:
        print(chess)
        coordinates = input("Enter your value: ")
        original_row, original_col, row, col = coordinates.split(',')
        chess.move(int(original_row), int(original_col), int(row), int(col), current_turn)
        
    print(chess)
    print(chess.move(1,1,2,1, 'w'))