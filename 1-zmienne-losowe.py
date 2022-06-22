# podstawowym narzędziem jest biblioteka NumPy
from numpy import *
from numpy.random import *
# wszystkie próby losowe staramy się zawsze trzymać w numpy.array
# ponieważ typ ten pozwala na dalsze obliczenia wektorowe
# zawsze możemy inicjalizować pustą tablicę
X = empty(10,dtype = float)
# po czym wpisać w nie nasze wyniki w pętli
for k in range(10):
    X[k] = rand()**2 # jakiś nasz algorytm
# generalnie jednak najlepiej korzystać z wbudowanych metod
# które są wektorowe i dużo szybsze niż pętle
X = rand(10)**2 # równoważne powyższemu, ale dużo efektywniejsze i␣,→przejrzystsze

# wektorową wersją if jest numpy.where
U = rand(10)
X = where(U>1/2, 1, -1) # kiedy U[k] > 1/2 X[k] = 1, przeciwnie -1

#def f(x):
#    while x < 10: # zawiera while zależny od x, nie jest wektorowe
#        x *= 2
#    return x
#f(rand(10)) # błąd


@vectorize
def f(x):
    while x < 10:
        x *= 2
    return x
f(rand(10)) # już ok

#Niestety vectorize (wbrew nazwie!) nie przeprowadza obliczeń wektorowo. Zapewnia elegancką
#składnię, ale jest obliczany wolno. Metody numpy są zdecydowanie preferowane

########################## Zmienne losowe w NumPy oraz SciPy #################

# rand generuje U(0,1) w zadanej ilości
rand(10) # 10 zmiennych U(0,1)
rand(10,10) # macierz 10x10 zmiennych U(0,1)

# randn generuje N(0,1) w zadanej ilości
randn() # 1 N(0,1)
rand(1,10) # macierz 1x10 zmiennych N(0,1) (tzn. pojedynczy wiersz macierzy)

# do liczb całkowitych z zakresu mamy randint
randint(1,5,100);

# jednostajnie wybierać z wektora możemy choice
tab = array([1,2.5,10])
choice([1,2.5,10],10) # z grubsza równoważne tab[randint(0,3,10)]

##############################################3

# więcej rozkładów mamy w scipy.stats
# lista rozkładów jest tutaj: https://docs.scipy.org/doc/scipy-0.16.0/reference/,→stats.html
from scipy.stats import *
from matplotlib.pyplot import *
# przykład
xs = linspace(0,5,100)
p = gamma.pdf(xs,2,0,1) # gęstość Gamma(2,0,1) od 0 do 5
plot(xs,p)
show()


# dystrybuanta jest dostępna pod .cdf
xs = linspace(-5,5,100)
d = norm.cdf(xs,1,2) # cdf Normal(1,2) w punktacch xs
plot(xs,d)
show()

# generowanie zmiennych losowych pod .rvs
X = expon.rvs(0,1,10) # 10 zmiennyc Exp(1)
hist(X,bins=30,density = True)
xs = linspace(0,5,100)
plot(xs,expon.pdf(xs)) # exp(-xs) w tym przypadku  ??? z histogramem problem

# znajdowanie parametrów metodą .fit
X = 2*randn(1000)+1 # rozkład N(1,2)
norm.fit(X) # powinny wyjść parametry (1,2)
# im większa próba, tym wynik powinien być dokładniejszy


########################### Statystyki opisowe ################
#metody, które pomagają nam zwizualizować zachowanie zmiennych i
#procesów losowych. Następnie możemy zweryfikować, czy zachowanie to jest spodziewane,
#czy też nie.
#Statystyki podobnie jak i próby są losowe i ich wynik nie jest dokładny. Powinny
#jednak zbiegać do dokładnego wyniku w kontrolowany sposób, zwykle
#wraz ze wzrostem próby losowej


# najprostszą formą statystyk są momenty
X = randn(1000) + 1 # Normal(1,1)
print(mean(X)) # pierwszy moment, powinien być blisko 1
print(mean(X**2)) # drugi moment, powinien być blisko 2
print(var(X)) # wariancja, powinna być blisko 1
5
print(std(X)) # odchylenie średniokwadratowe. tj. pierwiastek z wariancji


# zależność możemy badać za pomocą korelacji
X = randn(1000)
Y = randn(1000)
# corrcoef zwraca macierz korelacji
print(corrcoef(X,Y)) # korelacja X z Y to elementy 1,2 i 2,1; jak widzimy bliskie 0

# co do zbieżności, możemy to zilustrować
X = randn(1000) + 1
walkingMean = cumsum(X)/(arange(1,1001)) # elementy to (x1+..+xk)/k
plot(walkingMean) # jak widać zbiega do 1
show()  # pokazuje wykrers


