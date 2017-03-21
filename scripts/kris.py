#!/usr/bin/python
#dicetest
#by kris
import dice, sys

numberofdice = int(sys.argv[1]) #pulls argument after script name for number of 
dice to roll

rollit = dice.roll_d4(numberofdice)
print rollit
