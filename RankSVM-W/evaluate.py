import sys
from random import sample 
import numpy as np

predictions = sys.argv[1]
labels = sys.argv[2]
results = sys.argv[3]

prob = []
noisy = []

fp = open(predictions, 'r')
for line in fp:
	if line:
		prob.append(float(line.strip()))
fp.close()

fp = open(labels, 'r')
for line in fp:
	if line:
		noisy.append(float(line.strip()))
fp.close()

tp = 0
tn = 0
fp = 0
fn = 0

for i in range(len(prob)):
	if prob[i] < 0.5 and noisy[i] == 1:
		tp += 1
	elif prob[i] < 0.5 and noisy[i] == 0:
		fp += 1
	elif prob[i] >= 0.5 and noisy[i] == 1:
		fn += 1
	else:
		tn += 1

prec = 100*tp/(tp+fp)
recall = 100*tp/(tp+fn)

tp = tp/len(prob)*100
fp = fp/len(prob)*100
fn = fn/len(prob)*100
tn = tn/len(prob)*100

f = open(results, 'w')
f.write("True Positive: "+ str(tp) + "\n")
f.write("False Positive: "+ str(fp) + "\n")
f.write("False Negative: "+ str(fn) + "\n")
f.write("True Negative: "+ str(tn) + "\n")
f.write("Precision: "+ str(prec) + "\n")
f.write("Recall: "+ str(recall) + "\n")
f.close()

