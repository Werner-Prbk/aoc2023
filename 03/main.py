def find_symbols(lines : [], matcher):
    positions = []
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            d = lines[row][col]
            if (matcher(d) and d != "."):
                positions.append((row, col))

    return positions    

def find_numbers(lines : []):
    numbers = []
    for row in range(len(lines)):
        num = None
        for col in range(len(lines[row])):
            d = lines[row][col]
            if (d.isdecimal()):
                if num is None:
                    num = {"num" : d, "pos" : [(row, col)]}
                else:
                    num["num"] = num["num"] + d
                    num["pos"].append((row, col))
            else:
                if num is not None:
                    numbers.append(num)
                    num = None
        if num is not None:
            numbers.append(num)
    
    return numbers

def get_adj_numbers(symPos : (), numbers : []):
    searcher = [(-1,-1), (-1, 0), (-1, 1), 
                (0, -1),          (0, 1), 
                (1, -1), (1, 0),  (1, 1)]
    
    uniqNums = set()

    for s in searcher:
        absPos = (symPos[0] + s[0], symPos[1] + s[1])
        for idx in range(len(numbers)):
            if absPos in numbers[idx]["pos"]:
                uniqNums.add(idx)

    return [int(numbers[n]["num"]) for n in uniqNums]

def get_lines(filename):
    with open(filename) as f:
        # strip newline at end
        return [line[:-1] for line in f.readlines()]

def print_answer1(filename):
        lines = get_lines(filename)
        symPos = find_symbols(lines, lambda d: d.isdecimal() == False)
        numbers = find_numbers(lines)
        partNums = [get_adj_numbers(s, numbers) for s in symPos]
        res = [sum(n) for n in partNums]
        print(f"answer 1 for {filename} is {sum(res, 0)}")

def print_answer2(filename):
        lines = get_lines(filename)
        symPos = find_symbols(lines, lambda d: d == "*")
        numbers = find_numbers(lines)
        partNums = [get_adj_numbers(s, numbers) for s in symPos]
        gearNums = filter(lambda n: len(n) == 2, partNums)
        res = [n[0]*n[1] for n in gearNums]
        print(f"answer 2 for {filename} is {sum(res, 0)}")

if __name__ == "__main__":
    print_answer1("test.txt")
    print_answer1("input.txt")
    print_answer2("test.txt")
    print_answer2("input.txt")