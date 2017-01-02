#2D array, with random population
import random

aCords = []
aDetail = []
for x in range (0, 4):
    #Random Co-ord generator
    aDetail.insert(0,([random.randint(0,300)],[random.randint(0,300)]))
    aCords.insert(0,[aDetail])
print(aCords[[random.randint(0,300)]])
