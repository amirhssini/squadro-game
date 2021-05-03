# -*- coding: utf-8 -*-
"""Module de la classe  Squadro
Ce module possède la classe  Squadro
Classes:
    * SquadroError: Soulève l'exception SquadroError selon les paramètres du jeu.
    * Squadro: Mécanique du jeu Squadro Hors-Ligne
"""
from random import choice
from argparse import ArgumentParser
from squadro_interface import SquadroInterface


def analyser_commande():
    """Génère un analyseur de ligne de commande
    En utilisant le module argparse, génère un analyseur de ligne de commande.
    L'analyseur offre (1) argument positionnel:
        IDUL: IDUL du ou des joueurs.
    Ainsi que les (2) arguments optionnel:
        help: show this help message and exit
        parties: Lister les 20 dernières parties.
    Returns:
        Namespace: Retourne un objet de type Namespace possédant
            les clef «IDUL» et «parties».
    """

    parser = ArgumentParser(description="Squadro - Phase 3")
    parser.add_argument('-a', '--automatique', dest='parties', action='store_true',
                        help="Activer le mode automatique.")
    parser.add_argument('-l', '--local', dest='parties', action='store_true',
                        help="Jouer localement.")
    parser.add_argument('-p', '--parties', dest='parties', action='store_true',
                        help="Lister les 20 dernières parties.")
    parser.add_argument('IDUL', nargs='+', help="IDUL du ou des joueurs.")

    return parser.parse_args()


def afficher_parties(parties):
    """Afficher les parties
    Args:
        parties (list): Liste des parties d'un joueur.
    """

    aff_parties = ''
    for i in range(len(parties)):
        winner = (", gagnant: " +
                  str(parties[i]['gagnant']) if parties[i]['gagnant'] else '')
        sep = (" : " if i < 9 else ": ")
        aff_parties += str(i + 1) + sep + str(parties[i]['date']) + ", " \
            + str(parties[i]['joueurs'][0]) + " vs " + str(parties[i]['joueurs'][1]) \
            + winner + "\n"

    return aff_parties


def sauvergarder_partie_local(id, prochain_joueur, état, gagnant=None):
    return id, prochain_joueur, état, gagnant


def lister_parties_local(iduls):
    rep = requests.get(URL+'parties', params={'iduls': iduls})

    if rep.status_code == 200:
        rep = rep.json()
        rep = list(rep['parties'])
        return rep

    if rep.status_code == 406:
        rep = rep.json()
        raise RuntimeError(rep)

    else:
        print(
            f"Le GET sur '{URL}parties' a produit le code d'erreur suivant {rep.status_code}.")


def récupérer_parties_local():
    if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
        rep = rep.json()
        # retourne dictionnaire
        return (rep['id'], rep['prochain_joueur'], rep['état'])

    elif rep.status_code == 406:
        # Votre requête est invalide; décoder le JSON
        rep = rep.json()
        raise RuntimeError(rep)
    else:
        # Une erreur innatendue est survenu
        print(
            f"Le GET sur '{URL}parties' a produit le code d'erreur suivant {rep.status_code}.")


class SquadroError(Exception):
    '''
    Créé Exception SquadroError
    '''
    __module__ = 'builtins'


