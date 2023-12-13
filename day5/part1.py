inputFile = open('input.txt', 'r')
lines = inputFile.readlines()

data = []

def sortData():
    seeds = [int(j) for j in lines[0][lines[0].index(' '):].split()]
    data.append(seeds)

    series = []
    seriesStart = 0
    
    for i in range(2, len(lines)):
        line = lines[i]

        if line == '\n':
            data.append(series)
            series = []
            seriesStart = 0

        if seriesStart != 0:
            series.append([int(j) for j in line.split()])

        if line.find(':') != -1:
            seriesStart = i + 1

def findSeedLocation(seed):
    currNr = seed
    for i in range(1, len(data)):
        block = data[i]
        for j in range(len(block)):
            line = block[j]
            
            destStart, sourceStart, rangeLen = line[0], line[1], line[2]

            if sourceStart <= currNr < sourceStart + rangeLen:
                currNr = destStart + currNr - sourceStart
                break

    return currNr

def lowestLocation():
    sortData()

    lowest = -1

    for seed in data[0]:
        seedLocation = findSeedLocation(seed)
        if lowest < 0 or seedLocation < lowest:
            lowest = seedLocation

    return lowest

print(lowestLocation())
