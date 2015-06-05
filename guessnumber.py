import random

#random no from 1 to 20
secretNumber = random.randint(1,20)
print "I'm thinking of a number between 1 and 20"
print "Take a guess. You have 6 tries."

for guesstaken in range(1,7):
	#print "Take another guess."
	guess = int(raw_input())


	if guess < secretNumber:
		print "Your guess is too low. Guess again."

	elif guess > secretNumber:
		print "Your guess is too high. Guess again"

	#if condition is correct, end loop	
	else:
		break 

if guess == secretNumber:
	print "Good job! You guessed the correct number in", guesstaken, "tries"

else:

	print 'The correct number was', secretNumber

