def find_symbols(lines : []):
    positions = []
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            d = lines[row][col]
            if (d.isdecimal() == False and d != "."):
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

def flatten_list(l : []):
    for pn in l:
        for p in pn:
           yield p
    return

def print_answer1(filename):
        lines = get_lines(filename)
        symPos = find_symbols(lines)
        numbers = find_numbers(lines)
        partNums = [get_adj_numbers(s, numbers) for s in symPos]
        res = flatten_list(partNums)

        print(f"answer for {filename} is {sum(res, 0)}")

if __name__ == "__main__":
    print_answer1("test.txt")
    print_answer1("input.txt")