
import re

file1 = open('day1.txt', 'r')
Lines = file1.readlines()
sum = 0
for l in Lines:
    sum += int(re.sub('\D', '', l)[0]+re.sub('\D', '', l)[-1])
print(sum)