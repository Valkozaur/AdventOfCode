import re

# input = """
# 12.......*..
# +.......*200
# ......12....
# ..78........
# ..*....60...
# 78.........9
# .5.....23..$
# 8...90*12...
# ............
# 2.2......12.
# .*.........*
# 1.1..503+.56
# """


with open('input.txt', 'r') as file:
    input = file.read()

def get_gears(matrix):
    def get_adjestent_number_coordinates(matrix, row_index, col_index):
        # Checks in all eight directions around the cell
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # Above
            (0, -1),           (0, 1),   # Sides
            (1, -1),  (1, 0),  (1, 1)    # Below
        ]

        coordinates = []
        for dr, dc in directions:
            r, c = row_index + dr, col_index + dc
            if 0 <= r < len(matrix) and 0 <= c < len(matrix[r]) and re.match(r'[0-9]', matrix[r][c]):
                coordinates.append((r, c))
        return coordinates
    
    def filter_gears(matrix, coordinates):
        count = 0
        filtered_coordinates = []
        previous_row, previous_col = 0, 0
        for r, c in coordinates:
            if(previous_row == r and previous_col - c == -1):
                previous_row = r
                previous_col = c
                continue
            
            filtered_coordinates.append((r, c))
            count += 1
            previous_row = r
            previous_col = c
            
        if(count > 2):
            return False, filtered_coordinates
        
        return True, filtered_coordinates
        
    def get_sum_of_numbers_at_coordinates(matrix, coordinates):
        factor = 1
        for r, c in coordinates:            
            number = matrix[r][c]
            number_before = get_numbers_behind(matrix, r, c)             
            number_infront = get_numbers_infront(matrix, r, c)             
            wholeNumber = number_before + number + number_infront
            
            print(wholeNumber)
            
            factor *= int(wholeNumber)
            
            previous_row = r
            previous_col = c
        return factor
    
    def get_numbers_behind(matrix, row_index, col_index):
        number = ''
        if 0 <= row_index < len(matrix) and 0 <= col_index - 1 < len(matrix[row_index]) and matrix[row_index][col_index - 1].isdigit():
            number = matrix[row_index][col_index - 1] + number
            number = get_numbers_behind(matrix, row_index, col_index - 1) + number
        
        return number
    
    def get_numbers_infront(matrix, row_index, col_index):
        number = ''
        if 0 <= row_index < len(matrix) and 0 <= col_index + 1 < len(matrix[row_index]) and matrix[row_index][col_index + 1].isdigit():
            number += matrix[row_index][col_index + 1]
            number += get_numbers_infront(matrix, row_index, col_index + 1)
            
        return number
    
    sum = 0
    number = ''
    has_adjestent_number = False
    
    for row_index, row in enumerate(matrix):
        for col_index, cell in enumerate(row):
            if cell == '*':
                adjestent_number_coordinates = get_adjestent_number_coordinates(matrix, row_index, col_index)
                valid_gear, coordinates = filter_gears(matrix, adjestent_number_coordinates)
                if len(coordinates) == 2 and valid_gear:
                    
                    sum += get_sum_of_numbers_at_coordinates(matrix, coordinates)
                    print(f"Coordinates: {coordinates}")

    return sum


print(get_gears(input.strip().split('\n')))