#ces fonctions sont importées dans "graphique.py"

def intersect(a1, b1, a2, b2):
    """ 
    Détection d'intersection entre deux intervalles : renvoie `false` si l'intersection de [a1;a2] et [b1;b2] est vide.
    
    Arguments:
        a1 et b1 (float): bornes du premier intervalle
        a2 et b2 (float): bornes du second intervalle
    """
    if b1 < a2 or b2 < a1:
        return False
    else:
        return True
    
def collision(x1, y1, w1, h1, x2, y2, w2, h2):
    """
    Détection d'intersection entre deux rectangles : 
    renvoie `true` si les deux rectangles se rencontrent
    
    Arguments:
        x1 et y1 (float): coordonnées du centre du premier rectangle
        w1 et h1 (float): largeur et hauteur du premier rectangle
        x2 et y2 (float): coordonnées du centre du second rectangle
        w2 et h2 (float): largeur et hauteur du second rectangle
        
    Alias:
        collisionRR()
    """
    if( intersect(x1 - w1 / 2, x1 + w1 / 2, x2 - w2 / 2, x2 + w2 / 2) and intersect(y1 - h1 / 2, y1 + h1 / 2, y2 - h2 / 2, y2 + h2 / 2) ):
        return True
    else:
        return False

def collisionRR(x1, y1, w1, h1, x2, y2, w2, h2):
    collision(x1, y1, w1, h1, x2, y2, w2, h2)

def collisionRC(x1, y1, w, h, x2, y2, r):
    """
    Détection d'intersection entre un rectangle et un cercle : 
    renvoie `true` si les deux objets se rencontrent
    
    Arguments:
        x1 et y1 (float): coordonnées du centre du rectangle
        w et h (float): largeur et hauteur du rectangle
        x2 et y2 (float): coordonnées du centre du cercle
        r (float): rayon du cercle
    
    """
    if x2 > x1 + w / 2 + r:
        return False #le cercle est trop à droite du rectangle
    elif x2 < x1 - w / 2 - r:
        return False #il est trop à gauche du rectangle
    elif y2 > y1 + h / 2 + r:
        return False #cercle trop haut
    elif y2 < y1 - h / 2 - r:
        return False #cercle trop haut
    elif (x1 + w / 2 - x2) ** 2 + (y1 + h / 2 - y2) ** 2 > r ** 2:
        return False #cercle en haut à droite du rectangle, mais un peu trop loin du coin haut-droite
    elif (x1 - w / 2 - x2) ** 2 + (y1 + h / 2 - y2) ** 2 > r ** 2:
        return False #cercle en haut à gauche du rectangle, mais un peu trop loin du coin haut-gauche
    elif (x1 + w / 2 - x2) ** 2 + (y1 - h / 2 - y2) ** 2 > r ** 2:
        return False #cercle en bas à droite du rectangle, mais un peu trop loin du coin bas-droite
    elif (x1 - w / 2 - x2) ** 2 + (y1 - h / 2 - y2) ** 2 > r ** 2:
        return False #cercle en bas à gauche du rectangle, mais un peu trop loin du coin bas-gauche
    else:
        return True
