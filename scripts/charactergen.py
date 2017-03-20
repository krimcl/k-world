#!/usr/bin/python
#rev 0.01
#writen by Kevin Burkeland
import dice
print "Welcome to revision .01 of Kevin Burkelands Pathfinder Character Gen script"
print "Pick your stat gen style:"
print "1. Generous: 4d6 drops the lowest and gives you one 18 to start with"
print "2. Standard: roll 4d6 drops the lowest"
print "3. Rough: 3d6, thats all you get"
print "4. Old school: 3d6 down the line, you don't get to choose which role goes where"
#restart if they don't answer properly
while True:
	#gets the choice var
	choice = input('Enter your choice [1-4]:')
	#makes sure its a number
	choice = int(choice)
	if choice == 1:
		stats = []
		for _ in range(5):
			rolls = dice.roll_d6(4)
			stat = sum(rolls) - min(rolls)
			stats.append(stat)
		stats.append(18)
		print stats
		break
	if choice == 2:
		stats = []
		for _ in range(6):
			rolls = dice.roll_d6(4)
			stat = sum(rolls) - min(rolls)
			stats.append(stat)
		print stats
		break
	if choice == 3:
		stats = []
		for _ in range(6):
			rolls = dice.roll_d6(3)
			stat = sum(rolls)
			stats.append(stat)
		print stats
		break
	if choice == 4:
		print "work in progress comming soon"
		break
	print "please try again"

