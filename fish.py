
import random

class Fish:
    """
    Représente le Fish (poisson) dans cet environnement Planète. 
    Il sert de nourriture a Shark (requin) tout en ayant un deplacement qui lui est propre.
    Il est de classe "parent" par rapport a shark.
    
    [Attributes]:
        x (int) : sa position sur l'axe x de la grille, donc sa colonne 
        y (int) : sa position sur l'axe y de la grille, donc sa ligne 
        gestation_period (int) : le nombre de cycles nécessaires pour se reproduire
        pregnancy (int) : le nombre de cycles de l'entité, si pregnancy est égal à gestation_period, alors la reproduction est possible
    """

    def __init__(self, x, y, gestation_period): 
        self.x = x
        self.y = y
        self.pregnancy = 0  
        self.gestation_period = gestation_period

    def __repr__(self): # Image "F"
        """
        La réprésentation de l'objet quand on le print() en console.
        Dans notre cas, un carré vert.
        """
        return "\033[42m  \033[0m"

    def life_cycle(self, matrice):
        """
        Fonction gérant le cycle vivant du Fish appelée par Planet.

        [Args]:
            matrice (List[List[Object]]) : La matrice 2D de l'environnement dans lequel évolue notre entité
        """
        # On sauvegarde la position d'origine
        origin = (self.x, self.y)   

        # On demande à l'entité de regarder autour de soi 
        self.look_out(matrice)

        # On augmente le compteur de cycle de l'entité
        self.pregnancy += 1

        # Si le nombre de cycle de l'entité est supérieur ou égal à la période de gestation, et qu'il vient de se déplacer
        if self.pregnancy >= self.gestation_period and origin != (self.x, self.y):
            # Alors l'entité se reproduit
            self.reproduce(matrice, origin)

        # Cycle terminé
        return

    def look_out(self, matrice):
        """
        Fonction gérant l'observation de l'environnement dans lequel l'entité Fish évolue.
        Elle observe les cases adjacentes cardinalement et agit en conséquence.
        
        [Args]:
            matrice (List[List[Object]]) : La matrice 2D de l'environnement dans lequel évolue notre entité
        """
        # Liste de tuples contenant les positions des cases adjacentes (haut, bas, gauche, droite)
        # Le modulo permet, si on atteint la limite de la grille, de retourner à l'opposé sur la grille
        adj_cases = [
            (self.x, (self.y - 1) % len(matrice)),    
            (self.x, (self.y + 1) % len(matrice)),
            ((self.x - 1) % len(matrice[0]), self.y),
            ((self.x + 1) % len(matrice[0]), self.y)
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

        # On update le x et y de l'entité avec les nouvelles coordonnées
        self.x = coordinates[0]
        self.y = coordinates[1]

    def reproduce(self, matrice, origin):
        """
        Fonction gérant la reproduction de l'entité

        [Args]:
            matrice (List[List[Object]]) : La matrice 2D de l'environnement dans lequel évolue notre entité
            origin (Tupple(int)) : Les coordonnées de la case d'origine de Fish après un déplacement
        """
        # Aux coordonnées d'origines dans la matrice, crée une nouvelle entité Fish
        matrice[origin[1]][origin[0]] = Fish(origin[0], origin[1], 5, 3, 10, 4)

        # Reset le compteur de pregnancy
        self.pregnancy = 0
       
    

        

        
       

       

    
        
        


    

   



    

    

   

    
 

       
        
       
            
                        
                       
        


