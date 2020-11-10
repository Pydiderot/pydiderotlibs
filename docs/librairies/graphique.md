# Graphique

## A propos

Cette librairie permet l'affichage d'une fenêtre graphique dynamique et fournie des fonctions permettant d'y afficher des objets géométriques simples (point, cercle, segment, vecteur, rectangle).

Basée sur [pygame](https://www.pygame.org/wiki/about), vous pouvez également récupérer les événements clavier ou souris pour interagir avec l'utilisateur.

Vous pouvez, par exemple, l'utiliser pour construire un jeux de type [pong](https://fr.wikipedia.org/wiki/Pong).


## Utilisation

Voici un exemple qui affiche une fenêtre graphique traversée en diagonale par un point.

```python
# On importe la librairie
from pydiderotlibs.graphique import *
# Nous aurons également de la librairie time
from time import *

# On initialise les coordonnées du point au coin haut gauche de la fenêtre
x = 0
y = 0

# On créé la fenêtre graphique
creer_fenetre()

# Boucle principale
while 1:
    # Il est important d’appeler la fonction demande_evenements() qui gère la fermeture de la fenêtre
    demande_evenements()

    # Trace un cercle au coordonnées (x,y)
    cercle(x, y)
    # Attend un dixième de secondes
    sleep(0.1)
    # Efface le cercle
    cercle(x, y, couleur='blanc')
    # Ajoute le vecteur vitesse aux coordonnées du point
    x += 1
    y += 1
```
.. note::
  Il est important d’appeler la fonction `demande_evenements() <#graphique.demande_evenements>`_ qui gère la fermeture de la fenêtre

.. raw:: html

    <video width="604" height="525" autoplay loop>
    <source src="../_static/graphique.webm" type="video/mp4">
    Your browser does not support the video tag.
    </video>


## Événements
La fonction [demande_evenements()](#graphique.demande_evenements) permet une gestion simplifiée des entrées clavier et souris de l'utilisateur.

Elle retourne un dictionnaire contenant les touches pressées, les clics et déplacement souris.

### Touches clavier

 - Les touches spéciales sont présentes sous la forme: `'haut'`, `'bas'`, `'gauche'`, `'droite'` et `'espace'`
 - Les touches alphanumériques sont présentes sous leur forme ascii: `'a'`, `'b'`,... `';'`,...

Vous pouvez par exemple tester si les touches `'haut'` et `'a'` sont pressées :
```python
# On importe la librairie graphique
from pydiderotlibs.graphique import *
# On créé la fenêtre graphique
creer_fenetre()

# Boucle principale
while 1:

    evenements = demande_evenements()
    if 'haut' in evenements:
        print('la touche "haut" est enfoncée')
    if 'a' in evenements:
        print('la touche "a" est enfoncée')
```    

### Et la souris?
 - Un clic sur le bouton gauche de la souris sera présent sous la forme `'clic'`. Sa valeur contiendra les coordonnées de la souris au moment du clic.
 - Un déplacement de souris sera présent sous la forme `'souris'`. Sa valeur contiendra les coordonnées de la souris après le déplacement.

Vous pouvez par exemple tester si un utilisateur bouge la souris ou clique et récupérer les coordonnées de la souris:
```python
# On importe les librairie et time
from pydiderotlibs.graphique import *
# On créé la fenêtre graphique
creer_fenetre()

# Boucle principale
while 1:
    evenements = demande_evenements()

    if 'souris' in evenements:
        # ici evenements['souris'] est une liste [x, y]
        print("Nouvelle abscisse : " + str(evenements['souris'][0]))

    if 'clic' in evenements:
        # ici evenements['clic'] est une liste [x, y]
        print('clic aux coordonées ' + str(evenements['clic']))
```

.. _autorefresh:
## Rafraîchissement automatique
Par défaut, cette librairie rafraîchit automatiquement l'affichage a chaque modification de la fenêtre: création de point, de cercle, ...

Cela simplifie l'utilisation dans des cas simples mais, si vous souhaitez créer un programme complexe qui modifie fréquemment la fenêtre graphique, cela va créer des scintillements désagréables et ralentir le programme.

Vous pouvez désactiver ce rafraîchissement automatique en passant l'argument `autorefresh=fasle` à la fonction `fenetre()`. Il faudra alors appeler la fonction `rafraichir()` lorsque vous voulez rafraîchir l'affichage de la fenêtre graphique.

Notre exemple de départ devient alors:

```python
# On importe la librairie
from pydiderotlibs.graphique import *
# Nous aurons également de la librairie time
from time import *

# On initialise les coordonnées du point au coin haut gauche de la fenêtre
x = 0
y = 0

# On créé la fenêtre graphique en passant l'argument autorefresh=false
creer_fenetre(autorefresh=False)

# Boucle principale
while 1:
    # Il est important d’appeler la fonction demande_evenements() qui gère la fermeture de la fenêtre
    demande_evenements()

    # Trace un cercle au coordonnées (x,y)
    trace_cercle(x, y)
    # Attend un dixième de secondes
    sleep(0.1)
    # Efface le cercle
    trace_cercle(x, y, couleur='blanc')
    # Ajoute le vecteur vitesse aux coordonnées du point
    x += 1
    y += 1
    # On actualise la fenêtre graphique
    rafraichir()
```

.. _couleur:
.. mdinclude:: ../couleurs.md

## Documentation


.. automodule:: pydiderotlibs.graphique
    :members:
    :member-order: bysource

.. eof
