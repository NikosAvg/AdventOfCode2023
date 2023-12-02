import re

import re
file1 = open('day2.txt', 'r')
Lines = file1.readlines()

def check_valid_game(Lines):
    total_power = 0
    for l in Lines:
        red=[]
        blue=[]
        green=[]
        for i in range(len(l)):
            if l.startswith('red', i):
                red.append(int(l[i-3:i-1]))
            elif l.startswith('green', i):
                green.append(int(l[i-3:i-1]))
            elif l.startswith('blue', i):
                blue.append(int(l[i-3:i-1]))
        print(red,green,blue)
        power=max(red)*max(green)*max(blue)
        print(power)
        total_power+=power
    return total_power

print(check_valid_game(Lines))
