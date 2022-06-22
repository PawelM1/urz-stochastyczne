Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:23:07) [MSC v.1927 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from numpy import *
>>> from numpy.random import *
>>> X = rand(10)**2
>>> X
array([0.42376706, 0.77570716, 0.07737331, 0.37968772, 0.16527487,
       0.00851421, 0.83872929, 0.06302936, 0.23641669, 0.42993975])
>>> Y = rand(10)**2
>>> Y
array([0.06906866, 0.00482811, 0.5253077 , 0.16071688, 0.17511026,
       0.00724325, 0.97329665, 0.5476021 , 0.76774017, 0.91249692])
>>> Z = where( Y < 1/2, 0, Y**2 )
>>> Z
array([0.        , 0.        , 0.27594817, 0.        , 0.        ,
       0.        , 0.94730636, 0.29986806, 0.58942497, 0.83265063])
>>> X = randint(1,7,10000)
>>> mean(X)
3.4983
>>> stany = [ 1,2,3,4,5,6 ]
>>> prwd = [ 1/12, 1/6, 1/6, 1/6, 1/6, 3/12 ]
>>> Y = [ choice( stany, prwd ) for i in range(10000) ]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    Y = [ choice( stany, prwd ) for i in range(10000) ]
  File "<pyshell#12>", line 1, in <listcomp>
    Y = [ choice( stany, prwd ) for i in range(10000) ]
  File "mtrand.pyx", line 956, in numpy.random.mtrand.RandomState.choice
  File "mtrand.pyx", line 745, in numpy.random.mtrand.RandomState.randint
  File "_bounded_integers.pyx", line 1355, in numpy.random._bounded_integers._rand_int32
TypeError: 'float' object cannot be interpreted as an integer
>>> Y = choice( stany, 10000, p=prwd )
>>> mean(Y)
3.9126
>>> Y.count(6)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    Y.count(6)
AttributeError: 'numpy.ndarray' object has no attribute 'count'
>>> count_nonzero(Y == 6)
2512
>>> 10000 //6
1666
>>> count_nonzero(Y == 1)
819
>>> waga = [ 1,2,2,2,2,3 ]
>>> Y = random.choices( stany, weights = waga, k = 10000 )
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    Y = random.choices( stany, weights = waga, k = 10000 )
AttributeError: 'builtin_function_or_method' object has no attribute 'choices'
>>> import random
>>> Y = random.choices( stany, weights = waga, k = 10000 )
>>> mean(Y)
3.9368
>>> count_nonzero(Y == 6)
0
>>> Y.coiunt(6)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    Y.coiunt(6)
AttributeError: 'list' object has no attribute 'coiunt'
>>> Y.cont(6)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    Y.cont(6)
AttributeError: 'list' object has no attribute 'cont'
>>> Y.count(6)
2573
>>> rom scipy.stats import *
SyntaxError: invalid syntax
>>> from scipy.stats import *
>>> from matplotlib.pyplot import *
>>> linspace(0,1,10)
array([0.        , 0.11111111, 0.22222222, 0.33333333, 0.44444444,
       0.55555556, 0.66666667, 0.77777778, 0.88888889, 1.        ])
>>> linspace(0,1,11)
array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. ])
>>> p = norm.pdf(ls, 0,1)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    p = norm.pdf(ls, 0,1)
NameError: name 'ls' is not defined
>>> ls=linspace(0,1,11)
>>> p = norm.pdf(ls, 0,1)
>>> plot(ls,p)
[<matplotlib.lines.Line2D object at 0x018E96B8>]
>>> show()
>>> ls=linspace(-5,5,11)
>>> p = norm.pdf(ls, 0,1)
>>> plot(ls,p)
[<matplotlib.lines.Line2D object at 0x016BBF88>]
>>> show()
>>> ls=linspace(-5,5,101)
>>> 
>>> p = norm.pdf(ls, 0,1)
>>> plot(ls,p)
[<matplotlib.lines.Line2D object at 0x01802448>]
>>> show()
>>> p = uniform.pdf(ls, 0,1)
>>> plot(ls,p)
[<matplotlib.lines.Line2D object at 0x0177E9A0>]
>>> show()
>>> p = uniform.pdf(ls, 0,2)
>>> plot(ls,p)
[<matplotlib.lines.Line2D object at 0x04367520>]
>>> show()
>>> p1 = norm.pdf(ls, 0,1)
>>> p2 = norm.pdf(ls, 1,3)
>>> plot(ls,p1)
[<matplotlib.lines.Line2D object at 0x04396FD0>]
>>> plot(ls,p2)
[<matplotlib.lines.Line2D object at 0x043A41C0>]
>>> show()
>>> plot(ls,p1)
[<matplotlib.lines.Line2D object at 0x043D9568>]
>>> plot(ls,p2)
[<matplotlib.lines.Line2D object at 0x043D9730>]
>>> plot.title('gęstości N(0,1) oraz N(1,3)')
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    plot.title('gęstości N(0,1) oraz N(1,3)')
AttributeError: 'function' object has no attribute 'title'
>>> title('gęstości N(0,1) oraz N(1,3)')
Text(0.5, 1.0, 'gęstości N(0,1) oraz N(1,3)')
>>> plot(ls,p1, color='green',label='N(0,1)')
[<matplotlib.lines.Line2D object at 0x043D9898>]
>>> plot(ls,p2, color='red',label='N(1,3)')
[<matplotlib.lines.Line2D object at 0x043CCD78>]
>>> show()
>>> title('gęstości N(0,1) oraz N(1,3)')
Text(0.5, 1.0, 'gęstości N(0,1) oraz N(1,3)')
>>> plot(ls,p1, color='green',label='N(0,1)')
[<matplotlib.lines.Line2D object at 0x12BFFF10>]
>>> plot(ls,p2, color='red',label='N(1,3)')
[<matplotlib.lines.Line2D object at 0x12C0E100>]
>>> legends()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    legends()
NameError: name 'legends' is not defined
>>> legend()
<matplotlib.legend.Legend object at 0x12C0E358>
>>> show()
>>> ls=linspace(-5,5,11)
>>> p = norm.pdf(ls, 0,1)
>>> ls
array([-5., -4., -3., -2., -1.,  0.,  1.,  2.,  3.,  4.,  5.])
>>> p
array([1.48671951e-06, 1.33830226e-04, 4.43184841e-03, 5.39909665e-02,
       2.41970725e-01, 3.98942280e-01, 2.41970725e-01, 5.39909665e-02,
       4.43184841e-03, 1.33830226e-04, 1.48671951e-06])
