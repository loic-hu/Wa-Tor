from fish import Fish
import random

class Shark(Fish):

    def __init__(self, x, y, gestation_period, energy, max_energy, energy_regain):

        super().__init__(x, y, gestation_period)
        self.energy = energy
        self.max_energy = max_energy
        self.energy_regain = energy_regain
        self.pregnancy = 0


    def __repr__(self):

        return "\033[41m  \033[0m"

    def look_out(self, matrice):
       
        adj_cases = [(self.x, (self.y - 1 ) % len(matrice)),
                     (self.x, ( self.y + 1 ) % len(matrice)),
                     (( self.x -1 ) % len(matrice[0]), self.y),
                     (( self.x + 1) % len(matrice[0]), self.y)
                     ]

        empty_cases = []
        food_cases = []
        origin = (self.x, self.y)

        if self.energy == 0:

            self.die(matrice)
            return
     
        for case in adj_cases:
            if matrice[case[1]][case[0]] == None:
                empty_cases.append(case)
            elif isinstance(matrice[case[1]][case[0]], Fish) and not isinstance(matrice[case[1]][case[0]], Shark):
                food_cases.append(case)

        if food_cases:
            lunch = random.choice(food_cases)
            self.eat(matrice, lunch)
        elif empty_cases:
            dest = random.choice(empty_cases)
            self.move(matrice, dest )
        else:
            return

        self.pregnancy += 1

        if self.pregnancy >= self.gestation_period:

            self.reproduce(matrice, origin)

        self.energy -= 1

        return

        

    def move(self, matrice, coordinates):

        new_x = coordinates[0]
        new_y = coordinates[1]

        matrice[self.y][self.x] = None
        matrice[new_y][new_x] = self

        self.x = new_x
        self.y = new_y


    def eat(self, matrice, food):
        
        target_x = food[0]
        target_y = food[1]

        matrice[self.y][self.x] = None
        matrice[target_y][target_x] = self

        self.x = target_x
        self.y = target_y

        self.energy += self.energy_regain
        if self.energy > self.max_energy :
            self.energy = self.max_energy


    def reproduce(self, matrice, origin):
  
        matrice[origin[1]][origin[0]] = Shark(origin[0], origin[1], 5, 3, 10, 4)
        self.pregnancy = 0

    def die(self, matrice):

        matrice[self.y][self.x] = None



