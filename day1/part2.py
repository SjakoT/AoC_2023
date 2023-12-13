inputFile = open('input.txt', 'r')
lines = inputFile.readlines()

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
          'nine']

def calcValue(line):
    num1Found = False
    num1, num2, num1Pos, num2Pos = 0, 0, 0, 0

    def findTextDigits(offset = 0):
        nonlocal num1Found, num1, num1Pos, num2, num2Pos
        for i in range(0, len(digits)):
            foundDigit = line.find(digits[i], offset)
            if foundDigit != -1:
                if num1Found:
                    if foundDigit < num1Pos:
                        num1 = i + 1
                        num1Pos = foundDigit
                    if foundDigit > num2Pos:
                        num2 = i + 1
                        num2Pos = foundDigit
                else:
                    num1 = i + 1
                    num1Pos = foundDigit
                    num2 = i + 1
                    num2Pos = foundDigit
                    num1Found = True

                findTextDigits(foundDigit + 1)

    for i in range(0, len(line)):
        char = line[i]
        if char.isdigit():
            if not num1Found:
                num1 = char
                num1Pos = i
                num1Found = True
            num2 = char
            num2Pos = i

    findTextDigits()

    return int(str(num1) + str(num2))

def sumValues():
    sumTotal = 0
    counter = 0
    for line in lines:
        sumTotal += calcValue(line)
        counter += 1

    print(sumTotal)

sumValues()
