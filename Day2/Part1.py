maxRed = 12
maxGreen = 13
maxBlue = 14

def parse_game_data(lines):
    def is_round_braking_game(round, game_id):
        data = round.split(',')
        for color_data in data:
            color_tokens = color_data.strip().split(' ')
            count = int(color_tokens[0])
            color = color_tokens[1]

            if ("red" in color and count > maxRed) or ("green" in color and count > maxGreen) or ("blue" in color and count > maxBlue):
                return True
    
        return False
    
    game_id_total = 0
    for line in lines:
        game_values = line.split(':')
        game_id = int(game_values[0].split()[1])
        game_id_total += game_id

        rounds = game_values[1].split(';')
        for round in rounds:
            if is_round_braking_game(round, game_id):
                game_id_total -= game_id
                break

    return game_id_total

with open('input.txt', 'r') as file:
    case = file.read()

lines = case.split('\n')

game_data = parse_game_data(lines)
print(game_data)
