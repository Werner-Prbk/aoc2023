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

def get_mapped_value(map, src):
    for m in map:
        if src >= m[1] and src < m[1] + m[2]:
            return m[0] + (src - m[1])
        
    return src #default

def find_locations(input):
    res = []
    for seed in input["seeds"]:
        soil = get_mapped_value(input["seed-to-soil"], seed)
        fertilizer =get_mapped_value( input["soil-to-fertilizer"], soil)
        water = get_mapped_value(input["fertilizer-to-water"], fertilizer)
        light = get_mapped_value(input["water-to-light"], water)
        temperature = get_mapped_value(input["light-to-temperature"], light)
        humidity = get_mapped_value(input["temperature-to-humidity"], temperature)
        location = get_mapped_value(input["humidity-to-location"], humidity)
        res.append(location)

    return res

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

if __name__ == "__main__":
    print_answer1("test.txt")
    print_answer1("input.txt")