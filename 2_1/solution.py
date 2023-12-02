inputFile = open('input.txt', 'r')
lines = inputFile.readlines()

def validGame(game):
    isValid = True
    
    gameData = game[game.find(':') + 2 :]
    
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

        if red > 12 or green > 13 or blue > 14:
            isValid = False

    return isValid

def findPossibleGames():
    sumGames = 0
    for i in range(len(lines)):
        currLine = lines[i]

        if validGame(currLine):
            sumGames += i + 1

    print(sumGames)

findPossibleGames()
