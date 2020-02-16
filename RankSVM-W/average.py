import os
import sys 
import numpy as np

rootdir = sys.argv[1]
outputfile = open(os.path.join(rootdir, 'average.txt'), 'w')

avg_prec = 0.0
avg_recall = 0.0

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
    	if file == 'result':
        	result_file = open(os.path.join(subdir, file), 'r')
        	lines = result_file.readlines()
        	avg_prec += float(lines[4][11:-1])
        	avg_recall += float(lines[5][8:-1])

avg_prec /= 10
avg_recall /= 10

print('Average Precision	Average Recall', file = outputfile)
print('{:.4f}	{:.4f}'.format(avg_prec, avg_recall), file = outputfile)