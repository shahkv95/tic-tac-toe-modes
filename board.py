class Board:
    def __init__(self):
        Board.positions = ['1','2','3',
                           '4','5','6',
                           '7','8','9']

        Board.display_board()

    def display_board(): #Laptop number keypad
        print("\nKeypad/position format:\n")
        print('',Board.positions[6],'|',Board.positions[7],'|',Board.positions[8],'')
        print('---|---|---')
        print('',Board.positions[3],'|',Board.positions[4],'|',Board.positions[5],'')
        print('---|---|---')
        print('',Board.positions[0],'|',Board.positions[1],'|',Board.positions[2],'')
        print("\n")