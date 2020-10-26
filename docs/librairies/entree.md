# Entree

## A propos

Cette librairie fournie des fonctions d'entrées utilisateur affichant une fenêtre avec un champ de saisie texte.

Nous constatons qu'un utilisateur peu expérimenté peut être surpris par l'invite d'entrée peu interactive de la console python et proposons cette librairie comme solution.

Concrètement cela peut remplacer avantageusement la fonction python `input()` dans un cadre pédagogique.

Cette librairie fournie également une fonction `demander_reel()` dont la sortie est un nombre réel de type `float` et une fonction `demander_entier()` dont la sortie est un nombre entier de type `int`.

## Utilisation
```python
# on importe la librairie
from pydiderotlibs.entree import *

# On demande une chaîne de caractères à l'utilisateur que l'on stocke dans la variable x
x = demander_texte()
# x est une chaîne de caractère: str

# On demande un nombre réel à l'utilisateur que l'on stocke dans la variable y
y = demander_reel()
# y est un nombre réel: float
```
## Exemple
```python
# on importe la librairie
from pydiderotlibs.entree import *

# On demande un entier à l'utilisateur que l'on stocke dans la variable n
 n = demander_entier()
```

.. image:: /source/_static/demander_entier.png
  :align: center

## Documentation

.. automodule:: pydiderotlibs.entree
    :members:
    :member-order: bysource

.. eof
