# -*- coding: utf-8 -*-

"""Jeu Squadro
Ce programme permet de joueur au jeu Squadro.
Examples:
    `> python3 main.py --help`
        usage: main.py [-h] [-p] IDUL [IDUL ...]
        Squadro - Phase 1
        posipaOktional arguments:
        IDUL           IDUL du ou des joueur(s)
        optional arguments:
        -h, --help     show this help message and exit
        -p, --parties  Lister les 20 dernières parties
    `> python3 main.py jowic42`
        Légende:
          □ = jowic42
          ■ = robot
               . | . : | : : | : : | : . | .
                 █   . | .   |   . | .   ●
          ...    ●     |     |     |     █      .
        1 ──□□ ○─┼─────┼─────┼─────┼─────┼───────
          ...    |     |     |     |     |      .
          .      |     |     |     |     |    ...
        2 ───────┼────□□ ○───█─────┼─────┼───────
          .      |     |     ●     |     |    ...
          ..     |     ●     |     |     |     ..
        3 ───────┼─────█─────┼─────┼─────┼─○ □□──
          ..     |     |     |     |     |     ..
          .      |     |     |     |     |    ...
        4 ───────┼─────┼───○ □□────┼─────┼───────
          .      |     |     |     |     |    ...
          ...    |     |     |     |     |      .
        5 ──○ □□─┼─────┼─────┼─────┼─────┼───────
          ...    |     |     |     ●     |      .
               . | .   |     |     █   . | .
               : | : . | . : | : . | . : | :
        Au tour de jowick42 de jouer
        Choisissez le pion à déplacer: 3
"""


from api import lister_parties, débuter_partie, jouer_coup
from squadro import analyser_commande, afficher_parties


if __name__ == "__main__":

    args = analyser_commande()

    if args.parties:
        print(afficher_parties(lister_parties(args.IDUL)))
    elif not args.parties and args.IDUL:
        débuter_partie_retour = débuter_partie(args.IDUL)
        id_jeu = débuter_partie_retour['id']
        prochain_joueur = débuter_partie_retour['prochain_joueur']
        état_jeu = débuter_partie_retour['état']

        while état_jeu:
            afficher_damier_ascii(état_jeu)
            print(f'\n        Au tour de {prochain_joueur} de jouer')
            coup = input("        Choissisez le pion à déplacer: ")
            état_tout = jouer_coup(id_jeu, prochain_joueur, coup)
            état_jeu = état_tout['état']
            prochain_joueur = état_tout['prochain_joueur']
