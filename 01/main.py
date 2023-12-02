def get_calibration_value1(line : str) -> int: 
        first = next(filter(str.isdecimal, line))
        last = next(filter(str.isdecimal, reversed(line)))
        return int(first + last)

def get_calibration_value2(line: str) -> str:
    table = { "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
    newline = ""
    i = 0

    while i < len(line):
        if line[i].isdecimal():
            newline += line[i]
        else:
            for k,v in table.items():
                if line.startswith(k, i):
                    newline += str(v)
                    break

        i += 1
    
    return int(newline[0] + newline[-1])

def print_answer1(filename):
    with open(filename, "r") as f:
        res = [get_calibration_value1(line) for line in f.readlines()]
        print(f"for {filename} the calibration value is {sum(res, 0)}")

def print_answer2(filename):
     with open(filename, "r") as f:
        res = [get_calibration_value2(line) for line in f.readlines()]
        print(f"for {filename} the calibration value is {sum(res, 0)}")

if __name__ == "__main__":
    print_answer1("test1.txt")   # 142
    print_answer1("input.txt")  # 54698

    print_answer2("test2.txt")  # 281
    print_answer2("input.txt") # 54094 