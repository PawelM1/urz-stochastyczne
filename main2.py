import random
import statistics

from matplotlib.pyplot import *
import numpy
from scipy.stats import *
import scipy
from statsmodels.distributions.empirical_distribution import ECDF

sample_size=100
labels = [random.choice([-1,1]) for _ in range(sample_size)]

def sumlist(labels, x):
    sum = 0
    for i in range(x):
        sum+= labels[i]
    return sum

# print(labels)

print(sumlist(labels, 5))

# plot(list(range(sample_size)), [sumlist(labels,k) for k in range(sample_size)])
# show()


labels = 2 * numpy.random.uniform(low=-100, high=100, size=(100,100000)) - 1 - 2 * numpy.random.normal(size=(100,100000))**2
# print(labels)
labels = [ statistics.mean(x) for x in zip(*labels) ] #SUMOWANIE KOLUMN
print(labels[:10])

# plot(list(range(sample_size)), labels)
# show()

ecdf1 = ECDF(labels)   # dystrybuanta próbki
plot(ecdf1.x, ecdf1.y)
show()

# generowanie próbki zmiennej losowej o zadanej zgóry dystrybuancie (w danym przypadku ecdf1()
X = round(numpy.random.rand(100000),3)
print(X[:10])
# obliczamy ecdf1**(-1)
wykresEcdf = [ [x, ecdf1(x)] for x in range(0,1,0.001) ]
wykresOdwrocenejEcdf = [ [y[1],y[0]] for y in wykresEcdf]

delta = 0.01

ls=numpy.linspace(-5,5,round(10/delta)+1)

for x in ls:
    f

Y =


ls=numpy.linspace(-5,5,11)
print( [ ecdf(x) for x in ls ] )

delta = 0.1

ls=numpy.linspace(-5,5,round(10/delta)+1)
gestosc = [ (ecdf(x+delta)-ecdf(x))/delta for x in ls]
plot(ls,gestosc)
show()


