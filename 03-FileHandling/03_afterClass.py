########## 18
with open('numbers.txt','r') as file:
    nr = []
    for i in file:
        nr.append(int(i))
    print(nr)