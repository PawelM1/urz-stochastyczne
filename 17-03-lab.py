Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:23:07) [MSC v.1927 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from numpy import *
>>> from numpy.random import *
>>> X = empty(10, dtype = float)
>>> X
array([6.23042070e-307, 3.56043053e-307, 1.37961641e-306, 8.06613465e-308,
       1.24610383e-306, 1.69118108e-306, 8.06632139e-308, 1.20160711e-306,
       1.69119330e-306, 0.00000000e+000])
>>> for k in range(10):
    X[k] = rand()**2

    
>>> [ random.random() for i in range(5) ]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    [ random.random() for i in range(5) ]
  File "<pyshell#6>", line 1, in <listcomp>
    [ random.random() for i in range(5) ]
AttributeError: 'builtin_function_or_method' object has no attribute 'random'
>>> import random
>>> [ random.random() for i in range(5) ]
[0.6817361682361937, 0.3944377328219377, 0.15790400514075764, 0.3065340221152425, 0.534963841249794]
>>> [ rand() for i in range(5) ]
[0.0002754224762726576, 0.03299573880905582, 0.6215961628993074, 0.029577821824543493, 0.8429572840488737]
>>> [ rand() for i in range(5) ]
[0.3720744780531572, 0.8587404112029297, 0.8879677382916208, 0.8085298379402498, 0.6055799340446864]
>>> [ rand() for i in range(5) ]
[0.7121847231312324, 0.617630969705781, 0.6006885849702779, 0.18358674719535484, 0.5915570399785722]
>>> X
array([5.28547766e-02, 3.61004415e-02, 1.82799288e-01, 6.46071783e-04,
       6.21902356e-01, 8.86853930e-01, 4.75631453e-01, 5.74583436e-01,
       6.49932665e-05, 2.17999453e-01])
>>> X = rand(10)**2
>>> X
array([0.52917124, 0.18247791, 0.62352398, 0.52866275, 0.19788867,
       0.71699548, 0.16491107, 0.61991965, 0.00082576, 0.07048788])
>>> Y = [0,0,0,0,0]
>>> Y = rand(10)**2
>>> Y
array([0.97214258, 0.00673797, 0.02599228, 0.51798339, 0.83683102,
       0.08125351, 0.49989274, 0.03514687, 0.65756716, 0.32290182])
>>> X = random.random()**2
>>> X
0.17151842318351487
>>> Y
array([0.97214258, 0.00673797, 0.02599228, 0.51798339, 0.83683102,
       0.08125351, 0.49989274, 0.03514687, 0.65756716, 0.32290182])
>>> Y = (1-Y)**2
>>> Y
array([7.76036115e-04, 9.86569461e-01, 9.48691039e-01, 2.32340016e-01,
       2.66241155e-02, 8.44095108e-01, 2.50107276e-01, 9.30941558e-01,
       1.17260250e-01, 4.58461944e-01])
>>> X = where( Y > 1/2, 1, -1 )
>>> X
array([-1,  1,  1, -1, -1,  1, -1,  1, -1, -1])
>>> Y = [0,0,0,0,0]
>>> Y = (1-Y)**2
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    Y = (1-Y)**2
TypeError: unsupported operand type(s) for -: 'int' and 'list'
>>> def f(x):
	while x < 10:
		x *= 2
	return x

>>> f( 3)
12
>>> f(Y)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    f(Y)
  File "<pyshell#31>", line 2, in f
    while x < 10:
TypeError: '<' not supported between instances of 'list' and 'int'
>>> @vectorize
def f(x):
	while x < 10:
		x *= 2
	return x

>>> f(Y)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    f(Y)
  File "C:\Python39-32\lib\site-packages\numpy\lib\function_base.py", line 2113, in __call__
    return self._vectorize_call(func=func, args=vargs)
  File "C:\Python39-32\lib\site-packages\numpy\lib\function_base.py", line 2191, in _vectorize_call
    ufunc, otypes = self._get_ufunc_and_otypes(func=func, args=args)
  File "C:\Python39-32\lib\site-packages\numpy\lib\function_base.py", line 2151, in _get_ufunc_and_otypes
    outputs = func(*inputs)
  File "<pyshell#36>", line 4, in f
    x *= 2
KeyboardInterrupt
>>> Y
[0, 0, 0, 0, 0]
>>> Y = rand(10)**2
>>> f(Y)
array([15.72586086, 17.90115018, 11.81038859, 13.94649889, 11.19079514,
       16.58559565, 10.47916268, 15.1411239 , 12.88292564, 11.22335341])
>>> f(3)
array(12)
>>> X = rand(1)**2
>>> f(X)
array([11.74990938])
>>> Z = array( [ 0,1,2,3,4] )
>>> Z
array([0, 1, 2, 3, 4])
>>> Z = Z**2
>>> Z
array([ 0,  1,  4,  9, 16], dtype=int32)
>>> rand(10) # próbka o rozkładzie równomiernym
array([0.82402625, 0.79303895, 0.33078908, 0.26874579, 0.21316642,
       0.16901951, 0.95047864, 0.54203151, 0.62979253, 0.80563043])
>>> randn(10,0,1) # próbka o rozkładzie normalnym ~~ N(m,s)
array([], shape=(10, 0, 1), dtype=float64)
>>> randn(0,1,10) # próbka o rozkładzie normalnym ~~ N(m,s)
array([], shape=(0, 1, 10), dtype=float64)
>>> m + s* randn(2,3) # zwraca macierz rozmiaru 2*3 wartości losowych o rozkładzie normalnym ~~ N(m,s)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    m + s* randn(2,3) # zwraca macierz rozmiaru 2*3 wartości losowych o rozkładzie normalnym ~~ N(m,s)
NameError: name 'm' is not defined
>>> 2 + 1* randn(2,3) # zwraca macierz rozmiaru 2*3 wartości losowych o rozkładzie normalnym ~~ N(m,s)
array([[2.64776466, 0.50281549, 2.036171  ],
       [0.49110294, 1.93503281, 1.28479265]])
>>> X = randn(10)
>>> X
array([ 1.42320684, -0.78821432, -0.58885726,  0.22373378,  0.08926746,
       -1.13570354, -0.84106617, -0.68001062, -1.907136  , -0.21940719])
>>> mean(X)
-0.44241870306001846
>>> X = randn(10000)
>>> mean(0)
0.0
>>> mean(X)
-0.008910214496128478
>>> var(X)
0.9843877668176059
>>> Y = 2 + 3*X
>>> mean(Y)
1.9732693565116148
>>> var(Y)
8.859489901358454
>>> sqrt(var(Y))
2.976489526499036
>>> X = rand(10000)
>>> mean(X)
0.4999425325060068
>>> var(X)
0.08342855161198791
>>> X = rand(10000)	# rozkł.równoierany na przedziale od 0 do 1
>>> Y = 5 + (10-5)/(1-0)*X
>>> mean(Y)
7.5047244455299795
>>> Z = where( Y<5 or Y>10, 0, 1 )
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    Z = where( Y<5 or Y>10, 0, 1 )
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
>>> Z1 = where( Y<5, 0, Y )
>>> Z2 = where( Y>10, 0, Y )
>>> Z2.count(0)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    Z2.count(0)
AttributeError: 'numpy.ndarray' object has no attribute 'count'
>>> listZ2 = list(Z2)
>>> listZ2.count(0)
0
>>> count_nonzero(X < 7.5)
10000
>>> count_nonzero(Y < 7.5)
4994
>>> count_nonzero(Y < 5)
0
>>> count_nonzero(Y >10)
0
>>> count_nonzero(Y >9)
1973
>>> poisson(3)
1
>>> poisson(3)
2
>>> P = poisson(3,10000)
>>> mean(P)
3.0097
>>> var(P)
2.99640591
>>> count_nonzero(P < 1)
519
>>> count_nonzero(P <= 1)
1970
>>> count_nonzero(P <= 5)
9177
>>> count_nonzero(P <= 1000)
10000
>>> count_nonzero(P <= 50)
10000
>>> P = poisson(3,10000)
>>> count_nonzero(P <= 50)
10000
>>> P = poisson(3,1000000)
>>> count_nonzero(P <= 50)
1000000
>>> count_nonzero(P <= 25)
1000000
>>> max(P)
14
>>> randint(1,6,100)
array([5, 3, 5, 5, 3, 1, 3, 4, 1, 5, 4, 4, 1, 5, 3, 3, 2, 2, 1, 3, 1, 2,
       1, 4, 3, 4, 4, 5, 4, 5, 1, 3, 1, 1, 1, 3, 4, 3, 4, 1, 3, 1, 1, 5,
       4, 5, 5, 2, 3, 1, 3, 5, 5, 3, 4, 2, 2, 3, 4, 4, 3, 2, 1, 3, 4, 5,
       5, 2, 4, 4, 3, 2, 5, 3, 1, 3, 3, 2, 4, 3, 4, 1, 1, 3, 4, 1, 1, 1,
       2, 4, 2, 4, 5, 3, 3, 3, 5, 3, 1, 4])
>>> X = randint(1,7,100)
>>> mean(X)
3.33
>>> X = randint(1,6,100)
>>> mean(X)
3.0
>>> X = randint(1,6,100)
>>> mean(X)
3.05
>>> X = randint(1,7,100)
>>> X = randint(1,7,10000)
>>> mean(X)
3.5088
>>> stany = [ 1,2,3,4,5,6 ]
>>> prwd = [ 1/12, 1/6, 1/6, 1/6, 1/6, 3/12 ]
>>> waga = [ 1,2,2,2,2,3 ]
>>> [ choice( stany, prwd ) for i in range(10) ]
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    [ choice( stany, prwd ) for i in range(10) ]
  File "<pyshell#110>", line 1, in <listcomp>
    [ choice( stany, prwd ) for i in range(10) ]
  File "mtrand.pyx", line 956, in numpy.random.mtrand.RandomState.choice
  File "mtrand.pyx", line 745, in numpy.random.mtrand.RandomState.randint
  File "_bounded_integers.pyx", line 1355, in numpy.random._bounded_integers._rand_int32
TypeError: 'float' object cannot be interpreted as an integer
>>> [ choices( stany, prwd ) for i in range(10) ]
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    [ choices( stany, prwd ) for i in range(10) ]
  File "<pyshell#111>", line 1, in <listcomp>
    [ choices( stany, prwd ) for i in range(10) ]
NameError: name 'choices' is not defined
>>> choice( stany, 10, p = prwd )
array([1, 1, 6, 2, 1, 3, 5, 6, 1, 5])
>>> X = choice( stany, 10000, p = prwd )
>>> mean(X)
3.9111
>>> X = choice( stany, 10000, p = prwd )
>>> mean(X)
3.9433
>>> [ random.choices( stany, waga ) for i in range(10) ]
[[6], [2], [4], [5], [4], [6], [2], [5], [2], [2]]
>>> random.choices( stany, waga, 10 )
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    random.choices( stany, waga, 10 )
TypeError: choices() takes from 2 to 3 positional arguments but 4 were given
>>> random.choices( stany, weigths = waga, k = 10 )
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    random.choices( stany, weigths = waga, k = 10 )
TypeError: choices() got an unexpected keyword argument 'weigths'
>>> random.choices( stany, weights = waga, k = 10 )
[4, 4, 4, 5, 4, 2, 1, 5, 5, 3]
>>> Y = random.choices( stany, weights = waga, k = 10000 )
>>> mean(Y)
3.8814
>>> Y = random.choices( stany, weights = waga, k = 10000 )
>>> mean(Y)
3.9177
>>> Y = random.choices( stany, weights = waga, k = 10000000 )
>>> mean(Y)
3.9169063
>>> Y = random.choices( stany, weights = waga, k = 10000000 )
>>> mean(Y)
3.9160974
>>> Y = random.choices( stany, weights = waga, k = 10000000 )
>>> var(Y)
2.7428646046577603
>>> Y = random.choices( stany, weights = waga, k = 10000000 )
>>> var(Y)
2.742621760717751
>>> Y = random.choices( stany, weights = waga, k = 10000000 )
>>> 
>>> 
>>> var(Y)
2.74338208866876
>>> # X - rozkłąd równomierny na [0,1]
>>> X = rand(10000)
>>> # Y - rozkład normalny N(0,1)
>>> Y = randn(10000)
>>> # Z - rozkład Poissona o intensywności 2
>>> Z - poisson(2,10000)
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    Z - poisson(2,10000)
ValueError: operands could not be broadcast together with shapes (5,) (10000,) 
>>> Z = poisson(2,10000)
>>> # U = 2*X + Y^2 + 3*Z
>>> U = 2*X + Y^2 + 3*Z
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    U = 2*X + Y^2 + 3*Z
TypeError: ufunc 'bitwise_xor' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
>>> U = 2*X + Y**2 + 3*Z
>>> mean(U)
8.058066967639265
>>> # E( 2*X + Y**2 + 3*Z) = 2 * E(X) + E(Y**2) + 3 * E(Z) =
>>> # 2*1/2 + Var(Y)+E(Y)**2 + 3 *2 = 1 + 1+0**2 + 3*2 = 8
>>> X = rand(10000)
>>> Y = randn(10000)
>>> Z - poisson(2,10000)
array([ 0, -1,  2, ..., -1, -2,  0])
>>> U = 2*X + Y**2 + 3*Z
>>> mean(U)
8.056412062685432
>>> X = rand(10000)
>>> Y = randn(10000)
>>> Z - poisson(2,10000)
array([ 0, -2,  1, ...,  1, -1,  0])
>>> U = 2*X + Y^2 + 3*Z
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    U = 2*X + Y^2 + 3*Z
TypeError: ufunc 'bitwise_xor' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
>>> mean(U)
8.056412062685432
>>> U = 2*X + Y**2 + 3*Z
>>> mean(U)
8.054109701942556
>>> from scipy.stats import *
>>> from matplotlib.pyplot import *
>>> linspace(0,1,10)
array([0.        , 0.11111111, 0.22222222, 0.33333333, 0.44444444,
       0.55555556, 0.66666667, 0.77777778, 0.88888889, 1.        ])
>>> linspace(0,1,11)
array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. ])
>>> ls = linspace(-5, 5, 200 )
>>> p = norm.pdf(ls, 0,1)
>>> show()
>>> plot(ls,p)
[<matplotlib.lines.Line2D object at 0x013566E8>]
>>> show()
>>> p = norm.pdf(ls, 1,3)
>>> plot(ls,p)
[<matplotlib.lines.Line2D object at 0x2436BDD8>]
>>> show()
>>> p = norm.cdf(ls, 1,3)
>>> plot(ls,p)
[<matplotlib.lines.Line2D object at 0x011E7B50>]
>>> show()
>>> p = norm.pdf(ls, 0,1)
>>> show()
>>> plot(ls,p)
[<matplotlib.lines.Line2D object at 0x012F4508>]
>>> show()
>>> p = norm.cdf(ls, 0,1)
>>> 
>>> plot(ls,p)
[<matplotlib.lines.Line2D object at 0x0132BB20>]
>>> show()
>>> p = uniform.pdf(ls, 1,3)
>>> plot(ls,p)
[<matplotlib.lines.Line2D object at 0x10DC7628>]
>>> show()
>>> p = uniform.cdf(ls, 1,3)
>>> 
>>> plot(ls,p)
[<matplotlib.lines.Line2D object at 0x10E00430>]
>>> show()
>>> p = poisson.pdf(ls, 1)
Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    p = poisson.pdf(ls, 1)
AttributeError: 'poisson_gen' object has no attribute 'pdf'
>>> p = poisson.cdf(ls, 1)
>>> plot(ls,p)
[<matplotlib.lines.Line2D object at 0x22AEEEE0>]
>>> show()
>>> p = poisson.cdf(ls, 0.1)
>>> plot(ls,p)
[<matplotlib.lines.Line2D object at 0x229F79B8>]
>>> show()
>>> p = poisson.cdf(ls, 10)
>>> plot(ls,p)
[<matplotlib.lines.Line2D object at 0x10C624C0>]
>>> show()
>>> p = gamma.cdf(ls, 2,0,1)
>>> plot(ls,p)
[<matplotlib.lines.Line2D object at 0x10C97568>]
>>> show()
>>> p = gamma.pdf(ls, 2,0,1)
>>> plot(ls,p)
[<matplotlib.lines.Line2D object at 0x22A262B0>]
>>> show()
>>> 