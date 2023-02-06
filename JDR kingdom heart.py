import os
import pygame
import crud
import menu

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

# charge les image 
fond = pygame.image.load("assets\menu/fond.png").convert() # image pour le fond du menu 
fond = pygame.transform.scale(fond, (longueur, largeur)) # change la taille de l'image par rapport a la fenêtre

continuer = True # variable de la boucle principale
jeu = False # variable pour savoir si on est dans le jeu ou non (default False car on est dans le menu)

def afficher_menu_principale () :
        
    # éfface la fenêtre (le fond devient noir)
    fenetre.fill((0, 0, 0))

    # affiche le fond 
    fenetre.blit(fond, (0, 0))

    # affcihe le titre et les bouton
    bouton_continuer = menu.dessiner_texte(fenetre, "continuer", 18, (255, 255, 255, 128), longueur*0.1, largeur*0.8)
    bouton_nouveau = menu.dessiner_texte(fenetre, "nouvelle", 18, (255, 255, 255, 128), (bouton_continuer[0].x + bouton_continuer[0].width) * 1.3, largeur*0.8)
    bouton_charger = menu.dessiner_texte(fenetre, "charger", 18, (255, 255, 255, 128), (bouton_nouveau[0].x + bouton_nouveau[0].width) * 1.2, largeur*0.8)
    bouton_option = menu.dessiner_texte(fenetre, "options", 18, (255, 255, 255, 128), (bouton_charger[0].x + bouton_charger[0].width) * 1.6, largeur*0.8)
    bouton_quitter = menu.dessiner_texte(fenetre, "quitter", 18, (255, 255, 255, 128), (bouton_option[0].x + bouton_option[0].width) * 1.2, largeur*0.8)

    # liste des bouton 
    list_btn = [bouton_continuer, 
                bouton_nouveau, 
                bouton_charger, 
                bouton_option, 
                bouton_quitter]

    # vérifie si il y a collision avec la souris
    menu.gerer_collision_souri(fenetre, list_btn)

    # événement du menu
    event_menu = menu.gerer_event_menu(list_btn)

    if event_menu != None :
        return event_menu

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
        choix_menu = afficher_menu_principale()

        if choix_menu == 'continuer' :
            jeu = True
        elif choix_menu == 'nouveau' :
            jeu = True
        elif choix_menu == 'charger' : 
            jeu = True
        elif choix_menu == 'quitter' :
            continuer = False

    elif jeu == True : 
        # appel de la fonction jeu 
        pass

    # mise a jour de l'écran
    pygame.display.flip()

# arrêt de pygame complet et correctement (évite le crash)
pygame.quit()