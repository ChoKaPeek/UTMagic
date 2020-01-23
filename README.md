# Implémenter strlen(3) sur `Magic: The Gathering'

La machine de Turing est basée sur le papier suivant :
https://arxiv.org/pdf/1904.09828.pdf

## Rapport

https://fr.overleaf.com/read/cdcxfgfnrzqr

## Tester ?

```
pip3 install -r requirements.txt
python3 src/app.py <file.utm> <input>
```

UI réalisée sur pygame 1.9.6, utiliser la flèche droite pour avancer dans le
programme. Cliquer sur une carte du plateau permet de la visualiser. Appuyer sur
la barre espace permet de lancer la complétion de l'algorithme en mode
automatique. A la fin du processus, revenir à l'extrémité gauche du ruban est
possible en utilisant la flèche gauche.

## Et sinon ?

Importer un .utm sur le site https://turingmachinesimulator.com
