import random
from fish import Fish
from shark import Shark

    
class Planet:
    def __init__(self, column, row, chronon):
        self.column = column
        self.row = row
        self.chronon = chronon
        self.types = ["fish", "shark", None]
        self.poids = [17, 10, 73]
        self.matrice = []

    def populate(self):
        for y in range(self.row):
            ligne = []
            for x in range(self.column):
                choix = random.choices(self.types, weights=self.poids, k=1)[0]
                if choix == "fish":
                    ligne.append(Fish(x, y, 0, 6))
                elif choix == "shark":
                    ligne.append(Shark(x, y, 0, 8, 10, 20, 4))
                else:
                    ligne.append("\033[44m  \033[0m")
            self.matrice.append(ligne)
        return self.matrice

    def show_planet(self):
        for ligne in self.matrice:
            for case in ligne:
                print(case, end=" ")
            print()





