import sys
from random import sample
import math

def parse(line):
    sl = line.split()
    y = int(sl[0])
    id = int(sl[1].split(':')[1])
    X = []
    for i in range(2, 48):
        val = float(sl[i].split(':')[1])
        X.append(val)
    return id, X, y

def populate(data):
    relv = {}
    not_relv = {}
    relv_index = {}
    not_relv_index = {}
    index = 0
    for line in data:
        id, X, y = parse(line)
        if y == 0:
            if id in not_relv:
                not_relv[id].append(X)
                not_relv_index[id].append(index)
            else:
                not_relv[id] = [X]
                not_relv_index[id] = [index]
        else:
            if id in relv:
                relv[id].append(X)
                relv_index[id].append(index)
            else:
                relv[id] = [X]
                relv_index[id] = [index]
        index += 1
    return relv, not_relv, relv_index, not_relv_index

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

def l2norm(X1, X2):
    l2 = 0.00
    for i in range(len(X1)):
        l2 += ((X1[i] - X2[i])**2)
    return math.sqrt(l2)

def most_similar_antidocs(relv, not_relv, relv_index, not_relv_index):
    relv_ids = relv.keys()
    not_relv_ids = not_relv.keys()
    both_ids = intersection(relv_ids, not_relv_ids)
    
    similarity = []
    
    for id in both_ids:
        relv_docs = relv[id]
        relv_docs_index = relv_index[id]
        not_relv_docs = not_relv[id]
        not_relv_docs_index = not_relv_index[id]
        
        for i in range(len(relv_docs)):
            for j in range(len(not_relv_docs)):
                l2distance = l2norm(relv_docs[i], not_relv_docs[j])
                similarity.append((relv_docs_index[i], not_relv_docs_index[j], l2distance))
    
    similarity = sorted(similarity, key=lambda x: x[2])
    return similarity

def choosing_flips(similarity, num):
    flipped_indexes = []
    flipped_num = 0
    id = 0
    while flipped_num < num:
        not_relv_ind = similarity[id][1]
        if not_relv_ind not in flipped_indexes:
            flipped_indexes.append(not_relv_ind)
            flipped_num += 1
        id += 1
    return flipped_indexes

def flip(data, flipped):
    for f in flipped:
        actual_label = int(data[f][0])
        if actual_label == 0:
            flipped_char = '1'
        else:
            flipped_char = '0'
        data[f] = flipped_char + data[f][1:] 

input = sys.argv[1]
noise_ratio = float(sys.argv[2])
output = sys.argv[3]

fp = open(input, 'r')
data = fp.readlines()
fp.close()

relv, not_relv, relv_index, not_relv_index = populate(data)

similarity = most_similar_antidocs(relv, not_relv, relv_index, not_relv_index)

flipped = choosing_flips(similarity, int(len(data)*noise_ratio))
flipped.sort()

flip(data, flipped)

fp = open(output, 'w')
for line in data:
	fp.write(line)
fp.close()