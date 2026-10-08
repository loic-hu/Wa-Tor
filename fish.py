

# Classe reprÃ©sentant un poisson dans la grille
class Fish:
    
    def __init__(self, x, y, pregnancy, gestation_period):
        self.x = x
        self.y = y
        self.pregnancy = pregnancy
        self.gestation_period = gestation_period

    def look_out (self):
         pass    

    def move (self):
         pass

    def reproduce (self):
         pass

    
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


            
                
        


