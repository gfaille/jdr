import os
import pygame
import crud

# créer le fichier config.ini si il n'existe pas dans le dossier
if not os.path.isfile("config.ini") :
    crud.creer_fichier_config()

# initialise pygame
pygame.init()