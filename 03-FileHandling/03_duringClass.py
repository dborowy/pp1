########## 8
#with open('NoEducation.txt','r') as pF:
#    print(pF.read())

########## 9
#with open('NoEducation.txt','r') as pF:
#    i=1
#    for line in pF:
#        print(f'{i}',line, end='')
#        i+=1

########## 10
#with open('numbers.txt','r') as nr:
#    suma = 0
#    for line in nr:
#        suma+=int(line)
#print(suma)

########## 11
#with open('DanePersonalne.txt','w') as file:
#    file.write('Dominik Borowy\n'+'UEK\n'+'Informatyka Stosowana\n')

########## 12
#with open('shoppinglist.txt','a') as file:
#    file.write(input('Podaj nazwę produktu: ')+'\n')

########## 13
#with open('Cyfry.txt','a') as file:
#    tablica = [32, 16, 5, 8, 24, 7]
#    for i in tablica:
#        file.write(str(i)+'\n')

########## 16
#import re
#komunikat = 'wtorek - 23C, środa - 17C, czwartek 25C'
#cyfry = re.findall('\d{2}',komunikat)
#suma = 0
#for i in cyfry:
#    suma += int(i)
#avgTemp = suma/len(cyfry)
#print(avgTemp)

########## 17
#import re
#x = 'To be, or not to be, that is the question'
#vowels = re.findall('[aeyiou]',x)
#print(len(vowels))

