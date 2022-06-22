import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

X = npr.poisson(2,100)
X2 = [y for y in X]
Xcount = [(i,X2.count(i)) for i in range( len(list(set(X2))) )]
xkpk = [ (i, float(Xcount[i][1])/len(X)) for i in range( len(Xcount) )]
print(xkpk)


############
X = npr.uniform(-1,1,10000)
Y = X*X
ls = np.linspace(-2,2,400)

def dystr(ls, Y):
    F = np.zeros( len(ls), dtype=float)
    for xi in range(len(ls)):    #x=ls[xi]
        F[xi] = 0
        for j in range( len(Y) ):
            if Y[j] < ls[xi]:
                F[xi] += 1/len(Y)
    return F

F = dystr(ls,Y)
plt.plot(ls,F)
plt.show()

#F' = lim (F(t+dt)-F(t)) / (dt)

print('E(Y) =mY = ', sum(y for y in Y)/(len(Y)-1) )

rPearsona = ( np.mean( X*Y )-np.mean(X)*np.mean(Y) ) / np.std(X) /np.std(Y)

###############
X = npr.uniform(0,10,100000)

ls = np.linspace(-2,2,400)



# K(t,s)

# proces stacj. sprawdzenie
