import os
import sys
from random import sample 
from scipy.stats import sem, t
from scipy import mean

def statistics(data, confidence):
	n = len(data)
	m = mean(data)
	std_err = sem(data)
	h = std_err * t.ppf((1 + confidence) / 2, n - 1)
	return m, std_err, h

rootdir = sys.argv[1]
outputfile = open(os.path.join(rootdir, 'statistics.txt'), 'w')

maps = []
ndcgs = []

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
    	if file == 'eval':
        	# print(os.path.join(subdir, file))
        	eval_file = open(os.path.join(subdir, file), 'r')
        	lines = eval_file.readlines()
        	maps.append(float(lines[1].split()[-1]))
        	ndcgs.append(float(lines[4].split()[-1]))


maps_m, maps_std_err, maps_h = statistics(maps, 0.95)
ndcgs_m, ndcgs_std_err, ndcgs_h = statistics(ndcgs, 0.95)

print('MAP(M)	MAP(SE) MAP(CI) NDCG(M) NDCG(SE) NDCG(CI)', file = outputfile)
print('{:.4f}	{:.4f}	{:.4f}	{:.4f}	{:.4f}	{:.4f}'.format(maps_m, maps_std_err, maps_h, ndcgs_m, ndcgs_std_err, ndcgs_h), file = outputfile)