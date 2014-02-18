import numpy
from pylab import *
import scipy
from ksmeans import ksmeans
from random_clusters import random_clusters
import time
# Random cluster initialization; Set # of clusters and the amount of observations
# for each cluster. Setting lower_limit = upper_limit creates all clusters with
# the same amount of observations

clusters = 25
lower_limit = 25
upper_limit = 100
trials = 1000

obs,x,y,cls_labels = random_clusters(clusters,lower_limit,upper_limit)
plot(obs[:,0],obs[:,1],'.')
plot(x,y,'ok')
savefig('obs_space.png')
close()
size = len(obs)
size = size
print '%0.1f data points'%size
t0 = time.clock()

labels,k,centroids = ksmeans(obs,trials)
process = time.clock() - t0
print 'Process time: %0.2f secs'%process

#a = [0,0]
#b = [0,0]
#acc_array = zeros((clusters,k))
#for l in range(clusters):
#    for m in range(k):
#        for n in range(len(obs[cls_labels == l])):
#            for o in range(len(obs[labels == m])):
#                a[0] = obs[cls_labels == l][n,0]
#                a[1] = obs[cls_labels == l][n,1]
#                b[0] = obs[labels == m][o,0]
#                b[1] = obs[labels == m][o,1]
#                if a == b:
#                    acc_array[l,m] += 1

#classify = zeros(clusters)
#for g in range(clusters):
#    acc_array[g,:] = acc_array[g,:]/len(obs[cls_labels == g])
#    classify[g] = argmax(acc_array[g,:])
    
    


colors = rand(k,3)


figure()

for j in range(k):
    scatter(obs[labels == j,0],obs[labels == j,1],c = colors[j],linewidths=0)
    plot(x,y,'ok')
plot(centroids[:,0],centroids[:,1],'xk',ms=15)
title('Cluster time: %0.2f secs'%process)
    #cenx = mean(obs[labels == j,0])
    #ceny = mean(obs[labels == j,1])
    #text(cenx,ceny,'%0.2f' %acc_array[j,classify[j]])

savefig('clustered_obs_space.png')
print k
