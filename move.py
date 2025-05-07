from enum import Enum

class Move(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"
    
    def beats(self, other: 'Move') -> bool:
        if self == Move.ROCK and other == Move.SCISSORS:
            return True
        if self == Move.PAPER and other == Move.ROCK:
            return True
        if self == Move.SCISSORS and other == Move.PAPER:
            return True
        
        return False # player 1 didn't win with rock, paper or scissors

EMOJI_MAP = {
    Move.ROCK: "🪨",
    Move.PAPER: "📄",
    Move.SCISSORS: "✂️",
}