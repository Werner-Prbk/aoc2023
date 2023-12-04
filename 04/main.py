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
    cards = [ parse_card(c) for c in get_lines(filename) ]
    for c in cards: c["qnt"] = 1    # extend with quantity
    for a in range(len(cards)):
        for b in range(cards[a]["qnt"]):
            for c in range(count_winning_numbers(cards[a])):
                if (a + c + 1) < len(cards):
                    cards[a + c + 1]["qnt"] += 1
    
    print(f"answer 2 for {filename} is {sum([c["qnt"] for c in cards], 0)}")

if __name__ == "__main__":
    print_answer1("test.txt")
    print_answer1("input.txt")
    print_answer2("test.txt")
    print_answer2("input.txt")