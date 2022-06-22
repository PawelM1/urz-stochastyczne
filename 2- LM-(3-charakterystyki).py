import numpy as np
import numpy.random as npr
from itertools import combinations

class lancuchMarkowa:
    """
    inicializujemy objekt 'lancuchMarkowa'

    Parametry:
        macPP:
            dwo-wymiarowa (mac)ierz (p)rawpodopodobieństw (p)rzejścia
        stany:
            jednowymiarowy wektor, przedstawiający listę stanów lancucha M.
            Musi mieć długość, równą długości strony 'macPP'.
        self.slownik_indeksow:
            wykorzystuje się dla nawigacji po stanach
            ( łatwe przejście od stanów do indeksów stanówm )
        self.slownik_stanow:
            wykorzystuje się dla nawigacji po stanach
            ( łatwe przejście od indeksów stanów do stanów )

    """
    def __init__(self, macPP, stany):
        self.macPP = macPP
        self.stany = stany
        self.slownikIndeksow = {
            self.stany[indeks]: indeks for indeks in range(len(self.stany)) }
        self.slownikStanow = {
            indeks: self.stany[indeks] for indeks in range(len(self.stany))}

    def nastStan(self, potocznyStan):        pass
    def generacjaStanow(self, potocznyStan, k = 10):        pass
    def stanOsiagalny( self, iStan, jStan):        pass
    def stanyOsiagalneZeStanu( self, stan ):        pass
    def jestNieRedukowalny( self ):        pass
    def stanNieistotny( self, stan ):        pass
    def stanyNieistotne( self ):        pass
    def zamknietoscZbioruStanow( self, zbiorStanow ):        pass
    def stanPochlaniajacy( self, stan ):        pass
    def stanPowracajacy( self, stan ):        pass
    def stanChwilowy( self, stan ):        pass
    def stanOkresowy( self, stan, maksKroki = 1000 ):        pass
    def okresStanu( self, stan ):        pass
    def jestOkresowy( self, stan ):        pass
    def rozkladStacjonarny(self):        pass
    def rozkladStacjonarnyPotegi(self, epsilon = 0.0001):        pass
    def oczekiwanyCzasPowrotu( self, stan ):        pass
    def oczekiwanaIloscWizyt( self, stan ):        pass
    def jestNieOkresowy( self ):        pass
    # ...    #def jestErgodyczny(self):       pass
    
    
    def nastStan(self, potocznyStan):
        return npr.choice( self.stany,
                           p = self.macPP[ stany.index(potocznyStan) ]
                           )

    def generacjaStanow0(self, potocznyStan, k = 10):
        przyszleStany = []
        terazniejszyStan = potocznyStan        
        for i in range(k):
            kolejnyStan = self.nastStan( terazniejszyStan )
            przyszleStany.append( kolejnyStan )
            terazniejszyStan = kolejnyStan
        return przyszleStany

    def generacjaStanow(self, potoStan, k = 10):
        przyszleStany = [ potoStan ]
        tmpStan = potoStan        
        for i in range(k):
            if not self.stanPochlaniajacy(tmpStan):
                przyszleStany.append( self.nastStan(tmpStan))
                tmpStan = przyszleStany[ len(przyszleStany)-1 ]
            else:
                break
        return przyszleStany
    
    def stanOsiagalny( self, iStan, jStan):
        # sprawdza, czy jStan osiągalny z iStan-u
        if  (type(iStan) is int) and (type(iStan) is int):
            stany_osiagalne = [ self.slownikStanow[iStan] ]
        else:
            stany_osiagalne = [ iStan ]
        #print('macPP = ',self.macPP)
        #print( 'self.slownikIndeksow =', self.slownikIndeksow )
        #print( 'self.slownikStanow =', self.slownikStanow )
        for stan in stany_osiagalne:
            for k in range(len(self.stany)):
                #print('k = ',k,', stan = ',stan)
                if self.macPP[ self.slownikIndeksow[stan] ][k] > 0:
                    if stany[k] not in stany_osiagalne:
                        stany_osiagalne.append( self.stany[k] )
                #print('k = ',k, 'stany[k] =',stany[k])
        #print( stany_osiagalne )
        if  (type(iStan) is int) and (type(iStan) is int):
            return ( self.slownikStanow[jStan] in stany_osiagalne )
        else:
            return ( jStan in stany_osiagalne )

    def stanyOsiagalneZeStanu( self, stan ):
        listaOsiagalnychStanow = []
        for stan2 in self.stany:
            if self.stanOsiagalny( stan, stan2 ):
                listaOsiagalnychStanow.append( stan2 )
        return list(set(listaOsiagalnychStanow))

    def jestNieRedukowalny( self ):
        # sprawdza czy łańcuch jest nieredukowalnym (nieprzywiedlnym), tzn.
        # czy wszystkie jego stany komunikują (osiągalne w obie strony) pomiędzy sobą
        for stan1 in self.stany:
            if set(self.stanyOsiagalneZeStanu(stan1)) != set(self.stany):
                return False
            #for stan2 in self.stany:
            #    if not self.stanOsiagalny(stan1, stan2):
            #        return False
        return True
    
    def jestNieRedukowalny2( self ):         #metoda szybsza, ale czemuś ZLE działa... czemu ?!
        # sprawdza czy łańcuch jest nieredukowalnym (nieprzywiedlnym), tzn.
        # czy wsszystkie jego stany komunikują (osiągalne w obie strony) pomiędzy sobą
        for stan1, stan2 in combinations(self.stany, 2):
            if not self.stanOsiagalny(stan1, stan2):
                return False
        return True

    def stanNieistotny( self, stan ):
        # nieistotnym jest 'iStan', jeśli istnieje taki 'jStan',
        # że 'jStan' jest osiągalny z 'iStan'u, ale 'iStan' jest NIE osiągalny z 'jStan'u
        for stan2 in self.stany:
            if self.stanOsiagalny(stan, stan2) and (not self.stanOsiagalny(stan2, stan)):
                return True
        return False
        
    def stanyNieistotne( self ):
        listaStanowNieistotnych = []
        for stan in self.stany:
            if self.stanNieistotny( stan ):
                listaStanowNieistotnych.append( stan )
        return listaStanowNieistotnych

    def zamknietoscZbioruStanow( self, zbiorStanow ):
        # zbiór stanów łańcucha Markowa nazywa się 'zamkniętym',
        # jeśli kiedy trafiamy do tego zbioru, to już nigdy z niego nie wyjdziemy
        for stan in zbiorStanow:
            for stan2 in self.stany:
                if self.stanOsiagalny(stan, stan2):
                    if stan2 not in zbiorStanow:
                        return False
        return True

    def stanPochlaniajacy( self, stan ):    # sprawdza, czy stan pochłaniający
        indeksStanu = self.slownikIndeksow[stan]
        if self.macPP[indeksStanu][indeksStanu] == 1:
            return True
        else:
            return False

    def stanPowracajacy( self, stan ):      # sprawdza, czy stan powracajacy (przemijający)
        # sprawdza, czy stan powracający
        # tzn. ilość powrotów do tego stanu jest NIEskończona (jeśli proces trwa w nieskończoność)
        kolumnaWejscDoStanu = [ self.macPP[i][ self.slownikIndeksow[stan] ]
                                for i in range(len(self.stany)) ]
        for i in range(len(self.stany)):
            if i != self.slownikIndeksow[stan]
                if kolumnaWejscDoStanu[i] != 0:
                    return True
        return False

    def stanChwilowy( self, stan ):
        # sprawdza, czy stan chwilowy (=tranzytywny)
        # tzn. ilość powrotów do tego stanu jest skończona (jeśli proces trwa w nieskończoność)
        # ( można sprawdzić, czy w odp. kolumnie 'macPP' są wzystkie zera,
        # z wyjątkiem przejścia ze 'stan' do 'stan')
        return (not stanPowracajacy( stan ) )

    # ogólnie,
    # przestrzeń stanów łańcucha Markowa możemy jednoznacznie przedstawić w postaci sumy
    # zbioru stanów chwilowych
    # oraz zbiorów (może być takich kilka) stanów nieredukowalnych zamkniętych

    def oczekiwanyCzasPowrotu( self, stan ):
        # ...
        return
    
    def oczekiwanaIloscWizyt( self, stan ):
        # ...
        return
    
    def stanOkresowy( self, stan, maksKroki = 1000 ): # stan jest okresowy: True/False
        def wszystkieMozliweSciezki(graf):
            sciezki = []
            for stanPotoczny in self.stany:
                
            # brak na razie
            return
        # konstruowanie graf = ... z self.macPP (niezerowe wartości tylko)

        return gcd( [len(sciezka) for sciezka in wszystkieMozliweSciezki(graf)] )
        
    def okresStanu( self, stan, maksIloscKrokow = 100, maksIloscProb = 100 ):
        # zwraca okres stanu, lub -1 (jeśli nie okresowy)
        poczStan = stan
        okresy, wlasciwyOkres = [], []
        
        for i in range(1, maksIloscKrokow+1):
            for j in range(maksIloscProb):
                ostatniStan = self.generacjaStanow(poczStan, i)[-1]
                if ostatniStan == poczStan:
                    okresy.append(i)
                    break
        if len(okresy) > 0:
            wlasciwyOkres = reduce(gcd, okresy)     # odnajduje NWD ze wszystkich
            return wlasciwyOkres        
        return -1           # nie udało się odnaleźć żadnego okresu

    def jestOkresowy( self ):
        # proces jest okresowy? True/ False
        # proces nawyza się okresowym, jeśli wszystkie jego stany są okresowymi z okresami > 1
        if (not self.jestNieOkresowy()):
            pass
        return 

    def jestNieOkresowy( self ):
        # łancuch Markowa jest nieokresowym
        okresy = [self.okresStanu(stan) for stan in self.stany]
        for okres in okresy:
            if okres != 1 and okres != -1:
                return False
        return True        
        
    # rozkład stacjonarny
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

    
    def rozkladStacjonarny(self):
        # każdy nieredukowalny i nieokresowy łańcuch posiada rozkład stacjonarny,
        # i wtedy każdy stan jest powracalny
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
        # każdy nieredukowalny i nieokresowy łańcuch posiada rozkład stacjonarny
        # i wtedy każdy stan jest powracalny
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


        # warunek (*):
        # dla wszystkich i,j z przestrzeni stanów E
        # istnieje n0 takie,
        # że dla wszystkich n > n0 :
        # pp[i,j,n] > 0 ( prawd.przejścia za n kroków jest dodatnie )
        # (innymi słowy, wszystkie elementy macierzy są niezerowe)
        #
        # taki warunek jest równoznaczny temu,
        # że łańcuch Markowa jest nieredukowalnym i zamkniętym
        #
        # też z tego warunku wynika, że
        # łańcuch jest nieredukowalny i nieokresowy (= ergodyczny )
        # (to jest słabsze twierdzenie, a niż powyższe)
        #
        # a jeśli oprócz warunku (*) wiadomo, że
        # istnieje rozkład stacjonarny,
        # to wtedy:
        # każdy stan jest powracalny, a rozkład stacjonarny jest jednoznaczny
        # ( układ równań posiada dokładnie jedno rozwiązanie )
        #
        # natomiast jeśli oprócz warunku (*) zbiór stanów E jest skończonym,
        # to też:
        # każdy stan jest powracalny, a rozkład stacjonarny jest jednoznaczny
        # ( układ równań posiada dokładnie jedno rozwiązanie )
        
