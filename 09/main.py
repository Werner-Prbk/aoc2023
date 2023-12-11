import numpy as np

def get_lines(filename):
    with open(filename) as f:
        # strip newline at end
        return [line[:-1] for line in f.readlines()]

def predict(h):
    if np.all(h==0): 
        return 0
    else:
        diffs = np.array(h[1:]) - np.array(h[:-1])
        x = predict(diffs) + h[-1]
        return x

def print_answer1(filename):
    lines = get_lines(filename)
    histories = [[int(n) for n in l.split(" ")] for l in lines]
    predictions = [predict(np.array(h)) for h in histories]
    print(f"answer 1 for {filename} is {sum(predictions)}")

print_answer1("test.txt")
print_answer1("input.txt")