from random import randint
import sys


def roll():
	
	useroll = raw_input("Roll the dice?? Press enter to continue >>")
	print "You rolled a ", randint (1, 6)
	rollAgain()

def rollAgain():

	while True:
		again = raw_input("Try again? Enter y/n : ")

		if again == 'n':
			print "Thanks for playing!"
			sys.exit()

		elif again == 'y':
			print "Lets roll again"
			roll()

		else:
			print "Please enter 'y' or 'n'"	


roll()