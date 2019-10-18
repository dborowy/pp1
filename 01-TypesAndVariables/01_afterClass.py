###################  24
#import math
#wzCm = 193
#wzStopa = wzCm * 0.032808399
#(wzStopaC,wzStopaS) = math.modf(wzStopa)
#wzStopaC = round(wzStopaC*12)
#wzStopaS = int(wzStopaS)
#print('Mam {} cm wzrostu, tj. {} stóp i {} cali.'.format(wzCm,wzStopaS,wzStopaC))

###################  25
#nrRach = input('Wprowadź nr swojego rachunku bankowego: ')
#print('Nr rachunku:{} {} {} {} {} {} {}'.format(nrRach[0:2],nrRach[2:6],nrRach[6:10],nrRach[10:14],nrRach[14:18],nrRach[18:22],nrRach[22:26]))

###################  26
#def bmiCalc ():
#    wzrost = int(input('Podaj wzrost w cm: '))/100
#    waga = int(input('Podaj wagę w kg: '))
#    bmi = round(waga/wzrost**2, 1)
#    if bmi < 18.5:
#        print('Niedowaga')
#    elif 18.5 <= bmi <= 24.9:
#        print('Waga prawidłowa')
#    elif 25 <= bmi <= 29.9:
#        print('Nadwaga')
#    elif bmi > 30:
#        print('Otyłość')
#bmiCalc()
    
###################  27
#import math
#x = int(input('Podaj pierwszą dowolną liczbę naturalną: '))
#y = int(input('Podaj drugą dowolną liczbę naturalną: '))
#wspDziel = math.gcd(x,y)
#print('Największy wspólny dzielnik tych liczb to: {}'.format(wspDziel))

###################  28
#from random import sample
#trzyRzuty = sample([1, 2, 3, 4, 5, 6],3)
#print('Wartość oczek w trzech rzutach: ',trzyRzuty)
#print('Ich suma: ',sum(trzyRzuty))

###################  29
#from random import randrange
#rzutKomp = randrange(1,7)
#guess = int(input('Podaj ile oczek kostki wyrzucił komputer: '))
#print('Komputer wyrzucił: ',rzutKomp)
#if rzutKomp == guess:
#    x = 'Tak'
#else:
#    x = 'Nie'
#print('Zgadłeś: ',x)

###################  30

#lista = [12, 6, 4, 9, 3]
#for i in lista:
#    print('{}: {}'.format(i,i*'*'))