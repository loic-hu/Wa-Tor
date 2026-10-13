import pygame
from planet import Planet
from fish import Fish
from shark import Shark
from config import env_config1 as env_cfg

# configuration de la fenêtre
pygame.init()
size_case = 20 #taille d'une case en pixels

width_matrice = env_cfg.x
height_matrice = env_cfg.y

#creation de la fenêtre
window = pygame.display.set_mode((width_matrice * size_case, height_matrice * size_case))
pygame.display.set_caption("Wa-Tor")
clock = pygame.time.Clock()

case_water = (20, 20, 50)  # Bleu très foncé
case_fish = (0, 200, 0)  # Vert 
case_shark = (200, 0, 0)  # Rouge

running = True

world = Planet(env_cfg.x, env_cfg.y, env_cfg.weight)
world.populate()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    world.update_planet()
    for row in  range(height_matrice):

        for column in range(width_matrice):

            creature = world.matrice[row][column]

            if isinstance(creature, Shark):
                pygame.draw.rect(window, case_shark, (column * size_case, row * size_case, size_case, size_case))
            elif isinstance(creature, Fish):
                pygame.draw.rect(window, case_fish, (column * size_case, row * size_case, size_case, size_case))
            else:
                pygame.draw.rect(window, case_water, (column * size_case, row * size_case, size_case, size_case))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()

