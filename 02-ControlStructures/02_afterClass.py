############ 25
#for i in range(3):
#    print(7*'*')
    
############ 26
#for i in range(1,10):
#    print(i*f'{i}')

############ 27
#i=1
#while i<5:
#    print(i*'* ')
#    i+=1
#while i>0:
#    print(i*'* ')
#    i-=1

############ 28
#a = 4
#b = 15
#print(b*'*'+'\n'+(a-2)*('*'+(b-2)*' '+'*'+'\n')+b*'*')

############ 29
#lista = [15, 8, 31, 47, 2, 19]
#print(lista[::-1])

############ 30
#i = 3
#pinPop = '0805'
#while i>=0:
#    if i == 0:
#        print('Karta płatnicza zostaje zablokowana')
#        break
#    pinWp = input('Podaj kod PIN: ')
#    if pinWp == pinPop:
#        print('PIN poprawny')
#        break
#    else:
#        print('PIN niepoprawny')
#        i-=1

############ 31
#uczelnia = 'UEK w Krakowie'
#uczelniaR = ''
#for i in uczelnia:
#    uczelniaR+=i+' '
#print(uczelniaR)

############ 32
#x = input('Podaj ciąg znaków: ')
#print(x[::-1])

############ 33
#ciąg = input('Podaj ciąg liczb: ')
#liczebniki = ['zero','jeden','dwa','trzy','cztery','pięć','sześć','siedem','osiem','dziewięć']
#ciągliczeb = ''
#for i in ciąg:
#    ciągliczeb += liczebniki[int(i)]+' '
#print(ciąg+' - '+ciągliczeb)

############ 34
#pesel = input('Podaj pesel:')
#wiek = 2019 - (1900 + int(pesel[0:2]))
#if int(pesel[9])%2==0:
#    płeć = 'Kobieta'
#else:
#    płeć = 'Mężczyzna'
#print(f'Płeć: {płeć}'+'\n'+f'Wiek: {wiek}')

############ 35
#from math import sqrt
#a = int(input('Podaj a: '))
#b = int(input('Podaj b: '))
#c = int(input('Podaj c: '))
#deltaSq = sqrt(b**2 +(-4)*a*c)
#x1 = (-b-deltaSq)/(2*a)
#x2 = (-b+deltaSq)/(2*a)
#if x1 == x2:
#    print(f'Pierwiastek równania to: {x1}')
#else:
#    print(f'Pierwiastki równiania to: {x1}, {x2}')
    
############ 36
#def infinity():
#    i = 0
#    while 1:
#        yield i
#        i += 1
#for i in infinity():
#    if i%7==0 and i%2==1 and i%3==1 and i%4==1 and i%5==1 and i%6==1:
#        print(i)
#        break

############ 37
#x1 = int(input('Podaj pierwszą liczbę: '))
#x2 = int(input('Podaj drugą liczbę: '))
#x3 = int(input('Podaj trzecią liczbę: '))
#X = [x1,x2,x3]
#Z = sorted(X)
#print(Z[1])

############ 38
#for i in range(6,-1,-3):
#    for j in range(1,4):
#        print(f' {i+j}',end='')
#    print()

#i=6
#while i>=0:
#    for j in range(1,4):
#        print(f' {i+j}',end='')
#    i-=3
#    print()

############ 39
#ciąg = [0,1]
#i=1
#while i<49:
#    ciąg.append(ciąg[i-1]+ciąg[i])
#    i+=1
#ciągStr = ''
#for x in ciąg:
#    ciągStr += str(x)+' '
#print (ciągStr)

############ 40
#from random import randrange
#i = 1
#rzuty = []
#while i<101:
#    rzuty.append(randrange(1,7))
#    i+=1
#print(f'Szóstka: {rzuty.count(6)}'+'\n'+f'Piątka: {rzuty.count(5)}'+'\n'+f'Czwórka: {rzuty.count(4)}'+'\n'+f'Trójka: {rzuty.count(3)}'+'\n'+f'Dwójka: {rzuty.count(2)}'+'\n'+f'Jedynka: {rzuty.count(1)}')

############ 41
#x = 1
#licznik = 0
#suma = 0
#while x!=0:
#    x = int(input('Podaj liczbę: '))
#    licznik += 1
#    suma +=x
#    if x == 0:
#        licznik-=1
#print(f'REZULTAT: Liczb={licznik}, Suma={suma}, Średnia={suma/licznik}')

############ 42
#x = int(input('Podaj liczbę: '))
#y = int(input('Podaj liczbę: '))
#if y == 0:
#    print('Dzielenie przez 0 !')
#else:
#    print(f'Rezultat dzielenia x/y = {x/y}')

############ 43
#x1 = int(input('Podaj pierwszą liczbę: '))
#x2 = int(input('Podaj drugą liczbę: '))
#x3 = int(input('Podaj trzecią liczbę: '))
#X = [x1,x2,x3]
#Z = sorted(X)
#print(f'Liczby w kolejności rosnącej: {Z[0]}, {Z[1]}, {Z[2]}')

############ 44
#limit = int(input('Podaj limit prędkości (km/h): '))
#prędkość = int(input('Podaj prędkośc pojazdu (km/h): '))
#if prędkość>limit:
#    if prędkość-limit<=10:
#        mandat = (prędkość-limit)*5
#    else:
#        mandat = (prędkość-limit)*15
#print(f'Mandat (zł): {mandat}')

############ 45
#def infinity():
#    i=0
#    while 1:
#        yield i
#        i+=1
#N = int(input('Podaj N: '))
#for i in infinity():
#    if N==0:
#       break
#    if i>1:
#        for x in range(2,i):
#            if i%x==0:
#                break
#        else:
#            print(i)
#            N-=1
            
############ 46
#from random import randrange
#for i in range(20):
#    print(randrange(-20,-5))

############ 47
#kwota = int(input('Podaj kwotę w zł: '))
#z = kwota
#print(f'Kwota {kwota} zł w monetach:')
#if z>=5:
#    piątki = z//5
#    z=z%5
#    print(f'5zł - {piątki} szt')
#if z>=2:
#   dwójki = z//2
#    z=z%2
#    print(f'2zł - {dwójki} szt')
#if z>=1:
#    jedynki = 1
#    print(f'1zł - {jedynki} szt')

############ 48
#for x in range(1,8):
#    for i in range (0,43,7):
#        if (x+i)//10>0:
#            print(f'{x+i}',end=' ')
#        else:
#            print('',f'{x+i}',end=' ')
#    print()

############ 49
#nrDniaTygodnia = int(input('Początkowy numer dnia tygodnia (od 0–Pn do 6–Nd): '))
#print('| PN | WT | SR | CZ | PT | SB | ND |')
#for i in range(0,29,7):
#    print('| ',end='')
#    for x in range(1,8):
#        if (x+i)-nrDniaTygodnia <= 0:
#            print('   | ',end='')
#        elif (x+i)-nrDniaTygodnia > 30:
#            print('   | ',end='')
#        elif ((x+i)-nrDniaTygodnia)//10>0:
#            print(f'{x+i-nrDniaTygodnia}','| ',end='')
#        else:
#            print('',f'{x+i-nrDniaTygodnia}','| ',end='')
#    print()

############ 50
#x = int(input('Podaj liczbę: '))
#xB = ''
#while x>1:
#    xB+=str(int((x%2)))
#    x/=2
#print(xB[::-1])
    