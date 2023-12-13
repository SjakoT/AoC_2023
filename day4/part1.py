inputFile = open('input.txt', 'r')
lines = inputFile.readlines()

cardData = []

def mapCardData():
    data = []

    for i in range(len(lines)):
        line = lines[i]
        
        numSeries1 = line[line.index(':') + 2 : line.index('|')]
        numSeries2 = line[line.index('|') + 2 :]

        lineData = []
        lineData.append([int(j) for j in numSeries1.split()])
        lineData.append([int(j) for j in numSeries2.split()])

        data.append(lineData)

    return data

def cardPoints(card):
    points = 0
    
    winningNrs = card[0]
    cardNrs = card[1]

    for nr1 in winningNrs:
        for nr2 in cardNrs:
            if nr1 == nr2:
                if points == 0:
                    points = 1
                else:
                    points = points * 2

    return points

def sumPoints():
    sumPoints = 0

    cardData = mapCardData()
    
    for i in range(len(lines)):
        sumPoints += cardPoints(cardData[i])

    return sumPoints

print(sumPoints())
