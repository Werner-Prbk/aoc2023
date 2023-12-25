def get_lines(filename):
    with open(filename) as f:
        # strip newline at end
        return [line[:-1] for line in f.readlines()]

def find_start(map):
    for ridx in range(len(map)):
        idx = map[ridx].find('S')
        if idx != -1:
            return (ridx, idx)
    raise "no start found"

mapping = {
    "up" : { "|" : ((-1, 0), "up"), '7' : ((0, -1), "left"), 'F' : ((0, 1), "right") },
    "down" :  { "|" : ((1, 0), "down"), 'J' : ((0, -1), "left"), 'L' : ((0, 1), "right") },
    "left" : { "-" : ((0, -1), "left"), 'L' : ((-1, 0), "up"), 'F' : ((1, 0), "down") },
    "right" : { "-" : ((0, 1), "right"), 'J' : ((-1, 0), "up"), '7' : ((1, 0), "down") }
}

class Searcher:
    def __init__(self, pos, map, dir):
        self.pos = pos
        self.dir = dir
        self.map = map
        self.validate_pos()

    def validate_pos(self):
        if self.pos[0] < 0 or self.pos[0] > len(self.map):
            self.pos = None
        if self.pos[1] < 0 or self.pos[1] > len(self.map[0]):
            self.pos = None

    def next_pos(self):
        if self.pos is None: 
            return False
        
        sym = self.map[self.pos[0]][self.pos[1]]

        if sym == "S": return True

        if sym in mapping[self.dir].keys():
            relpos,self.dir = mapping[self.dir][sym]
            self.pos = (self.pos[0] + relpos[0], self.pos[1] + relpos[1])
            self.validate_pos()
        else:
            self.pos = None
        return False

def traverse(map, start):
    up = Searcher((start[0] - 1, start[1]), map, "up")
    down = Searcher((start[0] + 1, start[1]), map, "down")
    left = Searcher((start[0], start[1] - 1), map, "left")
    right = Searcher((start[0], start[1] + 1), map, "right")
    
    for distance in range(1, len(map)*len(map[0])):
        if up.next_pos() or down.next_pos() or left.next_pos() or right.next_pos():
            return distance / 2        
    raise "no solution found"


def print_answer1(filename):
    lines = get_lines(filename)
    start = find_start(lines)
    res = traverse(lines, start)
    print(f"Result is for 1 is {res}")

print_answer1("input.txt")