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
    card_numbers = []
    for card in cards:
        tokens = card.split('|')
        winning_numbers = set(re.sub(r'Card \d+: ', '', tokens[0]).strip().split(' '))
        winning_numbers = {number for number in winning_numbers if number != ''}
        numbers_to_check = set(tokens[1].strip().split(' '))
        numbers_to_check = {number for number in numbers_to_check if number != ''}
        card_numbers.append((winning_numbers, numbers_to_check))
        
    return card_numbers

def get_points(numbers):
    points = 0
    
    for winning_numbers, numbers_to_check in numbers:
        card_points = 0
        is_second = False
        for number in numbers_to_check:
            if number in winning_numbers and is_second:
                card_points = card_points * 2
            if number in winning_numbers and not is_second:
                card_points += 1
                is_second = True                
                
        points += card_points
                    
    return points
        
    
numbers = get_card_numbers(cards)
points = get_points(numbers)
print(points)