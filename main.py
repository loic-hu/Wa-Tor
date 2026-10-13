import matplotlib.pyplot as plt
import os

from planet import Planet

from graph import Graph
from config import env_config1 as env_cfg, graph_config as graph_cfg


os.system('clear')

world = Planet(env_cfg.x, env_cfg.y, env_cfg.weight)
world.populate()
world.show_planet()

graph = Graph(world, graph_cfg.max_points, graph_cfg.pause)

# s'arrête si on ferme la fenêtre du graphique
while plt.fignum_exists(graph.fig.number):  
    os.system('clear')
    world.update_planet_V2()
    world.chronon += 1
    print(world.chronon)
    graph.update()
