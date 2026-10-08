import random

# Classe representant un poisson dans la grille
class Fish:
    
    def __init__(self, x, y, pregnancy, gestation_period):
        self.x = x
        self.y = y
        self.pregnancy = pregnancy
        self.gestation_period = gestation_period

        

    def __repr__(self):
        return "F"

    def look_out (self, largeur, hauteur): #regarde les cases disponibles
            cases_vides = []
                # Directions : haut, bas, gauche, droite
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

            new_x = (self.x + directions.x) % largeur
            new_y = (self.y + directions.y) % hauteur
         
            if not cases_vides: #si aucune case n'est libre le fish ne bouge pas
                return None
          

    def move (self, x, y): #deplacement aleatoire
        
        #deplace au hasard (random.choice) en fonction des cases disponibles
        new_x, new_y = random.choice(cases_vides)
        old_x, old_y = self.x, self.y

        # Déplacer le poisson
        [old_y],[old_x] = None
        self.x, self.y = new_x, new_y
        [new_y],[new_x] = self
        

        if self.pregnancy >= self.gestation_period:
            self.reproduce()

    def reproduce (self,pregnancy, x, y):
            #gestion de la reproduction
        
        pregnancy = 0 
        baby_fish = Fish(x, y) #position baby fish
            
        pregnancy += 1 
            
        return baby_fish  
                                 
                             
                         

    
    """
    def obtenir_cases_vides(self, grille):
        vides = []
        # Directions : haut, bas, gauche, droite
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
"""
"""
#deplacement toroidale: 
    def deplacer_toroidal(x, y, dx, dy, largeur, hauteur):
        Calcule la nouvelle position sur une grille toroïdale.

        x, y       : Position actuelle
        dx, dy     : Déplacement (ex: +1, -1, 0)
        largeur    : Nombre de colonnes de la grille
            hauteur    : Nombre de lignes de la grille
    
        nouvel_x = (x + dx) % largeur
        nouvel_y = (y + dy) % hauteur

        return nouvel_x, nouvel_y

"""
"""
        for dx, dy in directions:
            
            nx = (self.x + dx) % LARGEUR
            ny = (self.y + dy) % HAUTEUR

            """


        
        
        

       
        
       
            
                        
                       
        


