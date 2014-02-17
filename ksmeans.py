from numpy import *
import matplotlib
from ksplit import *
from pylab import *
import commands, sys, time, os
from optparse import OptionParser
from ksplit2 import *

########################
########################
# Requires the following .py files to work: cluster.py, ksplit.py
# ks_means.py and ksplit.py take the data observations and cluster them using the KSmeans splitting
# method for finding sets of clusters within data.
## Git test
########################
######################## 
def ksmeans(obs,ks_crit,runs):

    num_k = []
    n_obs = zeros(shape(obs))

    # Normalize the parameter space for ksmeans
    for m in range(len(obs[0,:])):
        n_obs[:,m] = obs[:,m]/max(obs[:,m]) 

    j = 0
    q = 0
    
    # Run ksmeans for set amount of times. If ksmeans finds clusters of elements
    # less than 2, it will redo that iteration.
    centroids_list = zeros((1,shape(obs)[1]))
    i = 0
    while i < runs:
        pct = 100*i/float(runs)
        sys.stdout.write("\r%0.1f%%" %pct)
        sys.stdout.flush()
        centroids,labels,ks = ksplit2(n_obs,ks_crit)
        
        p = 0
        for j in range(300):
            l = where(labels==j)
            if len(l[0]) >= 2:
                labels[l[0]] = p
                p += 1
            else:
                continue    
        for t in range(max(labels)):
            if len(n_obs[labels == t,0]) < 2:
                i -= 1
                cond = 1
                break
            else:
                cond = 0
        if cond == 0:
            k = len(set(labels))
            num_k = append(num_k,k)
            centroids = zeros((max(labels),shape(obs)[1]))
            for q in range(max(labels)):
                for w in range(shape(obs)[1]):
                    centroids[q,w] = mean(n_obs[:,w][labels == q])
            centroids_list = vstack((centroids_list,centroids))
        cond = 0
        i += 1

    centroids_list = delete(centroids_list,0,0)

    # Bins the different cluster #'s found and uses the most popular one as the found cluster #
    bins = add(0.5,range(1,int(max(num_k))+1))
    his_k = hist(num_k,bins=bins)                                                                                                               
    max_k = int(round(his_k[1][argmax(his_k[0])]))  
    print his_k
    #figure()
    #hist(num_k,bins=bins)
    #show()
    print 'Finding ideal cluster number.'

    # Using the histogram, this will find the k, with the most occurences of ksmeans
    # finding such a k.
    new_k = 0
    b = 0
    if runs == 1:
        print ''
    else:
        while new_k != max_k:
            centroids,labels,ks = ksplit2(n_obs,ks_crit)
            new_k = len(set(labels))
            b += 1
            if b > 99:
                print 'Cluster # is taking too long to recreate. Re-run ksmeans.'
                break

    print 'Reordering cluster labels.'


    # Reorders the cluster labels, from 0 to last cluster.
    p = 0
    for i in range(1000):
        l = where(labels==i)
        if len(l[0]) >= 1:
            labels[l[0]] = p                                                                                                           
            p += 1
        else:
            continue
    centroids = zeros((max_k,shape(obs)[1]))
    for j in range(max_k):
        centroids[j,:] = mean(obs[labels == j],0)

    return labels,max_k,centroids
