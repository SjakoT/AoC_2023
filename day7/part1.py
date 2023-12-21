inputFile = open('input.txt', 'r')
lines = inputFile.readlines()

cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def cardStronger(hand1, hand2):
    for i in range(0, 5):
        char1, char2 = hand1[i], hand2[i]
        card1, card2 = cards.index(char1), cards.index(char2)
        if card1 < card2:
            return True
        if card1 > card2:
            return False

    return False

#0 high card
#1 one pair
#2 two pair
#3 three of a kind
#4 full house
#5 four of a kind
#6 five of a kind
def getType(hand):
    def nrInString(char, string):
        count = 0
        for c in string:
            if c == char:
                count += 1

        return count

    multiples, chars = [], []

    for char in hand:
        if not char in chars:
            occs = nrInString(char, hand)
            if occs > 1:
                multiples.append(occs)
                chars.append(char)

    if 5 in multiples:
        return 6
    if 4 in multiples:
        return 5
    if 3 in multiples:
        if 2 in multiples:
            return 4
        else:
            return 3
    if 2 in multiples:
        if len(multiples) > 1:
            return 2
        else:
            return 1

    return 0

def isStronger(hand1, hand2):
    type1 = getType(hand1)
    type2 = getType(hand2)

    if type1 > type2:
        return True
    if type1 < type2:
        return False

    return cardStronger(hand1, hand2)

def rankHands():
    hands = []

    for line in lines:
        hand = line.split()
        hand[1] = int(hand[1])

        hands.append(hand)

    handsR = []
    handsR.append(hands[0])

    for h in hands:
        hand = h[0]
        
        if isStronger(handsR[0][0], hand):
            handsR.insert(0, h)
            continue

        if isStronger(hand, handsR[len(handsR) - 1][0]):
            handsR.append(h)
            continue

        for i in range(len(handsR) - 1):
            prevHandR, nextHandR = handsR[i][0], handsR[i + 1][0]
            if isStronger(hand, prevHandR) and isStronger(nextHandR, hand):
                handsR.insert(i + 1, h)
                continue

    return handsR

handsRanked = rankHands()

winnings = 0

for i in range(len(handsRanked)):
    handBid = handsRanked[i][1]
    handWinnings = handBid * (i + 1)

    winnings += handWinnings

print(winnings)
