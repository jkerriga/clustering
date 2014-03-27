from numpy import *
import matplotlib
from gSplit import *
from pylab import *
import commands, sys, time, os
from optparse import OptionParser
from ksplit2 import *

########################
########################
# Requires the following .py files to work: cluster.py, ksplit.py
# ks_means.py and ksplit.py take the data observations and cluster them using the KSmeans splitting
# method for finding sets of clusters within data.
########################
######################## 
def gMeans(obs,runs):
    numKW = []
    num_k = []
    n_obs = zeros(shape(obs))

    # Normalize the observation(parameter) space for ksmeans
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
        centroids,labels,ks = gSplit(n_obs)
        
        p = 0
        for j in range(max(labels)+1):
            l = where(labels==j)
            if len(l[0]) >= 1:
                labels[l[0]] = p
                p += 1
            else:
                continue    
        cond = 0
        #for t in range(max(labels)):
        #    if len(n_obs[labels == t,0]) < 0:
        #        i -= 1
        #        cond = 1
        #        break
        #    else:
        #        cond = 0
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
        below = 0
        for r in range(max(labels)+1):
            if len(labels[labels == r]) <= 20:
                below += 1
            else:
                continue
            
        numKW.append((k-below))
    centroids_list = delete(centroids_list,0,0)

    # Bins the different cluster #'s found and uses the most popular one as the found cluster #
    bins = add(0.5,range(1,int(max(num_k))+1))
    his_k = hist(num_k,bins=bins)                                                                                                               
    max_k = int(round(his_k[1][argmax(his_k[0])]))  
    print his_k
    
    print "\n"+ str(max_k)
    figure()
    subplot(2,1,1)
    hist(num_k,bins=bins)
    title('Histogram of clusters found over %i trials'%runs)
    xlabel('clusters found')
    ylabel('# of occurrences')
    subplot(2,1,2)
    hist(numKW,bins=bins)
    title('Histogram of clusters found w/o clusters < 20 elements')
    xlabel('clusters found')
    ylabel('# of occurrences')
    savefig('k_cluster_histogram.png')
    close()
    print 'Finding ideal cluster number.'

    # Using the histogram, this will find the k, with the most occurences of ksmeans
    # finding such a k.
    if runs == 1:
        print "Only 1 run."
    else:
        new_k = 0
        b = 0
        while new_k != max_k:
            centroids,labels,ks = gSplit(n_obs)
            #centroids,labels = kmeans2(n_obs,max_k,minit='points')
            new_k = len(set(labels))
            b += 1
            # Stops ksplit from running forever
            if b > 99:
                print 'Cluster # is taking too long to recreate. Re-run ksmeans.'
                break

    print 'Reordering cluster labels.'


    # Reorders the cluster labels, from 0 to last cluster.
    p = 0
    for i in range(max(labels)+1):
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
