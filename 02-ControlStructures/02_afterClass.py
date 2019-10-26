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
#X.sort
#print(X[1])

############ 38
#for i in range(6,-1,-3):
#    for j in range(1,4):
#        print(f' {i+j}',end='')
#print()

#i=6
#while i>=0:
#    for j in range(1,4):
#        print(f' {i+j}',end='')
#    i-=3
#print()

############ 39

