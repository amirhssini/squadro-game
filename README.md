# Squadro

Ce projet est une implémentation du jeu **Squadro** dans le cadre d'un cours de programmation à l'Université Laval.

## 📋 Objectif du projet

Le but est de créer un programme qui permet de jouer au jeu **Squadro** contre un autre joueur humain ou un joueur robotisé, tout en respectant les règles officielles du jeu.

### 🎯 Règles essentielles

- Chaque joueur possède **5 pions** sur un plateau de **5 lignes horizontales** et **5 verticales**.
- Les pions avancent selon une valeur spécifique et peuvent rebondir ou sauter par-dessus des pions adverses.
- Le premier joueur à faire un **aller-retour** avec **4 de ses pions** gagne la partie.


## 🛠️ Fonctionnalités implémentées

- ✅ Lecture des arguments via la ligne de commande avec `argparse`
- ✅ Communication avec un serveur distant pour gérer l'état de la partie
- ✅ Affichage ASCII du plateau
- ✅ Interaction tour à tour avec le joueur
- ✅ Gestion des mouvements, des rebonds, et des sauts
- ✅ Affichage du gagnant
- ✅ Historique de parties (option `-p`)

## 🧠 Stratégie du robot

Le robot implémente une stratégie de base en analysant les déplacements possibles et en prenant des décisions simples mais efficaces pour progresser ou bloquer l'adversaire.

> 📌 *Bonus* : Possibilité de développer une stratégie avancée avec l’algorithme **minimax** + **élagage alpha-bêta**.

## 🖼️ Idées d'illustrations supplémentaires

1. **Diagramme du système** — Montrant l'interaction entre `main.py`, le module `squadro`, et le serveur.
2. **Exemple de damier ASCII** — Captures d'écran montrant une partie en cours dans le terminal.
3. **Capture du terminal** — Lors du lancement avec `python main.py idul1 idul2`.

## 🔧 Lancer le projet

### Partie solo (contre robot) :
```bash
python main.py idul_du_joueur
