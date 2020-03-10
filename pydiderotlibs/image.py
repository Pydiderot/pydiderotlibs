from PIL import Image
from pydiderotlibs.couleurs import *

#img = Image.open('lena.png').convert('LA')
#img.save('greyscale.png')

def creer_image(fichier,nom):
    nm=nom.split('.')
    if len(nm)==1:
        nom+='.png'
    nom = Image.open(fichier)
    
def definition_image(image):
    return image.size


#w,h=img.size
#r,v,b=img.getpixel((100,250))
#print(r)
#print(img.getpixel((101,250)))
#img.putpixel((100,250),(255,0,0))
#img.putpixel((102,250),(255,0,0))
#img.show()
def afficher_image(image):
    image.show()

def afficher_pixel(pixel):
    Image.new('RGB', (10,10), pixel).show()

def copier_pixel(image,coord):
    image.getpixel(coord)

def coller_pixel(image,coord):
    image.putpixel(coord)

def enregistrer_image(image,nom):
    nm=nom.split('.')
    if len(nm)==1:
        nom+='.png'
    image.save(nom)

#pixel=rgb('orange')
#afficher_pixel(pixel)
#enregistrer_image(img,'essai')
    

