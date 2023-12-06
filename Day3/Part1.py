import re

# input = """
# 467....114
# 111*...*..
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# """

with open('input.txt', 'r') as file:
    input = file.read()

parsedInput = input.strip().split('\n')

matrix = [list(row) for row in parsedInput]

def getSum(matrix):
    def is_adjacent_to_symbol(matrix, row_index, col_index):
        # Checks in all eight directions around the cell
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # Above
            (0, -1),           (0, 1),   # Sides
            (1, -1),  (1, 0),  (1, 1)    # Below
        ]

        for dr, dc in directions:
            r, c = row_index + dr, col_index + dc
            if 0 <= r < len(matrix) and 0 <= c < len(matrix[r]) and re.match(r'[^0-9.]', matrix[r][c]):
                return True
        return False
    
    sum = 0
    number = ''
    has_adjestent_symbol = False
    for row_index, row in enumerate(matrix):
        for col_index, cell in enumerate(row):
            if cell.isdigit():
                number += cell
                if is_adjacent_to_symbol(matrix, row_index, col_index):
                    has_adjestent_symbol = True
            else:
                if number and has_adjestent_symbol:
                    sum += int(number)
                    print("included " + number)
                if number and has_adjestent_symbol == False:
                    print("not included " + number)
                number = ''
                has_adjestent_symbol = False

        if number and has_adjestent_symbol:
            print("included " + number)
            sum += int(number)
            number = ''
            has_adjestent_symbol = False

    return sum

sum = getSum(matrix)
print(sum)