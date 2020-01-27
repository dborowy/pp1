class Miasto:
    def __init__(self,name,population):
        self.name = name
        self.population = population
    def __str__(self):
        return f'{self.name} posiada populację o wielkości {self.population}'

