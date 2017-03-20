#!/usr/bin/python
#rev 0.01
#writen by Kevin Burkeland
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
		print "bonk"
		break
	if choice == 2:
		print "foo"
		break
	if choice == 3:
		print "bar"
		break
	if choice == 4:
		print "thing"
		break
	print "you cheeky bastard"

