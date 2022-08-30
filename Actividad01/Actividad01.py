import numpy as np
import pandas as pd
import pylab as pl

from collections import Counter

def frecuency_table(frecuencyRange, items):
    total = len(items)
    max = items[total-1]
    min = 0
    rangeFrecuency = float(max) / float(frecuencyRange)
    countList = []
    for i in range(frecuencyRange):
        count = 0
        maxRange = ( rangeFrecuency / float(max)) * i
        for j in range(total):
            if(i != 0):
                if(float(items[j])) < maxRange and (float(items[j])) >= min:
                    count += 1
        countList.append(count)
        min = maxRange
    #last range
    count = 0
    for i in range(total):
        if(float(items[i])) <= float(max) and (float(items[i])) >= min:
            count += 1
    countList.append(count)
    return countList
    
    

def histogram_plot(rangeList, countList):
    xList = []
    for i in range(len(rangeList)):
        xList.append(i+1)
    x = xList
    xTicks = rangeList
    y = countList
    pl.xticks(x, xTicks)
    pl.xticks(range(len(rangeList)), xTicks, rotation=45) #writes strings with 45 degree angle
    pl.plot(x,y,'-')
    pl.show()
#    print("happy thoughts")

with open('data01.txt', 'r') as fd:
    lines = fd.read().split()
    # sorts items
    items = sorted(lines)
    # prints desired output

# positive number > 0
frecuencyRange = 11
count = frecuency_table(frecuencyRange, items)
print("range" + "                       " + "frecuency")
total = len(items)
max = items[total-1]
min = 0
rangeFrecuency = float(max) / float(frecuencyRange)
rangeList = []
for i in range(frecuencyRange+1):
    maxRange = ( rangeFrecuency / float(max)) * i
    if(i != 0):
        rangeList.append("[" + str(format(min,".4f")) +  "-" + str(format(float(maxRange),".4f")) + "]")
    min = maxRange

count.pop(0)
for i in range(len(rangeList)):
    print(rangeList[i], "           ", count[i])

histogram_plot(rangeList,count)


#for i in range(total):
#    print(items[i])

