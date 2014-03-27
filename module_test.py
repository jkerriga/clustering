import numpy
from pylab import *
import scipy
from gMeans import gMeans
from randomClusters import randomClusters
import time
from scipy.cluster.vq import *
from clusterClassification import clusterClassification

# Number of clusters in observation space 
clusters = 5
# Lower cluster element limit
lower_limit = 50
# Upper cluster element limit
upper_limit = 150
# Number of clustering trials
trials = 100

# Initializes an observation space with randomly placed clusters and background noise(if on)
# Note: Setting lower_limit = upper_limit will make all clusters have the same number of elements
obs,x,y,cls_labels = randomClusters(clusters,lower_limit,upper_limit,background = 'off')

# Plots observation space prior to clustering
plot(obs[:,0],obs[:,1],'.')
plot(x,y,'ok')
tick_params(axis='x',which='both',bottom='off',top='off',labelbottom='off')
tick_params(axis='y',which='both',left='off',labelleft='off',right='off')
savefig('obs_space.png')
close()

# Starts clustering time
size = len(obs)
size = size
print '%0.1f data points'%size
t0 = time.clock()

# This is the main clustering module being called, input is the observation space
# and how many times to cluster
labels,k,centroids = gMeans(obs,trials)

# Ends and prints clustering time
process = time.clock() - t0
print 'Process time: %0.2f secs'%process

# Finds clusters with < 20 elements and creates new index with all clusters
# containing > 20 elements
below = 0
greater_20_elem = []
for i in range(max(labels)+1):
    if len(labels[labels == i]) <= 20:
        below += 1
    else:
        greater_20_elem.append(i)
        continue
# Prints number of clusters found that are considered non-negligible(> 20 elements)
print "post k found: " ,(k-below)

## Classification test                                                                                                                         
xtest = [-8,1.0],[5,1],[3,-3.0],[6.9,-5.0]
xtest = vstack(xtest)
S,classy = clusterClassification(obs,labels,centroids,xtest)

print "Classification cluster label: ",classy," Log Likelihood: ",S



# Plots both the clustered observation space with clusters containing > 20 elements
# and all clusters found in the observation space in a subplot
colors = rand(k,3)
figure()

subplot(2,1,1)
for j in greater_20_elem:
#for j in range(max(labels)+1):
    scatter(obs[labels == j,0],obs[labels == j,1],c = colors[j],linewidths=0)
    text(centroids[j,0],centroids[j,1],"%i"%j,fontsize=10)

plot(x,y,'ok')
for i in range(len(xtest)):
    plot(xtest[i,0],xtest[i,1],'or')
    text(xtest[i,0],xtest[i,1],"%i"%classy[i],fontsize=23)
tick_params(axis='x',which='both',bottom='off',top='off',labelbottom='off')
tick_params(axis='y',which='both',left='off',labelleft='off',right='off')
plot(centroids[greater_20_elem,0],centroids[greater_20_elem,1],'xk',ms=15)
subplot(2,1,2)
for j in range(max(labels)+1):
    scatter(obs[labels == j,0],obs[labels == j,1],c = colors[j],linewidths=0)
    text(centroids[j,0],centroids[j,1],"%i"%j,fontsize=10)
plot(x,y,'ok')
for i in range(len(xtest)):
    plot(xtest[i,0],xtest[i,1],'or')
    text(xtest[i,0],xtest[i,1],"%i"%classy[i],fontsize=23)
tick_params(axis='x',which='both',bottom='off',top='off',labelbottom='off')
tick_params(axis='y',which='both',left='off',labelleft='off',right='off')
plot(centroids[greater_20_elem,0],centroids[greater_20_elem,1],'xk',ms=15)

title("gmeans w/ Gaussianity Test")
  
#subplot(2,1,2)

#for j in range(max(labels)+1):
#    scatter(obs[kmlabels == j,0],obs[kmlabels == j,1],c = colors[j],linewidths=0)
#plot(x,y,'ok')
#tick_params(axis='x',which='both',bottom='off',top='off',labelbottom='off')
#tick_params(axis='y',which='both',left='off',labelleft='off',right='off')
#plot(kmcentroids[:,0],kmcentroids[:,1],'xk',ms=15)
#title("Scipy Kmeans")
xlabel('Cluster time: %0.2f secs'%process + "Clusters (k): %i"%k)
savefig('clustered_obs_space.png')

