from colors import colorize, BOLD, GREEN, BLUE, RED, MAGENTA
from move import EMOJI_MAP
from player import Player

class Game:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.scores = [0, 0]

    def play_round(self):
        player1_move = self.player1.choose_move()
        player2_move = self.player2.choose_move()

        print(colorize(f"\n{self.player1.name} chose: {EMOJI_MAP[player1_move]} {player1_move.value.capitalize()}", BLUE))
        print(colorize(f"{self.player2.name} chose: {EMOJI_MAP[player2_move]} {player2_move.value.capitalize()}", RED))

        if player1_move == player2_move:
            print(colorize("It's a tie!", BOLD, MAGENTA))
        elif player1_move.beats(player2_move):
            print(colorize(f"{self.player1.name} wins this round!", BOLD, GREEN))
            self.scores[0] += 1
        else:
            print(colorize(f"{self.player2.name} wins this round!", BOLD, RED))
            self.scores[1] += 1

    def has_winner(self) -> bool:
        return any(score == 2 for score in self.scores)

    def get_winner(self) -> str:
        return self.player1.name if self.scores[0] == 2 else self.player2.name
