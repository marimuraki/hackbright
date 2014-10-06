# Guessing Game
# 	The computer will choose a random number between 1 and 100, 
#	and ask the user to guess the number, giving them a hint if it's high or low. 

# Source: https://github.com/chriszf/Hackbright-Curriculum/tree/master/Exercise01

from random import randint

name = raw_input("Hi, what's your name? ")
print name + ", I'm thinking of a number between 1 and 100."
print "You have 10 tries to guess it."

number = randint(1, 100)

counter = 0
while counter < 10:
	counter += 1
	guess = raw_input("Your guess? ")
	try:
		guess = int(guess)
		if guess == number:
			print "You got it in " + str(counter) + " tries!"
			break
		else:
			if guess < number:
				print "Your guess is too low. Try again."
			if guess > number:
				print "Your guess is too high. Try again."	
	except ValueError:
		print("Try again. Guess a number.")

print "The number was " + str(number) + "."

