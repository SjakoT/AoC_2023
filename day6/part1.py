#data = [[7, 9], [15, 40], [30, 200]] #test data
data = [[44, 283], [70, 1134], [70, 1134], [80, 1491]]

def nrStrategies(race):
    time, distReq = race[0], race[1]

    strategies = 0

    for i in range(time):
        timeRem = time - i
        distTrav = timeRem * i

        if distTrav > distReq:
            strategies += 1

    return strategies

product = 1

for race in data:
    product *= nrStrategies(race)

print(product)
