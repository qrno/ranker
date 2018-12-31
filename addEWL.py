def addEWL(line):
    return line[:-1] + ' 1400 0 0\n'

filenameR = 'albums.txt'
filenameW = 'albums2.txt'

openedFile = open(filenameR, 'r').readlines()
openedFile = [addEWL(line) for line in openedFile]

writeTo = open(filenameW, 'w')
for line in openedFile:
    writeTo.write(line)
