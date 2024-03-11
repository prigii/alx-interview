# Prime Number Game

## Description
This program simulates a game where players take turns choosing prime numbers and removing their multiples from a set of consecutive integers. The player who cannot make a move loses the game. The program determines the winner of each round based on optimal play.

## Usage
To use the program, call the `isWinner` function with the number of rounds (`x`) and an array of `nums`, where each element represents the value of `n` for each round. The function returns the name of the player with the most wins, or `None` if the winner cannot be determined.

Example:
```python
x = 3
nums = [4, 5, 1]
print(isWinner(x, nums))  # Output: Ben
