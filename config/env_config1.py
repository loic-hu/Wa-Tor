"""Configuration 1 de la simulation Wa-Tor.

Ce module regroupe les paramètres de la planète et des différentes espèces.
Modifier ces valeurs permet de changer le comportement de la simulation sans
toucher au reste du code.

Planet:
    x, y (int): Dimensions de la grille (60 colonnes x 60 lignes).
    types (list): Contenus possibles d'une case : ``"fish"``, ``"shark"``,
        ``"flying_fish"``, ``"super_fish"`` ou ``None`` (case vide).
    weight (list[int]): Poids de probabilité associés à chaque élément de
        ``types``, dans le même ordre, utilisés lors du peuplement initial.
        Ici : 99 poissons, 1 requin, aucune autre espèce, aucune case vide.

Configurations des espèces (dictionnaires):
    fish_config:
        - gestation_period (int): Nombre de chronons avant qu'un poisson puisse se reproduire (4).
    shark_config:
        - gestation_period (int): Nombre de chronons avant qu'un requin puisse se reproduire (8).
        - energy (int): Énergie initiale d'un requin (6).
        - max_energy (int): Énergie maximale qu'un requin peut accumuler (12).
        - energy_regain (int): Énergie récupérée par le requin lorsqu'il mange un poisson (6).
    flying_fish_config:
        - gestation_period (int): Nombre de chronons avant reproduction (4).
    super_fish_config:
        - gestation_period (int): Nombre de chronons avant reproduction (4).
"""

# planet
x, y = 60,60
weight = [99,       1,          0,          0,          0]
types = ["fish", "shark", "flying_fish", "super_fish", None]


# fish
fish_config = {
    "gestation_period" : 4
}

# shark
shark_config = {
    "gestation_period" : 8
    ,"energy" : 6
    ,"max_energy" : 12
    ,"energy_regain" : 6
}

# flying_fish
flying_fish_config = {
    "gestation_period" : 4
}

# super_fish
super_fish_config = {
    "gestation_period" : 4
}


