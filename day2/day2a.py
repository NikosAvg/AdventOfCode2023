import re
file1 = open('day2.txt', 'r')
Lines = file1.readlines()


def check_valid_game(Lines):
    valid_games = 0
    
    for l in Lines:
        #print(l)
        red=True
        blue=True
        green=True
        total_red = 12
        total_green = 13
        totel_blue = 14
        for i in range(len(l)):
            if l.startswith('red', i):
                # print('Red:')
                # print(l[i-3:i-1])
                if total_red<int(l[i-3:i-1]):
                    red=False
            elif l.startswith('green', i):
                # print('Green:')
                # print(l[i-3:i-1])
                if total_green<int(l[i-3:i-1]):
                    green=False
            elif l.startswith('blue', i):
                # print('Blue:')
                # print(l[i-3:i-1])
                if totel_blue<int(l[i-3:i-1]):
                    blue=False
        if red and blue and green:
            print(re.sub("\D",'', l[4:7]))
            valid_games+=int(re.sub("\D",'', l[4:7]))
    return valid_games

print(check_valid_game(Lines))
    