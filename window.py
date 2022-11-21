import pygame

# initialisation du module pygame
pygame.init()

# affichage de la fenêtre pygame en 720p
longueur = 1280
largeur = 720
flags = pygame.SHOWN
fenetre = pygame.display.set_mode((longueur, largeur), flags)

def effacer_ecran () :
    
    # éfface l'ecran
    fenetre.fill((0, 0, 0))