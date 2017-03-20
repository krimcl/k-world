#!/usr/bin/python
#rev 0.01
#writen by Kevin Burkeland
import dice, mod, cclass
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
		#initialize the stats array
		stats = []
		#rolls 5 times
		for _ in range(5):
			rolls = dice.roll_d6(4)
			stat = sum(rolls) - min(rolls)
			stats.append(stat)
		#adds the 18
		stats.append(18)
		print stats
		break
	if choice == 2:
		#initialize the stats array
		stats = []
		#rolls 6 times
		for _ in range(6):
			rolls = dice.roll_d6(4)
			stat = sum(rolls) - min(rolls)
			stats.append(stat)
		print stats
		break
	if choice == 3:
		#initialiaze the stats array
		stats = []
		#rolls 6 times
		for _ in range(6):
			rolls = dice.roll_d6(3)
			stat = sum(rolls)
			stats.append(stat)
		print stats
		break
	if choice == 4:
		attrib = ["str","dex","con","int","wis","cha"]
		stats = []
		for _ in range(6):
                        rolls = dice.roll_d6(3)
                        stat = sum(rolls)
                        stats.append(stat)
		attribs = dict(zip(attrib, stats))
		print attribs		
		break
	print "please try again"
#start of attributes
attrib = ["str","dex","con","int","wis","cha"]
if 'attribs' not in locals():
	attribs = {}
	for _ in attrib:
		while True:
			stat = int(input('what do you want '+str(_)+' to be: '))
			if stat in stats:
				attribs[_] = stat
				stats.remove(stat)
				print stats
				break
			else:
				print "you didn't roll that"
				print stats
#end of first attributes section
amods = mod.ablemod(attribs)
print amods
