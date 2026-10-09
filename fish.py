import random

class Fish: #Initialisation
    
    def __init__(self, x, y, gestation_period, Planet): 
        self.x = x
        self.y = y
        self.Planet = Planet
        self.pregnancy = 0  
        self.gestation_period = gestation_period


    def __repr__(self): #Image "F"
        return "\033[42m  \033[0m"

    def look_out(self, matrice): #Regarde les cases disponibles et retournes les coordonnées
        empty_cases = []
        
        adj_cases = [(self.x, (self.y - 1 ) % len(matrice)),
                             (self.x, ( self.y + 1 ) % len(matrice)),
                             (( self.x -1 ) % len(matrice[0]), self.y),
                             (( self.x + 1) % len(matrice[0]), self.y)
                             ]

        for case in adj_cases:#Parcours les cases adjacente et stock les cases vide dans blank.cell.append(case)
            if matrice[case[1]][case[0]] == None:
                empty_cases.append(case)

        if empty_cases:
            dest = random.choice(empty_cases)
            self.move(matrice, dest )
        else:
            return

    def move(self, matrice, coordinates): 
        
        self.pregnancy += 1 #Rajoute une unitée a chaque chronon

        new_x = coordinates[0]
        new_y = coordinates[1]

        
        matrice[self.y][self.x] = None
        matrice[new_y][new_x] = self

        self.x = new_x
        self.y = new_y

        return 
        """
        #Gestion de la reproduction
        if self.pregnancy >= self.gestation_period:
        #baby sur la old position
            baby = self.reproduce(old_x, old_y) #baby se retrouve sur la case d'origine fish avant le deplacement de celui ci
            matrice[old_x][old_y] = baby
            return baby 
            """
    def reproduce(self, x, y): #reinitialise pregnancy a 0
        self.pregnancy = 0 
        return Fish(x, y, self.gestation_period)

        
       

        

        
       

       

    
        
        


    

   



    

    

   

    
 

       
        
       
            
                        
                       
        


