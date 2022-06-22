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

    # rozkład stacjonarny (analityczny sposób odnaleźenia):
    # p0 * 0.1 + p1 * 0.4 + p2 * 0.3 = p0 (pr. wystąpienia 'cloudy')
    # p0 * 0.4 + p1 * 0.5 + p2 * 0.1 = p1 (pr. wystąpienia 'sunny')
    # p0 * 0.5 + p1 * 0.1 + p2 * 0.6 = p2 (pr. wystąpienia 'rainy')
    # p0 + p1 + p2 = 1

    # p0 * mpp[0][0] + p1 * mpp[1][0] + p2 * mpp[2][0] = p0 (pr. wystąpienia 'cloudy')
    # p0 * 0.4 + p1 * 0.5 + p2 * 0.1 = p1 (pr. wystąpienia 'sunny')
    # p0 * 0.5 + p1 * 0.1 + p2 * 0.6 = p2 (pr. wystąpienia 'rainy')
    # p0 + p1 + p2 = 1

    # p0 + p1 + p2 = 1
    # p0 * (mpp[0][0]-1) + p1 * mpp[1][0] + p2 * mpp[2][0] = 0 (pr. wystąpienia 'cloudy')
    # p0 * mpp[0][1] + p1 * (mpp[1][1]-1) + p2 * mpp[2][1] = 0 (pr. wystąpienia 'sunny')
    # p0 * mpp[0][2] + p1 * mpp[1][2] + p2 * (mpp[2][2]-1) = 0 (pr. wystąpienia 'rainy')

    def rozkladStacjonarnyAproks(self):
        a = [ [1 for i in range( len(stany) )] ]
        for i in range( len(stany) ):
            a.append( [ mpp[j][i]-1 if i==j else mpp[j][i] for j in range(len(stany)) ] )
        b = [ 1 ]
        for i in range( len(stany) ):
            b.append(0)
        print('a=',a)
        print('b=',b)
        rozw = np.linalg.lstsq(a,b,rcond=None) # approx.solving of lin.eq.system
        #print('approx. solution: ', rozw )
        return rozw[0]

    def rozkladStacjonarnyPotegi(self, epsilon = 0.0001):
        mppLast = mpp
        mx = 2*epsilon
        mppNext = np.matmul( mppLast, mpp )
        k = 2
        while mx > epsilon and k < 50:
            mppNext = np.matmul( mppLast, mpp )
            mx = max( [ abs( mppNext[i][j] -  mppLast[i][j] )
                     for i in range(len(stany))
                     for j in range(len(stany))
                     ])
            mppLast = mppNext
            if k % 2 == 0:
                print('potęga = ',k,',  max(eps) = ',mx, ', ostatnia mpp:', mppNext[0])
            k += 1
        print(' doszliśmy do potęgi ', k-1)
        return mppNext[0]
        
stany = [ 'cloudy', 'sunny', 'rainy' ]
mpp = [ [ 0.1, 0.4, 0.5 ],
        [ 0.4, 0.5, 0.1 ],
        [ 0.3, 0.1, 0.6 ]
    ]


LM = lancuchMarkowa(mpp, stany)
print( LM.generacjaStanow( 'rainy', 30 ))

print('\n')
print('rozkład stacjonarny \n'
      +'(szacujemy średnią częstotliwość występowania na długim okresie):\n')
pogoda = LM.generacjaStanow( 'cloudy', 10000 )
print( '(cloudy)   cloudy =', pogoda.count('cloudy')/10000,' sunny =', pogoda.count('sunny')/10000,' rainy =', pogoda.count('rainy')/10000 )

pogoda = LM.generacjaStanow( 'rainy', 10000 )
print( '(rainy)    cloudy =', pogoda.count('cloudy')/10000,' sunny =', pogoda.count('sunny')/10000,' rainy =', pogoda.count('rainy')/10000 )

pogoda = LM.generacjaStanow( 'sunny', 10000 )
print( '(sunny)    cloudy =', pogoda.count('cloudy')/10000,' sunny =', pogoda.count('sunny')/10000,' rainy =', pogoda.count('rainy')/10000 )

print('\n')
print('rozkład stacjonarny (przybliżone rozwiązanie układu równań liniowych):')
rS = LM.rozkladStacjonarnyAproks()
print( [ (stany[i],rS[i]) for i in range(len(stany)) ] )

print('\n')
rS2 = LM.rozkladStacjonarnyPotegi()
print('rozkład stacjonarny (za pomocą potęgowania macierzy Prawd. Przejść): \n',
      [ (stany[i],rS2[i]) for i in range(len(stany)) ])


print('\n\n\n KONTRPRZYKŁAD okresowego procesu, który \n'
      +'(ze względu na stosowane metody odnaleźenia stanu stacjonarneo)\n'
      + 'zachowuje się podobnie: jakby posiadał stan stacjonarny. \n'
      + 'W takim przypadku pewność stosownie istnienia st.st. \n'
      + 'daję tylko analityczne (nie aproksymacja!) rozwiązanie układu równań. \n\n')
stany = [ 'cloudy', 'sunny', 'rainy' ]
mpp = [ [ 0, 1, 0 ],
        [ 0, 0, 1 ],
        [ 1, 0, 0 ]
    ]
LM = lancuchMarkowa(mpp, stany)
print( LM.generacjaStanow( 'rainy', 30 ))

print('\n')
print('rozkład stacjonarny \n'
      +'(szacujemy średnią częstotliwość występowania na długim okresie):\n')

pogoda = LM.generacjaStanow( 'cloudy', 10000 )
print( '(cloudy)   cloudy =', pogoda.count('cloudy')/10000,' sunny =', pogoda.count('sunny')/10000,' rainy =', pogoda.count('rainy')/10000 )

pogoda = LM.generacjaStanow( 'rainy', 10000 )
print( '(rainy)    cloudy =', pogoda.count('cloudy')/10000,' sunny =', pogoda.count('sunny')/10000,' rainy =', pogoda.count('rainy')/10000 )

pogoda = LM.generacjaStanow( 'sunny', 10000 )
print( '(sunny)    cloudy =', pogoda.count('cloudy')/10000,' sunny =', pogoda.count('sunny')/10000,' rainy =', pogoda.count('rainy')/10000 )

print('\n')
print('rozkład stacjonarny (przybliżone rozwiązanie układu równań liniowych):')
rS = LM.rozkladStacjonarnyAproks()
print( [ (stany[i],rS[i]) for i in range(len(stany)) ] )

print('\n')
rS2 = LM.rozkladStacjonarnyPotegi()
print('rozkład stacjonarny (za pomocą potęgowania macierzy Prawd. Przejść): \n',
      [ (stany[i],rS2[i]) for i in range(len(stany)) ])

print('\n')
print('Tutaj widzimy, że proces jest okresowy, tzn. nigdy nie osiąga \n'
      + 'stanu stacjonranego, mimo tego, że niektóre metody tego nie pokazują')


