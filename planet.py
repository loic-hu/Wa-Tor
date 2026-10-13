#import main
import random

from fish import Fish
from shark import Shark
from flying_fish import Flying_fish

#from config import env_config1 as env_cfg
from config import env_config1 as env_cfg, graph_config as graph_cfg

    
class Planet:
    """Représente une planète sous forme d'une matrice peuplée de poissons, de requins et de vide.

    La planète est modélisée par une matrice de ``row`` lignes et ``column`` colonnes. 
    Chaque case contient soit un ``Fish``, soit un ``Shark``, soit ``None`` (case d'eau vide).

    Attributes:
        column (int): Nombre de colonnes de la grille (largeur).
        row (int): Nombre de lignes de la grille (hauteur).
        weight (list[int]): weight de probabilité associés à chaque type lors du peuplement initial
        chronon (int): Unité de temps de la simulation.
        types (list): Types de contenu possibles pour une case (``"fish"``, ``"shark"`` ou ``None``).
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
        self.types = ["fish", "shark", "flying_fish", None]
        self._matrice = []

    @property
    def matrice(self) -> list[list[Fish | Shark | Flying_fish | None]]:
        return self._matrice

    def populate(self):
        """Remplit aléatoirement la grille avec des poissons, des requins ou du vide.

        Pour chaque case, un type d'objet est tiré au hasard selon les ``weight`` définis dans ``self.weight``.
        Les poissons sont créés avec ``Fish(x, y, ...)`` et les requins avec ``Shark(x, y, ...)``.

        Returns:
            list[list]: La matrice 2D générée, également stockée dans
            ``self.matrice``
        """
        for y in range(self.row):
            ligne = []
            for x in range(self.column):
                #
                choix = random.choices(self.types, weights=self.weight, k=1)[0]
                if choix == "fish":
                    ligne.append(Fish(x, y))
                elif choix == "shark":
                    ligne.append(Shark(x, y))
                elif choix == "flying_fish":
                    ligne.append(Flying_fish(x, y))
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

        Récupère toutes les créatures, puis appelle pour chacune sa méthode ``look_out`` en lui passant la matrice,
        afin qu'elle observe son environnement et agisse en conséquence.
        """
        creatures = self.get_all_creatures()
        # Parcours de la liste des créatures présentes sur la grille
        for i in creatures:
            if self.matrice[i.y][i.x] == i:
                i.life_cycle(self.matrice)
        self.show_planet()

    def update_planet_V2(self):
        """Fait avancer la simulation d'un pas.

        Récupère toutes les créatures, puis appelle pour chacune sa méthode ``look_out`` en lui passant la matrice,
        afin qu'elle observe son environnement et agisse en conséquence.
        """
        creatures = self.get_all_creatures()
        while creatures:
            index = random.randrange(len(creatures))
            if self.matrice[creatures[index].y][creatures[index].x] == creatures[index]:
                creatures[index].life_cycle(self.matrice)
            creatures.pop(index)
        self.show_planet()


    def show_planet(self):
        """Affiche la planète dans la console.

        Les cases vides sont représentées par un bloc bleu (code ANSI ``\033[44m  \033[0m``, symbolisant l'eau).
        Les cases occupées affichent la représentation textuelle de la créature (``__str__``).
        """
        for ligne in self.matrice:
            for case in ligne:
                if case == None:
                    print("\033[44m  \033[0m", end="")
                else:
                    print(case, end="")
            print()

