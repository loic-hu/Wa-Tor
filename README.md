# Wa-Tor
Ce projet implémente une simulation de l'écosystème Wator en programmation orientée objet. Il s'agit d'une modélisation de vie marine peuplée de poissons et de requins, où chaque entité agit de manière autonome, se déplaçant en fonction d'une liste d'objets environnants. 

Wator est une simulation de vie marine où deux types d'espèces interagissent dans un environnement fermé :

    Les poissons se déplacent librement et se reproduisent après un certain nombre de cycles.

    Les requins chassent les poissons pour survivre, se déplacent, et se reproduisent également après plusieurs cycles. En l'absence de nourriture, les requins meurent aprés un nombre de cycles determinés.

Chaque espèce utilise la programmation orientée objet pour suivre des règles simples :

    Déplacement : Les poissons et requins se déplacent en fonction des objets environnants.

    Reproduction : Les espèces peuvent se reproduire après un certain nombre de cycles.

    Prédation : Les requins chassent les poissons proches. Sans nourriture, ils meurent après plusieurs cycles.


## Fonctionnalités


## Structure du projet

```
.
├── 
├── 
├── 
├── 
├── 
└── README.md
```

## Installation
Prérequis:
    Python (version >= 3.9)
    

Clonage du projet:
    bash git clone https://git@github.com:loic-hu/Wa-Tor.git

Lancer la simulation:
    Version Console python main.py
    


## Utilisation
Simulation d'environnement clos Wa-Tor comprenant deux espèces requins et poissons, et une relation de prédation entre les deux. 

Pour une simulation stable, les critères optimaux sont: 

-Taille de la grille : 60 x 60

-Population de requins: 10%

-Population de poissons: 17%

-Temps de reproduction requins: 8 chronons

-Temps de reproduction poissons : 4 chronons

-Energie (Shark): 6

-Max Energie: 12

-Energie Recovery: 6


## Données attendues
- Grille lisible et mise à jour en temps réel.
- Informations pertinentes affichées (nombre de poissons, requins, chronon actuel).
- (Bonus 1) Interface graphique fonctionnelle et intuitive.
- (Bonus 2) Les fonctionnalités supplémentaires: 


## Limites connues

## Contributeurs

Benoit Michaux (@ArkantHiris)

Loïc HURBLAIN (@loic-hu)

Xavier Durieux (@xav02165)