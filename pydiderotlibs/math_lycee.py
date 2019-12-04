# -*- coding: utf-8 -*-
#
# Version 1.1
"""
Module avec les fonctions de la classe de Seconde 2018 pour le lycée diderot (marseille).
On prend comme fichier de départ le module de l'irem d'Amiens
http://download.tuxfamily.org/amienspython/lycee.py
Licence http://www.cecill.info/
"""


import math

from .arithmetique import *
from .trigo import *
from .stats_proba import *
from .fonctions_usuelles import *
from .vecteurs import *
from .chaines import *
from .listes import *

print("""
Merci d'utiliser la librairie lycee du module pydiderot.\n
N'hésitez pas à consulter la documentation en ligne:\n
https://pydiderotlibs.rtfd.io/librairies/lycee.html
""")

pi = math.pi


def repeter(f, n):
    """ 
    Appelle `n` fois la fonction ``f``.

    Alias disponible: ``repeat()``
    """
    for i in range(n):
        f()

def repeat(f, n):
    repeter(f, n)
    
def intersect(a1,b1,a2,b2):
    """ 
    Détection d'intersection entre deux intervalles : renvoie `false` si l'intersection de [a1;a2] et [b1;b2] est vide.
    
    Arguments:
        a1 et b1 (float): bornes du premier intervalle
        a2 et b2 (float): bornes du second intervalle
    """
    if b1<a2 or b2<a1:
        return False
    else:
        return True
    
def collision(x1,y1,w1,h1,x2,y2,w2,h2):
    """
    Détection d'intersection entre deux rectangles : 
    renvoie `true` si les deux rectangles se rencontrent
    
    Arguments:
        x1 et y1 (float): coordonnées du centre du premier rectangle
        w1 et h1 (float): largeur et hauteur du premier rectangle
        x2 et y2 (float): coordonnées du centre du second rectangle
        w2 et h2 (float): largeur et hauteur du second rectangle
    """
    if( intersect(x1-w1/2,x1+w1/2,x2-w2/2,x2+w2/2) and intersect(y1-h1/2,y1+h1/2,y2-h2/2,y2+h2/2) ):
        return True
    else:
        return False
