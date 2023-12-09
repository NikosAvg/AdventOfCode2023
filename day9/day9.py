file1 = open('day9.txt', 'r')

def diff(data):
    return [data[i] - data[i-1] for i in range(1,len(data))]
######################## Part 1 ####################################
# Predict Forward
data = [[int(x) for x in l.strip('\n').split(' ')] for l in file1.readlines()]
result = 0
for d in data:
    ends = []
    while d != [0]*len(d):
        ends.append(d[-1])
        d = diff(d)
    result+=sum(ends)
print(f'Day 9, Part 1 Result = {result}')
######################## Part 1 ####################################

######################## Part 2 ####################################
# Predict Backward
result = 0
for d in data:
    starts = []
    while d != [0]*len(d):
        starts.append(d[0])
        d = diff(d)
    starts.append(0)
    res = 0
    starts = starts[::-1]
    for i in range(len(starts)):
        res = starts[i] - res
    result += res
print(f'Day 9, Part 2 Result = {result}')
######################## Part 2 ####################################


