class Macierz:
    from random import randrange
    def __init__(self,m,n):
        self.m = m
        self.n = n
        self.matrix = matrix()

    def matrix():
        matrixx = []
        matM = []
        matN = []
        for i in range(self.m):
            matM.append(randrange(0,10,1))
        for i in range(self.n):
            matN.append(randrange(0,10,1))
        matrixx.append(matM)
        matrixx.append(matN)


    def __add__(self,other):
        if self.m == other.m and self.n == other.n:
             