import re
import operator

file = open('day7.txt', 'r')
Lines = file.readlines()
Game_Dict = {
    'Five of a kind':  [],
    'Four of a kind': [],
    'Full house': [],
    'Three of a kind': [],
    'Two pair': [],
    'One pair': [],
    'High Card': []
    }

max_points = len(Lines)

for i in range(len(Lines)):
    hand,points = Lines[i].strip('\n').split(' ')
    
    # Count Character Frequency of the Hand
    all_freq = {}
    contains_j = False
    for j in hand:
        if j=='J':
            contains_j = True
        if j in all_freq:
            all_freq[j] += 1
        else:
            all_freq[j] = 1
    count_j = 0
    if contains_j:
        count_j = all_freq['J']

    # Find the max value with an other way
    max_value = max(all_freq.values())
    max_count = list(all_freq.values()).count(max_value)
    tmp = {'Hand': hand,'Points': int(points),' Js': count_j}

    print(len(all_freq),all_freq)
    # if len(all_freq) == 1:
    #     Game_Dict['Five of a kind'].append(tmp)
    # elif len(all_freq) == 2 and max_value == 4:
    #     if count_j == 0:
    #         Game_Dict['Four of a kind'].append(tmp)
    #     elif count_j == 1:
    #         Game_Dict['Five of a kind'].append(tmp)
    # elif len(all_freq) == 2 and max_value == 3:
    #     if count_j == 0:
    #         Game_Dict['Full house'].append(tmp)
    #     else: 
    #         Game_Dict['Five of a kind'].append(tmp)
    # elif len(all_freq) == 3 and max_value == 2 and max_count == 2:
    #     if count_j == 0:
    #         Game_Dict['Two pair'].append(tmp)
    #     elif count_j == 1:
    #         Game_Dict['Full house'].append(tmp)
    #     else:
    #         Game_Dict['Four of a kind'].append(tmp)
    # elif len(all_freq) == 4 and max_value == 2:
    #     if count_j == 0:
    #         Game_Dict['One pair'].append(tmp)
    #     else:
    #         Game_Dict['Three of a kind'].append(tmp)
    # elif len(all_freq) == 5:
    #     if count_j == 0:
    #         Game_Dict['High Card'].append(tmp)
    #     else:
    #         Game_Dict['One pair'].append(tmp)


    if len(all_freq) == 1: 
        Game_Dict['Five of a kind'].append(tmp)

    elif len(all_freq) == 2 and max_value==4 and count_j != 0:
        Game_Dict['Five of a kind'].append(tmp)
    elif len(all_freq) == 2 and max_value==4 and count_j == 0:
        Game_Dict['Four of a kind'].append(tmp)
    elif len(all_freq) == 2 and max_value==3 and count_j != 0:
        if count_j == 1:
            Game_Dict['Four of a kind'].append(tmp)
        else:
            Game_Dict['Five of a kind'].append(tmp)
    elif len(all_freq) == 2 and max_value==3 and count_j == 0:
        Game_Dict['Full house'].append(tmp)



    elif len(all_freq) == 3 and max_value==3 and count_j != 0:
        if count_j == 1:
            Game_Dict['Four of a kind'].append(tmp)
        else:
            Game_Dict['Full house'].append(tmp)
    elif len(all_freq) == 3 and max_value==3 and count_j == 0:
        Game_Dict['Three of a kind'].append(tmp)

    elif len(all_freq) == 3 and max_value==2 and max_count==2 and count_j == 0:
        Game_Dict['Two pair'].append(tmp)
    elif len(all_freq) == 3 and max_value==2 and max_count==2 and count_j != 0:
        if count_j == 1:
            Game_Dict['Full house'].append(tmp)
        else:
            Game_Dict['Four of a kind'].append(tmp)


    elif len(all_freq) == 4 and max_value==2 and count_j == 0:
        Game_Dict['One pair'].append(tmp)
    elif len(all_freq) == 4 and max_value==2 and count_j != 0:
        Game_Dict['Three of a kind'].append(tmp)

    elif len(all_freq) == 5 and count_j == 0:
        Game_Dict['High Card'].append(tmp)
    elif len(all_freq) == 5 and count_j != 0:
        Game_Dict['One pair'].append(tmp)
        

def custom_priority(char):
    priorities = {
    'A': 12,
    'K': 11,
    'Q': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1,
    'J': 0
}
    return priorities.get(char, 0)  # Default to 0 if character not in the dictionary

def custom_sort_string(item):
    return [custom_priority(char) for char in item['Hand']]

total_points = 0
for key in Game_Dict:
    Game_Dict[key] = sorted(Game_Dict[key], key=custom_sort_string,reverse=True)
    for v in  Game_Dict[key]:
        print(v['Hand'])
        total_points += v['Points']*max_points
        max_points-=1

print(f'Day 7, Part 2 Result = {total_points}')



