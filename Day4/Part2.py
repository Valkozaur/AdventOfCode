import re

# input = """
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
# """

with open('input.txt', 'r') as file:
    input = file.read()

cards = input.strip().split('\n')

def get_card_numbers(cards):
    card_collection = {}
    for card in cards:
        card_elements = card.split(':')
        card_numbers = card_elements[1].split('|')
        
        match = re.search(r'(\d+)', card_elements[0])
        card_number = int(match.group(1))
        
        winning_numbers = set(card_numbers[0].strip().split(' '))
        winning_numbers = {number for number in winning_numbers if number != ''}
        
        numbers = set(card_numbers[1].strip().split(' '))
        numbers = {number for number in numbers if number != ''}
        
        if(card_collection.get(card_number) == None):
            card_collection[card_number] = (winning_numbers, numbers)
        
    return card_collection

def get_points(card_collection):
    card_points_collection = {}
    for card_number, (winning_numbers, numbers_to_check) in card_collection.items():
        card_points = 0
        
        for number in numbers_to_check:
            if number in winning_numbers:
                card_points += 1
                
        card_points_collection[card_number] = card_points
    
    return card_points_collection
        
def get_sum(card_points_collection):
    card_occurances = {}
    for card_number in card_points_collection.keys():
        card_occurances[card_number] = 1

    iterator = iter(card_points_collection.keys())
    while True:
        try:
            current_card_number = next(iterator)
        except StopIteration:
            break
        
        card_points = card_points_collection[current_card_number]
        current_card_occurances = card_occurances[current_card_number]
        for i in range(current_card_occurances):
            if(card_points == 0):
                continue
            
            for i in range(card_points):
                card_number_to_add = current_card_number + i + 1
                if card_occurances.get(card_number_to_add) is None:
                    card_occurances[card_number_to_add] = 1
                else:
                    card_occurances[card_number_to_add] += 1       

    return sum(card_occurances.values())    
    
card_collection = get_card_numbers(cards)
card_points_collection = get_points(card_collection)
sum = get_sum(card_points_collection)
print(sum)