>>> plot(ls,p)
[<matplotlib.lines.Line2D object at 0x042AB130>]
>>> show()
>>> p1 = poisson.pdf(ls, 1)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    p1 = poisson.pdf(ls, 1)
AttributeError: 'poisson_gen' object has no attribute 'pdf'
>>> p1 = norm.pdf(ls, 0,1)
>>> p2 = norm.pdf(ls, 1,3)
>>> title('gęstości N(0,1) oraz N(1,3)')
Text(0.5, 1.0, 'gęstości N(0,1) oraz N(1,3)')
>>> plot(ls,p1, color='green',label='N(0,1)')
[<matplotlib.lines.Line2D object at 0x04265448>]
>>> plot(ls,p2, color='red',label='N(1,3)')
[<matplotlib.lines.Line2D object at 0x04265610>]
>>> legend()
<matplotlib.legend.Legend object at 0x042CE2C8>
>>> show()
>>> ls=linspace(-5,5,101)
>>> p1 = norm.pdf(ls, 0,1)
>>> p2 = norm.pdf(ls, 1,3)
>>> title('gęstości N(0,1) oraz N(1,3)')
Text(0.5, 1.0, 'gęstości N(0,1) oraz N(1,3)')
>>> plot(ls,p1, color='green',label='N(0,1)')
[<matplotlib.lines.Line2D object at 0x042E2580>]
>>> plot(ls,p2, color='red',label='N(1,3)')
[<matplotlib.lines.Line2D object at 0x042E2748>]
>>> legend()
<matplotlib.legend.Legend object at 0x0428F418>
>>> show()
>>> p1 = norm.cdf(ls, 0,1)
>>> p2 = norm.cdf(ls, 1,3)
>>> title('gęstości N(0,1) oraz N(1,3)')
Text(0.5, 1.0, 'gęstości N(0,1) oraz N(1,3)')
>>> plot(ls,p1, color='green',label='N(0,1)')
[<matplotlib.lines.Line2D object at 0x0427DD00>]
>>> plot(ls,p2, color='red',label='N(1,3)')
[<matplotlib.lines.Line2D object at 0x0427D490>]
>>> legend()
<matplotlib.legend.Legend object at 0x042783B8>
>>> show()
>>> p1 = uniform.cdf(ls, 0,1)
>>> plot(ls,p1)
[<matplotlib.lines.Line2D object at 0x042ABEB0>]
>>> show()
>>> p1 = poisson.cdf(ls, 1)
>>> p2 = poisson.cdf(ls, 5)
>>> plot(ls,p1, color='green',label='poisson(1)')
[<matplotlib.lines.Line2D object at 0x12BDDBC8>]
>>> plot(ls,p2, color='red',label='poisson(5)')
[<matplotlib.lines.Line2D object at 0x12BDDC10>]
>>> legend()
<matplotlib.legend.Legend object at 0x12BDDA30>
>>> show()
>>> p = gamma.cdf(ls, 2,0,1)
>>> plot(ls,p)
[<matplotlib.lines.Line2D object at 0x01802250>]
>>> show()
>>> p = gamma.cdf(ls, 2,0,5)
>>> plot(ls,p)
[<matplotlib.lines.Line2D object at 0x018E9688>]
>>> show()
>>> X = randn(1000)
>>> arange(1,11)
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
>>> walkingMean = cumsum(X)/(arange(1,1001))
>>> plot(walkingMean)
[<matplotlib.lines.Line2D object at 0x04383148>]
>>> show()
>>> X = randn(100000)
>>> walkingMean = cumsum(X)/(arange(1,100001))
>>> plot(walkingMean)
[<matplotlib.lines.Line2D object at 0x12C070A0>]
>>> show()
>>> X = randn(100000)
>>> walkingMean = cumsum(X)
>>> plot(walkingMean)
[<matplotlib.lines.Line2D object at 0x017F3F28>]
>>> show()
>>> X = randn(100000)
>>> walkingMean = cumsum(X)
>>> plot(walkingMean)
[<matplotlib.lines.Line2D object at 0x043B52E0>]
>>> show()
>>> X = randn(100000)
>>> walkingMean = cumsum(X)
>>> plot(walkingMean)
[<matplotlib.lines.Line2D object at 0x017A7D90>]
>>> show()
>>> hist(randn(1000),bins=30,density=True)
(array([0.01017655, 0.01526482, 0.03561792, 0.03561792, 0.05597101,
       0.10176547, 0.10176547, 0.15773648, 0.18317785, 0.20353094,
       0.29003159, 0.27985505, 0.40706189, 0.37653225, 0.36126742,
       0.50373908, 0.37144397, 0.29511987, 0.30020814, 0.22388404,
       0.20353094, 0.1933544 , 0.12211857, 0.08650065, 0.05088274,
       0.04579446, 0.04070619, 0.01526482, 0.01017655, 0.01017655]), array([-2.87033378, -2.67380347, -2.47727316, -2.28074285, -2.08421253,
       -1.88768222, -1.69115191, -1.49462159, -1.29809128, -1.10156097,
       -0.90503065, -0.70850034, -0.51197003, -0.31543972, -0.1189094 ,
        0.07762091,  0.27415122,  0.47068154,  0.66721185,  0.86374216,
        1.06027248,  1.25680279,  1.4533331 ,  1.64986341,  1.84639373,
        2.04292404,  2.23945435,  2.43598467,  2.63251498,  2.82904529,
        3.0255756 ]), <BarContainer object of 30 artists>)
