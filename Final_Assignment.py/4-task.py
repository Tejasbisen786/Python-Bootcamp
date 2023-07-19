import random

print("Welcome to Roll And Dice")
num_players = int(input("Enter the number of players: "))

players = {}
for i in range(1, num_players + 1):
    name = input(f"Enter the name of player {i}: ")
    players[name] = 0

print("Let's roll the dice!")

for name in players.keys():
    input(f"{name}, press Enter to roll the dice...")
    dice_roll = random.randint(1, 6)
    players[name] = dice_roll
    print(f"{name} rolled a {dice_roll}!")

winner = max(players, key=players.get)
max_roll = players[winner]

print(f"\nAnd the winner is... {winner} with a roll of {max_roll}! Congratulations!")
import random  # use random module for generating the random value 

print("Welcome to the Roll And Dice game")
numPlayers = int(input("Enter the number of players: ")) # taking number of player in input 

players = {}   # use dictionary type to store the name and it store value in key value pair
for i in range(1, numPlayers + 1):
    name = input(f"Enter the name of player {i}: ")   # here entering player name 
    players[name] = 0

print("Roll A Dice")

for name in players.keys():  
    input(f"{name}, press Enter to roll the dice...")
    dice_roll = random.randint(1, 6)   # Genrating the random value in between 1 to 6 
    players[name] = dice_roll    # String the random value in player as in form of value pair in dictonary 
    print(f"{name} rolled Number:  {dice_roll}")

winner = max(players, key=players.get)    #it return the max roll dice  value 
max_roll = players[winner]

print(f"\nAnd the winner is... {winner} with a roll of {max_roll}! Congratulations ")
