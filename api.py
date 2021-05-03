# -*- coding: utf-8 -*-
"""Module d'API du jeu Squadro
Ce module permet d'interagir avec le serveur
afin de pouvoir jouer contre un adversaire robotisé.
Attributes:
    URL (str): Constante représentant le début de l'url du serveur de jeu.
Functions:
    * lister_parties - Retourne la liste des parties reçus du serveur.
    * récupérer_partie - Retourne l'état d'une partie spécifique.
    * débuter_partie - Créer une nouvelle partie et retourne l'état de cette dernière.
    * jouer_coup - Joue un coup et retourne le nouvel état de jeu.
"""
import requests
URL = "https://pax.ulaval.ca/squadro/api/"  # URL du serveur


def lister_parties(iduls):
    """Lister les identifiants de vos parties les plus récentes.
    Args:
        iduls (list): Liste des identifiant des joueurs.
    Returns:
        list: Liste des parties reçues du serveur,
            après avoir décodé le JSON de sa réponse.
    Raises:
        RuntimeError: Erreur levée lorsqu'il y a présence d'un message
            dans la réponse du serveur.
    """

    rep = requests.get(URL+'parties', params={'iduls': iduls})

    if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
        rep = rep.json()
        rep = list(rep['parties'])
        return rep  # retourne dictionnaire

    if rep.status_code == 406:
        # Votre requête est invalide; décoder le JSON
        rep = rep.json()
        raise RuntimeError(rep)


def récupérer_partie(id_partie):
    """Récupérer une partie depuis son identifiant.
    Récupère une partie depuis son identifiant en effectuant une requête à l'URL cible
    squadro/api/partie/
    Args:
        id_partie (str): Identifiant de la partie à récupérer.
    Returns:
        tuple: Tuple constitué de l'identifiant de la partie en cours,
            du prochain joueur à jouer et de l'état courant du jeu,
            après avoir décodé le JSON de sa réponse.
    Raises:
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
    """

    rep = requests.get(URL+'partie', params={'id': id_partie})

    if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
        rep = rep.json()
        # retourne dictionnaire
        return (rep['id'], rep['prochain_joueur'], rep['état'])

    if rep.status_code == 406:
        # Votre requête est invalide; décoder le JSON
        rep = rep.json()
        raise RuntimeError(rep)
        # Une erreur innatendue est survenu


def débuter_partie(iduls):
    """Débuter une nouvelle partie.
    Débute une partie en effectuant une requête à l'URL cible
    squadro/api/partie/
    Args:
        iduls (list): Liste de string représentant le ou les identifiant(s) du ou des joueur(s).
    Returns:
        tuple: Tuple constitué de l'identifiant de la partie en cours,
            du prochain joueur à jouer et de l'état courant du jeu,
            après avoir décodé le JSON de sa réponse.
    Raises:
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
    """

    # créer la nouvelle partie et retourner l'état initial

    rep = requests.post(URL+'partie', data={'iduls': iduls, 'bot': None})

    if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
        rep = rep.json()
        return rep  # retourne dictionnaire

    if rep.status_code == 406:
        # Votre requête est invalide; décoder le JSON
        rep = rep.json()
        raise RuntimeError(rep)


def jouer_coup(id_partie, idul, pion):
    """Jouer votre coup dans une partie en cours
    Joue un coup en effectuant une requête à l'URL cible
    squadro/api/jouer/
    Args:
        id_partie (str): identifiant de la partie;
        idul (str): IDUL jouant un coup;
        pion (int): Numéro du pion à déplacer.
    Returns:
        tuple: Tuple constitué de l'identifiant de la partie en cours,
            du prochain joueur à jouer et de l'état courant du jeu,
            après avoir décodé le JSON de sa réponse.
    Raises:
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
        StopIteration: Erreur levée lorsqu'il y a un gagnant dans la réponse du serveur.
    """

# créer la nouvelle partie et retourner l'état initial

    rep = requests.put(
        URL+'jouer', data={'id': id_partie, 'idul': idul, 'pion': pion})

    if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
        rep = rep.json()
        if rep['gagnant']:
            raise StopIteration(rep['gagnant'])

        return rep  # retourne dictionnaire

    if rep.status_code == 406:
        # Votre requête est invalide; décoder le JSON
        rep = rep.json()
        raise RuntimeError(rep)
    # Une erreur innatendue est survenu
