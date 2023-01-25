import os
import pygame
import crud
import menu

# créer le fichier config.ini si il n'existe pas dans le dossier
if not os.path.isfile("config.ini") :
    crud.creer_fichier_config()

# initialise pygame
pygame.init()

continuer = True # variable de la boucle principale
jeu = False # variable pour savoir si on est dans le jeu ou non (default False car on est dans le menu)

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
    
    # verfie si on est dans le jeu ou le menu
    if jeu == False :
        menu.afficher_menu_principale()
    elif jeu == True : 
        # appel de la fonction jeu 
        pass

    # mise a jour de l'écran
    pygame.display.flip()

# arrêt de pygame complet et correctement (évite le crash)
pygame.quit()