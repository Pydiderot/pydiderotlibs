from PIL import Image
from pydiderotlibs.couleurs import *


# Un petit message invitant a lire la doc
print("""
Merci d'utiliser la librairie images du module pydiderotlibs.\n
N'hésitez pas à consulter la documentation en ligne:\n
https://pydiderotlibs.rtfd.io/librairies/images.html
""")

def creer_image(fichier):
    """
    Crée, à partir d'une image enregistrée sur l'ordinateur (dans le même dossier que le fichier python sur lequel on travaille),
    une image manipulable dans le langage python (avec la librairie PIL)
    
    Arguments :
        fichier : nom du fichier enregistré sur l'ordinateur (avec le suffixe : par exemple "monimage.png")
        Le plus simple est d'avoir le fichier de l'image dans le même dossier que le fichier python sur lequel on travaille
        
    """
    nm=fichier.split('.')
    if len(nm)==1:
        fichier+='.png'
    return Image.open(fichier)
    
def definition_image(image):
    """
    Retourne la définition de l'image ``image``.
    C'est une liste de deux nombres.
    Le premier est la largeur (en pixels), le second la hauteur (en pixels).
    
    Par exemple : (200,300)
    
    Arguments :
        img : nom de la variable Python contenant l'image
    """
    return image.size

def largeur_image(image):
    """
    Retourne la largeur de l'image ``image`` (en pixels).
    
    Arguments :
        img : nom de la variable Python contenant l'image
    """
    return image.size[0]

def hauteur_image(image):
    """
    Retourne la hauteur de l'image ``image`` (en pixels).
    
    Arguments :
        img : nom de la variable Python contenant l'image
    """
    return image.size[1]


def afficher_image(image):
    """
    Affiche ``image`` (attention : sans l'enregistrer !).
    
    Arguments :
        img : nom de la variable Python contenant l'image
    """
    image.show()

def afficher_pixel(pixel):
    """
    Affiche une petite image unie, de 10x10 pixels, de la couleur du pixel ``pixel``.
    
    Arguments :
        pixel : un pixel, c'est à dire un triplet de trois nombres entiers entre 0 et 255. Par exemple : (0,0,0) (pixel noir) ou : (255,255,255) (pixel blanc)    
    """
    Image.new('RGB', (10,10), pixel).show()

def rouge(pixel):
    """
    Donne la valeur de rouge du pixel ``pixel``.
    
    Arguments :
        pixel : un pixel, c'est à dire un triplet de trois nombres entiers entre 0 et 255. Par exemple : (0,0,0) (pixel noir) ou : (255,255,255) (pixel blanc)    

    """
    return pixel[0]

def vert(pixel):
    """
    Donne la valeur de vert du pixel ``pixel``.
    
    Arguments :
        pixel : un pixel, c'est à dire un triplet de trois nombres entiers entre 0 et 255. Par exemple : (0,0,0) (pixel noir) ou : (255,255,255) (pixel blanc)    

    """
    return pixel[1]

def bleu(pixel):
    """
    Donne la valeur de bleu du pixel ``pixel``.
    
    Arguments :
        pixel : un pixel, c'est à dire un triplet de trois nombres entiers entre 0 et 255. Par exemple : (0,0,0) (pixel noir) ou : (255,255,255) (pixel blanc)    

    """
    return pixel[2]

def pixel_voisin(image, coord):
    """
    Donne les coordonnées du pixel situé à droite du pixel ``pixel``.
    (S'il n'y a pas de pixel plus à droite car on est au bord de l'image,
    retourne les mêmes coordonnées.)
    
    Arguments :
        coord : coordonnées du pixel
        image : nom de la variable Python contenant l'image

    """
    x,y=coord
    xmax,ymax=image.size
    if x < xmax - 1 :
        return x+1,y
    else :
        return (x,y)

def copier_pixel(image,coord):
    """
    Retourne le pixel de l'image ``image``, situé aux coordonnées ``coord``.
    
    Arguments :
        coord : coordonnées du pixel
        image : nom de la variable Python contenant l'image
    """
    return image.getpixel(coord)

def coller_pixel(image,coord,pixel):
    """
    Remplace le pixel de l'image ``image``, situé aux coordonnées ``coord``, par le pixel ``pixel``.
    
    Arguments :
        coord : coordonnées du pixel
        image : nom de la variable Python contenant l'image
        pixel : un pixel, c'est à dire un triplet de trois nombres entiers entre 0 et 255. Par exemple : (0,0,0) (pixel noir) ou : (255,255,255) (pixel blanc)    

    """
    image.putpixel(coord,pixel)

def enregistrer_image(image,nom):
    """
    Enregistre l'image ``image``, avec le nom de fichier indiqué.
    
    Arguments :
        image : nom de la variable Python contenant l'image
        nom : nom du fichier avec extension, par exemple "monimage.png"
        
    """
    nm=nom.split('.')
    if len(nm)==1:
        nom+='.png'
    image.save(nom) 
    
def changer_les_pixels(image, fonction, x0=0, x1=0, y0=0, y1=0):
    """
    Modifie les pixels de l'image ``image``, en leur appliquant la fonction ``fonction``.
    
    Arguments :
        image : nom de la variable Python contenant l'image       
        fonction : fonction à appliquer aux pixels. Ce doit être une fonction qui prend un pixel en argument et qui retourne un pixel
        x0 (optionnel) : valeur minimale de la première coordonnée des pixels à modifier (0 par défaut)
        x1 (optionnel) : valeur maximale de la première coordonnée des pixels à modifier (0 par défaut, ce qui signifie que les pixels seront modifiés jusqu'à xmax)
        y0 (optionnel) : valeur minimale de la deuxième coordonnée des pixels à modifier (0 par défaut)
        y1 (optionnel) : valeur maximale de la deuxième coordonnée des pixels à modifier (0 par défaut, ce qui signifie que les pixels seront modifiés jusqu'à ymax)
    
    """
    if x1==0:
        x1=image.size[0]
    if y1==0:
        y1=image.size[1]
    for x in range(x0,x1):
        for y in range(y0,y1):
            pixel=copier_pixel(image,(x,y))
            pixel=fonction(pixel)
            coller_pixel(image,(x,y),pixel)
    

