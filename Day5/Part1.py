import re

class Ranges:
    def __init__(self, destination, source, range):
        self.destination = destination
        self.source = source
        self.range = range
        
class Mapping:    
    def __init__(self, name, ranges):
        self.name = name
        self.ranges = ranges
        
class Almanac:
    def __init__(self, seeds, mappings):
        self.seeds = seeds
        self.mappings = mappings
        

input = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

with open('input.txt', 'r') as file:
    input = file.read()

def create_almanac(input):
    input = input.strip()
    
    seedsMatch = re.search(r'^seeds: ([\s\d]+)$', input, re.MULTILINE)
    
    seeds = list(map(int, seedsMatch.group(1).split(' ')))
    
    mapsMatch = re.findall(r'^(\w+-to-\w+ map:)((?:\n\d+ \d+ \d+)+)', input, re.MULTILINE)
    
    maps = []
    for match in mapsMatch:
        map_name, numbers = match
        numbers = numbers.strip().split('\n')
        
        ranges = []
        for mapping in numbers:
            tokens = list(map(int, mapping.split(' ')))
            ranges.append(Ranges(tokens[0], tokens[1], tokens[2]))
            
        maps.append(Mapping(map_name, ranges))
            
    return Almanac(seeds, maps)

def getLocations(almanac):
    locations = []
    for seed in almanac.seeds:
        currentSeed = seed
        for mapping in almanac.mappings:
            for range in mapping.ranges:
                sourceEnd = range.source + range.range
                difference = range.destination - range.source
                if(range.source <= currentSeed < sourceEnd):
                    currentSeed = currentSeed + difference
                    break
                
        locations.append(currentSeed)
                
    return locations

almanac = create_almanac(input)
locations = getLocations(almanac)
smallest_number = min(locations)
print(smallest_number)

                        
                
                
                