from Live import load_game, welcome

'''#from MemoryGame import play
#from GuessGame import play
#from CurrencyRouletteGame import play


def main():
    name = welcome()
    game_choice, game_difficulty = load_game()
    
    # Now you can use them:
    if game_choice and game_difficulty:
        print(f"Hello {name}, you chose game {game_choice} with difficulty {game_difficulty}!\n")
        # Add logic to launch the selected game here

''' 


# Import game modules (assuming each has a play(difficulty) function)
import GuessGame
import MemoryGame
import CurrencyRouletteGame

def main():
    name = welcome()
    game_choice, game_difficulty = load_game()
    
    if game_choice and game_difficulty:
        print(f"Hello {name}, you chose game {game_choice} with difficulty {game_difficulty}!\n")

    # Route to the selected game
        if game_choice == 1:
            MemoryGame.play(game_difficulty)
        elif game_choice == 2:
            GuessGame.play(game_difficulty)
        elif game_choice == 3:
            CurrencyRouletteGame.play(game_difficulty)
        else:
            print("Invalid game choice. Exiting.")

if __name__ == '__main__':
    main()