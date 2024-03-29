# Mettre à jour le paquet sur pypi

## 0. Environnement
Cette étape décrit la mise en place de l’environnement de travail sous UNIX.

- Créer un environnement python: `virtualenv -p python3 venv`
- L'activer: `source venv/bin/activate`
- Cloner le dépot: `git clone https://github.com/cspaier/pydiderotlibs.git`
- Se placer dans le dossier: `cd pydiderotlibs`
- Installer les dépendances: `pip install -r requirements.txt`
- Installer `twine`: `pip install --upgrade twine`
- Installer `wheel` : `pip install wheel`


## 1. Mettre à jour le numéro de version

Augmenter de `0.1` le numéro de version dans `__init__.py` et dans `setup.py`.

## 2. Pousser sur github
- Eventuellement, vérifier qu'on est à jour avec le dépôt distant : `git pull`
- `git add __init__.py setup.py`
- `git commit -m 'maj version 0.?'`
- `git push`

## 3. Installer et nettoyer
- `python3 setup.py sdist bdist_wheel`
- Dans le dossier dist, ne laisser que les fichiers correspondants au nouveau numéro de version.

## 4. Uploader sur pypi
`twine upload dist/*`
