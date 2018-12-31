# Random Numbers
import random
# Sorting Classes with a specific attribute
import operator

sum = 0
amount = 0

class Competitor:
    def __init__(self, name, elo, w, l):
        self.name = name
        self.elo = elo
        # wins/losses
        self.w = w
        self.l = l

    # How to print a song
    def __repr__(self):
        desc = ''
        desc += 'name: ' + self.name + '\n'
        desc += 'elo: ' + str(int(self.elo)) + '\n'
        desc += 'w/l: ' + str(int(self.w)) + ' ' + str(int(self.l)) + '\n'
        if (self.l != 0):
            desc += 'ratio: ' + str(float(self.w/self.l)) + '\n'
        return desc

# Prints 'amount' newlines
def newLines(amount):
    for i in range(amount):
        print('\n')

# Parses a line from the input file
def parseLine(line):
    words = line.split()
    print(words)

    name = str(words[0])
    elo = float(words[1])
    w = float(words[2])
    l = float(words[3])

    competitor = Competitor(name, elo, w, l)

    global sum
    sum += w+l
    global amount
    amount += 1

    return competitor

# Parses all lines from the input file
def getCompetitors(filename):
    openedFile = open(filename, 'r').readlines()
    competitors = [parseLine(line) for line in openedFile]
    return competitors

# Gets two random competitors from the competior pool
def getRandom(objectList):
    if len(objectList) == 1:
        return 0, 0

    a = random.randint(0, len(objectList)-1)
    global sum
    global amount
    while objectList[a].w+ objectList[a].l > sum/amount:
        a = random.randint(0, len(objectList)-1)

    b = a
    while b == a:
        b = random.randint(0, len(objectList)-1)

    return a, b

# Calculates constants reffered to 
def calculateConstants(a, b, objectList):
    cA = objectList[a]
    cB = objectList[b]

    qA = 10**(cA.elo/400)
    qB = 10**(cB.elo/400)

    eA = qA/(qA+qB)
    eB = qB/(qA+qB)

    return eA, eB

def getWinner(a, b, objectList):
    newLines(30)

    print(objectList[a])
    print(objectList[b])

    newLines(10)

    winner = input()
    while winner not in ['a', 'l', 'r', 'q', 's']:
        winner = input()

    return winner


def main(filename):
    competitors = getCompetitors(filename)
    
    while True:
        a, b = getRandom(competitors)
        eA, eB = calculateConstants(a, b, competitors)
        
        winner = getWinner(a, b, competitors)

        k = 50

        global sum
        global amount

        # A
        if winner == 'a':
            competitors[a].elo += k*(1-eA)
            competitors[a].w += 1
            competitors[b].elo += k*(-eB)
            competitors[b].l += 1
            sum += 2
        if winner == 'l':
            competitors[a].elo += k*(-eA)
            competitors[a].l += 1
            competitors[b].elo += k*(1-eB)
            competitors[b].w += 1
            sum += 2
        if winner == 'q':
            ranked = getSorted(competitors)
            saveData(ranked, filename)
            break
        if winner == 's':
            ranked = getSorted(competitors)
            saveData(ranked, filename)
        if winner == 'r':
            newLines(30)
            ranked = getSorted(competitors)
            counter = 1
            for comp in ranked:
                print('#'+str(counter), end=' ')
                print(comp.name+' '+str(int(comp.elo)) + ' w/l:'+str(int(comp.w))+' '+str(int(comp.l)))
                counter += 1

            print(sum, amount)

            dummy = input()

def getSorted(competitors):
    ranked = sorted(competitors, reverse=True, key=operator.attrgetter('elo'))
    return ranked

def saveData(competitors, filename):
    openedFile = open(filename, 'w')
    for competitor in competitors:
        stringToWrite = ''
        stringToWrite += competitor.name + ' '
        stringToWrite += str(competitor.elo) + ' '
        stringToWrite += str(competitor.w) + ' '
        stringToWrite += str(competitor.l) + '\n'
        openedFile.write(stringToWrite)
    openedFile.close()

radiohead = 'radiohead.txt'
countries = 'countries.txt'
letters = 'letters.txt'
albums = 'albums.txt'
universities = 'universities.txt'

main(albums)
