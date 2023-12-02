
import re
file1 = open('day1.txt', 'r')
Lines = file1.readlines()

texted_nums = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
    }
sum = 0
for l in Lines:
    print(l)
    dic = {}
    for k in texted_nums.keys():
        if k in l:
            for i in range(len(l)):
                if l.startswith(k, i):
                    dic[i] = int(texted_nums[k])

    digits = {m.start(0):int(m.group(0)) for m in re.finditer("\d", l)}
    print(dic, digits)
    fin = {**digits,**dic}
    print(int(str(fin[min(fin.keys())])+str(fin[max(fin.keys())])))
    sum += int(str(fin[min(fin.keys())])+str(fin[max(fin.keys())]))

print(sum)