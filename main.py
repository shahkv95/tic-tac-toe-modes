from game import Game

if __name__=="__main__":
    print("\nTic Tac Toe [3x3]\n")
    print("Press 1: Human vs Human")
    print("Press 2: Human vs Bot")
    print("Press any other key(s): To quit\n")

    user_choice = input("Choose your game mode to play: ")

    game = Game(user_choice)
    game.play_game()
