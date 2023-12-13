inputFile = open('input.txt', 'r')
lines = inputFile.readlines()

def calcValue(line):
    num1Found = False
    num1, num2 = 0, 0

    for char in line:
        if char.isdigit():
            if not num1Found:
                num1 = char
                num1Found = True
            num2 = char

    return int(num1 + num2)

def sumValues():
    sumTotal = 0
    for line in lines:
        sumTotal += calcValue(line)

    print(sumTotal)

sumValues()
