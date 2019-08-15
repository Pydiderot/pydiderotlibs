# -*- coding: utf-8 -*-
#

# import des librairies
import pygame
import sys
import math

from time import sleep #pour rendre transparent côté élève l'utilisation de "sleep"
from .couleurs import rgb


def creer_fenetre(largeur=200, hauteur=300, titre="Fenetre graphique"):
    """
    Crée et affiche une fenêtre graphique.

    Arguments:
        largeur (int, optionel): Largeur de la fenetre en pixels (``200`` par défaut)
        hauteur (int, optionel): Hauteur de la fenetre en pixels (``300`` par défaut)
        titre (str, optionel): Titre de la fenetre (``Fenetre graphique`` par défaut)
    """

    pygame.init()
    global fenetre
    fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption(titre)
    # active la répétition des touches
    pygame.key.set_repeat(1)
    fenetre.fill(rgb('blanc'))
    pygame.display.update()



def demande_evenements():
    """
    Récupère les évenements pygame gère la fermeture de la fenetre et retourne les évenements formatés.

    Renvoie un dictionaire d'évenements formaté comme suit:
    ``{'touche1': None, 'touche2':None, 'souris': [x,y], 'click': [x,y]}``

    Les valeurs ``None`` pour les touches peuvent surprendre mais il est nécéssaire d'utiliser un dictionaire pour avoir les coordonnées
    éventuelles de la souris lors d'un click par exemple. Pour les touches clavier, l'importance est la présence de la cléf et la valeur associé est donc ``None``.

    - Les caractères alphanumériques sont encodés en ascii (``'a'``, ``'n'``, ``';'``) et, si présent, leur valeur est ``None``.
    - les touches spéciales ont les clefs ``'espace'``, ``'haut'``, ``'bas'``, ``'droite'``, ``'gauche'`` et, si présent, leur valeur est ``None``.
    - Un clic avec le bouton gauche de la souris ajoute une clef ``'clic'``. Sa valeur est une liste ``[x, y]`` des coordonées de la souris.
    - Un déplacement de la souris ajoute une clef ``'souris'``. Sa valeur est une liste ``[x, y]`` des coordonées de la souris.

    """

    # Initialisation du dictionnaire de sortie
    evenements = {}

    touches_speciales = {
        'haut': pygame.K_UP,
        'bas': pygame.K_DOWN,
        'gauche': pygame.K_LEFT,
        'droite': pygame.K_RIGHT,
        'espace': pygame.K_SPACE
    }

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            for c, v in touches_speciales.items():
                # On parcourt le dictionnaire par clef, valeur
                # Par exmple c = 'haut' et v = pygame.K_UP
                if event.key == v:
                    # L'important est simplement d'avoir la clef dans le dictionnaire.
                    # La valeur n'a pas d'importance et est donc None
                    evenements[c] = None

            # Si l'unicode peut être convertit en ascii, on ajoute la clef au dictionnaire sous unicode
            if event.unicode.encode('ascii', 'ignore'):
                evenements[event.unicode] = None

        # Gestion des evenements souris
        elif event.type == pygame.MOUSEMOTION:
            evenements['souris'] = list(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            evenements['clic'] = list(event.pos)

    return evenements


def trace_cercle(x, y, rayon=5, epaisseur=0, couleur='bleu'):
    """
    Trace un cercle dans la fenetre graphique.

    Arguments:
        x (int): Abscisse du centre du cercle
        y (int): Ordonnée du centre du cercle
        rayon (int, optionel): Rayon du cercle (5 par défaut)
        epaisseur (int, optionel): Epaisseur du cercle (``0`` par défaut). Si ``0``, le cercle sera rempli et apparaitra comme un disque.
        couleur (:ref:`couleur <couleur>`, optionnel): Couleur du cercle (bleu par défaut)
    """
    couleur = rgb(couleur)
    pygame.draw.circle(fenetre, couleur, (x,y), rayon, epaisseur)
    pygame.display.update()


def trace_point(x, y, couleur='bleu'):
    """
    Trace un point dans la fenetre graphique.

    Arguments:
        x (int): Abscisse du point
        y (int): Ordonnée du point
        couleur (:ref:`couleur <couleur>`, optionnel): Couleur du point (bleu par défaut)
    """
    couleur = rgb(couleur)
    pygame.draw.circle(fenetre, couleur, (x,y), 1, 0)
    pygame.display.update()


def trace_rectangle(x, y, largeur, hauteur, couleur='bleu', epaisseur=1):
    """
    Trace un rectangle horizontal dans la fenetre graphique .

    Le sommet haut-gauche à pour coordonées ``(x,y)``, la ``largeur`` est la taille en abscisse
    et la ``hauteur`` la taille en ordonnée.

    Arguments:
        x (int): abscisse du sommet haut gauche du rectangle
        y (int): ordonnée du sommet haut gauche du rectangle
        largeur (int): taille du rectangle sur l'axe des abscisses
        hauteur (int): taille du rectangle sur l'axe des ordonnées
        couleur (:ref:`couleur <couleur>`, optionnel): Couleur du rectangle (``bleu`` par défaut)
        epaisseur (int, optionnel): Epaisseur des cotés du rectangle (``1`` par défaut). Si ``0``, le rectangle est rempli.

    """
    couleur = rgb(couleur)
    pygame.draw.rect(fenetre, couleur, (x, y, largeur, hauteur), epaisseur)
    pygame.display.update()


def trace_segment(x1, y1, x2, y2, couleur='bleu', epaisseur=1):
    """
    Trace un segment entre les points de coordonées ``(x1, y1)`` et ``(x2, y2)``.

    Arguments:
        x1 (int): abscisse de la première extremité du segment
        y1 (int): ordonnée de la première extremité du segment
        x2 (int): abscisse de la deuxieme extrémité du segment
        y2 (int): ordonnée de la deuxieme extrémité du segment
        couleur (:ref:`couleur <couleur>`, optionel): Couleur du segment (``bleu`` par défaut)
        epaisseur (int, optionel): Epaisseur du segment (``1`` par défaut)
    """
    couleur = rgb(couleur)
    pygame.draw.lines(fenetre, couleur, False, [(x1, y1), (x2, y2)], epaisseur)
    pygame.display.update()


def trace_vecteur(x, y, v, couleur='rouge', epaisseur=2):
    """
    Trace la représentation du vecteur ``v`` à partir du point d'origine ``(x, y)``.

    Arguments:
        x (int): abscisse du point d'origine de la représentation du vecteur
        y (int): ordonnée du point d'origine de la représentation du vecteur
        v (list): Coordonnées de la deuxieme extrémité du segment
        couleur (:ref:`couleur <couleur>`, optionel): Couleur du segment (``rouge`` par défaut)
        epaisseur (int, optionel): Epaisseur du segment (``1`` par défaut)
    """

    couleur = rgb(couleur)

    trace_segment(x, y, x+v[0], y+v[1], couleur, epaisseur)
    w1[0] = -.3 * math.cos(15 * math.pi / 180) * v[0] + .3 * math.sin(15 * math.pi/180) * (-v[1])
    w1[1] = -.3 * math.cos(15 * math.pi / 180) * v[1] + .3 * math.sin(15 * math.pi/180) * v[0]
    w2[0] = -.3 * math.cos(15 * math.pi / 180) * v[0] - .3 * math.sin(15 * math.pi/180) * (-v[1])
    w2[1] = -.3 * math.cos(15 * math.pi / 180) * v[1] - .3 * math.sin(15 * math.pi/180) * v[0]
    pygame.draw.polygon(
        fenetre,
        couleur,
        [
            (x + v[0], y + v[1]),
            (x + v[0] + w1[0], y + v[1] + w1[1]),
            (x + v[0] + w2[0], y + v[1] + w2[1]),
            (x + v[0], y + [1])
        ],
        0
    )
    pygame.display.update()

def trace_image(x, y, nom, largeur=50, hauteur=50):
    """
    Trace une image dans la fenetre graphique.

    Arguments:
        x (int): Abscisse du centre de l'image
        y (int): Ordonnée du centre de l'image
        largeur (int, optionel): Largeur de l'image (50 par défaut)
        hauteur (int, optionel): Hauteur de l'image (50 par défaut)
    """
    image = pygame.transform.scale(pygame.image.load(nom).convert_alpha(), (largeur, hauteur))
    fenetre.blit(image, (int(x-largeur/2),int(y-hauteur/2)))
    pygame.display.update()

def explosion(x,y,r=10,couleur='vert',c=0.5,n=10):
    '''
    trace un polygône régulier étoilé à 2n côté,
    coloré dans la couleur indiquée,
    centré en (x,y) (x et y sont des entiers),
    de rayon extérieur r,
    et tel que le rayon intérieur est égal à c*r
    (pour c=0, le polygône est réduit à n rayons du cencle de rayon r
    pour c=1, c'est un polygône régulier à 2n côtés)
    '''
    couleur = rgb(couleur)
    pointlist=[]
    theta=2*math.pi/n
    for k in range(n):
        pointlist.append((x+r*math.cos(k*theta),y+r*math.sin(k*theta)))
        pointlist.append((x+c*r*math.cos((k+1/2)*theta),y+c*r*math.sin((k+1/2)*theta)))
    pointlist.append((x+r,y))
    pygame.draw.polygon(fenetre, couleur, pointlist)
    pygame.display.update()

def axes(color='noir'):
    '''
    dessine les axes de coordonnées pour une meilleure compréhension par les élèves
    '''
    couleur = rgb(color)
    ymax=pygame.display.Info().current_h
    xmax=pygame.display.Info().current_w
    epaisseur=2
    pygame.draw.lines(fenetre, couleur, False, [(5, 0), (5, ymax)], epaisseur)
    pygame.draw.lines(fenetre, couleur, False, [(0, ymax-5), (5, ymax)], epaisseur)
    pygame.draw.lines(fenetre, couleur, False, [(10, ymax-5), (5, ymax)], epaisseur)
    pygame.draw.lines(fenetre, couleur, False, [(0, 5), (xmax, 5)], epaisseur)
    pygame.draw.lines(fenetre, couleur, False, [(xmax-5, 0), (xmax, 5)], epaisseur)
    pygame.draw.lines(fenetre, couleur, False, [(xmax-5, 10), (xmax, 5)], epaisseur)
    font=pygame.font.Font(None, 24,bold=False,italic=False)
    text=font.render(str(ymax),1,couleur)
    fenetre.blit(text, (15, ymax-30))
    text=font.render("y",1,couleur)
    fenetre.blit(text, (15, ymax-17))
    text=font.render(str(xmax),1,couleur)
    fenetre.blit(text, (xmax-35, 10))
    text=font.render("x",1,couleur)
    fenetre.blit(text, (xmax-15, 22))
    text=font.render("0",1,couleur)
    fenetre.blit(text, (10, 10))
    pygame.display.update()
