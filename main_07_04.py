import random
from matplotlib.pyplot import *
import numpy
from numpy.random import *
import math
from scipy.stats import *
import scipy
from statsmodels.distributions.empirical_distribution import ECDF

sample_size=10

#>>> X = numpy.random.uniform(low=0, high=1, size=10000)
#>>> Y = where( X>0.5, 1, -1)
#>>> Z = [ sumlist( Y[:k], k ) for k in range(len(Y)) ]
#>>> plot( list(range(10000)), Z )
#[<matplotlib.lines.Line2D object at 0x013AA280>]
#>>> show()

labels0 = [choice([-1,1]) for _ in range(sample_size)]

def sumlist(labels, x):
    sum = 0
    for i in range(x):
        sum+= labels[i]
    return sum

print(labels0)

print(sumlist(labels0, 5))

# plot(list(range(sample_size)), [sumlist(labels,k) for k in range(sample_size)])
# show()


labels = numpy.random.uniform(low=-1, high=1, size=(100,20000))
# print(labels)
labels = [ sum(x) for x in zip(*labels) ] #SUMOWANIE KOLUMN
#print(labels)
print( stats.normaltest(labels) )
print( scipy.mean(labels) )
print( math.sqrt(numpy.var(labels)) )


# plot(list(range(sample_size)), labels)
# show()
ls1=numpy.linspace(-15,15,101)
labelsEstNorm =  norm.cdf(ls1, scipy.mean(labels),math.sqrt(numpy.var(labels)))
plot( ls1, labelsEstNorm )
show()

ecdf = ECDF(labels)
plot(ecdf.x, ecdf.y)
show()

ls=numpy.linspace(-15,15,15)
print( [ ecdf(x) for x in ls ] )

delta = 0.1

ls=numpy.linspace(-15,15,round(10/delta)+1)
gestosc = [ (ecdf(x+delta)-ecdf(x))/delta for x in ls]
plot(ls,gestosc)
show()

labelsEstNorm =  norm.pdf(ls1, scipy.mean(labels),math.sqrt(numpy.var(labels)))
plot( ls1, labelsEstNorm )
show()

print()
