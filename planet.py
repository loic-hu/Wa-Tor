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
                    ligne.append(Fish(x, y, 0))
                elif choix == "shark":
                    ligne.append(Shark(x, y, 0, 8, 10, 20))
                else:
                    ligne.append(None)
            self.matrice.append(ligne)
        return self.matrice


    def get_all_creatures(self): 
        all_creatures = []
        for row in self.matrice:
            for column in row:
                if column != None:
                    all_creatures.append(column)
        return all_creatures
 

    def update_planet(self):
        creatures = self.get_all_creatures()
        for i in creatures:
            i.look_out(self.matrice)


    def show_planet(self):
        for ligne in self.matrice:
            for case in ligne:
                if case == None:
                    print("\033[44m  \033[0m", end=" ")
                else:
                    print(case, end=" ")
            print()





