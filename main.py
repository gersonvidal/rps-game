from player import HumanPlayer, RandomComputerPlayer
from colors import colorize, BOLD, CYAN, YELLOW
from game import Game

def main():
    print(colorize("Welcome to Rock, Paper, Scissors!", BOLD))
    player_name = input("What's your name? ").strip()
    player1 = HumanPlayer(player_name)

    while True:
        player2 = RandomComputerPlayer()
        game = Game(player1, player2)

        print(colorize(f"\nHello, {player1.name}! You are playing against {player2.name}.", CYAN))

        while not game.has_winner():
            game.play_round()

        winner = game.get_winner()
        print(colorize(f"\n🏆 {winner} wins the game! 🏆", BOLD, YELLOW))
        
        play_again = input(colorize("\nDo you want to play again? (y/n): ", CYAN)).strip().lower()
        if play_again != 'y':
            print(colorize("\nThanks for playing! Goodbye!", BOLD, YELLOW))
            break

if __name__ == "__main__":
    main()