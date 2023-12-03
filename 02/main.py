import math

def get_set(gameset : str):
    cubes = [s.strip() for s in gameset.split(",")]
    d = dict()
    for c in cubes:
        spl = c.strip().split(" ")
        d[spl[1]] = int(spl[0])

    return d

def parse_line(line: str):
    (game, sets) = line.split(":")
    gameId = int(game[5:])
    setList = [get_set(s) for s in sets.split(";")]
    return { "gameId" : int(gameId), "sets" : setList }

def set_is_possible(s, possible):
        for g in s:
            for color, cnt in g.items():
                if cnt > possible.get(color, 0):
                    return False
    
        return True

def get_possible_games(games : [], possible : dict):
    goodGames = []
    for game in games:
        if set_is_possible(game["sets"], possible):
            goodGames.append(game["gameId"])

    return goodGames

def get_power(game : dict):
    maxDice = dict()
    for g in game["sets"]:
        for color, cnt in g.items():
            maxDice[color] = max(maxDice.get(color, 0), cnt)

    return math.prod(maxDice.values())


def print_answer1(filename):
    with open(filename) as f:
        games = [parse_line(l) for l in f.readlines()]
        possible = get_possible_games(games, {"red" : 12, "green" : 13, "blue" : 14 })
        print(f"answer for {filename} is {sum(possible, 0)}")

def print_answer2(filename):
    with open(filename) as f:
        games = [parse_line(l) for l in f.readlines()]
        game_power = [get_power(g) for g in games]
        print(f"answer for {filename} is {sum(game_power, 0)}")

if __name__ == "__main__":
    print_answer1("test1.txt")
    print_answer1("input.txt")

    print_answer2("test1.txt")
    print_answer2("input.txt")