import re,math

####### Part 1 ####################
file1 = open('day8.txt', 'r')
Lines = file1.readlines()
intrstruction = [*Lines[0].strip('\n')]
mapp = {}
for i in range(2,len(Lines)):
    Lines[i] = Lines[i].strip('\n').replace(' ','')
    mapp[Lines[i][:3]] = {'L': Lines[i][5:8],'R': Lines[i][9:12]}
steps = 0
prev_position = 'AAA'
found = False
while True:
    for i in intrstruction:
        current_position = mapp[prev_position][i]
        steps+=1
        if current_position == 'ZZZ':
            found = True
            break
        else:
            prev_position = current_position
    
    if found:
        break
        
print(f'Day 8, Part 1 = {steps}')
####### Part 1 ####################

####### Part 2 ####################
file2 = open('day8.txt', 'r')
Lines = file2.readlines()

intrstruction = [*Lines[0].strip('\n')]
# Match All starting points that end with **A
mapp = {}
for i in range(2,len(Lines)):
    Lines[i] = Lines[i].strip('\n').replace(' ','')
    mapp[Lines[i][:3]] = {'L': Lines[i][5:8],'R': Lines[i][9:12]}

starts = [x for x in mapp.keys() if x.endswith('A')]
step = []
for s in starts:
    print(s)
    prev_position = s
    found = False
    steps=0
    while True:
        for i in intrstruction:
            current_position = mapp[prev_position][i]
            steps+=1
            if current_position.endswith('Z'):
                found = True
                break
            else:
                prev_position = current_position
        
        if found:
            step.append(steps)
            break

print(f'Day 8, Part 2 = {math.lcm(*step)}')
####### Part 2 ####################

