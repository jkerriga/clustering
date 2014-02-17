from numpy import *
import matplotlib
from matplotlib.font_manager import FontProperties
import pylab
from scipy import io
from sklearn import mixture
from matplotlib.pyplot import imread
from numpy.linalg import norm

fignum=1
pylab.figure(fignum)

#mat = io.loadmat('digits_full.mat')
mat = loadtxt('pendigits.csv',delimiter=',')
labels = loadtxt('/Users/joshkerrigan/Documents/LIGO Collab/clustering/digits_labels.txt')
# Grab the array of digits out of the 'dict' structure                                                                                                                                               
#digit_data = mat['digits']
digit_data = mat
digits = digit_data
print max(labels)
print digits
le = 0
clu = max(labels)
pylab.ion()
for i in range(40):
    digitclass = digits[labels == i,:]
    if len(digitclass)< 10:
        continue
    le += len(digitclass)
    digit_mean = mean(digitclass,0)
    digit_mean.shape = (16,16)

    pylab.subplot(6,10,i+1)
    pylab.title(i)#'\n#'+ str(len(digitclass)))
    pylab.imshow(digit_mean,cmap=pylab.cm.gray)
    #pylab.draw()
    #pylab.show()
    #labels[labels == i] = input('What is this? ')

    pylab.xticks(visible=False)
    pylab.yticks(visible=False)

    ax = pylab.gca()
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
#pylab.show()
print 'Total Samples: ',le
pylab.savefig('digit_mean.png')
centroids = loadtxt('digits_centroids.txt')
#savetxt('new_labs.txt',labels)

zz = imread('eight16.png')
z = []
for m in range(16):
    z = append(z,zz[m,:])
z = reshape(z,(256,))

r = zeros(2)
for j in range(int(clu)):
    xyz = norm((z  - centroids[j,:])**2)
    
    if j == 0:
        r[0] = xyz
    if xyz < r[0]:
        r[0] = xyz
        r[1] = j
new_labs = loadtxt('new_labs.txt')
print 'This is a ...',(new_labs[int(r[1])]-100)
        
    
    


