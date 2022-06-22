from numpy import *

class lancuchMarkowa:
    def __init__(self, macPP, stany):
        self.macPP = macPP
        self.stany = stany
        self.slownikIndeksow = {
            self.stany[indeks]: indeks for indeks in range(len(self.stany)) }
        self.slownikStanow = {
            indeks: self.stany[indeks] for indeks in range(len(self.stany))}

    def nastStan(self, potoStan):
        return random.choice( self.stany, p = self.macPP[ stany.index(potoStan) ] )

    def generacjaStanow0(self, potoStan, k = 10):
        przyszleStany = [ potoStan ]
        tmpStan = potoStan        
        for i in range(k):
            przyszleStany.append( self.nastStan(tmpStan))
            tmpStan = przyszleStany[ len(przyszleStany)-1 ]
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

    def stanPochlaniajacy( self, stan ):    # sprawdza, czy stan pochłaniający
        nrStanu = self.slownikIndeksow[stan]
        if self.macPP[nrStanu][nrStanu] == 1:
            return True
        else:
            return False
        
    def stanOsiagalny( self, iStan, jStan):     # sprawdza, czy jStan osiągalny z iStan-u
        slownikStanow = {}      # używamy słownika, żeby nie używać funkcji 'index'
        for i in range( len(self.stany)):
            slownikStanow[ self.stany[i] ] = i
        stany_osiagalne = [ iStan ]
        for stan in stany_osiagalne:
            for k in range( len( self.macPP[ slownikStanow[stan] ] ) ):
                if not self.macPP[ slownikStanow[stan] ][k] == 0:
                    if stany[k] not in stany_osiagalne:
                        stany_osiagalne.append( self.stany[k] )
                #print('k = ',k, 'stany[k] =',stany[k])
        #print( stany_osiagalne )
        if jStan in stany_osiagalne:
            return True
        else:
            return False

    def jestRedukcyjny( self ):         # sprawdza czy łańcuch jest redukcyjnym
        for stan1 in stany:
            for stan2 in stany:
                if not self.stanOsiagalny(stan1, stan2):
                    return False
        return True

    def okresStanu( self, iStan ):
        pass

    def jestOkresowosc( self ):
        pass

    def nieokresowosc( self):
        pass

    def stanPochlanajacy( self, iStan):
        pass

    def iloscWizyt( seelf, iStan):
        pass

    
    
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
        a = [ [1 for i in range( len(stany) )] ]
        for i in range( len(stany) ):
            a.append( [ self.macPP[j][i]-1 if i==j else self.macPP[j][i] for j in range(len(stany)) ] )
        b = [ 1 ]
        for i in range( len(stany) ):
            b.append(0)
        print('a=',a)
        print('b=',b)
        rozw = linalg.lstsq(a,b,rcond=None) # approx.solving of lin.eq.system
        #print('approx. solution: ', rozw )
        return rozw[0]

    def rozkladStacjonarnyPotegi(self, epsilon = 0.0001):
        mppLast = self.macPP
        mx = 2*epsilon
        mppNext = matmul( mppLast, self.macPP )
        k = 2
        while mx > epsilon and k < 50:
            mppNext = matmul( mppLast, self.macPP )
            mx = max( [ abs( mppNext[i][j] -  mppLast[i][j] )
                     for i in range(len(stany))
                     for j in range(len(stany))
                     ])
            mppLast = mppNext
            if k % 2 == 0:
                print('potęga = ',k,'  max(eps) = ',mx, mppNext[0])
            k += 1
        print(' doszliśmy do potęgi ', k-1)
        return mppNext[0]

        # warunek (*):
        # dla wszystkich i,j z przestrzeni stanów E
        # istnieje n0 takie,
        # że dla wszystkich n > n0 :
        # pp[i,j,n] > 0 ( prawd.przejścia za n kroków jest dodatnie )
        #
        # taki warunek jest równoznaczny temu,
        # że łańcuch Markowa jest nieredukowalnym i zamkniętym
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
        
