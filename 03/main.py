from operator import truediv


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

def get_number_at_pos(pos : (), lines : []):
    row : str = lines[pos[0]]
    num = ""
    for fwd in row[pos[1]:]:
        if fwd.isdecimal():
            num += fwd
        else:
            break
    
    for bwd in reversed(row[0:pos[1]]):
        if bwd.isdecimal():
            num = bwd + num
        else:
            break
    
    return int(num)

def get_adj_numbers(symPos : (), numbers : []):
    searcher = [(-1,-1), (-1, 0), (-1, 1), 
                (0, -1),          (0, 1), 
                (1, -1), (1, 0),  (1, 1)]
    
    nums = set()

    for s in searcher:
        absPos = (symPos[0] + s[0], symPos[1] + s[1])
        for idx in range(len(numbers)):
            if absPos in numbers[idx]["pos"]:
                nums.add(idx)
            #nums.append(get_number_at_pos(absPos, lines))

    return [int(numbers[n]["num"]) for n in nums]

def get_lines(filename):
    with open(filename) as f:
        return [line[:-1] for line in f.readlines()]

def print_answer1(filename):
        lines = get_lines(filename)
        symPos = find_symbols(lines)
        numbers = find_numbers(lines)
        partNums = [get_adj_numbers(s, numbers, lines) for s in symPos]
        
        res = []
        for pn in partNums:
            for p in pn:
                res.append(p)

        print(f"answer for {filename} is {sum(res, 0)}")

if __name__ == "__main__":
    print_answer1("test.txt")
    print_answer1("input.txt")