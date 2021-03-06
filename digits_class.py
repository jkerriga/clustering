from numpy import *
import matplotlib
from matplotlib.font_manager import FontProperties
import pylab
from scipy import io
from sklearn import mixture
from matplotlib.pyplot import imread

fignum=1
pylab.figure(fignum)

#mat = io.loadmat('digits_full.mat')
mat = loadtxt('pendigits.csv',delimiter=',')
labels = loadtxt('/Users/joshkerrigan/Documents/LIGO Collab/ksmodule/digits_labels.txt')
# Grab the array of digits out of the 'dict' structure                                                                                                                                               
#digit_data = mat['digits']
digit_data = mat
digits = digit_data
print max(labels)
for i in range(30):
    digitclass = digits[labels == i,:]

    digit_mean = mean(digitclass,0)
    digit_mean.shape = (16,16)

    pylab.subplot(2,15,i+1)
    pylab.title('%i'%i)
    pylab.imshow(digit_mean,cmap=pylab.cm.gray)

    pylab.xticks(visible=False)
    pylab.yticks(visible=False)

    ax = pylab.gca()
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)

pylab.savefig('digit_mean.png')
good = [2,3,6,7,9,10]
zz = imread('zero.png')
z = []
for m in range(28):
    z = append(z,zz[:,m])
z = reshape(z,(784,))

prob = zeros(len(good))
#prob = zeros(int(max(labels)))
m = 0
for t in good:
    prob[m] = cov(mean(digits[labels == t,:],0),z)
    m += 1
print prob
print good[argmin(prob)]
