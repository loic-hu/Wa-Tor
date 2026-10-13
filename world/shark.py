from world.fish import Fish
import random

class Shark(Fish):
    """
    Représente le prédateur Shark (Requin) dans cet environnement Planète. 
    Il hérite de la class Fish (Poisson), sa proie.

    Il hérite des déplacements cardinaux de Fish, ainsi que sa capacité de reproduction, cependant plus longue.

    En plus, il a la capacité de manger un objet Fish. Cette capacité lui est indispensable à sa survie.
    En effet, contrairement à Fish il a une energie limitée, si celle-ci tombe à 0, il meurt.
    Manger un Fish lui permet de remonter cette énergie.

    [Attributes]:
        x (int) : sa position sur l'axe x de la grille, donc sa colonne (hérité de Fish)
        y (int) : sa position sur l'axe y de la grille, donc sa ligne (hérité de Fish)
        gestation_period (int) : le nombre de cycles nécessaires pour se reproduire (hérité de Fish)
        energy (int) : l'énergie de l'entité, si elle tombe à 0, Shark meurt de faim.
        max_energy (int) : l'énergie max de l'entité car son estomac n'est pas infini.
        energy_regain (int) : l'énergie gagnée en consommant Fish
        pregnancy (int) : le nombre de cycles de l'entité, si pregnancy est égal à gestation_period, alors la reproduction est possible
    """

    def __init__(self, x, y,):
        """
        Initialise l'objet Shark avec ses attributs.
        """

        from config import env_config1 as env_cfg

        super().__init__(x, y)
        self.energy = env_cfg.shark_config["energy"]
        self.max_energy = env_cfg.shark_config["max_energy"]
        self.energy_regain = env_cfg.shark_config["energy_regain"]
        self.pregnancy = 0
        self.gestation_period = env_cfg.shark_config["gestation_period"]


    def __repr__(self):
        """
        La réprésentation de l'objet quand on le print() en console.
        Dans notre cas, un carré rouge.
        """

        return "\033[41m  \033[0m"

    def life_cycle(self, matrice):
        """
        Fonction gérant le cycle vivant de Shark, appelée par Planet.

        [Args]:
            matrice (List[List[Object]]) : La matrice 2D de l'environnement dans lequel évolue notre entité
        """

        # On sauvegarde la position d'origine
        origin = (self.x, self.y)   

        # On vérifie en premier si l'entité a consommé toute son énergie
        if self.energy == 0:

            # Si oui, on provoque la mort de l'entité puis on arrête le cycle
            self.die(matrice)
            return

        # On demande à l'entité de regarder autour de soi, et agir en conséquence (déplacement ou manger ou ne rien faire)
        self.look_out(matrice)

        # On augmente le compteur de cycle de l'entité
        self.pregnancy += 1

        # Si le nombre de cycle de l'entité est supérieur ou égal à la période de gestation, et qu'il vient de se déplacer
        if self.pregnancy >= self.gestation_period and origin != (self.x, self.y):

            # Alors l'entité se reproduit
            self.reproduce(matrice, origin)

        # On diminue l'energie de 1 à la fin du cycle
        self.energy -= 1

        # Cycle terminé
        return

    def look_out(self, matrice):
        """
        Fonction gérant l'observation de l'environnement dans lequel l'entité Shark évolue.
        Elle observe les cases adjacentes cardinalement et agit en conséquence.
        Si elle peut bouger, elle privilégie un repas à un simple mouvement.
        Si plusieurs choix, de même priorités, sont possibles, elle choisit au hasard.

        [Args]:
            matrice (List[List[Object]]) : La matrice 2D de l'environnement dans lequel évolue notre entité
        """

        # Liste de tuples contenant les positions des cases adjacentes (haut, bas, gauche, droite)
        # Le modulo permet, si on atteint la limite de la grille, de retourner à l'opposé sur la grille
        adj_cases = [(self.x, (self.y - 1 ) % len(matrice)),    
                     (self.x, ( self.y + 1 ) % len(matrice)),
                     (( self.x -1 ) % len(matrice[0]), self.y),
                     (( self.x + 1) % len(matrice[0]), self.y)
                     ]

        # Listes stockant les cases vides, et cases nourritudes adjacentes
        empty_cases = []
        food_cases = []

        # Pour chaque case dans les cases adjacentes
        for case in adj_cases:

            # Si la case est vide, on la stocke dans la liste empty_cases
            if matrice[case[1]][case[0]] == None:
                empty_cases.append(case)

            # Si la case est un Fish et n'est pas un Shark (car Shark hérite de Fish), on la stocke dans la liste food_cases
            elif isinstance(matrice[case[1]][case[0]], Fish) and not isinstance(matrice[case[1]][case[0]], Shark):
                food_cases.append(case)

        # Si on a une case nourriture disponible
        if food_cases:

            # On choisit au hasard une case de la liste
            lunch = random.choice(food_cases)
            # Et on apelle la fonction eat() pour manger la cible
            self.eat(matrice, lunch)

        # Si on a une case libre disponible
        elif empty_cases:

            # On choisit au hasard une case de la liste
            dest = random.choice(empty_cases)
            # Et on apelle la fonction move() vers la case cible
            self.move(matrice, dest )

        # Sinon on ne fait rien
        else:
            return    

    def move(self, matrice, coordinates):
        """
        Fonction gérant le déplacement de l'entité

        [Args]:
            matrice (List[List[Object]]) : La matrice 2D de l'environnement dans lequel évolue notre entité
            coordinates (Tuple(int)) : Les coordonnées de la case cible
        """

        # On efface la présence de l'entité à la position actuelle dans la matrice
        matrice[self.y][self.x] = None
        # Puis on place aux nouvelles coordonnées
        matrice[coordinates[1]][coordinates[0]] = self

        # On update le x et y de l'entité avec les nouvelles coordonées
        self.x = coordinates[0]
        self.y = coordinates[1]


    def eat(self, matrice, food):
        """
        Fonction gérant la capacité de manger de l'identité.
        C'est à dire détruire une instance de poisson, en gagner de l'energie, puis prendre sa place

        [Args]:
            matrice (List[List[Object]]) : La matrice 2D de l'environnement dans lequel évolue notre entité
            food (Tuple(int)) : Les coordonnées de la case Fish à dévorer
        """

        # On efface la présence de l'entité à la position actuelle dans la matrice
        matrice[self.y][self.x] = None
        # Puis on place aux nouvelles coordonnées, ce qui supprime le Fish présent à cet emplacement
        matrice[food[1]][food[0]] = self

        # On update le x et y de l'entité avec les nouvelles coordonées
        self.x = food[0]
        self.y = food[1]

        # On ajoute l'énergie gagnée par ce repas
        self.energy += self.energy_regain

        # Si l'énergie suite à se repas dépasse l'energie maximale
        if self.energy > self.max_energy :
            
            # Alors on abaisse l'energie à la valeur maximale autorisée
            self.energy = self.max_energy

    
    def reproduce(self, matrice, origin):
        """
        Fonction gérant la reproduction de l'entité

        [Args]:
            matrice (List[List[Object]]) : La matrice 2D de l'environnement dans lequel évolue notre entité
            origin (Tupple(int)) : Les coordonées de la case d'origine de Shark après un déplacement
        """

        # Aux coordonées d'origines dans la matrice, crée une nouvelle entité Shark
        matrice[origin[1]][origin[0]] = Shark(origin[0], origin[1])

        # Reset le compteur de pregnancy
        self.pregnancy = 0

    def die(self, matrice):
        """
        Fonction gérant la mort de l'entité

        [Args]:
            matrice (List[List[Object]]) : La matrice 2D de l'environnement dans lequel évolue notre entité
        """

        # Remplace l'emplacement de l'entité par None
        matrice[self.y][self.x] = None



