# Comment faire un pull request
Vous souhaiter modifier les librairies et effectuer une Pull Request (PR). Merci!
Ce guide va vous aider à mettre en place l'environnement de travail et tester vos modifications en local avant d'effectuer une PR.
Si vous êtes familier avec ce genre de processus, vous pouvez probablement vous épargner la lecture car vous n'y trouverez rien d'exotique. Soumettez simplement votre PR sur la branche `master`.
## Créer un fork sous github
Vous pouvez faire cela sur le site github en suivante cette [documentation](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository).


## Mise en place de l'environnement
Les commandes sont adaptées à un environnement UNIX. Si quelqu'un veut mettre à jour la doc pour Windows il est bienvenue.
1. Créer un dossier de travail et s'y placer
`mkdir pydiderotlibs`
`cd pydiderotlibs`

2. Créer un environnement virtuel python
`python3.8 -m venv venv`
L'activer
`source venv\bin\activate`

3. Cloner votre fork. Attention, il faut adapter l'url au dépot de votre fork. Vous pouvez suivre si besoin la documentation [github](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
`git clone https://github.com/VOTREPSEUDOGITHUB/pydiderotlibs.git`
Se placer dans le dossier du dépot
`cd pydiderotlibs`

4. Installer les dépendances
`pip install -r requirements.txt`

## Faire vos modifications et les tester.
Vous pouvez maintenant ouvrir le dossier pydiderotlibs dans votre éditeur de texte préféré (par exemple [Thonny](https://thonny.org/)). Si créez un fichier test dans ce dossier et importez la bibliothèque `pydiderotlibs` avec, par exemple, `from pydiderotlibs.graphique import *`, python utilisera la bibliothèque locale.

N'oubliez pas de suivre [nos recommandations](contributing.html#conventions-de-code-et-de-commentaires) pour le style du code et des commentaires.

## Ca fonctionne, je veux soumettre ma PR!
1. Supprimez les éventuels fichiers de test que vous auriez créés!
2. Créez un commit et poussez le sur votre dépôt
`git add les fichiers modifiés`
`git commit -m 'nom de votre commit'`
`git push origin master`
3. créez votre PR.
Vous pouvez par exemple faire cela depuis le site github en suivant cette [documentation](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork).

## Attendez les commentaires de l'équipe pydiderotlibs
Nous devrions réagir à votre PR rapidement. Si ce n'est pas le cas et que l'un de vos enseignant fait partie de l'équipe de pydiderotlibs, n'hésitez pas à lui en parler pendant votre cours!


## Bravo et merci!
Si vous avez fait tout ça, vous avez probablement beaucoup appris. Bravo. Sachez que c'est ainsi que travaillent les développeurs pour travailler collectivement. Cet apprentissage est donc loin d'être vain si vous pensez coder par la suite. Mais existe-t-il de vain apprentissages?
