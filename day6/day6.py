from functools import reduce
import re
import math

file1 = open('day6.txt', 'r')
############## Part 1 ######################
# Brute Force Solution because the numbers are small and allow it.
times,distance = file1.readlines()
times1 = [int(s) for s in re.split('[\s,]+',times) if s.isdigit()]
distance1 = [int(s) for s in re.split('[\s,]+',distance) if s.isdigit()]

total = []
for t,d in zip(times1,distance1):
    count=0
    for i in range(t):
        if i*(t-i) > d:
            print(i, i*(t-i))
            count+=1
    total.append(count)

result = reduce((lambda x, y: x * y), total)
print(f'Day 6, Part 1 Result = {result}')

############## Part 1 ######################

############## Part 2 #####################
# Brute Force takes too much time.
# Solving the quadratic inequality -i^2 + ti - d > 0, you can find the lower and upper limits of the range. 
# The range between these roots represents the intervals where the inequality is satisfied, indicating where the expression is positive.
# By calculating the roots, you establish the lower and upper bounds of the range.
# The length of this range provides the solution to the quadratic inequality.

times2 = int(re.sub('\D+','',times))
distance2 = int(re.sub('\D+','',distance))

sol1 = (-times2 + math.sqrt(times2**2 - 4*distance2))/(-2)
sol2 = (-times2 - math.sqrt(times2**2 - 4*distance2))/(-2)

lower_lim = min(sol1,sol2)
upper_lim = max(sol1,sol2)

result=len(list(range(math.ceil(lower_lim),math.ceil(upper_lim))))

print(f'Day 6, Part 2 Result = {result}')

############# Part 2 ######################


