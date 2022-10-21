from game import Game

if __name__=="__main__":
    print("\nTic Tac Toe [3x3]\n")
    print("Press 1: To start the game")
    print("Press any key(s): To quit\n")

    user_choice = input("Do you want to start the game? ")

    game = Game(user_choice)
    game.play_game()
