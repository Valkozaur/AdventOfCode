
def process_strings(strings):
    def replace_spelled_numbers(s):
        # Dictionary mapping spelled-out numbers to digits
        digit_numbers = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", 
                     "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

        output = ""
        i = 0

        while i < len(s):
            if s[i].isdigit():
                # If the character is a digit, add it directly to the output
                output += s[i]
            else:
                # Check each number starting with the current character
                for number in digit_numbers:
                    if s[i:].startswith(number):
                        # If the number is found in the string, add its digit to the output
                        output += digit_numbers[number]
                        # i += len(number)
                        break
                
            i += 1
        
        return output

    def find_first_and_last_digit(s):
        first_digit = next((char for char in s if char.isdigit()), None)
        last_digit = next((char for char in reversed(s) if char.isdigit()), None)
        return first_digit, last_digit

    result = 0
    for string in strings:
        replaced = replace_spelled_numbers(string)
        first_digit, last_digit = find_first_and_last_digit(replaced)
        combined = int(first_digit + last_digit)
        result += combined

    return result


with open('Part1.txt', 'r') as file:
    case = file.read()

# Split the string into a list of strings by empty lines
list_of_strings = case.split('\n')

total = process_strings(list_of_strings)

print(total)