import itertools


def get_nums(line):
    return [int(c) for c in filter(lambda l: str.isdecimal(l), line.split(" "))]

def parse_all(lines : []):
    res = {"seeds" : get_nums(lines[0].split(":")[1]) }

    for l in lines[2:]:
        if len(l) > 0:
            if (str.isalpha(l[0])):
                currentKey, _ = l.split(" ")
                res[currentKey] = []
            elif str.isdecimal(l[0]):
                res[currentKey].append(get_nums(l))

    return res

#works like a charm for the test input...
#def expand_maps(input):
#    for k in input:
#        if k != "seeds":
#            tmp = dict()
#            v = input[k]
#            for idx in range(len(v)):
#                dst = [*range(v[idx][0], v[idx][0] + v[idx][2])]
#                src = [*range(v[idx][1], v[idx][1] + v[idx][2])]
#                tmp.update(zip( src, dst))
#            input[k] = tmp

def get_dst_by_src(map, src):
    for m in map:
        if src >= m[1] and src < m[1] + m[2]:
            return m[0] + (src - m[1])
        
    return src #default

def find_locations(input):
    res = []
    for seed in input["seeds"]:
        soil = get_dst_by_src(input["seed-to-soil"], seed)
        fertilizer = get_dst_by_src( input["soil-to-fertilizer"], soil)
        water = get_dst_by_src(input["fertilizer-to-water"], fertilizer)
        light = get_dst_by_src(input["water-to-light"], water)
        temperature = get_dst_by_src(input["light-to-temperature"], light)
        humidity = get_dst_by_src(input["temperature-to-humidity"], temperature)
        location = get_dst_by_src(input["humidity-to-location"], humidity)
        res.append(location)

    return res

def is_seed_available(seeds, seed):
    for idx in range(0, len(seeds), 2):
        if seed >= seeds[idx] and seed < (seeds[idx] + seeds[idx+1]):
            return True
    
    return False

def get_src_by_dst(map, dst):
    for m in map:
        if dst >= m[0] and dst < m[0] + m[2]:
            return m[1] + (dst - m[0])
        
    return dst #default

def resolve_backwards(input):
    input["humidity-to-location"].sort(key = lambda e: e[0])
    input["temperature-to-humidity"].sort(key = lambda e: e[0])
    input["light-to-temperature"].sort(key = lambda e: e[0])
    input["water-to-light"].sort(key = lambda e: e[0])
    input["fertilizer-to-water"].sort(key = lambda e: e[0])
    input["soil-to-fertilizer"].sort(key = lambda e: e[0])
    input["seed-to-soil"].sort(key = lambda e: e[0])

    vals = [
        input["humidity-to-location"][0][0],
        input["temperature-to-humidity"][0][0],
        input["light-to-temperature"][0][0],
        input["water-to-light"][0][0],
        input["fertilizer-to-water"][0][0],
        input["soil-to-fertilizer"][0][0],
        input["seed-to-soil"][0][0],
    ] 

    startVal = min(vals)
    #startVal = 46
    hIdx = 0
    for location in itertools.count(start=startVal):
        humidity = get_src_by_dst(input["humidity-to-location"], location)
        temperature = get_src_by_dst(input["temperature-to-humidity"], humidity)
        light = get_src_by_dst(input["light-to-temperature"], temperature)
        water = get_src_by_dst(input["water-to-light"], light)
        fertilizer = get_src_by_dst(input["fertilizer-to-water"], water)
        soil = get_src_by_dst(input["soil-to-fertilizer"], fertilizer)
        seed = get_src_by_dst(input["seed-to-soil"], soil)

        if is_seed_available(input["seeds"], seed):
            return location
    
    return -1

def get_lines(filename):
    with open(filename) as f:
        # strip newline at end
        return [line[:-1] for line in f.readlines()]

def print_answer1(filename):
    lines = get_lines(filename)
    res = parse_all(lines)
    #expand_maps(res)
    locations = find_locations(res)
    print(f"answer 1 for {filename} is {min(locations)}")

def print_answer2(filename):
    lines = get_lines(filename)
    res = parse_all(lines)
    #expand_maps(res)
    location = resolve_backwards(res)
    print(f"answer 2 for {filename} is {location}")

if __name__ == "__main__":
    #print_answer1("test.txt")
    #print_answer1("input.txt")
    print_answer2("test.txt")
    print_answer2("input.txt")