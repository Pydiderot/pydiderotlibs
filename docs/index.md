# Python à Diderot : les librairies pydiderotlibs
## A propos
Ce site documente des librairies python utilisées par les enseignants regroupées sous le paquet pydiderotlibs du lycée Diderot à Marseille pour enseigner l'informatique. Le code est disponible sur ce dépot [github](https://github.com/cspaier/pydiderotlibs) et hebergé sur [pypi](https://pypi.org/project/pydiderotlibs/).

L'objectif général est de cacher certaines difficultés techniques liées au langage de programmation afin de pouvoir cibler certains points pédagogiques. Ces librairies ont été écrites pour fonctionner avec l'environnement de travail [pydiderot](https://pydiderot.readthedocs.io)

## Installation
Deux méthodes d'installations sont disponibles:
- Avec pip: `pip3 install pydiderotlibs`.

- manuellement: Télécharger nos librairies zippées avec ce [lien](_static/pydiderotlibs.zip), décompresser le dossier et le placer à un emplacement de `PYTHONPATH`.

## Problèmes rencontrés à l'installation
- La commande `pip install pydiderotlibs` semble ne pas fonctionner.
- Il semble que, en l'état, pydiderotlibs soit compatible avec python entre 3.0 et 3.7. Avec Python 3.8, l'installation plante : la librairie [graphique](/librairies/graphique.html) utilise Pygame 1.9 qui utilise  SDL 1.2 et non le nouveau SDL2.
### Solutions possibles 
- utiliser Python 3.7 avec un environnement de travail dédier :
``` 
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.7 python3.7-dev python3.7-venv python3.7-tk
python3.7 -m venv venv-3.7
source venv-3.7/bin/activate
```
Pour le désactiver: `deactivate`

Notons que venv-3.7 est le nom du venv. On peut choisir ce qu'on veut.

- ou utiliser Python 3.8 et Pygame 2.0. avec `python3 -m pip install pygame==2.0.0.dev10`


## Librairies
 Vous pouvez télécharger nos librairies zippées [ici](_static/pydiderotlibs.zip).

- [repere](/librairies/repere.html): Permet l'affichage d'un repère du plan interactif (zoom, déplacer).
- [entree](/librairies/entree.html): Fonctions d'entrées utilisateur avec des fenêtres tkinter.
- [lycee](/librairies/lycee.html) : Regroupe les fonctions principales que sont amenés à utiliser les élèves de lycée en mathématiques (toutes filières confondues).
- [graphique](/librairies/graphique.html): Permet l'affichage d'une fenêtre graphique dynamique et une gestion simplifiée des entrées clavier et souris.


## Participez !
Ce projet est un travail collaboratif initié par des enseignants du lycée Diderot à Marseille. Nous serions ravis de travailler avec vous et toute aide est la bienvenue. Si vous souhaitez participer, [un guide](contributing.html) est a votre disposition.
