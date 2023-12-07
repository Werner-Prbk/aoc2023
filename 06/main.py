import math

test = [(7,9),(15,40),(30,200)]
input = [(35,213),(69,1168),(68,1086),(87,1248)]

def calc_winning_hold_times(race):
    totalTime, winDistance = race
    startWinning = totalTime / 2 + math.sqrt((totalTime**2) / 4 - winDistance)
    endWinning = totalTime / 2 - math.sqrt((totalTime**2) / 4 - winDistance)
    return abs(math.ceil(startWinning) - math.floor(endWinning + 1))

testSolutions = [calc_winning_hold_times(t) for t in test]
print (f"Solution 1 for test is: {math.prod(testSolutions)}")

inputSolutions = [calc_winning_hold_times(t) for t in input]
print (f"Solution 1 for input is: {math.prod(inputSolutions)}")