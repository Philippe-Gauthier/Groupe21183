# Mon projet
## concepte
Aventure texte médiéval-fantastique (genre DnD) dont vous êtes le héro sous forme digitale entièrement comprise dans le terminal.
## Structure
### - structure
Arbre décisionnel, chaque action amène un résultat différent.
### - Entrée
les choix, soit l'option 1, 2 ou 3 dépendament de ce que le joueur décide.
### - Sortie
le résultat du-dit choix, qui promptera d'autre choix, d'ou la structure d'arbre.

## avant de jouer
### - Dans le code
- s'assurer que la variable debug_mode est à 0, normalement, elle l'est mais il est possible qu'elle a été changé
### - Dans VScode
- assurez vous que votre terminale par défault est cmd.exe ou powershell, le programme n'a pas été testé pour d'autre (ex: GitBash, AzureShell, Fish, Zsh ou WSL) 

### - Assurer les dépendances
#### language
- Python 3.14.-- ou plus
#### librairies
##### - Time
- natif à python, normalement, aucun problème.
##### - Termcolor
- nécéssaire pour ajouter de la couleure au text.

    s'installe simplement avec cette commande dans le terminal cmd.exe:
```cmd
pip install termcolor
```
assurez vous d'utiliser la bonne version den python, sinon, le code ne trouvera pas trermcolor, ne pourra pas l'importer et ne démarrera pas.
## Arbre
à faire

## Fonctionnalitées en attente
### nécéssaire
rien
### optionnel -probablement jamais-
un système de combat tour-à-tour

un système d'inventaire avec des items et cartes utilisable en combat
## Pour la correction
le fichier que j'ai écrit se nomme Text_adventure_01.py, malheureusement, j'écrit mieux en anglais qu'en français, j'ai donc fait mon histoire en anglais, cela a eu comme fâcheux effet de me faire commenter mon code en anglais. Comme je n'ai appris les restrictions linguistiques de la documentation que très tard dans le projet (par exemple, le jour de la remise), j'ai donc rapidement passé mon code dans DeepL translator afin de traduire le tout en français. j'ai ensuite utilisé ctrl+f et la vonction 'replace all', le 'replace all' ne fait pas la différence entre ce qui est du code et ce qui est un commentaire, il est donc possible que du ciode soit changé et inutile suite à la traduction

Veuillez donc, s'il-vous-plait, corriger la documentation dans le fichier Aventure_texte_fr.py mais le code comme tel dans le fichier Text_adventure.py.

merci de votre compréhention