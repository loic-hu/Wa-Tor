# Wa-Tor

Ce projet implémente une simulation de l'écosystème **Wa-Tor** en programmation orientée objet. Il s'agit d'une modélisation de vie marine peuplée de poissons et de requins, où chaque entité agit de manière autonome et se déplace en fonction de son environnement.

Wa-Tor est une simulation où deux types d'espèces interagissent dans un environnement fermé :
*   **Les poissons :** Ils se déplacent librement et se reproduisent après un certain nombre de cycles.
*   **Les requins :** Ils chassent les poissons pour survivre, se déplacent et se reproduisent. En l'absence de nourriture, ils perdent de l'énergie et meurent d'inanition.

---

## Table des matières
*   [Fonctionnalités](#fonctionnalités)
*   [Structure du projet](#structure-du-projet)
*   [Installation](#installation)
*   [Utilisation](#utilisation)
*   [Données attendues](#données-attendues)
*   [Limites connues](#limites-knows)
*   [Contributeurs](#contributeurs)

---

## Fonctionnalités

Chaque espèce utilise la programmation orientée objet (POO) pour suivre des règles simples :
*   **Déplacement autonome :** Les poissons et les requins analysent les cases adjacentes pour choisir leur direction.
*   **Reproduction par chronons :** Les espèces génèrent un nouvel individu sur une case libre après un cycle de vie défini.
*   **Système de prédation :** Les requins ciblent prioritairement les poissons proches pour se nourrir.
*   **Gestion de l'énergie :** Les requins consomment de l'énergie à chaque déplacement et meurent si leur jauge tombe à zéro.

---

## Structure du projet

```text
.
├── main.py                 
├──                
│        
│       
├── entities/               
│   ├── animal.py          
│   ├── fish.py            
│   └── shark.py           
└── README.md               
```

---

## Installation

### Prérequis
*   **Python** (version $\ge$ 3.9)

### Clonage du projet
```bash
git clone https://github.com:loic-hu/Wa-Tor.git
cd Wa-Tor
```

### Lancer la simulation
```bash
# Lancement de la version console de base
python main.py
```

---

## Utilisation

La simulation évolue tour par tour (chronons). Pour obtenir un écosystème stable et éviter une extinction précoce de l'une des deux espèces, nous recommandons les critères optimaux suivants :

| Paramètre | Valeur recommandée |
| :--- | :--- |
| **Taille de la grille** | 60 x 60 |
| **Population initiale de requins** | 10% |
| **Population initiale de poissons** | 17% |
| **Temps de reproduction (requins)**| 8 chronons |
| **Temps de reproduction (poissons)**| 4 chronons |
| **Énergie initiale (requins)** | 6 |
| **Énergie maximale (requins)** | 12 |
| **Gain d'énergie par poisson mangé**| 6 |

---

## Données attendues

*   **Rendu visuel :** Grille lisible et mise à jour en temps réel dans le terminal.
*   **Statistiques :** Affichage dynamique du nombre de poissons, de requins et du chronon actuel.
*   **Interface (Bonus 1) :** Interface graphique fonctionnelle et intuitive.
*   **Historique (Bonus 2) :** Graphique d'évolution des populations à la fin de la simulation.

---

## Limites connues

*   **Performances :** Le rafraîchissement de la grille en mode console peut scintiller sur certains terminaux Windows.

---

## Contributeurs

*   Benoit Michaux ([@ArkantHiris](https://github.com))
*   Loïc HURBLAIN ([@loic-hu](https://github.com))
*   Xavier Durieux ([@xav02165](https://github.com))
