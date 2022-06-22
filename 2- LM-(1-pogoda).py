import numpy as np
import numpy.random as npr

class lancuchMarkowa:
    """
    inicializujemy objekt 'lancuchMarkowa'

    Parametry:
        macPP:
            dwo-wymiarowa (mac)ierz (p)rawpodopodobieństw (p)rzejścia
        stany:
            jednowymiarowy wektor, przedstawiający listę stanów lancucha M.
            Musi mieć długość, równą długości strony 'macPP'.
    """
    def __init__(self, macPP, stany):
        self.macPP = macPP
        self.stany = stany

    def nastStan(self, potocznyStan):
        return npr.choice( self.stany,
                           p = self.macPP[ stany.index(potocznyStan) ]
                           )

    def generacjaStanow(self, potocznyStan, k = 10):
        przyszleStany = []
        terazniejszyStan = potocznyStan        
        for i in range(k):
            kolejnyStan = self.nastStan( terazniejszyStan )
            przyszleStany.append( kolejnyStan )
            terazniejszyStan = kolejnyStan
        return przyszleStany
'''        
stany = [ 'cloudy', 'sunny', 'rainy' ]
mpp = [ [ 0.1, 0.4, 0.5 ],
        [ 0.4, 0.5, 0.1 ],
        [ 0.3, 0.1, 0.6 ]
    ]


LM = lancuchMarkowa(mpp, stany)
print( LM.generacjaStanow( 'rainy', 30 ))

pogoda = LM.generacjaStanow( 'cloudy', 100 )
print( '\nzaczynamy z (cloudy), częstotliwość występowania stanów w 100 krokach:')
print( 'cloudy =', pogoda.count('cloudy'),' sunny =', pogoda.count('sunny'),' rainy =', pogoda.count('rainy') )
'''
#print('\nUrządzenie działa, dopóki nie jest złamane:')
#stany = [ 'działa', 'złamane' ]
stany = [ 0, 1 ]
mpp = [ [ 0.99, 0.01 ],
        [ 0.05, 0.95 ]
    ]
LM = lancuchMarkowa(mpp, stany)
#print( LM.generacjaStanow( 0, 100 ))

Xt = np.empty((4000,100),int)
for i in range(4000):
    if npr.rand() < 0.5:
        x0 =0
    else:
        x0 = 1
    Xt[i] = np.array( LM.generacjaStanow( x0, 100 ) )

print( Xt[100:104] )

