import re

# input = """
# Time:      7  15   30
# Distance:  9  40  200
# """

with open('input.txt', 'r') as file:
    input = file.read()

def get_single_time_distance_group(input):
    lines = input.strip().split('\n')
    tokens = [re.findall(r'(\d+)', line.strip()) for line in lines]
    time = int(''.join(tokens[0]))
    distance = int(''.join(tokens[1]))
    return time, distance

def getMarginOfErrors(time, distance):
    number_of_ways = 0
    for i in range(1, time + 1):
        posible_distance = (time - i) * i
        if(posible_distance > distance):
            number_of_ways += 1
    return number_of_ways

time, distance = get_single_time_distance_group(input)
margin = getMarginOfErrors(time, distance)

print(margin)