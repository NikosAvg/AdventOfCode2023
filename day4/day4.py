import re
data = []
with open('day4.txt') as f:
    for line in f:
        data.append(line)


######## Part 1 ###########

total = 0
for d in data:
    count=0
    winning_nums = d.replace('\n','').split(':')[1].split('|')[0].split()
    our_nums = d.replace('\n','').split(':')[1].split('|')[1].split()
    for w in winning_nums:
        if w in our_nums:
            count+=1
            #print(w)
    if count>0:
        total += 2**(count-1)

print(f'Day 4 Part 1 Total = {total}')

######## Part 1 ###########

######## Part 2 ###########

count=len(data)*[0]
for i in range(len(data)):
    total = 0
    count[i]+=1
    winning_nums = data[i].replace('\n','').split(':')[1].split('|')[0].split()
    our_nums = data[i].replace('\n','').split(':')[1].split('|')[1].split()
    for w in winning_nums:
        if w in our_nums:
            total+=1
    for j in range(1,total+1):
        count[i+j]+=count[i]

print(f'Day 4 Part 2 Total = {sum(count)}')
######## Part 2 ###########
    
    