def parse_card(line : str):
    splt = line.split(":")
    card = { "id" : int(splt[0][5:]) }
    splt = splt[1].split("|")
    card["win"] = {int(c) for c in filter(lambda l: l.isdecimal(), splt[0].split(" "))}
    card["num"] = {int(c) for c in filter(lambda l: l.isdecimal(), splt[1].split(" "))}
    return card

def count_winning_numbers(card : {}):
    return len(card["win"].intersection(card["num"]))

def calc_card_points(card : {}):
    wins = count_winning_numbers(card)
    if (wins == 0):
        return 0
    else:
        return 2 ** (wins - 1)

def get_lines(filename):
    with open(filename) as f:
        # strip newline at end
        return [line[:-1] for line in f.readlines()]

def print_answer1(filename):
    cards = [parse_card(c) for c in get_lines(filename)]
    res = [calc_card_points(c) for c in cards]
    print(f"answer 1 for {filename} is {sum(res, 0)}")

def print_answer2(filename):
    return

if __name__ == "__main__":
    print_answer1("test.txt")
    print_answer1("input.txt")