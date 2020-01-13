########### 5
#a = 5
#b = 0
#assert b!=0, 'Wartość b równa 0!'
#assert type(a)==int, 'Wartość a nie jest liczbą całkowitą'
#assert type(b)==int, 'Wartość b nie jest liczbą całkowitą'
#print(f'{a}/{b} = {a/b}')

########### 7
#height = int(input('Wprowadź wzrost: '))
#weight = float(input('Wprowadź wagę: '))
#assert height in range(150,221,1)
#assert weight>=40.0 and weight<=150.0

########### 8,9
#import math
#def square():
#    try:
#        number = float(input('Enter any number: '))
#        print (f'sqrt({number}) = {math.sqrt(number)}' )
#    except:
#        print('Please enter a valid number greater than 0')
#        square()
#square()

########### 10
#def read():
#    try:
#        with open ('NoEducation.txt','r') as f:
#            for row in f:
#                print (row)
#    except FileNotFoundError:
#        print('No such file!')
#read()

########### 11
#wiek = 25
#if type(wiek) != int:
#    raise TypeError('Wiek powinien być liczbą całkowitą!')
#if wiek<=0 or wiek>120:
#    raise ValueError('Podaj poprawną wartość')
#print(f'Masz {wiek} lat')


########### 12

def elo():
    netto = float(input('Podaj cenę netto:'))
    try:
        if type(netto)==int or not type(netto)==float:
            brutto = round(netto*1.23,2)
            print(brutto)
    except:
        raise ValueError('Podaj poprawną wartość')
        elo()
elo()
