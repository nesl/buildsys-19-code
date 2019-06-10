import os
import glob
from statistics import mean, stdev

for fileName in glob.glob(os.path.join('.', '*.txt')):
    with open(fileName) as fh:
        data = []
        for number in fh:
            data.append(float(number))
        average = mean(data)
        std_dev = stdev(data)
        print(fileName + ' ' + str(average) + ' ' + str(std_dev))
