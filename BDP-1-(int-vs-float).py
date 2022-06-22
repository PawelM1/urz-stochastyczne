import numpy as np
import numpy.random as npr
from math import log
import matplotlib.pyplot as plt
import scipy.interpolate as intp

beta_birth, k0, N0 = 0.2, 0.025, 20.0

def wait_time(beta):
    return  -(1/beta)*log(npr.rand())

# beta_birth - częstość narodzin, k0*populacja - częstość śmierci
# dla tego przyjmujemy mi_birth = beta_birth, mi_death(pop) = k0*pop
#mi_birth = beta_birth
#def mi_death( k0, pop ):
#    return k0*pop

# ma być: mi_birth/mi_death == xi1/xi2
# xi2 = 1 - xi1, skąd mi_b/mi_d == xi1/(1-xi1)
# skąd mi_b/mi_d - xi1 * mi_b/mi_d = xi1
# skąd xi1 = mi_b/mi_d / (1+ mi_b/mi_d) = mi_b / ( mi_b + mi_d )

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

def simulationInteger( N0, t0, t_end, beta_birth, k0 ):
    pop = N0
    trajectory = [ [t0, pop] ]
    t = t0 + wait_time(beta_birth)
    while t < t_end and pop > 0:
        if npr.rand() < xi1( beta_birth, k0, pop):      # narodziny
            pop += 1
        else:                                           # śmierć
            pop -= 1
        trajectory.append( [ t, pop ] )
        t += wait_time(beta_birth)
    trajectory.append( [ t_end, pop ] )
    return simul_correction( trajectory )

def simulationFloat( N0, t0, t_end, beta_birth, k0 ):
    pop = N0
    trajectory = [ [t0, pop] ]
    t = t0 + wait_time(beta_birth)
    while t < t_end and pop > 0:
        if npr.rand() < xi1( beta_birth, k0, pop):      # narodziny
            pop += beta_birth
        else:                                           # śmierci
            pop = (1 - k0) * pop
        trajectory.append( [ t, pop ] )
        t += wait_time(beta_birth)
    trajectory.append( [ t_end, pop ] )
    return simul_correction( trajectory )

def simulationBothSimultaneously( N0, t0, t_end, beta_birth, k0 ):
    pop1, pop2 = N0, N0
    trajectory1, trajectory2 = [ [t0, N0] ], [ [t0, N0] ]
    t = t0 + wait_time(beta_birth)
    while t < t_end:
        r = npr.rand()      # żeby losowanie było jednakowe dla obu rodzajów procesu
        if r < xi1( beta_birth, k0, pop1):  # narodziny (float)
            pop1 += beta_birth
        else:                               # śmierci (float)
            pop1 = (1 - k0) * pop1
        if pop2 > 0:
            if r < xi1( beta_birth, k0, pop2):  # narodziny (integer)
                pop2 += 1
            else:                               # śmierć (integer)
                pop2 -= 1
        trajectory1.append( [ t, pop1 ] )
        trajectory2.append( [ t, pop2 ] )
        t += wait_time(beta_birth)        
    trajectory1.append( [ t_end, pop1 ] )
    trajectory2.append( [ t_end, pop2 ] )
    return simul_correction( trajectory1 ), simul_correction( trajectory2 ) # float, integer

def graphic_trajectory( trajectory, ls ):
    coordsX = [ tr[0] for tr in trajectory ]
    coordsY = [ tr[1] for tr in trajectory ]
    # my POTRZEBUJEMY interpolacji dla konstruowania wykresów,
    # bo funkcje z matplotlib.py wymagają jednakowych odstępów w listach, a my mamy - losowe
    f = intp.interp1d( coordsX, coordsY )
    fls = [ f(t) for t in ls ]
    return fls

def infoString( N0, beta_birth, k0, t0, t_end ):
    return( "\n{starting pop =" + str(N0) + ", freq.birthes =" + str(beta_birth)
            + ", % deathes = " + str(k0) + ", time =" + str(t_end-t0) +"}" )

def plotDrawing( numPlots, lsX, lsY, labels, title="",
                 legend="lower left", xlabel="time", ylabel="population"):
    for i in range(numPlots):
        plt.plot( lsX, lsY[i], label = labels[i] )
    plt.legend(loc=legend)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title( title ) 
    #plt.show()
    return plt.show()


############## PRZYKŁADY dla porównania populacji o całkowitych wartościach, a o rzeczywistych
beta_birth, k0, N0 = 0.4, 0.025, 6
t0, t_end = 0, 1000
ls = np.linspace( t0, t_end, 10001)

trajectory1, trajectory2 = simulationBothSimultaneously(
    N0, t0, t_end, beta_birth, k0 )
'''
plt.plot( ls, graphic_trajectory( trajectory1, ls ), label = "float population")
plt.plot( ls, graphic_trajectory( trajectory2, ls ), label = "integer population")
plt.legend(loc="upper right")
plt.xlabel('time')
plt.ylabel('population')
plt.title('difference between (float vs integer) for SAME values:\n'
          + 'as we see, integer case is "more random"'
          + infoString( N0, beta_birth, k0, t0, t_end ) )
plt.show()
'''
fls = [ graphic_trajectory( trajectory1, ls), graphic_trajectory( trajectory2, ls) ]
plotDrawing( numPlots = 2, lsX = ls, lsY = fls,
             labels = [ "float population", "integer population" ],
             title='difference between (float vs integer) for SAME values:\n'
             + 'as we see, integer case is "more random" here'
             + infoString( N0, beta_birth, k0, t0, t_end ),
             legend = "upper right"
             )

##############
beta_birth, k0, N0 = 4, 0.025, 60
t0, t_end = 0, 1000
ls = np.linspace( t0, t_end, 10001)

trajectory1, trajectory2 = simulationBothSimultaneously(
    N0, t0, t_end, beta_birth, k0 )

fls = [ graphic_trajectory( trajectory1, ls), graphic_trajectory( trajectory2, ls) ]
plotDrawing( numPlots = 2, lsX = ls, lsY = fls,
             labels = [ "float population", "integer population" ],
             title='difference between (float vs integer) for SAME values:\n'
             + 'as we see, float case is "more random" here'
             + infoString( N0, beta_birth, k0, t0, t_end ),
             legend = "upper right"
             )

##############
beta_birth, k0, N0 = 0.2, 0.2, 4
t0, t_end = 0, 1000
ls = np.linspace( t0, t_end, 10001)

trajectory1, trajectory2 = simulationBothSimultaneously(
    N0, t0, t_end, beta_birth, k0 )

fls = [ graphic_trajectory( trajectory1, ls), graphic_trajectory( trajectory2, ls) ]
plotDrawing( numPlots = 2, lsX = ls, lsY = fls,
             labels = [ "float population", "integer population" ],
             title='difference between (float vs integer) for SAME values:\n'
             + 'as we see, with k0=0.2 population dies out in integer case, but not in float'
             + infoString( N0, beta_birth, k0, t0, t_end ),
             legend = "upper right"
             )
