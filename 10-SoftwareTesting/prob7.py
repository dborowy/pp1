class Stos():
    def __init__(self):
        self.stos = []
    def wstaw(self,nazwa_karty):
        self.stos.append(nazwa_karty)
    def zdejmij(self):
        self.stos.remove(self.stos[len(self.stos)-1])
    def jest_pusty(self):
        if len(self.stos) == 0 :
            response = 'Jest pusty'
        else:
            response = 'Nie jest pusty'
        return response
    def __str__(self):
        return f'{self.stos}'