import random

#compare choices
def compare (c1, c2):

#if equal
	if (c1 == c2):
		print "It's a tie"

#if c1 is paper
	elif (c1 == "paper"):

		if (c2 == "rock"):
			print "Paper wins!"

		else:
			print "scissors wins!"

#if c1 is scissors
	elif (c1 == "scissors"):

		if (c2 == "rock"):
			print "Rock wins!"

		else:
			print "Paper wins!"

#if c1 is rock
	elif (c1 == "rock"):
	
		if (c2 == "paper"):
			print "Paper wins!"

		else:
			print "Rock wins!"	

	
#user input
def userC ():
	user = raw_input("Rock, Paper or Scissors? >>")

	user = user.lower()


	user_table = ['rock', 'paper', 'scissors']

	while user not in user_table:
		print "Invalid entry"
		user = raw_input("Rock, Paper or Scissors? >>")

	return user


#comp input
def compC ():
	#generate random floating point no 0 to 1
	comp = random.random()

	#print the random no.
	#print comp

	#this will assign rock,paper, scissors based on random no.
	if comp < 0.34:

		comp = "rock"

	elif 0.34 < comp < 0.67 :

		comp = "paper"
		
	else:
		comp = "scissors"

	return comp


#main function  
def main():

	print "Lets play rock paper scissors!"

	user = userC()

	comp = compC()

	
	#print choices, winner
	print "\n", "Computer chose %s" %comp		

	print "You chose %s" %user

	print "%s vs %s" %(comp, user)

	print "*" * 20, "\n"  
	
	compare(user, comp)

	print "*" * 20, "\n" 


#run prog
main()