>>> show()
>>> p1=hist(randn(1000),bins=30,density=True)
>>> p2=norm.pdf(0,1)
>>> p2=norm.pdf(ls,0,1)
>>> plot(ls,p2)
[<matplotlib.lines.Line2D object at 0x043D0D78>]
>>> show()
>>> p1=hist(randn(10),bins=30,density=True)
>>> p2=norm.pdf(ls,0,1)
>>> plot(ls,p2)
[<matplotlib.lines.Line2D object at 0x01817850>]
>>> show()
>>> p1=hist(randn(100000),bins=30,density=True)
>>> p2=norm.pdf(ls,0,1)
>>> plot(ls,p2)
[<matplotlib.lines.Line2D object at 0x042DB238>]
>>> show()
>>> p1=hist(randn(1000000),bins=30,density=True)
>>> p2=norm.pdf(ls,0,1)
>>> plot(ls,p2)
[<matplotlib.lines.Line2D object at 0x016D2F70>]
>>> show()
>>> den = gaussian_kde(randn(1000)) # rozkład Normalny jest gładki
>>> ls = linspace(-3,3,100)
>>> plot(xs,den(ls))
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    plot(xs,den(ls))
NameError: name 'xs' is not defined
>>> plot(ls,den(ls))
[<matplotlib.lines.Line2D object at 0x12BEB4D8>]
>>> plot(ls, norm.pdf(ls,0,1))
[<matplotlib.lines.Line2D object at 0x12BEBC10>]
>>> show()
>>> den = gaussian_kde(randn(10000)) # rozkład Normalny jest gładki
>>> ls = linspace(-3,3,100)
>>> plot(xs,den(ls))
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    plot(xs,den(ls))
NameError: name 'xs' is not defined
>>> plot(ls,den(ls))
[<matplotlib.lines.Line2D object at 0x12C08CA0>]
>>> plot(ls, norm.pdf(ls,0,1))
[<matplotlib.lines.Line2D object at 0x12C08E68>]
>>> show()
>>> den = gaussian_kde(randn(10000)) # rozkład Normalny jest gładki
>>> ls = linspace(-3,3,1000)
>>> plot(xs,den(ls))
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    plot(xs,den(ls))
NameError: name 'xs' is not defined
>>> plot(ls,den(ls))
[<matplotlib.lines.Line2D object at 0x042AB808>]
>>> plot(ls, norm.pdf(ls,0,1))
[<matplotlib.lines.Line2D object at 0x042AB9D0>]
>>> show()
>>> den = gaussian_kde(randn(100000)) # rozkład Normalny jest gładki
>>> ls = linspace(-3,3,1000)
>>> plot(ls,den(ls))
[<matplotlib.lines.Line2D object at 0x0428D370>]
>>> show()
>>> plot(ls,den(ls))
[<matplotlib.lines.Line2D object at 0x042FDCB8>]
>>> plot(ls, norm.pdf(ls,0,1))
[<matplotlib.lines.Line2D object at 0x042FDE80>]
>>> show()
>>> den = gaussian_kde(randn(1000)) # rozkład Normalny jest gładki
>>> ls = linspace(-3,3,100)
>>> ccdf = cumsum(den)*0.06
Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    ccdf = cumsum(den)*0.06
TypeError: unsupported operand type(s) for *: 'gaussian_kde' and 'float'
>>> ccdf = cumsum(den)*[0.06 for i in range(len(den)]
		    
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> ccdf = cumsum(den)*[0.06 for i in range(len(den))]
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    ccdf = cumsum(den)*[0.06 for i in range(len(den))]
TypeError: object of type 'gaussian_kde' has no len()
>>> ccdf = cumsum(den)
>>> plot(ls,ccdf)
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    plot(ls,ccdf)
  File "C:\Python39-32\lib\site-packages\matplotlib\pyplot.py", line 3019, in plot
    return gca().plot(
  File "C:\Python39-32\lib\site-packages\matplotlib\axes\_axes.py", line 1605, in plot
    lines = [*self._get_lines(*args, data=data, **kwargs)]
  File "C:\Python39-32\lib\site-packages\matplotlib\axes\_base.py", line 315, in __call__
    yield from self._plot_args(this, kwargs)
  File "C:\Python39-32\lib\site-packages\matplotlib\axes\_base.py", line 501, in _plot_args
    raise ValueError(f"x and y must have same first dimension, but "
ValueError: x and y must have same first dimension, but have shapes (100,) and (1,)
>>> ccdf = cumsum(den(ls))
>>> plot(ls,ccdf)
[<matplotlib.lines.Line2D object at 0x04253820>]
>>> show()
>>> ccdf = 0.06*cumsum(den(ls))
>>> plot(ls,ccdf)
[<matplotlib.lines.Line2D object at 0x2261AB38>]
>>> plot(ls, norm.pdf(ls,0,1))
[<matplotlib.lines.Line2D object at 0x2261AD00>]
>>> plot(ls, norm.cdf(ls,0,1))
[<matplotlib.lines.Line2D object at 0x2261AEC8>]
>>> show()
>>> plot(ls,den(ls))
[<matplotlib.lines.Line2D object at 0x042E1790>]
>>> plot(ls, norm.pdf(ls,0,1))
[<matplotlib.lines.Line2D object at 0x042E1C70>]
>>> plot(ls,ccdf)
[<matplotlib.lines.Line2D object at 0x042E1AD8>]
>>> plot(ls, norm.cdf(ls,0,1))
[<matplotlib.lines.Line2D object at 0x042E1E80>]
>>> show()
>>> # jak generować próbkę, posiadając dystrybuantę lub gęstość