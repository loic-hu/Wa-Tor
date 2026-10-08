import random

class Planet:
    def __init__(self, width, lenght, chronon):
        self.width = width
        self.lenght = lenght
        self.chronon = chronon
        self.matrice = [[]]

    def populate(self):
        self.matrice = [random.choices(["F", "S", " "], weights=[17, 10, 73], k=self.lenght) for _ in range(self.width)]
        return self.matrice

# def __repr__()
    def show_planet(self):
        for ligne in range(len(self.matrice)):
            print()
            for colonne in range(len(self.plamatricenete)):
                print(self.matrice[ligne][colonne], end=" ")

    #def remplir