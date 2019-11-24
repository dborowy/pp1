########### 5
#def printName():
#    print('Dominik Borowy')
#printName()

########### 6
#def uek():
#    print('Uniwersytet Ekonomiczny w Krakowie')
#    print('ul. Rakowicka 27')
#    print('31-510 Kraków')
#uek()

########### 7
#def telKey():
#    for i in range(1,8,3):
#        for x in range(3):
#            print(x+i,end=' ')
#        print()
#telKey()

########### 8
#x=3
#def f():
#    x=1
#f()
#print(x)

########### 9
#def f():
#    s = "I love Disco Polo!"
#    print(s)
#s = "I love Rock & Roll!"
#f()
#print(s)

########### 10
#def f():
#    y = x + 2
#    return x + y
#x = 3
#y = x + 4
#z = f() + x + y
#print(x, y, z)

########### 11
#def f():
#    x = y
#    x[1] = y[0] + x[1]
#x = [1,2,3]
#y = [4,5]
#f()
#print(x,y)

########### 13
#def suma(tablica):
#    print('Tablica: ',end='')
#    for i in range(len(tablica)):
#        print(tablica[i],end=' ')
#    print()
#    print(f'Suma wartości: {sum(tablica)}')
#suma([4,3,7,1,3])

########### 14
#def wystepuje(liczba,tablica):
#    print(f'Liczba: {liczba}')
#    print('Tablica: ',end='')
#    for i in tablica:
#        print(i,end=' ')
#    print()
#    if liczba in tablica:
#        x = 'występuje'
#    else:
#        x = 'nie występuje'
#    print(f'Rezultat: Podana liczba {x} w tablicy')
#wystepuje(23,[15,38,7,23,14])

########### 16
#def czytajLiczbe():
#    x = input('Podaj liczbę: ') 
#    return x
#print(czytajLiczbe())

########### 17
#def rzucKostka():
#    from random import randrange
#    return randrange(1,7)
#def elo():
#    x = rzucKostka()
#    y = rzucKostka()
#    z = rzucKostka()
#    print(f'Wyrzucone oczka: {x} {y} {z}\nSuma oczek: {x+y+z}')
#elo()

########### 18
#def silnia(n):
#    #0!=1 oraz 1!=1
#    if n==0 or n==1:return 1
#    #n! = n * (n-1)!
#    if n > 1:
#        return n * silnia(n-1)
#print(f'5! = {silnia(5)}')

########### 19
#def suma(N):
#    if N==1:
#        return 1
#    if N>0:
#        return N + suma(N-1)
#print(suma(500))

########### 20
#def potega(x,n):
#    if n>1:
#        return x * potega(x,n-1)
#    else:
#        return x
#print(potega(2,10))

########### 22
#even = lambda x: x%2==0
#print(even(5))

########### 23
#bigger = lambda x,y: x>y
#print(bigger(3,2))

########### 24
#def miesiac(x):
#    listaMiesiecy = ['sty','lut','marz','kwie','maj','czerw',]
#    return listaMiesiecy[x-1]
#print(miesiac(2))

########### 25
#def imieIn(x):
#    imiona = ['Janek', 'Ania', 'Wojtek', 'Zosia']
#    imionaStr = ' '.join(imiona)
#    if x in imiona:
#        wynik = ''
#    else:
#        wynik = 'nie '
#    print(f'Imiona: {imionaStr}\nImie: {x}\nRezultat: imię {wynik}zawarte jest w wykazie imion')
#imieIn('Janek')

########### 26
#def podatek(dochod):
#    dochod = int(dochod)
#    if dochod<=5000:
#        tax = int(dochod*0.17)
#    else:
#        tax = int(5000*0.17 + (dochod-5000)*0.32)
#    print(f'Podany dochod: {dochod}\nPodatek nalezny: {tax} zł')
#podatek(6000)

########### 27
#def ileSam():
#    import re
#    text = 'Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi.'
#    listaSam = re.findall('a|e|i|o|u|y|ą|ę|ó',text)
#    return len(listaSam)
#print(ileSam())

########### 28
#def langGraph():
#    lang = ['Java','Python','JavaScript','C++','C#','Ruby','Perl','PHP','C','Android']
#    demand = [61,47,37,32,26,18,14,14,9,7]
#    langLineup = []
#    longestLang = len(max(lang,key=len))
#    for i in lang:
#        langLineup.append((' '*(longestLang-len(i))+i))
#        
#    for i in range(len(lang)-1):
#        hasht = '#'*demand[i]
#        print(f'{langLineup[i]}: {hasht}')
#langGraph()

########### 29
#tab = [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]
#def medAndDom(tablica):
#    tablica.sort
#    if len(tablica)%2==0

########### 32
def transp(x):
    xTransp = []
    bttm = []
    for i in range(len(x)-1):
        xTransp.append(x[i][:len(x[0])-1])
        bttm.append(x[i][len(x[i])-1])
    xTransp.append(bttm)
    for i in range(len(x)):
        xTransp[i].append(x[len(x)-1][i])
    
    for i in xTransp:
        for j in i:
            print(j,end=' ')
        print()
    #print(xTransp)
mac = [[1,2,0,2],[0,0,3,4],[5,1,1,5],[1,4,3,2]]
transp(mac)