def is_possible(config, game):
    cube_counts = config.copy()
    for subset in game:
        for cube in subset:
            color, count = cube.split()
            count = int(count)
            if cube_counts[color] < count:
                return False
            cube_counts[color] -= count
    return True

def possible_games(config, games):
    possible = []
    for game_id, game in games.items():
        if is_possible(config, game):
            possible.append(game_id)
    return possible

def main():
    cube_config = {'red': 12, 'green': 13, 'blue': 14}

    games = {
        1: [['3 blue', '4 red'], ['1 red', '2 green', '6 blue'], ['2 green']],
        2: [['1 blue', '2 green'], ['3 green', '4 blue', '1 red'], ['1 green', '1 blue']],
        3: [['8 green', '6 blue', '20 red'], ['5 blue', '4 red', '13 green'], ['5 green', '1 red']],
        4: [['1 green', '3 red', '6 blue'], ['3 green', '6 red'], ['3 green', '15 blue', '14 red']],
        5: [['6 red', '1 blue', '3 green'], ['2 blue', '1 red', '2 green']],
    }

    possible_ids = possible_games(cube_config, games)

    print("Possible games:", possible_ids)
    print("Sum of IDs:", sum(possible_ids))

if __name__ == "__main__":
    main()
