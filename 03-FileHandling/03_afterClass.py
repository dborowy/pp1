########## 18
#with open('numbers.txt','r') as file:
#    nr = []
#    for i in file:
#        nr.append(int(i))
#    nr.sort()
#    for i in nr:
#        print(i,end=' ')

########## 19
#with open('universities.txt','r') as file:
#    lista = []
#    for i in file:
#        lista.append(i)
#    listaCr = []
#    for i in lista:
#        x = i.replace('"', '')
#        listaCr.append(x)        
#    print(listaCr)
#    listaCr.sort()
#    with open('universities.txt','w') as file:
#        for i in listaCr:
#            file.write(i)

########## 20
#with open('numbers.txt','r') as f1:
#    evenNo = []
#    for i in f1:
#        if int(i)%2 == 0:
#            evenNo.append(i)
#    with open('evennumbers.txt','w') as f2:
#        for i in evenNo:
#            f2.write(i)

########## 21
#with open('numbersinrows.txt','r') as f1:
#    lista = []
#    for i in f1:
#        x = i.split(',')
#        lista.append(x)
#    corrlista = []
#    for i in lista:
#        for x in i:
#            corrlista.append(x)
#    finLista = []
#    for i in corrlista:
#        x = i.replace('\n','')
#        finLista.append(x)
#    suma = 0
#    for i in finLista:
#        suma += int(i)
#    print(len(finLista),suma)

########## 22
#with open('students.txt','r') as f1:
#    lista = []
#    for i in f1:
#        lista.append(i.split(','))
#    #print(lista)
#    for i in lista[1:]:
#        if int(i[2])<30:
#            print(i[0],i[1],i[4])

########## 23
#with open('land.txt','r') as f1:
#    import re
#    x = f1.read()
#    cyfry = re.findall('\d+',x)
#    suma = 0
#    for i in cyfry:
#        suma += int(i)
#    print(suma)

########## 24
#lista = [['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'],['Piotr','Wyga','wygap@gop.pl']]
#with open('zad24.csv','w') as f1:
#    f1.write('Imie,Nazwisko,Email')
#    for i in lista:
#        f1.write('\n'+i[0]+','+i[1]+','+i[2])