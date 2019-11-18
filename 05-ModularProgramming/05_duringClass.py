############## 4
#import math
#x = 3.7
#y = 4
#xSqrt = math.sqrt(x)
#xyPwr = math.pow(x,y)
#poleK = math.pi * math.sqrt(y)
#yFact = math.factorial(y)
#xFloor = math.floor(x)
#
#print(f'a) {xSqrt}\nb) {xyPwr}\nc) \nd) {poleK}\ne) {yFact}\nf) {xFloor}')

############## 5
#import re
#import statistics
#wynagTekst = '21600 zł (wynagrodzenie prezesa),4350 zł, 3920 zł,5590 zł,3250 zł, 4010 zł'
#wynagLiczT = re.findall('\d+',wynagTekst)
#wynagLicz = []
#for i in wynagLiczT:
#    wynagLicz.append(int(i))
#avgWynag = statistics.mean(wynagLicz)
#medWynag = statistics.median(wynagLicz)
#stDevWynag = statistics.pstdev(wynagLicz)
#print(f'a) {avgWynag}\nb) {medWynag}\nc) {stDevWynag}')

############## 6
#import csv
#import statistics
#with open('employees.csv', newline='') as f:
#    reader = csv.reader(f)
#    wiekPrac = []
#    for no, row in enumerate(reader):
#        if no == 0:
#            eq = '='
#            print(f'#    {row[1].upper()}    {row[0].upper()}    {row[2].upper()}   {row[3].upper()}\n{eq*40}')
#        else:
#            print(f'{no}    {row[1].upper()}    {row[0]}    {row[2]}    {row[3]}')
#            wiekPrac.append(int(row[2]))
#    print(f'\nŚredni wiek pracowników: {statistics.mean(wiekPrac)}')

############## 7
