import sys
from random import sample 
import numpy as np

input = sys.argv[1]
noise_ratio = float(sys.argv[2])
output = sys.argv[3]
labels = sys.argv[4]

fp = open(input, 'r')
data = fp.readlines()
fp.close()

n = len(data)
k = int(n*noise_ratio)
flipped = sample(range(0, n-1), k)
flipped.sort()
noise_labbeled = np.zeros(n, dtype=int)

for f in flipped:
	actual_label = int(data[f][0])
	if actual_label == 0:
		flipped_char = '1'
	else:
		flipped_char = '0'
	data[f] = flipped_char + data[f][1:]
	noise_labbeled[f] = 1 

fp = open(output, 'w')
for dp in data:
	fp.write(dp)
fp.close()

fp = open(labels, 'w')
for l in noise_labbeled:
	fp.write(str(l) + "\n")
fp.close()

