##########  8
#x = 7
#y = 8
#if x > y:
#    print(x)
#else:
#    print(y)

##########  9
#x = 4
#if x%2==0:
#    print('Parzysta')
#else:
#    print('Nieparzysta')
    
##########  10
#x = int(input('Podaj liczbę całkowitą: '))
#if x > 0 and x%2!=0:
#    print ('Liczba dodatnia i nieparzysta')

##########  11
#login = 'marek'
#hasło = 'm-123'
#x = input('Podaj login: ')
#y = input('Podaj hasło: ')
#if x==login and y==hasło:
#    print('Podane dane są prawidłowe')
#else:
#    print('Podane dane są nieprawidłowe')

##########  12
#x = int(input('Podaj pierwszą liczbę całkowitą: '))
#y = int(input('Podaj drugą liczbę całkowitą: '))
#if x<0 or y<0:
#    print('Jedna z nich jest ujemna')

##########  13
#x = int(input('Podaj współrzędną x: '))
#y = int(input('Podaj współrzędną y: '))
#if x<0 and y>0:
#    print('Punkt({},{}) znajduję się w pierwszej ćwiartce układu współrzędnych'.format(x,y))
#elif x>0 and y>0:
#    print('Punkt({},{}) znajduję się w drugiej ćwiartce układu współrzędnych'.format(x,y))
#elif x<0 and y<0:
#    print('Punkt({},{}) znajduję się w trzeciej ćwiartce układu współrzędnych'.format(x,y))
#elif x>0 and y<0:
#    print('Punkt({},{}) znajduję się w czwartej ćwiartce układu współrzędnych'.format(x,y))
#elif x==0 and y!=0:
#    print('Punkt({},{}) znajduję się na osi Y'.format(x,y))
#elif x!=0 and y==0:
#    print('Punkt({},{}) znajduję się na osi X'.format(x,y))
#elif x==0 and y==0:
#    print('Punkt({},{}) znajduję się w początku układu współrzędnych'.format(x,y))

##########  14
#x = int(input('Wpisz wiek psa: '))
#if x <= 2:
#    wiek = x*10.5
#else:
#    wiek = 21+(x-2)*4
#print (wiek)

##########  15
#x = int(input('Podaj liczbę: '))
#for i in range(1,11):
#    print('{} x {} = {}'.format(x,i,x*i))

##########  16
#for i in range(1,11):
#    print (f'1/{i} = {1/i}')

##########  17
#sumaP = 0
#sumaNP = 0
#for i in range(1,51):
#    if i%2 == 0:
#        sumaP += i
#    else:
#        sumaNP += i
#print(f'Suma liczb parzystych to: {sumaP}'+'\n'+f'Suma liczb nieparzystych to: {sumaNP}')

##########  18
#x = ''
#for i in range(1,31):
#    if i%3 == 0 and i%5 == 0:
#        x += 'BINGO' + ' '
#    elif i%3 == 0:
#        x += 'THREE' + ' '
#    elif i%5 == 0:
#        x += 'FIVE' + ' '
#    else:
#        x += str(i) + ' '
#print(x)

##########  19
#N = int(input('Wprowadź N: '))
#x = 'Ciąg arytmetyczny o różnicy 3: '
#z = -2
#while N>0:
#    z += 3
#    x += f'{z}'
#    N -= 1
#    if N>0:
#        x += ', '
#print(x)

##########  20
#x = 2
#y = 5
#if x > y:
#    print(x)
#else:
#    print(y)

##########  21
#x = 3
#y = 1 + x
#z = 2 * x - 4
#for n in range(z):
#    y += n + x
#    x = x + 1
#print(x,y,n)

##########  22
#lista = [15, 8, 31, 47, 2, 19]
#listaNp = []
#for i in lista:
#    if i % 2 != 0:
#        listaNp.append(i)
#średnia = sum(listaNp)/len(listaNp)
#print('Średnia arytmetyczna liczb nieparzystych w tym zbiorze to: {}'.format(średnia))

##########  23
#ocenySłow = ['niedostateczny','mierny','dostateczny','dobry','bardzo dobry','celujący']
#ocenaNum = int(input('Podaj ocenę: '))
#print(f'Ocena słownie: {ocenySłow[ocenaNum-1]}')

##########  24
#tablicaImion = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy', 'Teofil']
#z = ''
#for i in tablicaImion:
#    if len(i)>len(z):
#        z = i
#print(z)
