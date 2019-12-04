#ces fonctions sont importées dans "graphique.py"

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

