from abc import ABC, abstractmethod
from move import Move
import random

class Player(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def choose_move(self) -> Move:
        pass

class HumanPlayer(Player):
    def choose_move(self) -> Move:
        while True:
            print("\nChoose your move:")
            print("1. 🪨 Rock")
            print("2. 📄 Paper")
            print("3. ✂️ Scissors")

            choice = input("Select 1, 2 or 3: ").strip()
            if choice == '1':
                return Move.ROCK
            elif choice == '2':
                return Move.PAPER
            elif choice == '3':
                return Move.SCISSORS
            else:
                print("Invalid option. Please try again.")

class RandomComputerPlayer(Player):
    def __init__(self):
        random_name = self.__generate_random_name()
        super().__init__(random_name + " (bot)")

    def choose_move(self) -> Move:
        return random.choice(list(Move))
    
    def __generate_random_name(self) -> str:
        bot_names = ["Patito Juan", "Dominik Mysterio", "Penta Zero Miedo", "Sonic el Jechjog", "Alberto"]
        
        return random.choice(bot_names)