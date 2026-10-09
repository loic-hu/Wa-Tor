import random

class Fish: #Initialisation
    
    def __init__(self, x, y, gestation_period, Planet): 
        self.x = x
        self.y = y
        self.Planet = Planet
        self.pregnancy = 0  
        self.gestation_period = gestation_period


    def __repr__(self): #Image "F"
        return "F"

    def look_out(self, matrice): #Regarde les cases disponibles et retournes les coordonnées
        blank_cell = []
        
        adj_cases = [matrice[( self.y - 1 ) % len(matrice)][self.x], 
                     matrice[( self.y + 1 ) % len(matrice)][self.x],
                     matrice[self.y][( self.x -1 ) % len(matrice[0])],
                     matrice[self.y][( self.x + 1) % len(matrice[0])]]

        for case in adj_cases: #Parcours les cases adjacente et stock les cases vide dans blank.cell.append(case)
             if case == None :
                blank_cell.append(case)

        if blank_cell : #Choisis de se deplacer si des cases adjacente sont vide
                return blank_cell
        

    def move(self, grid, matrice): 
        # Cherche les cases disponibles
        blank_cell = self.look_out(grid)
        
        self.pregnancy += 1 #Rajoute une unitée a chaque chronon

        #Déplacement aléatoire avec random.choice
        new_x, new_y = random.choice(blank_cell) #-> uniquement
        old_x, old_y = self.x, self.y #ancienne coordonnées deviennent reference avant mise a jour

        # Mettre à jour la grille et les coordonnées du poisson
        self.x, self.y = new_x, new_y
        matrice[old_x][old_y] = None
        matrice[new_x][new_y] = self
        
        #Gestion de la reproduction
        if self.pregnancy >= self.gestation_period:
        #baby sur la old position
            baby = self.reproduce(old_x, old_y) #baby se retrouve sur la case d'origine fish avant le deplacement de celui ci
            matrice[old_x][old_y] = baby
            return baby 
            
    def reproduce(self, x, y): #reinitialise pregnancy a 0
        self.pregnancy = 0 
        return Fish(x, y, self.gestation_period)

        
       

        

        
       

       

    
        
        


    

   



    

    

   

    
 

       
        
       
            
                        
                       
        


