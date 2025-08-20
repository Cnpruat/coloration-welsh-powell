# 🕸️ Coloration de Welsh-Powell - Python

Programme permettant de réaliser la coloration d'un graphe par la méthode de **Welsh-Powell** en Python.

L'idée est d'attribuer une couleur à chaque sommet d'un graphe de telle sorte qu'aucun sommets adjacents ne portent la même couleur. 

---

# Algorithme
L’algorithme de Welsh Powell se décompose ainsi :

1.  Calculer le degré de chaque sommet.
2.  Ranger les sommets par ordre de degrés décroissants (dans
     certains cas plusieurs possibilités).
3.  Attribuer au premier sommet (A) de la liste une couleur.
4.  Suivre la liste en attribuant la même couleur au premier sommet
    (B) qui ne soit pas adjacent à (A).
5.  Suivre (si possible) la liste jusqu'au prochain sommet (C) qui ne
     soit adjacent ni à A ni à B.
6.  Continuer jusqu'à ce que la liste soit finie.
7.  Prendre une deuxième couleur pour le premier sommet (D) non
     encore coloré de la liste.
8.  Répéter les opérations 3 à 7.
9.  Continuer jusqu'à avoir colorié tous les sommets.


---

# 📁 Structure du projet

```
coloration-welsh-powell/
│
├── algorithme.py           # Programme principal
├── graph.py                # Fonctions associées
├── .gitignore
├── README.md
└── LICENSE.txt
```

---
# 👨‍🏭 Auteurs


**Lola Combrouze**, **Pierre Bourrandy** - **ENSIL-ENSCI**

Ce projet a été réalisé dans le cadre du module de mathématiques discrètes de 1ère année de Formation Initiale aux Métiers d'Ingénieurs. 

## Contact detail
pierre.bourrandy@etu.unilim.fr *(ENSIL-ENSCI)*

https://github.com/Cnpruat/coloration-welsh-powell *(GitHub)*

