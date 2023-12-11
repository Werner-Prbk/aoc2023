def get_lines(filename):
    with open(filename) as f:
        # strip newline at end
        return [line[:-1] for line in f.readlines()]

def parse_nodes(line : str):
    line.replace(" ", "")
    a,b = line.split("=")
    b1,b2 = b.strip("() ").split(",")
    return (a.strip(), (b1,b2.strip()))

def find_z(instructions, nodes, currNode):
    idx = 0
    while True:
        if currNode == "ZZZ":
            return idx
        if instructions[idx % len(instructions)] == "L":
            currNode = nodes[currNode][0]
        else:
            currNode = nodes[currNode][1]
        idx += 1


def print_answer1(filename):
    lines = get_lines(filename)
    instructions = lines[0]
    nodes = dict([parse_nodes(n) for n in lines[2:]])
    steps = find_z(instructions, nodes, "AAA")
    print(f"answer 1 for {filename} is {steps}")

print_answer1("test1.txt")
print_answer1("test2.txt")
print_answer1("input.txt")