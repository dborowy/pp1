#zadanie z lekcji
#x=7
#y=34
#x=x*y
#y=x/y
#x=x/y
#print(x,y)

######################9
#from random import *
#a
#print(random(), random(), random())
#b
#print(randrange(100), randrange(100), randrange(100))
#c
#print(randrange(5,100), randrange(5,100), randrange(5,100))
#d
#kolory = ['karo', 'kier', 'pik', 'trefl']
#print(choice(kolory))

######################11
#liczba1 = 5
#liczba2 = 1
#liczba3 = 8
#liczba4 = 6
#liczba5 = 3
#a
#liczby = [liczba1,liczba2,liczba3,liczba4,liczba5]
#print(sum(liczby))
#b
#kwliczby = []
#for x in liczby :
    #kwliczby.append(x**2)
#print(sum(kwliczby))
#c
#print(liczba3*liczba5)
#d
#print(liczba1%liczba5)
#h
#print(liczba3<<2)

######################12
#uczelnia = 'Uniwersytet Ekonomiczny w Krakowie'
#e
#print(uczelnia[3:9])
#f
#print(uczelnia[0:11],uczelnia[24:34])

######################14
#liczby = [2,7,3,5]
#a
#print(liczby[1])
#b
#print(sum(liczby))
#c
#print(len(liczby))
#d
#print(liczby[len(liczby)-2])
#e
#print(sum(liczby)/len(liczby))

######################15
#zdanie = 'Wartość liczby to {}, a {} to jej druga potęga.'
#liczba = 5
#print(zdanie.format(liczba,liczba**2))

######################16
#zdanie = 'Mam na imię {} i mam {} lat, a mój wzrost to {} cm'
#imię = 'Dominik'
#wiek = 20
#wzrost  = 193
#print(zdanie.format(imię,wiek,wzrost))

######################17
#kwota = 15.84
#VAT = 0.23
#wartośćVAT = round(kwota*VAT,2)
#print('Kwota: {}'.format(kwota)+'\n'+'VAT 23%: {}'.format(wartośćVAT))

######################18
#imię = input('Wprowadź swoję imię: ')
#nazwisko = input('Wprowadź swoję nazwisko: ')
#print(imię,nazwisko)

######################19
#x = int(input('Wprowadź pierwszą liczbę całkowitą: '))
#y = int(input('Wprowadź drugą liczbę całkowitą: '))
#print('Suma tych dwóch liczb to:',x+y)

######################20
#import math
# Obliczanie pola powierzchni i obwodu koła o zadanym promieniu

# ustal promień koła i PI
#prmKoła = 5
#PI = math.pi
# oblicz pole i obwód
#poleKoła = round(PI*prmKoła**2,2)
#obwódKoła = round(2*PI*prmKoła,2)
# wyświetl rezultaty
#print('Pole koła o promieniu {} wynosi {}'.format(prmKoła,poleKoła))
#print('Obwód koła o promieniu {} wynosi {}'.format(prmKoła,obwódKoła))

######################21
#tempC = int(input('Temperatura w stopniach Celcjusza: '))
#tempF = (tempC*1.8)+32
#tempK = tempC+273.15
#print('Ta temperatura w skali Fahreneheita to: {}, a w skali Kelvina to: {}'.format(tempF,tempK))

######################22
#import math
#print('Podaj długości boków trójkąta')
#a = int(input('Długość boku a: '))
#b = int(input('Długość boku b: '))
#c = int(input('Długość boku c: '))
#p = (a+b+c)/2
#poleTr = math.sqrt(p*(p-a)*(p-b)*(p-c))
#print('Pole trójkąta dla tych boków wynosi: {}'.format(poleTr))