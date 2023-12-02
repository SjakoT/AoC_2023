inputFile = open('input.txt', 'r')
lines = inputFile.readlines()

def gameMinPower(game):
    gameData = game[game.find(':') + 2 :]

    minRed, minGreen, minBlue = 0, 0, 0
    
    sets = []
    lastSemi = 0
    for i in range(len(gameData)):
        char = gameData[i]
        if char == ';' or char == '\n':
            if lastSemi == 0:
                sets.append(gameData[lastSemi : i])
            else:
                sets.append(gameData[lastSemi + 2 : i])

            lastSemi = i

    for gameSet in sets:
        red, green, blue = 0, 0, 0
        
        redPos = gameSet.find('red')
        if redPos != -1:
            red = int(gameSet[gameSet.rfind(' ', None, redPos - 2) + 1 :
                              redPos - 1])
        greenPos = gameSet.find('green')
        if greenPos != -1:
            green = int(gameSet[gameSet.rfind(' ', None, greenPos - 2) + 1 :
                              greenPos - 1])
        bluePos = gameSet.find('blue')
        if bluePos != -1:
            blue = int(gameSet[gameSet.rfind(' ', None, bluePos - 2) + 1 :
                              bluePos - 1])

        if red > minRed:
            minRed = red
        if green > minGreen:
            minGreen = green
        if blue > minBlue:
            minBlue = blue

    return minRed * minGreen * minBlue

def sumMinPowers():
    sumGames = 0
    for i in range(len(lines)):
        currLine = lines[i]

        sumGames += gameMinPower(currLine)

    print(sumGames)

sumMinPowers()
