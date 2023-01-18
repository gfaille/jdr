import configparser
import pygame

# initialise configparser
config = configparser.ConfigParser()


def creer_fichier_config () :
    """ Fonction qui créer le fichier config.ini avec les paramétre par défault
    """

    config["affichage"] = {
        "longueur" : 720,
        "largeur" : 480,
        "flags" : pygame.SHOWN,
        "vsinc" : 0
    }

    config["son"] = {
        "fond" : 1.0,
        "effets" : 1.0
    }

    config["jeu"] = {
        "fps" : 60,
        "difficulter" : "normal",
        "sauvegarde auto" : "oui",
        "niveau auto" : "non" # l'augmentation de niveau sera géré par l'ia
    }

    config["commande"] = {
        "avancer" : pygame.K_o,
        "reculer" : pygame.K_l,
        "gauche" : pygame.K_k,
        "droite" : pygame.K_m,
        "interaction" : pygame.K_i,
        "inventaire" : pygame.K_e,
        "stats" : pygame.K_s,
        "quete" : pygame.K_q,
        "carte" : pygame.K_TAB,
        "sauvegarde rapide" : pygame.K_F5,
        "chargement rapide" : pygame.K_F9,
    }

    # écrit dans le fichier config.ini 
    with open("config.ini", "w") as configfile :
        config.write(configfile)