class Prostokat():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __add__(self,other):
        return self.a*self.b+other.a*other.b
