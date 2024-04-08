import math
import random

class Player:
  def __init__(self,letter):
    # x or o
    self.letter=letter

  def get_move(self,game):
    pass

class RandomComputerPlayer(Player):
  def __init__(self, letter):
    super().__init__(letter)

  def get_move(self, game):
    #get a random valid spot for next move
    square=random.choice(game.available_moves())
    return square

class HumanPlayer(Player):
  def __init__(self, letter):
    super().__init__(letter)

  def get_move(self, game):
    valid_square=False
    val=None
    while not valid_square:
      square=input(' X player Input move (0-9)')
      #we are going to check that this is correct value by trying to cast
      try:
        val=int(square)
        if val not in game.available_moves():
          raise ValueError
        valid_square=True
      except ValueError:
        print("Invalid Square .Try again")

    return val