# Code created by Grégory Marchesan to perform the Snake Ladders game

import numpy as np
import random
from datetime import datetime

# Represents a die
def roll_die():
  """
  Represents a die and returns a random number between 1 and 6

  Returns:
  (int): a random number between 1 and 6
  """
  return random.randint(1, 6)
  
# Represents each player in the game
class Player:

  """
  Represents each player in the game Snakes And Ladders
  """

  def __init__(self):
    """
    Initializes the player

    Initializes the game, with the start position to each player as 1, 
    resets the game counter, resets the snakes immunity,
    sets 0 to avoid ladder probability, and resets counters for snakes and ladders

    """
    self.position = 1                # position
    self.wins = 0                    # number of wins
    self.snakes_immunity = 0         # number of snakes immunity
    self.avoid_ladder_prob = 0       # probability to avoid a ladder
    self.snakes = 0                  # overall snakes count
    self.ladder = 0                  # overall ladders count

  def set_start_position(self, position):
    """ Sets the start position to the player """

    self.position = position

  def move(self, newPos):
    """ Moves the player to the new position """

    self.position = newPos

  def win(self):
    """ Counts the number of wins for the player"""
    self.wins = self.wins + 1

  def set_snake_immunity(self, number_immunity):
    """ Set the immunity for snakes for the player. The default is 0"""
    self.snakes_immunity = number_immunity

  def set_avoid_ladder_prob(self, prob):
    """ Set the probability of the player avoid ladders. The Default is 0"""

    self.avoid_ladder_prob = prob

class GameStatistics:
  """ Collects statistics of each game """

  def __init__(self):
    """ Resets players and statistics """
    self.winner = 0               # winner (1 or 2)
    self.rolls = 0                # rolls/rounds of game
    self.snakes_usage = 0         # number of snakes usage
    self.ladder_usage = 0         # number of ladders usage
    self.player1 = Player()       # players
    self.player2 = Player()       #
    
  def update_statistics(self, winner, rolls, snakes_usage, ladder_usage, player1, player2):
    """ Update statistics after each game """
    self.winner = winner
    self.rolls = rolls
    self.snakes_usage = snakes_usage
    self.ladder_usage = ladder_usage
    self.player1 = player1
    self.player2 = player2
     
class OverallStatistics(GameStatistics):
    """ Collects statistics of all simulated games """

    def __init__(self):
      """ Same attributes of game statistics (but winner) applied to all games """
      super().__init__()
      
    def update_statistics(self, game_statistics):
      """Accumulates statistics  for all games
      
      Parameters:
      game_statistics (GameStatistics): The statistics for each game to be summarized in this object
      """
      self.rolls = self.rolls + game_statistics.rolls 
      self.snakes_usage = self.snakes_usage + game_statistics.snakes_usage
      self.ladder_usage = self.ladder_usage + game_statistics.ladder_usage
      self.player1.wins = game_statistics.player1.wins + self.player1.wins
      self.player2.wins = game_statistics.player2.wins + self.player2.wins
      self.player1.snakes = game_statistics.player1.snakes + self.player1.snakes
      self.player2.snakes = game_statistics.player2.snakes + self.player2.snakes
      self.player1.ladder = game_statistics.player1.ladder + self.player1.ladder
      self.player2.ladder = game_statistics.player2.ladder + self.player2.ladder
      
    def toString(self):
      """Print overall statistics"""
      print("\nTotal number of rolls: %s\nPlayer 1 wins: %s\nPlayer 2 wins: %s\nTotal number of snakes used: %s\nTotal number of ladders used: %s\n" % (self.rolls, self.player1.wins, self.player2.wins, self.snakes_usage, self.ladder_usage))

class SnakeLadders:
  """The Snake Laddders original game, using Player and GameStatistics class"""

  def __init__(self):
    """ Initializes players, round and statistics"""
    self.player1 = Player()          # players
    self.player2 = Player()          # 
    self.currentPlayerTurn = 1       # turns
    self.round = 1                   # rounds
    random.seed(datetime.now())          # seed to die roll
    self.statistics = GameStatistics()   # game statistics
    
  def restart(self):
    """ Restart an created game"""
    self.player1 = Player()
    self.player2 = Player()
    self.currentPlayerTurn = 1
    self.round = 1
    random.seed(datetime.now())
    self.statistics = GameStatistics()
    
  def play(self):
    """ Plays the game - walk until the end
    
    Used to collect statistics about the game
    """
    while(self.walk() == 0):           # continues to play
      
      # change turn
      if(self.currentPlayerTurn == 1):
        self.currentPlayerTurn = 2
      else:
        self.currentPlayerTurn = 1
        
      self.round = self.round + 1      # increases round
      
    winner = self.currentPlayerTurn    # find the winner
    
    # update statistics
    self.statistics.update_statistics(winner, self.round, 
                                      self.player1.snakes + self.player2.snakes, 
                                      self.player1.ladder + self.player2.ladder, 
                                      self.player1, self.player2)
    return self.statistics
    
  def walk(self):
    """ Walk through the game applying snakes and ladders"""

    # instance to player
    if (self.currentPlayerTurn == 1):
      currentPlayer = self.player1
    else:
      currentPlayer = self.player2
        
    die_data = roll_die()   # roll die
    initial_position = currentPlayer.position
    next_position = die_data + initial_position  # finds the next position
    

    if(next_position >= 36): # end game
      currentPlayer.win()
      return self.currentPlayerTurn # returns the winner
    
    # ladders
    elif(next_position == 3):
      next_position = 16
      currentPlayer.ladder = currentPlayer.ladder + 1
    elif(next_position == 5):
      next_position = 7
      currentPlayer.ladder = currentPlayer.ladder + 1
    elif(next_position == 15):
      next_position = 25
      currentPlayer.ladder = currentPlayer.ladder + 1
    elif(next_position == 18):
      next_position = 20
      currentPlayer.ladder = currentPlayer.ladder + 1
    elif(next_position == 21):
      next_position = 32
      currentPlayer.ladder = currentPlayer.ladder + 1
      
    # snakes
    elif(next_position == 12):
      next_position = 2
      currentPlayer.snakes = currentPlayer.snakes + 1 
    elif(next_position == 14):
      next_position = 11
      currentPlayer.snakes = currentPlayer.snakes + 1
    elif(next_position == 17):
      next_position = 4
      currentPlayer.snakes = currentPlayer.snakes + 1
    elif(next_position == 31):
      next_position = 19
      currentPlayer.snakes = currentPlayer.snakes + 1
    elif(next_position == 35):
      next_position = 22
      currentPlayer.snakes = currentPlayer.snakes + 1
      
    currentPlayer.move(next_position) # move player
    return 0 # continues to play
    
class Simulate_game:
  """ Simulation of the game"""

  def __init__(self):
    """ Initializes the game simulation reseting the statistics"""
    self.overallStatistics = OverallStatistics()
  
  def simulate(self, game, times): # plays all the "times"
    """ Simulate the game, running the 'times' passed argument'

    Parameters:
    game (SnakeLadders): The game reference
    times (int): The number of simulations to be performed

    Returns:
    OverallStatistics: All statistics collected using the simulation as an object
    """
    for _ in range(0, times):
      stat = game.play()   # plays
      game.restart()       # starts a new game
      self.overallStatistics.update_statistics(stat) # update statistics
    return self.overallStatistics


