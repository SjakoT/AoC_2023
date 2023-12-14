#data = [[71530, 940200]] #test data
data = [[44707080, 283113411341491]]

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
