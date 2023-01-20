import os
import pygame
import crud

# créer le fichier config.ini si il n'existe pas dans le dossier
if not os.path.isfile("config.ini") :
    crud.creer_fichier_config()

# initialise pygame
pygame.init()

# création de la fenêtre du jeu
display = crud.lire_fichier_config("affichage") # lis la section affichage 

# lis est stocke les valeur des clé de la section affichage
# pour obtenir la longueur et largeur de la fenetre puis le flags pour le mode de l'écran et la synchronisation verticale
longueur = display.getint("longueur")
largeur = display.getint("largeur")
flags = display.getint("flags")
vsinc = display.getint("vsinc")

fenetre = pygame.display.set_mode((longueur, largeur), flags, vsinc) # affiche la fenetre et la stocke en tant que surface

continuer = True

while continuer :

    # capture les événnement 
    for event in pygame.event.get() :
        # quitte si on clique sur la croix rouge de la fenêtre
        if event.type == pygame.QUIT :
            continuer = False

        # capture les événnement de type keydown (touche appuyé)
        if event.type == pygame.KEYDOWN :
            # quitte si alt + f4 sont appuyé
            if event.key == pygame.K_LALT and event.key == pygame.K_F4 :
                continuer = False
                
# arrêt de pygame complet et correctement (évite le crash)
pygame.quit()