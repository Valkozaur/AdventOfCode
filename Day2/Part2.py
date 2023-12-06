def parse_game_data(lines):
    
    def get_colors_count(round):
        data = round.split(',')
        round_data = {}
        for color_data in data:
            color_tokens = color_data.strip().split(' ')
            count = int(color_tokens[0])
            color = color_tokens[1]
            round_data[color] = count

        return round_data
    
    total_powers = 0
    for line in lines:
        game_values = line.split(':')
        rounds = game_values[1].split(';')
        least_minimum_balls = { "red": 0, "green": 0, "blue": 0 }
        
        for round in rounds:
            round_data = get_colors_count(round)

            if round_data.get("red") is not None and round_data["red"] > least_minimum_balls["red"]:
                least_minimum_balls["red"] = round_data["red"]
            if round_data.get("green") is not None and round_data["green"] > least_minimum_balls["green"]:
                least_minimum_balls["green"] = round_data["green"]
            if round_data.get("blue") is not None and round_data["blue"] > least_minimum_balls["blue"]:
                least_minimum_balls["blue"] = round_data["blue"]

        total_powers += least_minimum_balls["red"] * least_minimum_balls["green"] * least_minimum_balls["blue"]

    return total_powers

with open('input.txt', 'r') as file:
    case = file.read()

lines = case.split('\n')

game_data = parse_game_data(lines)
print(game_data)
