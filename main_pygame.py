import pygame
from world.planet import Planet
from world.fish import Fish
from world.shark import Shark
from world.flying_fish import Flying_fish
from world.super_fish import Super_fish
from config import env_config1 as env_cfg

# Configuration de la fenêtre
pygame.init()
size_case = 20  #taille d'une case en pixels

# On récupère la taille de la matrice via la config
width_matrice = env_cfg.x
height_matrice = env_cfg.y

# Création de la fenêtre, sa dimension, son nom puis le système temporel
window = pygame.display.set_mode((width_matrice * size_case, height_matrice * size_case))
pygame.display.set_caption("Wa-Tor")
clock = pygame.time.Clock()

# Attribution de chaque case couleur pour chaque type d'entité
case_water = (0, 119, 190)  # Bleu ciel
case_fish = (0, 200, 0)  # Vert 
case_shark = (200, 0, 0)  # Rouge
case_flying_fish = (255, 165, 0) #Orange
case_super_fish = (255, 255, 0) #Jaune


running = True

# Création du monde de la simulation, basé sur la config
world = Planet(env_cfg.x, env_cfg.y, env_cfg.weight, env_cfg.types)
# Initialisation de la population de ce monde
world.populate()

# Tant que l'app tourne
while running:

    # on capture les events, si l'un est quit, on stoppe l'app
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # On lance l'update de l'objet monde
    world.update_planet_V2()

    # Pour chaque ligne de la matrice
    for row in  range(height_matrice):

        # Pour chaque colonne de la matrice
        for column in range(width_matrice):

            # On récupère la créature stockée
            creature = world.matrice[row][column]

            # On affiche le carré de couleur correspondant selon le type de la créature
            if isinstance(creature, Shark):
                pygame.draw.rect(window, case_shark, (column * size_case, row * size_case, size_case, size_case))
            elif isinstance(creature, Flying_fish):
                pygame.draw.rect(window, case_flying_fish, (column * size_case, row * size_case, size_case, size_case))
            elif isinstance(creature, Super_fish):
                pygame.draw.rect(window, case_super_fish, (column * size_case, row * size_case, size_case, size_case))
            elif isinstance(creature, Fish):
                pygame.draw.rect(window, case_fish, (column * size_case, row * size_case, size_case, size_case))
            else:
                pygame.draw.rect(window, case_water, (column * size_case, row * size_case, size_case, size_case))

    # Refresh le display
    pygame.display.flip()
    # Timer des frames
    clock.tick(5)

# On quitte pygame une fois que l'app ne tourne plus
pygame.quit()