stany = [ 'cloudy', 'sunny', 'rainy' ]
mpp = [ [ 0.1, 0.4, 0.5 ],
        [ 0.4, 0.5, 0.1 ],
        [ 0.3, 0.1, 0.6 ]
    ]

mpp = [ [ 0.5, 0, 0.5 ],
        [ 0.4, 0.3, 0.3 ],
        [ 0.4, 0, 0.6 ]
    ]
LM = lancuchMarkowa(mpp, stany)
print( LM.stanOsiagalny('cloudy', 'rainy') )
print( LM.stanOsiagalny('cloudy', 'sunny') )
print( LM.stanOsiagalny('sunny', 'rainy') )
print( LM.stanOsiagalny('sunny', 'sunny') )

print()
print( LM.jestRedukcyjny() )
mpp = [ [ 0.1, 0.4, 0.5 ],
        [ 0.4, 0.5, 0.1 ],
        [ 0.3, 0.1, 0.6 ]
    ]

print( LM.jestRedukcyjny() )

print()
print( LM.generacjaStanow( 'sunny', 10 ))



print('\n')
stany = [ 'działa', 'złamane' ]
mpp = [ [ 0.95, 0.05 ],
        [ 0, 1 ]
    ]
LM = lancuchMarkowa(mpp, stany)
print( LM.generacjaStanow( 'działa', 50 ))


# problem ruiny gracza
# start: gracz posiada 'k' zł
# partia: pr. wygranej 'p', a przegranej 'q'=1-'p' - z góry ustalone
# w każdej partii gracz wygrywa lub przegrywa 'z' zł
# koniec: gracz posiada zero albo >=N zł

p = 0.49
q = 1 - p
k, N, z = 50, 55, 1

stany = list( range(0,N+z,min(1,z)) )     #[0... N+z-1]
# gracz posiada j zł, i wygrywa -> j+z;    mpp(j, j+z) = p
# gracz posiada j zł, i przegrywa -> j-z;    mpp(j, j-z) = q
# mpp(0, i) = 0 przy i != 0, oraz mpp(0,0)=1
# mpp(N, i) = 0 przy i != N, oraz mpp(N,N)=1
# ...
# mpp(N+z-1, i) = 0 przy i != N+z-1, i mpp(N+z-1,N+z-1)=1

#print('przestrzeń stanów: ', stany)

# generowanie MPP dla problemu ruiny gracza
mpp = [[ 0 for _ in range(N+z)] for __ in range(N+z)]
for j in range(N+z):
    if j < N:
        mpp[j][j+z] = p
    if j >= z:
        mpp[j][j-z] = q
    else:
        mpp[j][0] = q
for i in range(N+z):
    mpp[0][i] = 0
    for j in range(N,N+z):
        mpp[j][i] = 0
        mpp[j][j] = 1
mpp[0][0] = 1
print('macierz prawdopodobieństw przejścia: ')
#for wiersz in mpp:
#   print(wiersz)
LM = lancuchMarkowa(mpp, stany)
print()
print( LM.generacjaStanow( k, 200 ))

wyniki = []
games = 1000
for runda in range(games):
    gra = LM.generacjaStanow( k, 100000 )
    if gra[-1] == 0:
        dlug = gra.index(0)
    else:
        dlug = gra.index(N)
    if runda % (games//20) == 0:
        print('zegranych do końca rund = ',runda)
    wyniki.append( [gra[-1], dlug] )

dane1 = [ x[0] for x in wyniki ]
dane2 = [ x[1] for x in wyniki ]

print('pr. przegranej i wygranej: ', dane1.count(0)/games, dane1.count(N)/games )
print('średnia długość gry: ', sum(dane2)/games ) # mean(dane2)
print('standardowe odchylenie długości gry: ', std(dane2) ) # sqrt(np.var(dane2))
