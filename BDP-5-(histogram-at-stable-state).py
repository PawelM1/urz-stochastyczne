import numpy as np
import numpy.random as npr
from math import log,exp,sqrt
import matplotlib.pyplot as plt
import scipy.interpolate as intp
import pandas as pd

beta_birth, k0, N0 = 0.2, 0.025, 20.0

def wait_time(mi):
    return  -(1/mi)*log(npr.rand())

def xi1( beta_birth, k0, pop):
    return beta_birth / ( beta_birth + k0 * pop)
# xi2 = 1 - xi1

def simul_correction( trajectory, epsilon=1e-6 ):
    corrected_trajectory = [ trajectory[0] ]
    for i in range(1,len(trajectory)):
        corrected_trajectory.append(
            [ trajectory[i][0] - epsilon, trajectory[i-1][1] ]
            )
        corrected_trajectory.append( trajectory[i] )
    return corrected_trajectory

def simulation( N0, t0, t_end, beta_birth, k0, popul_Integer = True ):
    pop = N0
    trajectory = [ [t0, pop] ]
    t = t0 + wait_time(beta_birth)
    while t < t_end and pop > 0:
        if npr.rand() < xi1( beta_birth, k0, pop):          # narodziny
            if popul_Integer:
                pop += 1                # integer case (default)
            else:
                pop += beta_birth       # float case
        else:                                               # śmierć
            if popul_Integer:
                pop -= 1                # integer case (default)
            else:
                pop = (1 - k0) * pop    # float case
        trajectory.append( [ t, pop ] )
        t += wait_time(beta_birth)
    trajectory.append( [ t_end, pop ] )
    return simul_correction( trajectory )

def graphic_trajectory( trajectory, ls ):
    coordsX = [ tr[0] for tr in trajectory ]
    coordsY = [ tr[1] for tr in trajectory ]
    f = intp.interp1d( coordsX, coordsY )
    fls = [ f(t) for t in ls ]
    return fls

def analyticalSolution( t, N0, beta_birth, k0 ):
    return exp(-t*k0) * ( N0 - beta_birth / k0 ) + beta_birth / k0

def infoString( N0, beta_birth, k0, t0, t_end ):
    return( "\n{starting pop =" + str(N0) + ", freq.birthes =" + str(beta_birth)
            + ", % deathes = " + str(k0) + ", time =" + str(t_end-t0) +"}" )

def plotDrawing( numPlots, lsX, lsY, labels, title="",
                 legend="lower right", xlabel="time", ylabel="population"):
    for i in range(numPlots):
        plt.plot( lsX, lsY[i], label = labels[i] )
    plt.legend(loc=legend)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title( title ) 
    #plt.show()
    return plt.show()

def graphic_mean_trajectory( nr_trajectories, trajectories, ls ):
    ff = []
    for i in range(nr_trajectories):
        coordsX = [ tr[0] for tr in trajectories[i] ]
        coordsY = [ tr[1] for tr in trajectories[i] ]
        f = intp.interp1d( coordsX, coordsY )
        ff.append(f)
    fls = [ np.mean( [ ff[i](t) for i in range(nr_trajectories) ] ) for t in ls ]
    return fls

#############
beta_birth, k0, N0 = 0.2, 0.025, 8
t0, t_end = 0, 100000

nr_trajectories, trajectories = 6, []
for i in range(nr_trajectories):
    trajectories.append( simulation( N0, t0, t_end, beta_birth, k0 ) )

probki = []
for i in range(nr_trajectories):
    probki.append( [ tr[1] for tr in trajectories[i] ] )

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
#df = []
#df1 = pd.DataFrame(dict(a=[1, 1, 1, 1, 3]))
#df2 = pd.DataFrame(dict(b=[1, 1, 2, 1, 3]))

fig, axes = plt.subplots(3, 2)
dct, df = [], []
for i in range(nr_trajectories):
    print( 'trajectory ', i,
           ': len =', len( probki[i] ),
           ', mean = ', np.mean( probki[i] ),
           ', Var = ', np.var( probki[i] ),
           ', stDev = ', np.std( probki[i] )
           )
    dct.append( {} )
    dct[i][ 'trajectory '+str(i) ] = probki[i]
    df.append( pd.DataFrame(dct[i]) )
    df[i].hist( 'trajectory '+str(i), ax = axes[i%3][i//3], bins = 20 )

fig.tight_layout()
plt.show()

print()
#############
beta_birth, k0, N0 = 2.0, 0.025, 80
t0, t_end = 0, 100000

nr_trajectories, trajectories = 6, []
for i in range(nr_trajectories):
    trajectories.append( simulation( N0, t0, t_end, beta_birth, k0 ) )

probki = []
for i in range(nr_trajectories):
    probki.append( [ tr[1] for tr in trajectories[i] ] )

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
#df = []
#df1 = pd.DataFrame(dict(a=[1, 1, 1, 1, 3]))
#df2 = pd.DataFrame(dict(b=[1, 1, 2, 1, 3]))

fig, axes = plt.subplots(3, 2)
dct, df = [], []
for i in range(nr_trajectories):
    print( 'trajectory ', i,
           ': len =', len( probki[i] ),
           ', mean = ', np.mean( probki[i] ),
           ', Var = ', np.var( probki[i] ),
           ', stDev = ', np.std( probki[i] )
           )
    dct.append( {} )
    dct[i][ 'trajectory '+str(i) ] = probki[i]
    df.append( pd.DataFrame(dct[i]) )
    df[i].hist( 'trajectory '+str(i), ax = axes[i%3][i//3], bins = 20 )

fig.tight_layout()
plt.show()