############
        '''
stany = [ 'A', 'B', 'C' ]
mpp = [ [ 0.5, 0,  0.5 ],
        [ 0,   1,   0 ],
        [ 0.3, 0.1, 0.6 ]
    ]

stany = [ 'A', 'B', 'C' ]
mpp = [ [ 0.1, 0.4, 0.5 ],
        [ 0.0, 0.3, 0.7 ],
        [ 0.0, 0.6, 0.4 ]
    ]

stany = [ 'A', 'B', 'C', 'D' ]
mpp = [ [ 0.6, 0.0, 0.4, 0.0 ],
        [ 0.1, 0.3, 0.4, 0.2 ]
        [ 0.4, 0.0, 0.6, 0.0],
        [ 0.3, 0.2, 0.3, 0.2]
    ]

stany = [ 'A', 'B', 'C', 'D' ]
mpp = [ [ 0.2, 0.4, 0.4, 0.0 ],
        [ 0.3, 0.3, 0.4, 0.0 ]
        [ 0.4, 0.0, 0.6, 0.0],
        [ 0.3, 0.2, 0.3, 0.2]
    ]
'''
###########
stany = [ 'A', 'B', 'C' ]
mpp = [ [ 0.5, 0,  0.5 ],
        [ 0,   1,   0 ],
        [ 0.3, 0.1, 0.6 ]
    ]
