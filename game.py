from random import choice
from board import Board

class Game:
    def __init__(self, user_choice):
        self.user_choice = user_choice

    def play_game(self):

        if(self.user_choice == "1"):
            Game.mode = "multiplayer"
        elif(self.user_choice == "2"):
            Game.mode = "bot"
        else:
            return
        
        Board()

        Game.symbol = choice(['X', '0'])
        print("Starting with", Game.symbol, "turn\n")

        Game.player_chance()

        if(Game.player_wins):
            print("Player", Game.winner_symbol, "wins!")
        else:
            print("No one wins! It's a draw!")

        start_another_game = input("Press 1: To start another game; any other key to quit ")
        if(start_another_game == "1"):
            Game()

    def player_chance():
        Game.player_wins = False
        # loop repeats until someone wins or runs out of steps
        i = 0
        while((not Game.player_wins) and (i < 9)):
            if(Game.mode == "multiplayer"):
                Game.get_player_move()
                Game.check_player_win()
                Game.swap_symbols()
                i += 1
            else:
                # code to be updated for bot as a player
                Game.get_player_move()
                Game.check_player_win()
                Game.swap_symbols()
                i += 1

    def get_player_move():
        Game.add_valid_positions()
        Board.display_board()

    def check_player_win():
        if(
                # row wise conditions -> total 3 possibilities
                (Board.positions[0]== Game.symbol) and (Board.positions[1] == Game.symbol) and (Board.positions[2] == Game.symbol)) or (
                (Board.positions[3]== Game.symbol) and (Board.positions[4] == Game.symbol) and (Board.positions[5] == Game.symbol)) or (
                (Board.positions[6]== Game.symbol) and (Board.positions[7] == Game.symbol) and (Board.positions[8] == Game.symbol)) or (

                # column wise conditions -> total 3 possibilities
                (Board.positions[0]== Game.symbol) and (Board.positions[3] == Game.symbol) and (Board.positions[6] == Game.symbol)) or (
                (Board.positions[1]== Game.symbol) and (Board.positions[4] == Game.symbol) and (Board.positions[7] == Game.symbol)) or (
                (Board.positions[2]== Game.symbol) and (Board.positions[5] == Game.symbol) and (Board.positions[8] == Game.symbol)) or (

                # diagonal wise conditions -> total 2 possibilities
                (Board.positions[0]== Game.symbol) and (Board.positions[4] == Game.symbol) and (Board.positions[8] == Game.symbol)) or (
                (Board.positions[2]== Game.symbol) and (Board.positions[4] == Game.symbol) and (Board.positions[6] == Game.symbol)):
            Game.winner_symbol = Game.symbol
            Game.player_wins = True

        Game.has_game_finished()

    def swap_symbols():
        if(Game.symbol == 'X'):
            Game.symbol = '0'
        else:
            Game.symbol = 'X'

    def add_valid_positions():
        isValid = False
        while(not isValid):
            player_turn = input("Enter the position number: ")
            while(not(int(player_turn) > 0 and int(player_turn) <= 9)):
                player_turn = input("Enter a valid integer between 1 to 9, both inclusive")
            Game.player_turn = int(player_turn)
            if(Board.positions[Game.player_turn - 1] == 'X' or Board.positions[Game.player_turn - 1] == '0'):
                print("position is already filled try another place")
                isValid = False
            else:
                isValid = True
        Board.positions[Game.player_turn - 1] = Game.symbol


    def has_game_finished():
        if(not Game.player_wins):
            draw = True
            for i in range(9):
                if(Board.positions[i] != 'X' and Board.positions[i] != '0'):
                    draw = False
            if(draw):
                # if match is Draw
                Game.player_wins = False
