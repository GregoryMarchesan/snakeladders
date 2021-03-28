# Snakes And Ladders

## Project Motivation

The code provided here performs the Snakes And Ladders game, as depicted in the image below.

![SnakeandLadders](https://github.com/GregoryMarchesan/snakeladders/blob/master/snakeladders/docs/snakeladders_img.png)



The basic idea of the game is as follows: Each player begins on square 1 and takes turns rolling a fair 6-sided 
die. The player moves the number of spaces indicated on the die. If you land at the bottom of a ladder, you automatically move to the square 
at the top of the ladder. Conversely, if you land on a snake head, then you fall to the square at the snake's tail. The winner is the first person to 
make it onto or past the last square.


## Code Usage
The code contains some basic features for the snakes and ladders game. There are three main classes:
- SnakeLadders: The game itself, with two players and following the above logic
- SimulateGame: Passing a game, it perform the number of simulations required
- Overrall Statistics: Calculate the statistics to games simulated

A simple example to run different simulations of the game is depicted below:

'''
game = SnakeLadders()
simulate = Simulate_game()
stats_Q1 = simulate.simulate(game, SIMULATION_TIMES)
'''
where the stats_Q1 will get all statistic results for all the number of times to simulate specified in SIMULATION_TIMES. Additionally, if you want to make this the backend of any frontend game of snake and ladders, you can use the 'walk' method from 'SnakeLadders' class which will move each player consistently to the appropriete place.

## Instalation
- Numpy (1.16.2)
- Datetime (4.3)
- Random

## Acknowledgements & Licensing

The code provided here is free to use and it is under MIT Licensing.