LM = lancuchMarkowa(mpp,stany)
print( LM.jestNieRedukowalny() )
print( LM.zamknietoscZbioruStanow(['B']) )

'''
############ testy
print('\n')        
stany = [ 'cloudy', 'sunny', 'rainy' ]
mpp = [ [ 0.1, 0.4, 0.5 ],
        [ 0.4, 0.5, 0.1 ],
        [ 0.3, 0.1, 0.6 ]
    ]
print('stany łańcucha: ', stany)
print('macierz prawdopodobieństw przejścia:')
for wiersz in mpp:
    print(wiersz)
LM = lancuchMarkowa(mpp, stany)
print( LM.generacjaStanow( 'rainy', 30 ))
i,j = 0,2
print('stan (',LM.stany[i],') osiągalny ze stanu ',LM.stany[j],' ? ', end='\t')
print( LM.stanOsiagalny(j,i))
print('czy jest łancuch Markowa nieredukowalny: ', LM.jestNieRedukowalny() )
print('czy jest łancuch Markowa nieredukowalny(v.2): ', LM.jestNieRedukowalny2() )
print('lista stanów nieistotnych: ', LM.stanyNieistotne() )
zbior = ['cloudy', 'sunny']
print("czy jest zbiót ",zbior," zamkniętym: ", LM.zamknietoscZbioruStanow( zbior ) )
zbior = [ 'cloudy', 'sunny', 'rainy' ]
print("czy jest zbiót ",zbior," zamkniętym: ", LM.zamknietoscZbioruStanow( zbior ) )


print('\n')
stany = [ 'cloudy', 'sunny', 'rainy' ]
mpp = [ [ 0, 1, 0 ],
        [ 0, 0, 1 ],
        [ 1, 0, 0 ]
    ]
print('stany łańcucha: ', stany)
print('macierz prawdopodobieństw przejścia:')
for wiersz in mpp:
    print(wiersz)
LM = lancuchMarkowa(mpp, stany)
print( LM.generacjaStanow( 'rainy', 30 ))
i,j = 0,2
print('stan (',LM.stany[i],') osiągalny ze stanu ',LM.stany[j],' ? ', end='\t')
print( LM.stanOsiagalny(j,i))
i,j = 1,2
print('stan (',LM.stany[i],') osiągalny ze stanu ',LM.stany[j],' ? ', end='\t')
print( LM.stanOsiagalny(j,i))
print('czy jest łancuch Markowa nieredukowalny: ', LM.jestNieRedukowalny() )
print('czy jest łancuch Markowa nieredukowalny(v.2): ', LM.jestNieRedukowalny2() )
print('lista stanów nieistotnych: ', LM.stanyNieistotne() )
zbior = ['cloudy', 'sunny']
print("czy jest zbiót ",zbior," zamkniętym: ", LM.zamknietoscZbioruStanow( zbior ) )
zbior = [ 'cloudy', 'sunny', 'rainy' ]
print("czy jest zbiót ",zbior," zamkniętym: ", LM.zamknietoscZbioruStanow( zbior ) )


print('\n')
stany = [ 'działa', 'złamane' ]
mpp = [ [ 0.9, 0.1 ],
        [ 0.0, 1.0 ]
    ]
print('stany łańcucha: ', stany)
print('macierz prawdopodobieństw przejścia:')
for wiersz in mpp:
    print(wiersz)
LM = lancuchMarkowa(mpp, stany)
print( LM.generacjaStanow( 'działa', 30 ))
i,j = 0,1
print('stan (',LM.stany[i],') osiągalny ze stanu ',LM.stany[j],' ? ', end='\t')
print( LM.stanOsiagalny(j,i))
i,j = 1,0
print('stan (',LM.stany[i],') osiągalny ze stanu ',LM.stany[j],' ? ', end='\t')
print( LM.stanOsiagalny(j,i))
print('czy jest łancuch Markowa nieredukowalny: ', LM.jestNieRedukowalny() )
print('czy jest łancuch Markowa nieredukowalny(v.2): ', LM.jestNieRedukowalny2() )
print('lista stanów nieistotnych: ', LM.stanyNieistotne() )
zbior = ['działa']
print("czy jest zbiót ",zbior," zamkniętym: ", LM.zamknietoscZbioruStanow( zbior ) )
zbior = ['złamane']
print("czy jest zbiót ",zbior," zamkniętym: ", LM.zamknietoscZbioruStanow( zbior ) )
zbior = [ 'działa', 'złamane' ]
print("czy jest zbiót ",zbior," zamkniętym: ", LM.zamknietoscZbioruStanow( zbior ) )



print('\n')
stany = [ 'cloudy', 'sunny', 'rainy' ]
mpp = [ [ 1, 0, 0 ],
        [ 0, 0.5, .5 ],
        [ 0, .5, 0.5 ]
    ]
print('stany łańcucha: ', stany)
print('macierz prawdopodobieństw przejścia:')
for wiersz in mpp:
    print(wiersz)
LM = lancuchMarkowa(mpp, stany)

print('czy jest łancuch Markowa nieredukowalny: ', LM.jestNieRedukowalny() )
print('czy jest łancuch Markowa nieredukowalny(v.2): ', LM.jestNieRedukowalny2() )
print('lista stanów nieistotnych: ', LM.stanyNieistotne() )
zbior = ['sunny', 'rainy']
print("czy jest zbiót ",zbior," zamkniętym: ", LM.zamknietoscZbioruStanow( zbior ) )
zbior = ['cloudy', 'sunny']
print("czy jest zbiót ",zbior," zamkniętym: ", LM.zamknietoscZbioruStanow( zbior ) )
zbior = [ 'cloudy'
          ]
print("czy jest zbiót ",zbior," zamkniętym: ", LM.zamknietoscZbioruStanow( zbior ) )


############ koniec testów osiągalności
'''
