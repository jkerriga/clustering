import pylab
from scipy import io
from numpy import *
import scipy
from ksmeans import ksmeans
import time
#mat = io.loadmat('digits_full.mat')
#digit_data = mat['digits']
digit_data = loadtxt('pendigits.csv',delimiter=',')
print shape(digit_data)

size = shape(digit_data)
size = size[0]*size[1]
t0 = time.clock()
labels,k,centers = ksmeans(digit_data,10)
process = time.clock() - t0
print 'Process time: %0.2f secs'%process
print '%0.1f data points'%size
print k

savetxt('digits_labels.txt',labels)
