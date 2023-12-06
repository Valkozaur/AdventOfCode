import re

input = """
Time:      7  15   30
Distance:  9  40  200
"""

with open('input.txt', 'r') as file:
    input = file.read()

def get_time_distance_group(input):
    lines = input.strip().split('\n')
    tokens = [re.findall(r'(\d+)', line.strip()) for line in lines]
    time_distance_group = list(zip(tokens[0], tokens[1]))
    time_distance_group = [(int(time), int(distance)) for time, distance in time_distance_group]
    return time_distance_group

def getMarginOfErrors(time_distance_groups):
    margin = 1
    for time, distance in time_distance_groups:
        number_of_ways = 0
        for i in range(1, time + 1):
            posible_distance = (time - i) * i

            if(posible_distance > distance):
                number_of_ways += 1
        margin = margin * number_of_ways
    return margin

time_distance_groups = get_time_distance_group(input)
margin = getMarginOfErrors(time_distance_groups)

print(margin)