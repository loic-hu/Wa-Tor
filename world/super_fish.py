from world.fish import Fish
import random

class Super_fish(Fish):
    """
    Représente l'entité Super Fish (Super poisson) dans cet environnement Planète. 
    Il hérite de la class Fish (Poisson).

    Il hérite de sa capacité de reproduction.

    [Attributes]:
        x (int) : sa position sur l'axe x de la grille, donc sa colonne (hérité de Fish)
        y (int) : sa position sur l'axe y de la grille, donc sa ligne (hérité de Fish)
        gestation_period (int) : le nombre de cycles nécessaires pour se reproduire (hérité de Fish)
        pregnancy (int) : le nombre de cycles de l'entité, si pregnancy est égal à gestation_period, alors la reproduction est possible
    """

    def __init__(self, x : int, y : int) -> None:
        """
        Initialise l'objet Super_fish avec ses attributs.
        """

        from config import env_config1 as env_cfg

        super().__init__(x, y)
        self.pregnancy = 0
        self.gestation_period = env_cfg.super_fish_config["gestation_period"]


    def __repr__(self) -> None:
        """
        La réprésentation de l'objet quand on le print() en console.
        Dans notre cas, un carré orange.
        """

        return "\033[48;5;208m  \033[0m"


    def look_out(self, matrice : list[list]) -> None:
        """
        Fonction gérant l'observation de l'environnement dans lequel l'entité Super_fish évolue.
        Elle observe les cases adjacentes cardinalement et en diagonale et agit en conséquence.
        Si elle peut bouger, elle se déplace

        [Args]:
            matrice (List[List[Object]]) : La matrice 2D de l'environnement dans lequel évolue notre entité
        """

        # Liste de tuples contenant les positions des cases adjacentes (haut,haut droite, droite, bas droite, bas, bas droite, gauche, gauche haut)
        # Le modulo permet, si on atteint la limite de la grille, de retourner à l'opposé sur la grille
        adj_cases = [
            ((self.x-1) % len(matrice) , (self.y - 1) % len(matrice)),  
            (self.x, (self.y - 1) % len(matrice)),
            ((self.x+1) % len(matrice) , (self.y - 1) % len(matrice)),
            ((self.x + 1) % len(matrice[0]), self.y),
            ((self.x+1) % len(matrice) , (self.y + 1) % len(matrice)),
            (self.x, (self.y + 1) % len(matrice)),
            ((self.x-1) % len(matrice) , (self.y + 1) % len(matrice)),
            ((self.x - 1) % len(matrice[0]), self.y)
        ]

        # Listes stockant les cases vides, et cases nourritudes adjacentes
        empty_cases = []

        # Pour chaque case dans les cases adjacentes
        for case in adj_cases:
            # Si la case est vide, on la stocke dans la liste empty_cases
            if matrice[case[1]][case[0]] == None:
                empty_cases.append(case)

        # Si on a une case libre disponible
        if empty_cases:
            # On choisit au hasard une case de la liste
            dest = random.choice(empty_cases)
            # Et on appelle la fonction move() vers la case cible
            self.move(matrice, dest)
        # Sinon on ne fait rien
        else:
            return      

    
    def reproduce(self, matrice : list[list], origin : tuple[int,int]):
        """
        Fonction gérant la reproduction de l'entité

        [Args]:
            matrice (List[List[Object]]) : La matrice 2D de l'environnement dans lequel évolue notre entité
            origin (Tupple(int)) : Les coordonnées de la case d'origine de Super_fish après un déplacement
        """
        # Aux coordonnées d'origines dans la matrice, crée une nouvelle entité Fish
        matrice[origin[1]][origin[0]] = Super_fish(origin[0], origin[1])

        # Reset le compteur de pregnancy
        self.pregnancy = 0
