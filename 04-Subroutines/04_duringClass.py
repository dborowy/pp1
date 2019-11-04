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
def silnia(n):
    #0!=1 oraz 1!=1
    if n==0 or n==1:return 1
    #n! = n * (n-1)!
    if n > 1:
        return n * silnia(n-1)
print(f’10! = {silnia(10)}’)