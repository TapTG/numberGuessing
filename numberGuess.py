"""
Chapter 3 Example
Program: numberGuess.py
Author: Teri  06.22.23

Python version of the number guessing game. User will provide the range of numbers for the game. Program will guide the user until they get the right number.
"""

import random

# Input phase
smaller = int(input("Please, enter the smaller number: >>"))
larger = int(input("Now, please enter the larger number: >>"))

# Processing phase
magicNum = random.randint(smaller, larger)
count = 0

while True: 
	count += 1
	userNumber = int(input("Enter your guess: >>"))

	if userNumber < magicNum:
		print("Sorry, your guess was too SMALL")
	elif userNumber > magicNum:
		print("Sorry, your guess was too LARGE")
	else:
		print("Congratulations! You've got it in", count, "tries!")
		break
input("Thank you for playing! Press ENTER to quit.")