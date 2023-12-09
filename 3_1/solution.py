inputFile = open('input.txt', 'r')
lines = inputFile.readlines()

def checkIfValid(line, start, end):
    def symbolPresent(l, s, e):
        line = lines[l]
        for char in line[max(start - 1, 0) : min(end + 1, len(line))]:
            if not char.isdigit() and char != '.' and char != '\n':
                return True

        return False

    prevLine = line - 1
    if prevLine >= 0:
        if symbolPresent(prevLine, start, end):
            return True

    if symbolPresent(line, start, end):
        return True

    nextLine = line + 1
    if nextLine <= len(lines) - 1:
        if symbolPresent(nextLine, start, end):
            return True

    return False

def sumValidNumbers():
    sumNrs = 0

    for i in range(len(lines)):
        line = lines[i]
        
        countingDigit = False
        digitStart = 0
            
        for j in range(len(line)):
            char = line[j]

            if countingDigit:
                if not char.isdigit():
                    nr = int(line[digitStart : j])
                    if checkIfValid(i, digitStart, j):
                        sumNrs += nr
                        
                    countingDigit = False
                    digitStart = 0
            else:
                if char.isdigit():
                    countingDigit = True
                    digitStart = j

    return sumNrs

print(sumValidNumbers())
