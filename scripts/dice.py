#!/usr/bin/python
def roll_d6(number_of_dice):
    rolls = []

    for _ in range(number_of_dice):
        roll = random.randint(1,6)
        rolls.append(roll)

    return rolls
