import pyglet
from pyglet.window import key, mouse
from pyglet import shapes


class Fenetre(pyglet.window.Window):
    def __init__(self,
                 hauteur=600,
                 largeur=800,
                 plein_ecran=False,
                 redimentionable=True):

        super(Fenetre, self).__init__(
            width=largeur,
            height=hauteur,
            resizable=redimentionable,
            fullscreen=plein_ecran)

        #Evenements
        self.events = {}
        # Elements du graphique
        # Pour l'instant je propose: On ajoute les éléments dans fenetre.elements.
        # Une fonction efface videra fenetre.elements
        self.batch = pyglet.graphics.Batch()
        self.elements = []
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        pyglet.clock.schedule_interval(self.update, 0.1)

    def on_draw(self):
        self.clear()
        self.batch.draw()

    def efface(self):
        self.elements = []

    # Du brouillon pour la gestion des evenements
    def on_key_press(self, symbol, modifiers):
        # ferme la fenetre si on appui sur la touche échape
        if symbol == key.ESCAPE:
            self.close()


    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            print('The left mouse button was pressed.')

    def update(self, dt):
        for touche, state in self.keys.items():
            if state:
                print(key.symbol_string(touche))
        self.clear()
        self.batch.draw()



# Initialise l'objet fenetre
fenetre = Fenetre()

# première fonction pour tester
def cercle(x, y, couleur='bleu', rayon=25, epaisseur=0):
    """
    Trace un cercle dans la fenetre graphique.

    Alias: ``circle()``, ``trace_cercle()``

    Arguments:
        x (int): Abscisse du centre du cercle
        y (int): Ordonnée du centre du cercle
        rayon (int, optionnel): Rayon du cercle (25 par défaut)
        epaisseur (int, optionnel): Epaisseur du cercle (``0`` par défaut). Si ``0``, le cercle sera rempli et apparaitra comme un disque.
        couleur (:ref:`couleur <couleur>`, optionnel): Couleur du cercle (bleu par défaut)
    """
    global fenetre
    fenetre.elements.append(shapes.Circle(700, 150, 100, color=(50, 225, 30), batch=fenetre.batch))


cercle(700,410)

pyglet.app.run()
