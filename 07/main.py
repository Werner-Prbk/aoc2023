import functools

strongness_map = { "2" : "0", "3" : "1", "4" : "2", "5" : "3", "6" : "4", "7" : "5", "8" : "6", 
                  "9" : "7", "T" : "8", "J" : "9", "Q" : "A", "K" : "B", "A" : "C" }

hand_types = { 
    "fiveOfAKind" : 7, 
    "fourOfAKind" : 6, 
    "fullHouse" : 5, 
    "threeOfAKind" : 4, 
    "twoPair" : 3, 
    "onePair" : 2, 
    "highCard" : 1
    }

def get_hand_type(hand):
    handValue = ""
    d = {}
    for h in hand:
        d[h] = d.get(h, 0) + 1
        handValue += strongness_map[h]

    handValue = int(handValue, 16)
    match len(d):
        case 1: return handValue, hand_types["fiveOfAKind"]
        case 2:
            if 4 in d.values(): return handValue, hand_types["fourOfAKind"]
            else: return handValue, hand_types["fullHouse"]
        case 3:
            if 3 in d.values(): return handValue, hand_types["threeOfAKind"]
            if 1 in d.values(): return handValue, hand_types["twoPair"]
        case 4: return handValue, hand_types["onePair"]
        case _: return handValue, hand_types["highCard"]

def hands_cmp(a,b):
    # compare types
    if a[3] < b[3]: return -1
    if a[3] > b[3]: return 1
    #compare cards when equal types
    if a[2] < b[2]: return -1
    else: return 1


def get_lines(filename):
    with open(filename) as f:
        # strip newline at end
        return [line[:-1] for line in f.readlines()]

def print_answer1(filename):
    lines = get_lines(filename)
    hands, bids = zip(*[l.split(' ') for l in lines])
    weightedHandTypes = [get_hand_type(h) for h in hands]
    help = list(zip(hands, bids, *zip(*weightedHandTypes)))
    help.sort(key=functools.cmp_to_key(hands_cmp))

    sum = 0
    for x in range (0, len(help)):
        sum += (1 + x)*int(help[x][1])

    print(f"answer 1 for {filename} is {sum}")

print_answer1("test.txt")
print_answer1("input.txt")