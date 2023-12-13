inputFile = open('input.txt', 'r')
lines = inputFile.readlines()

gears = []

def getGearIndex(line, pos):
    for i in range(len(gears)):
        currGear = gears[i]
        if currGear[0] == line and currGear[1] == pos:
            return i

def mapGears():
    for i in range(len(lines)):
        line = lines[i]
        for j in range(len(line)):
            char = line[j]
            if char == '*':
                gears.append([i, j, []])

def linkWithGears(nr, line, start, end):
    def searchLine(l):
        line = lines[l]
        for i in range(len(line)):
            char = line[i]

            if max(start - 1, 0) <= i < min(end + 1, len(line)):
                if char == '*':
                    gears[getGearIndex(l, i)][2].append(nr)

        return False

    prevLine = line - 1
    if prevLine >= 0:
        searchLine(prevLine)

    searchLine(line)

    nextLine = line + 1
    if nextLine <= len(lines) - 1:
        searchLine(nextLine)

    return False

def sumGearRatios():
    mapGears()
    
    sumRatios = 0

    for i in range(len(lines)):
        line = lines[i]
        
        countingDigit = False
        digitStart = 0
            
        for j in range(len(line)):
            char = line[j]

            if countingDigit:
                if not char.isdigit():
                    nr = int(line[digitStart : j])

                    linkWithGears(nr, i, digitStart, j)
                        
                    countingDigit = False
                    digitStart = 0
            else:
                if char.isdigit():
                    countingDigit = True
                    digitStart = j

    for gear in gears:
        if len(gear[2]) == 2:
            sumRatios += gear[2][0] * gear[2][1]
    
    return sumRatios

print(sumGearRatios())
