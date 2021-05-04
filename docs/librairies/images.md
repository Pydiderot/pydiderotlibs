# Images

## A propos

Cette librairie a été conçue pour l'enseignement de la [SNT](https://eduscol.education.fr/1670/programmes-et-ressources-en-sciences-numeriques-et-technologie-voie-gt).

Elle permet de manipuler des images assez facilement.

L'objectif est de permettre aux élèves d'accéder au contenu des pixels d'une image numérique (enregistrée dans le même répertoire que le fichier python sur 
lequel on travaille), de modifier les valeurs des composantes des pixels et finalement de rendre possible l'exécution de petits scripts de manipulation d'images.

La librairie est basée sur [PIL](https://he-arc.github.io/livre-python/pillow/index.html) et utilise les noms de couleurs de pydiderotlibs, comme détaillé
dans la section suivante.

Vous pouvez, par exemple, l'utiliser pour créer un script convertissant une image couleurs en niveaux de gris ou encore un script générant le négatif d'une image donnée.

 
.. _couleur:
.. mdinclude:: ../couleurs.md


## Utilisation

Voici quelques exemples : 

```python
# On importe la librairie
from pydiderotlibs.images import *

# On affiche dans la console la composante bleue du pixel (100,200,300) (le résultat est '300')
print(bleu((100,200,300)))

# On crée une version de l'image ``essai.png`` qui sera manipulable par Python et qui sera stockée sous le nom de variable ``img``
img = creer_image('essai.png')

# On affiche la définition de l'image, puis sa largeur.
print(definition_image(img))
print(largeur_image(img))

# On affiche l'image dans la visionneuse du système d'exploitation
afficher_image(img)

# On affiche le pixel de composantes RVB (100,100,100) (c'est un pixel de couleur grise)
afficher_pixel((100, 100, 100))

# On affiche les trois composantes RVB du pixel situé juste à droite du pixel de coordonnées (100,100). 
# Ce pixel voisin à pour coordonnées (101,100)
print(pixel_voisin((100, 100), img))

# On affiche les 3 composantes RVB du pixel de coordonnées (10,10)
print(copier_pixel(img, (10, 10)))

# On remplace le pixel de coordonnées (10,10) par un pixel noir (0,0,0)
coller_pixel(img, (10, 10), (0, 0, 0))

# On définit une fonction qui convertit un pixel donné en pixel "niveau de gris"
def gris(pixel):
    g = int((rouge(pixel) + vert(pixel) + bleu(pixel)) / 3)
    return (g, g, g)
    
# On applique la fonction ``gris()`` précédente aux pixels de l'image ``img`` dont les coordonnées sont situées dans le rectangle de diagonale '(100,300)--(200,500)'
changer_les_pixels(img,gris,100,200,300,500)

```

## Documentation

.. automodule:: pydiderotlibs.images
    :members:
    :member-order: bysource

.. eof
