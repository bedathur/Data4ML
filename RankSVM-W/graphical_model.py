import sys
from random import sample
import math
import numpy as np

def parse(line):
    sl = line.split()
    y = int(sl[0])
    if y == 2:
        y = 1
    id = int(sl[1].split(':')[1])
    X = []
    for i in range(2, 48):
        val = float(sl[i].split(':')[1])
        X.append(val)
    return id, X, y

def populate(data):
    X_dict = {}
    y_dict = {}
    index_dict = {}
    X_global = np.empty((0,46), float)
    y_global = []
    ind = 0
    for line in data:
        id, X, y = parse(line)
        X_global = np.append(X_global, [X], axis=0)
        y_global.append(y)
        if id in X_dict:
            X_dict[id] = np.append(X_dict[id], [X], axis=0)
            y_dict[id].append(y)
            index_dict[id].append(ind)
        else:
            X_dict[id] = np.empty((0,46), float)
            y_dict[id] = []
            index_dict[id] = []
            X_dict[id] = np.append(X_dict[id], [X], axis=0)
            y_dict[id].append(y)
            index_dict[id].append(ind)
        ind += 1
    return X_dict, y_dict, X_global, y_global, index_dict

def getalpha(y):
	alpha0 = 0
	alpha1 = 0
	for yi in y:
	    if yi == 0:
	        alpha0 += 1
	    else:
	        alpha1 += 1
	alpha0 /= len(y)
	alpha1 /= len(y)
	return [alpha0, alpha1]

def quantize(f, b):
    f_min = np.min(f, axis=0)
    f_max = np.max(f, axis=0)
    mq = f.shape[0]
    tf = f.shape[1]
    f_new = np.zeros((mq, tf), dtype=int)
    for i in range(mq):
        for j in range(tf):
            if f_min[j] == f_max[j]:
                f_new[i][j] = 1
            else:
                f_new[i][j] = round(b*(f[i][j] - f_min[j])/(f_max[j] - f_min[j])) + 1
    return f_new

def getbeta(X, y, b):
    X_new = quantize(X, b-1)
    mq = X.shape[0]
    nf = X.shape[1]
    beta = np.zeros((2, nf, b), dtype = float)
    i0 = 0
    i1 = 0
    for i in range(mq):
        if y[i] == 0:
            i0 += 1
        else:
            i1 += 1
        for j in range(nf):
            k = X_new[i][j]
            yi = y[i]
            beta[yi][j][k-1] += 1
    if i0 != 0:
        for j in range(nf):
            for k in range(b):
                beta[0][j][k]/=i0
    if i1 != 0:
        for j in range(nf):
            for k in range(b):
                beta[1][j][k]/=i1
    return beta

def estimateparameters(X, y, X_global, y_global, b, lamb):
    alpha_global = getalpha(y_global)
    beta_global = getbeta(X_global, y_global, b)
    alphas = {}
    betas = {}
    for qid in X:
        alphas[qid] = lamb * np.array(getalpha(y[qid])) + (1 - lamb) * np.array(alpha_global)
        betas[qid] = lamb * np.array(getbeta(X[qid], y[qid], b)) + (1 - lamb) * np.array(beta_global)
    return alphas, betas

def predictcondprob(X, y, alphas, betas, b):
    condprob = {}
    for qid in X:
        X_q = quantize(X[qid], b-1)
        mq = X_q.shape[0]
        nf = X_q.shape[1]
        condprob[qid] = []
        for i in range(mq):
            p0 = alphas[qid][0]
            p1 = alphas[qid][1]
            for j in range(nf):
                k = X_q[i][j]
                p0 *= betas[qid][0][j][k-1]
                p1 *= betas[qid][1][j][k-1]
            if y[qid][i] == 0:
                condprob[qid].append(p0/(p0+p1))
            else:
                condprob[qid].append(p1/(p0+p1))
    return condprob

def getindexedresults(condprob, index_dict, m):
    prob = np.zeros(m, dtype=float)
    for id in condprob:
        for i in range(len(condprob[id])):
            prob[index_dict[id][i]] = condprob[id][i]
    return prob

input = sys.argv[1]
output = sys.argv[2]

fp = open(input, 'r')
data = fp.readlines()
fp.close()

X, y, X_global, y_global, index_dict = populate(data)

alphas, betas = estimateparameters(X, y, X_global, y_global, 5, 0.75)

conditional_probability = predictcondprob(X, y, alphas, betas, 5)

correctprob = getindexedresults(conditional_probability, index_dict, X_global.shape[0])

fp = open(output, 'w')
for p in correctprob:
	fp.write(str(p)+"\n")
fp.close()

