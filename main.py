from random import choice

class Game:
    def __init__(self):
        print("\nTic Tac Toe\n")
        print("Press 1: To start the game")
        print("Press any key(s): To quit\n")

        Game.user_choice = input("Do you want to start the game? ")

        if(Game.user_choice == "1"):
            Game.mode = "Multiplayer"
        else:
            return

        Board()
        Board.symbol = choice(['X', '0'])
        # print(Board.symbol)

        Game.player_chance()

        # Game.player_wins = True
        if(Game.player_wins):
            # needs to be updated
            print("Player", Board.symbol, "wins!")
        else:
            print("No one wins! It's a draw!")

        start_another_game = input("Press 1: To start another game? ")
        if(start_another_game == "1"):
            Game()

    def player_chance():
        Game.player_wins = True # default should be set to False
        # loop repeats until someone wins or runs out of steps
        while(not Game.player_wins):
            Game.player_move()
            Game.check_player_win()
            Game.swap_symbol()

    def player_move():
        pass

    def check_player_win():
        pass

    def swap_symbol():
        if(Board.symbol == 'X'):
            Board.symbol = '0'
        else:
            Board.symbol = 'X'

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

if __name__=="__main__":
    game = Game()
