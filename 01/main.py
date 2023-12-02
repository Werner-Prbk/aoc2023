def get_calibration_value(line : str) -> int:
        # try with filter()

        res = ""
        for c in line:
            if c.isnumeric():
                res = (c)
                break
        for rc in reversed(line):
             if rc.isnumeric():
                res += rc 
                break
        return int(res)

def print_answer(filename):
    with open(filename, "r") as f:
        res = [get_calibration_value(line) for line in f.readlines()]
        calibration = sum(res, 0)
        print(f"for {filename} the calibration value is {calibration}")

print_answer("test.txt")
print_answer("input1.txt")