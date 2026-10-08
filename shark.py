from fish import Fish

class Shark(Fish):

    def __init__(self, x, y, pregnancy, gestation_period, energy, max_energy, energy_regain):

        super().__init__(x, y, pregnancy, gestation_period)
        self.energy = energy
        self.max_energy = max_energy
        self.energy_regain = energy_regain

    def __repr__(self):

        return "S"


    def look_out(self):

        up = ( self.y - 1 ) % 100
        down = ( self.y + 1 ) % 100
        left = ( self.x -1 ) % 100
        right = ( self.x + 1) % 100

        up_case = [self.x, up ]
        down_case = [self.x, down]
        left_case = [left, self.y]
        right_case = [right, self.y]