class Squadro(SquadroInterface):
    '''
    La classe Squadro implémente la mécanique de jeux.
    '''

    def validation(self, joueur1, joueur2):
        """Validateur d'initialisation d'une instance de la classe Squadro.
        Valide les données arguments de construction de l'instance et retourne
        l'état si valide.
        Args:
            joueur1 (str/Dict): une chaîne de caractère représentant soit le nom du joueur
                soit un dictionnaire contant la clef `nom` représentant le nom du joueur
                et la clef `pions` représentant la liste des pions du joueur.
                Le premier élément de la liste de pions représente le premier pion du joueur
                (de haut en bas pour le joueur 1, et de gauche à droite pour le joueur 2).
                L'entier assigné au pion représente sa position
                (0 pour le départ, 6 pour la mi-chemin et 12 pour la fin).
            joueur2 (str/Dict): une chaîne de caractère représentant soit le nom du joueur
                soit un dictionnaire contant la clef `nom` représentant le nom du joueur
                et la clef `pions` représentant la liste des pions du joueur.
                Le premier élément de la liste de pions représente le premier pion du joueur
                (de haut en bas pour le joueur 1, et de gauche à droite pour le joueur 2).
                L'entier assigné au pion représente sa position
                (0 pour le départ, 6 pour la mi-chemin et 12 pour la fin).
        Returns:
            List: L'état actuel du jeu sous la forme d'une liste de deux dictionnaires.
                Le joueur 1 doit être à la première position de la liste.
                Notez que les pions doivent être sous forme de liste \
                    [x1, x2, x3, x4, x5] uniquement.
        Raises:
            SquadroError: Le nom du joueur doit être une chaîne de caractère.
            SquadroError: L'élément `pions` doit être une liste.
            SquadroError: L'élément `pions` doit posséder 5 éléments uniquement.
            SquadroError: La position des pions doit être un entier.
            SquadroError: La position des pions doit être entre 0 et 12 inclusivement.
            SquadroError: Le joueur doit être un dictionnaire ou une chaîne de caractère.
            """

        if (isinstance(joueur1, dict) or isinstance(joueur2, dict)) or \
                (isinstance(joueur1, str) and isinstance(joueur2, str)):
            pass
        else:
            raise SquadroError("Le joueur doit être un dictionnaire ou \
                une chaîne de caractère.")

        if isinstance(joueur1, dict):

            if not isinstance(joueur1['nom'], str) or not isinstance(joueur2['nom'], str):
                raise SquadroError(
                    "Le nom du joueur doit être une chaîne de caractère.")

            if not isinstance(joueur1['pions'], list) or not isinstance(joueur2['pions'], list):
                raise SquadroError("L'élément `pions` doit être une liste.")

            if len(joueur1['pions']) != 5 or len(joueur2['pions']) != 5:
                raise SquadroError(
                    "L'élément `pions` doit posséder 5 éléments uniquement.")

            for i in joueur1['pions'] + joueur2['pions']:
                if not isinstance(i, int):
                    raise SquadroError(
                        "SquadroError: La position des pions doit être un entier.")

            for i in joueur1['pions'] + joueur2['pions']:

                if i < 0 or i > 12:
                    raise SquadroError("SquadroError: La position des pions doit être \
                        entre 0 et 12 inclusivement.")
            return [joueur1, joueur2]

        if isinstance(joueur1, str):

            return [{'nom': joueur1, 'pions': [0, 0, 0, 0, 0]},
                    {'nom': joueur2, 'pions': [0, 0, 0, 0, 0]}]

    def __str__(self):
        """Produire un représentation en art ASCII de l'état actuel de la partie.
        Ne faites preuve d'aucune originalité dans votre «art ascii»,
        car votre fonction sera testée par un programme et celui-ci est
        de nature intolérante (votre affichage doit être identique à
        celui illustré). Notez aussi que votre fonction sera testée
        avec plusieurs états de jeu différents.
        Returns:
            str: La chaîne de caractères de la représentation.
        Afficher le damier
        Args:
        état (dict): Dictionnaire représentant l'état du jeu.
        """

        # Nom des joueurs
        joueur1 = self.état[0]['nom']  # nom joueur 1
        joueur2 = self.état[1]['nom']  # nom joueur 2

        # Listes d'état des pions des joueurs 1 et 2
        j1 = self.état[0]['pions']  # pions joueur 1
        j2 = self.état[1]['pions']  # pions joueur 2

        # Initialisation de la grille
        p = []
        for i in range(85):
            p.append('|')
        for i in range(85)[10::15]:
            p[i] = "─────┼──"
            for j in range(3):
                p[i+j+1] = "──|──"
            p[i+4] = "──┼─────"

    # JOUEUR 1 - Ligne - Blanc

        for i in range(5):
            # Aller
            if j1[i] == 0:
                p[10+15*i] = '□□ ○─┼──'
            elif j1[i] == 1:
                p[10+15*i] = '────□□ ○'
            elif j1[i] == 2:
                p[11+15*i] = '─□□ ○'
            elif j1[i] == 3:
                p[12+15*i] = '─□□ ○'
            elif j1[i] == 4:
                p[13+15*i] = '─□□ ○'
            elif j1[i] == 5:
                p[14+15*i] = '─□□ ○───'
        # Tourne
            elif j1[i] == 6:
                p[14+15*i] = '──┼─○ □□'
        # Retour
            elif j1[i] == 7:
                p[14+15*i] = '○ □□────'
            elif j1[i] == 8:
                p[13+15*i] = '○ □□─'
            elif j1[i] == 9:
                p[12+15*i] = '○ □□─'
            elif j1[i] == 10:
                p[11+15*i] = '○ □□─'
            elif j1[i] == 11:
                p[10+15*i] = '───○ □□─'
            elif j1[i] == 12:
                p[10+15*i] = '○ □□─┼──'

        # JOUEUR 2 - Colonne - Noir

        # Colonne 1 - Début de colonne; ne peut être bouclé

        i = 0
        # Aller
        if j2[i] == 0:
            p[0] = '█'
            p[5] = '●'
        elif j2[i] == 1:
            p[10] = p[10][0:4] + '─█──'
            p[15] = '●'
        elif j2[i] == 2:
            p[25] = p[25][0:4] + '─█──'
            p[30] = '●'
        elif j2[i] == 3:
            p[40] = p[40][0:4] + '─█──'
            p[45] = '●'
        elif j2[i] == 4:
            p[55] = p[55][0:4] + '─█──'
            p[60] = '●'
        elif j2[i] == 5:
            p[70] = p[70][0:4] + '─█──'
            p[75] = '●'

        # Tourne
        elif j2[i] == 6:
            p[75] = '●'
            p[80] = '█'
        # Retour
        elif j2[i] == 7:
            p[65] = '●'
            p[70] = p[70][0:4] + '─█──'
        elif j2[i] == 8:
            p[50] = '●'
            p[55] = p[55][0:4] + '─█──'
        elif j2[i] == 9:
            p[35] = '●'
            p[40] = p[40][0:4] + '─█──'
        elif j2[i] == 10:
            p[20] = '●'
            p[25] = p[25][0:4] + '─█──'
        elif j2[i] == 11:
            p[5] = '●'
            p[10] = p[10][0:4] + '─█──'
        elif j2[i] == 12:
            p[0] = '●'
            p[5] = '█'

        # Colonne 2,3,4
        # Les colonnes 2, 3 et 4 ont une form similaire donc peuvent être bouclés.

        for i in range(1, 4):
            # Aller
            if j2[i] == 0:
                p[0 + i] = '█'
                p[5 + i] = '●'
            elif j2[i] == 1:
                p[10 + i] = '──█──'
                p[15 + i] = '●'
            elif j2[i] == 2:
                p[25 + i] = '──█──'
                p[30 + i] = '●'
            elif j2[i] == 3:
                p[40 + i] = '──█──'
                p[45 + i] = '●'
            elif j2[i] == 4:
                p[55 + i] = '──█──'
                p[60 + i] = '●'
            elif j2[i] == 5:
                p[70 + i] = '──█──'
                p[75 + i] = '●'

        # Milieu
            elif j2[i] == 6:
                p[75 + i] = '●'
                p[80 + i] = '█'
        # Retour
            elif j2[i] == 7:
                p[65 + i] = '●'
                p[70 + i] = '──█──'
            elif j2[i] == 8:
                p[50 + i] = '●'
                p[55 + i] = '──█──'
            elif j2[i] == 9:
                p[35 + i] = '●'
                p[40 + i] = '──█──'
            elif j2[i] == 10:
                p[20 + i] = '●'
                p[25 + i] = '──█──'
            elif j2[i] == 11:
                p[5 + i] = '●'
                p[10 + i] = '──█──'
            elif j2[i] == 12:
                p[0 + i] = '●'
                p[5 + i] = '█'

        # Colonne 5. Fin de Colonne; ne peut être bouclé

        i = 4
        # Aller
        if j2[i] == 0:
            p[0 + i] = '█'
            p[5 + i] = '●'
        elif j2[i] == 1:
            p[10 + i] = '──█─' + p[10 + i][4:]
            p[15 + i] = '●'
        elif j2[i] == 2:
            p[25 + i] = '──█─' + p[25 + i][4:]
            p[30 + i] = '●'
        elif j2[i] == 3:
            p[40 + i] = '──█─' + p[40 + i][4:]
            p[45 + i] = '●'
        elif j2[i] == 4:
            p[55 + i] = '──█─' + p[55 + i][4:]
            p[60 + i] = '●'
        elif j2[i] == 5:
            p[70 + i] = '──█─' + p[70 + i][4:]
            p[75 + i] = '●'

        # Milieu
        elif j2[i] == 6:
            p[75 + i] = '●'
            p[80 + i] = '█'

        # Retour
        elif j2[i] == 7:
            p[65 + i] = '●'
            p[70 + i] = '──█─' + p[70 + i][4:]
        elif j2[i] == 8:
            p[50 + i] = '●'
            p[55 + i] = '──█─' + p[55 + i][4:]
        elif j2[i] == 9:
            p[35 + i] = '●'
            p[40 + i] = '──█─' + p[40 + i][4:]
        elif j2[i] == 10:
            p[20 + i] = '●'
            p[25 + i] = '──█─' + p[25 + i][4:]
        elif j2[i] == 11:
            p[5 + i] = '●'
            p[10 + i] = '──█─' + p[10 + i][4:]
        elif j2[i] == 12:
            p[0 + i] = '●'
            p[5 + i] = '█'

        # Construction de la grille

        damier = "            Légende:\n"
        damier += "              □ = " + joueur1 + "\n"
        damier += "              ■ = " + joueur2 + "\n\n"

        damier += "                   . | . : | : : | : : | : . | .     \n"
        damier += "                     " + p[0] + "   . " + p[1] + " .   " + p[2] + "   . " \
            + p[3] + " .   " + p[4] + "       \n"
        damier += "              ...    " + p[5] + "     " + p[6] + "     " + p[7] + "     " \
            + p[8] + "     " + p[9] + "      .\n"
        damier += "            1 ──" + p[10] + "─" + p[11] + "─" + p[12] + "─" + p[13] + "─" \
            + p[14] + "──\n"
        damier += "              ...    " + p[15] + "     " + p[16] + "     " + p[17] + "     " \
            + p[18] + "     " + p[19] + "      .\n"
        damier += "              .      " + p[20] + "     " + p[21] + "     " + p[22] + "     " \
            + p[23] + "     " + p[24] + "    ...\n"
        damier += "            2 ──" + p[25] + "─" + p[26] + "─" + p[27] + "─" + p[28] + "─" \
            + p[29] + "──\n"
        damier += "              .      " + p[30] + "     " + p[31] + "     " + p[32] + "     " \
            + p[33] + "     " + p[34] + "    ...\n"
        damier += "              ..     " + p[35] + "     " + p[36] + "     " + p[37] + "     " \
            + p[38] + "     " + p[39] + "     ..\n"
        damier += "            3 ──" + p[40] + "─" + p[41] + "─" + p[42] + "─" + p[43] + "─" \
            + p[44] + "──\n"
        damier += "              ..     " + p[45] + "     " + p[46] + "     " + p[47] + "     " \
            + p[48] + "     " + p[49] + "     ..\n"
        damier += "              .      " + p[50] + "     " + p[51] + "     " + p[52] + "     " \
            + p[53] + "     " + p[54] + "    ...\n"
        damier += "            4 ──" + p[55] + "─" + p[56] + "─" + p[57] + "─" + p[58] + "─" \
            + p[59] + "──\n"
        damier += "              .      " + p[60] + "     " + p[61] + "     " + p[62] + "     " \
            + p[63] + "     " + p[64] + "    ...\n"
        damier += "              ...    " + p[65] + "     " + p[66] + "     " + p[67] + "     " \
            + p[68] + "     " + p[69] + "      .\n"
        damier += "            5 ──" + p[70] + "─" + p[71] + "─" + p[72] + "─" + p[73] + "─" \
            + p[74] + "──\n"
        damier += "              ...    " + p[75] + "     " + p[76] + "     " + p[77] + "     " \
            + p[78] + "     " + p[79] + "      .\n"
        damier += "                   . " + p[80] + " .   " + p[81] + "     " + p[82] + "     " \
            + p[83] + "   . " + p[84] + " .     \n"
        damier += "                   : | : . | . : | : . | . : | :"

        return damier

    def déplacer_pion(self, joueur, pion):
        """Déplace un jeton.
        Pour le joueur spécifié, déplacer le pion spécifié pour le nombre permis de cases.
        Args:
            joueur (str): Le nom du jouer tel que présent dans l'état.
            pion (int): Le pion à déplacer (de 1 à 5 inclusivement).
        Raises:
            SquadroError: Le nom du joueur est inexistant pour la partie en cours.
            SquadroError: Le numéro du pion devrait être entre 1 à 5 inclusivement.
            SquadroError: La partie est déjà terminée.
            SquadroError: Ce pion a déjà atteint la destination finale.
        """

        if 1 > pion > 5:
            raise SquadroError(
                'Le numéro du pion devrait être entre 1 à 5 inclusivement.')

        if self.état[0]['nom'] == joueur:

            for i, _ in enumerate(self.état):
                pionroundtrip = 0
                for j in self.état[i]['pions']:
                    if j == 12:
                        pionroundtrip += 1
                if pionroundtrip == 4:
                    raise SquadroError(
                        'SquadroError: La partie est déjà terminée.')

            if self.état[0]['pions'][pion-1] == 12:
                raise SquadroError(
                    'Ce pion a déjà atteint la destination finale.')
                # établir mécanique pour avancer pions
            if pion in (1, 5):
                self.mecanique_bouger_pion(0, pion, 3, 1)
            if pion in (2, 4):
                self.mecanique_bouger_pion(0, pion, 1, 3)
            if pion == 3:
                self.mecanique_bouger_pion(0, pion, 2, 2)

        elif self.état[1]['nom'] == joueur:

            for i, _ in enumerate(self.état):
                pionroundtrip = 0
                for j in self.état[i]['pions']:
                    if j == 12:
                        pionroundtrip += 1
                if pionroundtrip == 4:
                    raise SquadroError(
                        'SquadroError: La partie est déjà terminée.')

            if self.état[1]['pions'][pion-1] >= 12:
                raise SquadroError(
                    'Ce pion a déjà atteint la destination finale.')

            # établir mécanique pour avancer pions
            if pion in (1, 5):
                self.mecanique_bouger_pion(1, pion, 1, 3)
            if pion in (2, 4):
                self.mecanique_bouger_pion(1, pion, 3, 1)
            if pion == 3:
                self.mecanique_bouger_pion(1, pion, 2, 2)

        else:
            raise SquadroError(
                'Le nom du joueur est inexistant pour la partie en cours.')

    def mecanique_bouger_pion(self, ind_joueur, pion, aller, retour):
        '''
        La mécanique de bouger_pion a été mise en place dans cette fonction.
        '''

        # avancer le pion selon la ligne ou la colonne

        if ind_joueur == 0:
            ind_autrejoueur = 1
        else:
            ind_autrejoueur = 0

        pjactif = self.état[ind_joueur]['pions']
        pjautre = self.état[ind_autrejoueur]['pions']

        partant = 0

        if pjactif[pion-1] <= 5:
            tot_pas = aller
            partant = 1
        elif pjactif[pion-1] >= 6:
            tot_pas = retour

        rencontre = 0

        for _ in range(tot_pas):

            pjactif[pion - 1] += 1  # Déplacer de un le pion actif

            pos = 0

            # Bouclier pour voir s'il y a des superpositions
            if pjactif[pion - 1] in (0, 6, 12):
                pass
            if 0 < pjactif[pion - 1] <= 5:
                pos = pjactif[pion - 1]
            elif 6 <= pjactif[pion - 1] < 12:
                pos = 12 - pjactif[pion - 1]

            while 0 < pos <= 5 and (pjautre[pos-1] == pion or pjautre[pos-1] == 12 - pion):
                if pjautre[pos-1] <= 5:
                    # Retourner le pion adverse à la case départ
                    pjautre[pos-1] = 0
                elif pjautre[pos-1] >= 6:
                    # Retourner le pion adverse à la case de retournement
                    pjautre[pos-1] = 6
                pjactif[pion-1] += 1  # Ajouter 1 si superpostion
                pos += 1
                rencontre = 1

            # Conditions de cessation de l'ajout de pas.
            if pjactif[pion-1] >= 6 and partant == 1:
                pjactif[pion-1] = 6
                break

            if pjactif[pion-1] >= 12:
                pjactif[pion-1] = 12
                break

            if rencontre == 1:  # Condition si pion adverse a été rencontré
                break

    def jouer_coup(self, joueur):

        if isinstance(self.partie_terminée(), str):
            return

        if self.état[0]['nom'] == joueur:

            pionsactifs = []
            for index, value in enumerate(self.état[0]['pions']):
                if value < 12:
                    pionsactifs.append(index)

            p = choice(pionsactifs)  # choix au hasard

            self.déplacer_pion(joueur, p + 1)

            return (joueur, p + 1)

        if self.état[1]['nom'] == joueur:

            pionsactifs = []
            for index, value in enumerate(self.état[1]['pions']):
                if value < 12:
                    pionsactifs.append(index)

            p = choice(pionsactifs)  # choix au hasard

            self.déplacer_pion(joueur, p + 1)

            return (joueur, p + 1)

        else:
            raise SquadroError(
                "Le nom du joueur est inexistant pour la partie en cours.")

    def demander_coup(self, joueur):
        """
        Demander le coup à jouer via le terminal
        En utilisant input, vous devez demander au joueur le pion qu'il désire déplacer.
        Cette méthode ne devrait poser qu'une seule question et retourner la réponse de
        l'utilisateur après avoir effectué les validations, et ne rien faire d'autre.
        Args:
            joueur (str): Le nom du jouer à qui la question est posée.
        Raises:
            SquadroError: Le nom du joueur est inexistant pour la partie en cours.
            SquadroError: Le numéro du pion devrait être entre 1 à 5 inclusivement.
            SquadroError: Ce pion a déjà atteint la destination finale.
        Returns:
            int: Un entier représentant le numéro du pion à déplacer.
            """

        npion = input('Quel pion désirez vous déplacer ?: ')
        npion = int(npion)

        if not self.état[0]['nom'] == joueur:
            raise SquadroError(
                "Le nom du joueur est inexistant pour la partie en cours.")

        if not 1 <= npion <= 5:
            raise SquadroError(
                'Le numéro du pion devrait être entre 1 à 5 inclusivement.')

        if self.état[0]['pions'][npion-1] == 12:
            raise SquadroError('Ce pion a déjà atteint la destination finale.')

        return npion

    def partie_terminée(self):
        """Déterminer si la partie est terminée.
        Returns:
            str/bool: Le nom du gagnant si la partie est terminée; False autrement.
        """

        # Itérer sur chacun des joueurs pour déterminer le vainqueur:
        for i, joueur in enumerate(self.état):
            pionroundtrip = 0
            for j in self.état[i]['pions']:
                if j == 12:
                    pionroundtrip += 1
            if pionroundtrip == 4:
                return joueur["nom"]

        return False
