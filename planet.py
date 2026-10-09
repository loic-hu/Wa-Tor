import random
from collections import Counter
from fish import Fish
from shark import Shark

    
class Planet:
    """Représente une planète sous forme d'une matrice peuplée de poissons, de requins et de vide.

    La planète est modélisée par une matrice de ``row`` lignes et ``column`` colonnes. 
    Chaque case contient soit un ``Fish``, soit un ``Shark``, soit ``None`` (case d'eau vide).

    Attributes:
        column (int): Nombre de colonnes de la grille (largeur).
        row (int): Nombre de lignes de la grille (hauteur).
        chronon (int): Unité de temps de la simulation.
        types (list): Types de contenu possibles pour une case (``"fish"``, ``"shark"`` ou ``None``).
        weight (list[int]): weight de probabilité associés à chaque type lors du peuplement initial
        matrice (list[list]): Grille 2D contenant les créatures ou ``None``.
    """
    def __init__(self, column, row, weight):
        """Initialise la planète avec ses dimensions et une grille vide.

        Args:
            column (int): Nombre de colonnes de la grille.
            row (int): Nombre de lignes de la grille.
            chronon (int): Unité de temps de la simulation.
            type: 
            weight:
        """
        self.column = column
        self.row = row
        self.weight = weight
        self.chronon = 1
        self.types = ["fish", "shark", None]
        self.matrice = []


    def populate(self):
        """Remplit aléatoirement la grille avec des poissons, des requins ou du vide.

        Pour chaque case, un type est tiré au hasard selon les weight définis
        dans ``self.weight``. Les poissons sont créés avec ``Fish(x, y, 0)`` et
        les requins avec ``Shark(x, y, 0, 8, 10, 20)``.

        Returns:
            list[list]: La matrice 2D générée, également stockée dans
            ``self.matrice``.
        """
        for y in range(self.row):
            ligne = []
            for x in range(self.column):
                choix = random.choices(self.types, weights=self.weight, k=1)[0]
                if choix == "fish":
                    ligne.append(Fish(x, y, 0))
                elif choix == "shark":
                    ligne.append(Shark(x, y, 0, 8, 10, 20))
                else:
                    ligne.append(None)
            self.matrice.append(ligne)
        return self.matrice


    def get_all_creatures(self): 
        """Récupère toutes les créatures présentes sur la planète.

        Parcourt la matrice et collecte chaque case non vide.

        Returns:
            list: Liste des objets ``Fish`` et ``Shark`` présents dans la grille.
        """
        all_creatures = []
        for row in self.matrice:
            for column in row:
                if column != None:
                    all_creatures.append(column)
        return all_creatures
 

    def update_planet(self):
        """Fait avancer la simulation d'un pas.

        Récupère toutes les créatures, puis appelle pour chacune sa méthode
        ``look_out`` en lui passant la matrice, afin qu'elle observe son
        environnement et agisse en conséquence.
        """
        creatures = self.get_all_creatures()
        #print(f"Shark : {count(type(creatures))}")

        compte_types = Counter(type(element) for element in creatures)
        for type_objet, quantite in sorted(compte_types.items(), key=lambda x: x[0].__name__):
            print(f"Type {type_objet.__name__} : {quantite}")

        for i in creatures:
            if self.matrice[i.y][i.x] == i:
                i.look_out(self.matrice)
        self.show_planet()



    def show_planet(self):
        """Affiche la planète dans la console.

        Les cases vides sont représentées par un bloc bleu (code ANSI
        ``\\033[44m``, symbolisant l'eau). Les cases occupées affichent la
        représentation textuelle de la créature (``__str__``).
        """
        for ligne in self.matrice:
            for case in ligne:
                if case == None:
                    print("\033[44m  \033[0m", end="")
                else:
                    print(case, end="")
            print()
