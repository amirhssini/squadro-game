# -*- coding: utf-8 -*-
"""Module de la classe abstraite de SquadroInterface
Ce module possède la classe abstraite SquadroInterface
ce module ne doit en aucun cas être modifié car lors de la
correction, ce fichier sera remplacé par sa version originale
pour garantir qu'il n'a pas été altéré.
Classes:
    * SquadroInterface - Classe parent dont vous devez hériter pour créer votre classe Squadro.
"""
from copy import deepcopy


class SquadroInterface:
    """
    SquadroInterface procure les fonctions de base et soulève une excetion NotImplemented
    si la fonction n'est pas présente dans la classe enfant.
    """

    def __init__(self, joueur1, joueur2):
        """Constructeur de la classe Squadro.
        Initialise une partie de Squadro avec les joueurs,
        en s'assurant de faire une copie profonde de tout ce qui a besoin d'être copié.
        Appel la méthode `validation` pour valider les données et assigne ce qu'elle retourne
        à l'attribut `self.état`.
        Cette méthode ne devrait pas être redéfinie par la classe enfant.
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
        """
        self.état = deepcopy(self.validation(joueur1, joueur2))

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
                Notez que les pions doivent être sous forme de liste
                [x1, x2, x3, x4, x5] uniquement.
        Raises:
            SquadroError: Le nom du joueur doit être une chaîne de caractère.
            SquadroError: L'élément `pions` doit être une liste.
            SquadroError: L'élément `pions` doit posséder 5 éléments uniquement.
            SquadroError: La position des pions doit être un entier.
            SquadroError: La position des pions doit être entre 0 et 12 inclusivement.
            SquadroError: Le joueur doit être un dictionnaire ou une chaîne de caractère.
        """
        raise NotImplementedError()

    def état_partie(self):
        """Produire l'état actuel de la partie.
        Retourne l'état actuel de la partie.
        Cette méthode ne devrait pas être réécrite par la classe enfant.
        Returns:
            List: Une copie de l'état actuel du jeu sous la forme d'une liste de deux dictionnaires.
            Notez que les pions doivent être sous forme de liste [x1, x2, x3, x4, x5] uniquement.
        Examples:
            [
                {'nom': nom1, 'pions': [x1, x2, x3, x4, x5]},
                {'nom': nom2, 'pions': [x1, x2, x3, x4, x5]}
            ]
            où la clé 'nom' d'un joueur est associée à son nom, la clé 'pions' est associée
            à la liste des pions du joueur. Le premier élément de la liste de pions représente
            le premier pion du joueur (de haut en bas pour J1, et de gauche à droite pour J2).
            L'entier assigné au pion représente sa position
                (0 pour le départ, 6 pour la mi-chemin et 12 pour la fin).
        """
        return deepcopy(self.état)

    def __str__(self):
        """Produire un représentation en art ASCII de l'état actuel de la partie.
        Ne faites preuve d'aucune originalité dans votre «art ascii»,
        car votre fonction sera testée par un programme et celui-ci est
        de nature intolérante (votre affichage doit être identique à
        celui illustré). Notez aussi que votre fonction sera testée
        avec plusieurs états de jeu différents.
        Returns:
            str: La chaîne de caractères de la représentation.
        """
        raise NotImplementedError()

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
        raise NotImplementedError()

    def jouer_coup(self, joueur):
        """Jouer un coup automatique pour un joueur.
        Pour le joueur spécifié, jouer automatiquement son meilleur coup pour l'état actuel
        de la partie.
        Args:
            joueur (str): Le nom du jouer tel que représenté dans l'état.
        Raises:
            SquadroError: Le nom du joueur est inexistant pour la partie en cours.
        Returns:
            Tuple[str, int]: Un tuple composé du nom du joueur et du numéro du pion joué.
        """
        raise NotImplementedError()

    def demander_coup(self, joueur):
        """Demander le coup à jouer via le terminal
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
        raise NotImplementedError()

    def partie_terminée(self):
        """Déterminer si la partie est terminée.
        Returns:
            str/bool: Le nom du gagnant si la partie est terminée; False autrement.
        """
        raise NotImplementedError()
