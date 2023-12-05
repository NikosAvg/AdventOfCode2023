import numpy as np
import concurrent.futures


def split_list(input_list, delimiter):
    result = []
    for item in input_list:
        if item == delimiter:
            result.append([])
        else:
            result[-1].append(item)
    return result

def map_creation(sublists):
    map_dictionary = {
                    'source': [],
                    'destination': [],
    }
    tmp_list = []
    for d in sublists[1:]:
        tmp = d.strip('\n').split(' ')
        nums = [int(t) for t in tmp]
        tmp_list.append(nums)
    tmp_list = np.array(tmp_list)

    for s,r in zip(tmp_list[:, 1],tmp_list[:,2]):
        map_dictionary['source'].append([s,s+r-1])
    
    for s,r in zip(tmp_list[:, 0],tmp_list[:,2]):
        map_dictionary['destination'].append([s,s+r-1]) 

    return map_dictionary


def find_dest(map_dict,value):
    #print(map_dict['source'],map_dict['destination'])
    for pair,s in zip(map_dict['source'],map_dict['destination']):
        
        if value >= pair[0] and value <= pair[1]:
            dist = value - pair[0]
            return dist + s[0]
            return dest
        else:
            dest = value
    return dest


########## Part 1 ######################
data = []
with open('day5.txt') as f:
    for line in f:
        data.append(line)

seeds = data[0][7:].strip('\n').split(' ')
# Filter Data out in sublists
sublists = split_list(data[1:],'\n')
# Create Source and Destination Dictionary for Seed to Soil
seed_to_soil_map = map_creation(sublists[0])
# Create Source and Destination Dictionary for Soil to Fertilizer
soil_to_fert_map = map_creation(sublists[1])
# Create Source and Destination Dictionary for Fertilizer to Water
fert_to_water_map = map_creation(sublists[2])
# Create Source and Destination Dictionary for Water to Light
water_to_light_map = map_creation(sublists[3])
# Create Source and Destination Dictionary for Light to Temperature
light_to_temp_map = map_creation(sublists[4])
# Create Source and Destination Dictionary for Temperature to Humidity
temp_to_hum_map = map_creation(sublists[5])
# Create Source and Destination Dictionary for Humidity to Location
hum_to_loc_map = map_creation(sublists[6])


# Check if any of the seed is in the source value?
positions = []
for s in seeds:
    soil = find_dest(seed_to_soil_map,int(s))
    fert = find_dest(soil_to_fert_map,soil)
    water = find_dest(fert_to_water_map,fert)
    light = find_dest(water_to_light_map,water)
    temp = find_dest(light_to_temp_map,light)
    hum = find_dest(temp_to_hum_map,temp)
    loc = find_dest(hum_to_loc_map,hum)
    positions.append(loc)
    #print(soil,fert,water,light,temp,hum,loc)

print(f'Day 5, Part 1 = {min(positions)}')

########## Part 1 ######################
   
########## Part 2 ######################
def generate_numbers(pair):
    start, rng = pair
    return list(range(int(start), int(start) + int(rng) + 1))
def generate_numbers_parallel(pairs):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(generate_numbers, zip(pairs[::2], pairs[1::2])))

    return [num for sublist in results for num in sublist]

seeds = [int(seed) for seed in seeds]
new_seeds = [[seeds[i],seeds[i]+seeds[i+1]-1] for i in range(0,len(seeds),2)]
print(new_seeds)

positions=[]
for seed in new_seeds:
    start, end = seed
    for i in range(start,end):
        soil = find_dest(seed_to_soil_map,int(i))
        fert = find_dest(soil_to_fert_map,soil)
        water = find_dest(fert_to_water_map,fert)
        light = find_dest(water_to_light_map,water)
        temp = find_dest(light_to_temp_map,light)
        hum = find_dest(temp_to_hum_map,temp)
        loc = find_dest(hum_to_loc_map,hum)
        positions.append(loc)

print(f'Day 5, Part 2 = {min(positions)}')
# # ########## Part 2 ######################

