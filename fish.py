
 
 
import random

class Fish: #Represente le poisson dans sa grille
    
    def __init__(self, x, y, gestation_period): #gestation_period a determiner
            self.x = x
            self.y = y
            self.pregnancy = 0  
            self.gestation_period = gestation_period

    def __repr__(self): #renvoi une image "F" pour fish
        return "F"

def look_out(self, grid, rows, columns): #regarde les cases disponibles et retournes les coordonnées
        
        cases_vides = []
        
        # Directions : haut, bas, gauche, droite
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


        for dx, dy in directions: #a relire
            # Position avec modulo
            nx = (self.x + dx) % rows
            ny = (self.y + dy) % columns
            # Si la case dans la grille est vide 
            if grid[nx][ny] is None:
                cases_vides.append((nx, ny))
                
        return cases_vides

        

def move(self, grid, rows, columns): 
        
            # cherche les cases disponibles
            cases_vides = self.look_out(grid, rows, columns)
        
        
            self.pregnancy += 1 #rajoute une unitée a chaque chronon
        
            #le poisson ne bouge pas si pas de cases vide a proximité
            if not cases_vides:
                return None

            #Déplacement aléatoire avec random.choice
            new_x, new_y = random.choice(cases_vides) #-> uniquement
            old_x, old_y = self.x, self.y #ancienne coordonnées deviennent reference avant mise a jour

            # Mettre à jour la grille et les coordonnées du poisson
            grid[old_x][old_y] = None
            self.x, self.y = new_x, new_y
            grid[new_x][new_y] = self
        
            #Gestion de la reproduction
            if self.pregnancy >= self.gestation_period:
            #baby sur la old position
                baby = self.reproduce(old_x, old_y) #baby se retrouve sur la case d'origine fish avant le deplacement de celui ci
                grid[old_x][old_y] = baby
            return baby 
            

def reproduce(self, x, y): #reinitialise pregnancy a 0
    self.pregnancy = 0 
    return Fish(x, y, self.gestation_period)

        
        

       
        
       
            
                        
                       
        


