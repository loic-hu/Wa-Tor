"""Point d'entrée de la simulation Wa-Tor.
 
Ce script crée la planète à partir de la configuration, la peuple de
créatures, puis fait tourner la simulation en boucle. Un graphique en direct
affiche l'évolution des populations à chaque chronon.
 
La simulation s'arrête lorsque la fenêtre du graphique est fermée.
 
Dépendances:
    - matplotlib (affichage du graphique)
    - world.planet.Planet (grille et créatures)
    - graph.graph.Graph (graphique en direct)
    - config (paramètres de l'environnement et du graphique)
"""

import matplotlib.pyplot as plt
import os

from world.planet import Planet

from graph.graph import Graph

# env_configx : paramètres de la planète / graph_config : paramètres du graphique
# x = numéro de la configuration
from config import env_config1 as env_cfg, graph_config as graph_cfg

# Efface la console avant de commencer
os.system('clear')

# Création de la planète : dimensions, poids de probabilité et types de contenu
world = Planet(env_cfg.x, env_cfg.y, env_cfg.weight, env_cfg.types)
# Remplissage aléatoire de la grille (poissons, requins, cases vides...)
world.populate()
# Affichage de l'état initial dans la console
world.show_planet()

# Création du graphique en direct : nombre de points conservés et pause entre deux mises à jour
graph = Graph(world, graph_cfg.max_points, graph_cfg.pause)

# Boucle principale : s'arrête si on ferme la fenêtre du graphique
while plt.fignum_exists(graph.fig.number):  
    os.system('clear')
    # Fait avancer la simulation d'un chronon (déplacements, reproduction, repas...)
    world.update_planet_V2()
    # Incrémente le compteur de chronons
    world.chronon += 1
    # Affiche le numéro du chronon courant
    print(world.chronon)
    # Compte les créatures et rafraîchit les courbes (inclut la pause)
    graph.update()
