# 06 Objects-Oriented Programming (OOP)
    # Abstraction
#018 Lab: Build a Player Interface

from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0,0)
        self.path = [self.position]

    def make_move(self):
        new_move = random.choice(self.moves)
        x, y = self.position
        dx, dy = new_move
        new_position = (x + dx, y + dy)
        self.position = new_position # il giocatore ora si trova nella nuova posizione, gli spostamenti successivi partiranno da qui
        self.path.append(new_position)
        return new_position
    
    @abstractmethod
    def level_up():
        pass
# l'astrazione impedisce a qualcuno di usare una classe che non è ancora completa. 

# La classe Player agisce come un "contratto". 
# Dice: "Io so come muovermi (logica in make_move), ma non so quali siano le direzioni possibili finché 
# non mi dici che tipo di giocatore sono".
class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(0,1), (0,-1), (-1,0), (1,0)] # up, down, left, right

    def level_up(self):
        self.moves += [(1,1), (1,-1), (-1,-1), (-1,1)] # adding more moves to the moves attribute, representing the four diagonal movements (for example, 1 unit down plus 1 unit left)

p = Pawn()
p.make_move()