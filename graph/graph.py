from collections import Counter, deque

from matplotlib import pyplot as plt, colors as mcolors


class Graph:
    """Graphique en direct de l'évolution des populations de poissons et de requins.

    La classe gère la fenêtre matplotlib, l'historique des effectifs et le
    rafraîchissement des courbes à chaque chronon.

    Attributes:
        world (Planet): Planète dont on suit les populations.
        pause (float): Durée de la pause (en secondes) entre deux rafraîchissements.
        fish_historical (deque[int]): Effectifs de poissons des derniers chronons.
        shark_historical (deque[int]): Effectifs de requins des derniers chronons.
        fig (Figure): Fenêtre matplotlib.
        ax (Axes): Zone de dessin des courbes.
        fish_ligne (Line2D): Courbe des poissons.
        shark_ligne (Line2D): Courbe des requins.
    """

    def __init__(self, world, max_points, pause):
        """Crée la fenêtre du graphique et ses deux courbes vides.

        Args:
            world (Planet): Planète dont on suit les populations.
            max_points (int): Nombre maximal de chronons conservés dans
                l'historique. Au-delà, les plus anciens sont supprimés.
            pause (float): Pause (en secondes) entre deux rafraîchissements.
        """
        # On garde une référence vers la planète pour pouvoir compter ses créatures
        self.world = world
        self.pause = pause

        # deque(maxlen=N) : liste qui supprime automatiquement son plus ancien
        # élément quand elle dépasse N éléments (fenêtre glissante)
        self.fish_historical = deque(maxlen=max_points)
        self.shark_historical = deque(maxlen=max_points)
        self.flying_fish_historical = deque(maxlen=max_points)
        self.super_fish_historical = deque(maxlen=max_points)

        # Mode interactif : la fenêtre se met à jour sans bloquer le programme
        plt.ion()

        # fig = la fenêtre entière, ax = la zone de dessin à l'intérieur
        self.fig, self.ax = plt.subplots()

        # Création de deux courbes vides (remplies plus tard par update()).
        # La virgule après le nom extrait la courbe de la liste renvoyée par plot()
        self.fish_ligne, = self.ax.plot([], [], label="Fishs", color="lime")
        self.shark_ligne, = self.ax.plot([], [], label="Sharks", color="tab:red")
        self.flying_fish_ligne, = self.ax.plot([], [], label="Flying fishs", color="darkgreen")
        self.super_fish_ligne, = self.ax.plot([], [], label="Super fishs", color="tab:orange")

        # Titres des axes et du graphique
        self.ax.set_xlabel("Chronon")
        self.ax.set_ylabel("Population")
        self.ax.set_title("Population trends")

        # Légende construite à partir des "label" donnés aux courbes
        self.ax.legend()

    def is_open(self):
        """Indique si la fenêtre du graphique est toujours ouverte.

        Returns:
            bool: ``True`` si la fenêtre est ouverte, ``False`` si elle a été fermée.
        """
        # Renvoie False dès que l'utilisateur ferme la fenêtre
        return plt.fignum_exists(self.fig.number)

    def update(self):
        """Compte les créatures, met à jour l'historique et rafraîchit les courbes."""
        # Compte le nombre d'objets de chaque classe : {"Fish": ..., "Shark": ... "Flying_fish": ... "Super_fish": ...}
        count = Counter(type(c).__name__ for c in self.world.get_all_creatures())

        # Ajoute les effectifs du chronon courant à l'historique
        # (get(..., 0) évite une erreur si un type a totalement disparu)
        self.fish_historical.append(count.get("Fish", 0))
        self.shark_historical.append(count.get("Shark", 0))
        self.flying_fish_historical.append(count.get("Flying_fish", 0))
        self.super_fish_historical.append(count.get("Super_fish", 0))

        # Met à jour les points des courbes : x = numéro du point, y = effectif
        self.fish_ligne.set_data(range(len(self.fish_historical)), self.fish_historical)
        self.shark_ligne.set_data(range(len(self.shark_historical)), self.shark_historical)
        self.flying_fish_ligne.set_data(range(len(self.flying_fish_historical)), self.flying_fish_historical)
        self.super_fish_ligne.set_data(range(len(self.super_fish_historical)), self.super_fish_historical)

        # Recalcule les limites des axes pour que les courbes restent visibles
        self.ax.relim()
        self.ax.autoscale_view()

        # Attend self.pause secondes ET laisse matplotlib redessiner la fenêtre
        # (remplace time.sleep : sans cet appel, le graphique resterait figé)
        plt.pause(self.pause)  
