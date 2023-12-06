def find_first_and_last_digit(s):
    first_digit = last_digit = None
    for i in range(len(s)):
        if first_digit is None and s[i].isdigit():
            first_digit = s[i]
        if last_digit is None and s[-i-1].isdigit():
            last_digit = s[-i-1]
        if first_digit is not None and last_digit is not None:
            break
    return first_digit + last_digit


with open('Part1.txt', 'r') as file:
    case = file.read()

# Split the string into a list of strings by empty lines
list_of_strings = case.split('\n')

total = 0

for string in list_of_strings:
    total += int(find_first_and_last_digit(string))


print(total)