# znamy już histogram, który jest estymatorem gęstości
hist(randn(1000),bins=30,density=True)
show()

#W przypadku robienia histogramu należy uważać na ilość belek. Zbyt mała zniekształca kształ
#uzyskanego pdfu, ale zbyt duża sprawia, że pojawia się chaotyczne zachowanie. Optymalna ilość
#belek niestety zależy od rozkładu, więc nie ma dokładnych wytycznych, ale warto nie odchodzić
#zbyt daleko od pierwiastka długości próby.


# alternatywą do histogramu jest jądrowy estymator pdf
# działa on dobrze dla zmiennych o gładkich gęstościach
# i krótkich ogonach
# dla dobrego działania może wymagać długich prób losowych
# w Pythonie mamy scipy.stats.gaussian_kde
den = gaussian_kde(randn(1000)) # rozkład Normalny jest gładki
xs = linspace(-3,3,100)
plot(xs,den(xs)) # estymowane
show()
plot(xs,norm.pdf(xs,0,1)) # dokładne
show()


# jak widzimy dla rozkładu U(0,1) ze skokami
# estymator robi błędy w otoczeniu skoków
# które zanikają wolno wraz ze wzrostem długości próby
den = gaussian_kde(rand(5000))
xs = linspace(-0.2,1.2,100)
plot(xs,den(xs)) # estymowane
plot(xs,uniform.pdf(xs,0,1)) # dokładne

# z kolei cdf jest bardzo łatwy do estymowania
# wymaga relatywnie krótkich prób losowych
# można użyć prostej funkcji ecdf
from statsmodels.distributions.empirical_distribution import ECDF
X = cauchy.rvs(0,1,500)
e = ECDF(X)
xs = linspace(-4,4,100)
plot(xs,e(xs)) # estymowane
plot(xs,cauchy.cdf(xs,0,1)) # teoretyczne



####################  Testy statystyczne ####################

#Testami odpowiadamy na pytanie, czy badana próba zdradza odchylenia od zadanej własności,czy
#też klasy. Wynik testu również jest losowy, więc gdy sami symulujemy warto go powtórzyć
#kilkukrotnie, jak też porównywać wyniki kilku testów
#Testy zwracają tzw. p-wartość, czyli oszacowane prawdopodobieństwo, że badany odchył cechy
#może być dziełem przypadku. Duża p-wartość oznacza więc “w normie” a mała potwierdza występowanie osobliwości. Za próg istotności odchyleń zwykle przyjmuje się 0.05, ale w przypadku
#symulacji warto myśleć nawet o mniejszych wartościach jak 0.005.


 # najważniejszym testem, jakiego będziemy używać jest test Kołmogorova-Smirova
# sprawdza on, czy próba ma dystrybuantę jak zadana
# w Pythonie scipy.stats.kstest
X = randn(1000)
kstest(X,'norm') # p-val = 0.15 to dużo, nie ma odchyleń od rozkładu Normal(0,1)

X = expon.rvs(0,1,1000)
kstest(X,'norm') # p-val jest bardzo małe, wykryto odchylenia od rozkładu␣,→Normal(0,1)


X = expon.rvs(0,1,1000)
kstest(X,'expon') # p-val = 0.6 to dużo, nie ma odchyleń od Exp(1)

X = randn(1000) + 1
kstest(X,'norm') # p-val jest bardzo małe, wykryto odchylenia od rozkładu␣,→Normal(0,1)

: # jeżeli chcemy testować ogólny rozkład, musimy podać testowany cdf jako␣,→funkcję x
X = 2*randn(1000) + 1
kstest(X, cdf = lambda x: norm.cdf(x,1,2)) # cdf rozkładu Normal(1,2)


#Za pomocą testu K-S możemy więc weryfikować, czy próba jest z rozkładu dokładnie takiego, jak
#zadany. Nie możemy za jego pomocą sprawdzić, czy próba jest z zadanej klasy rozkładów, np. czy
#jest z dowolnego rozkładu normalnego, a nie tylko jakiegoś konkretnego, np. Normal(0,1). Czasami
#można próbę przekształcić, aby uniknąć tego problemu. W ogólności trzeba jednak używać innych
#testów.
#Test Jarque-Bery sprawdza, czy momenty próby zgadzają się z momentami rozkładu normalnego.


# w Pythonie scipy.stats.jarque_bera
X = 2*randn(1000) + 2
jarque_bera(X) # nie ma odchyleń

X = laplace.rvs(0,1,1000) # rozkład Laplace(0,1)
jarque_bera(X) # są odchylenia

X = randn(1000) + rand(1000)
jarque_bera(X) # nie ma odchyleń, a powinny
# większość testów da się oszukać

X = randn(1000) + 5*rand(1000)
jarque_bera(X) # zwiększone zaburzenie już wychwytuje





