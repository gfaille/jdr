import os
import pygame
import crud
import menu

# créer le fichier config.ini si il n'existe pas dans le dossier
if not os.path.isfile("config.ini") :
    crud.creer_fichier_config()

# initialise pygame
pygame.init()

# lis les sections du fichier ini
display = crud.lire_fichier_config("affichage") 
option_game = crud.lire_fichier_config("jeu")

# création de la fenêtre du jeu
longueur = display.getint("longueur")
largeur = display.getint("largeur")
flags = display.getint("flags")
vsinc = display.getint("vsinc")

fenetre = pygame.display.set_mode((longueur, largeur), flags, vsinc) # affiche la fenetre et la stocke en tant que surface

# charge les image 
fond = pygame.image.load("assets\menu/fond.png").convert() # image pour le fond du menu 
fond = pygame.transform.scale(fond, (longueur, largeur)) # change la taille de l'image par rapport a la fenêtre

continuer = True # variable de la boucle principale
jeu = False # variable pour savoir si on est dans le jeu ou non (default False)
sous_menu = {
    "options" : False,
    "option_jeu" : False,
    "opttion_affichage" : False,
    "option_son" : False,
    "option_raccourci" : False
}

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

def options () :

    # éfface la fenêtre (le fond devient noir)
    fenetre.fill((255, 255, 255))

    if sous_menu["option_jeu"] == True :
        option_jeu()
    elif sous_menu["opttion_affichage"] == True :
        option_affichage()
    elif sous_menu["option_son"] == True :
        option_son()
    elif sous_menu["option_raccourci"] == True :
        option_commande()
    else :
        
        menu.dessiner_texte(fenetre, "Options", 24, (255, 255, 255), longueur*0.4, largeur*0.1)
        bouton_jeu = menu.dessiner_texte(fenetre, "Général", 18, (255, 255, 255), longueur*0.2, largeur*0.2)
        bouton_affichage = menu.dessiner_texte(fenetre, "Affichage", 18, (255, 255, 255), longueur*0.2, largeur*0.3)
        bouton_son = menu.dessiner_texte(fenetre, "Son", 18, (255, 255, 255), longueur*0.2, largeur*0.4)
        bouton_commande = menu.dessiner_texte(fenetre, "Commande", 18, (255, 255, 255), longueur*0.2, largeur*0.5)
        bouton_retour = menu.dessiner_texte(fenetre, "Retour", 18, (255, 255, 255), longueur*0.2, largeur*0.6)

        list_btn = [bouton_jeu, 
                    bouton_affichage, 
                    bouton_son, 
                    bouton_commande, 
                    bouton_retour]
        
        menu.gerer_collision_souri(fenetre, list_btn)

        event_option = menu.gerer_event_options(list_btn)

        if event_option == "Général" :
            sous_menu["option_jeu"] = True
        elif event_option == "Affichage" :
            sous_menu["opttion_affichage"] = True
        elif event_option == "Son" :
            sous_menu["option_son"] = True
        elif event_option == "Commande" :
            sous_menu["option_raccourci"] = True
        elif event_option == "retour" :
            sous_menu["options"] = False

def option_jeu() :

    fps = option_game.getint("fps")
    difficulte = option_game.get("difficulte")
    save_auto = option_game.get("sauvegarde auto")
    niv_auto = option_game.get("niveau auto")

    # éfface la fenêtre (le fond devient noir)
    fenetre.fill((255, 255, 255))

    menu.dessiner_texte(fenetre, "Options général", 24, (255, 255, 255), longueur*0.4, largeur*0.1)

    menu.dessiner_texte(fenetre, "difficulté :", 18, (255, 255, 255), longueur*0.2, largeur*0.3)
    bouton_difficulte = menu.dessiner_texte(fenetre, difficulte, 18, (255, 255, 255), longueur*0.3, largeur*0.3)

    menu.dessiner_texte(fenetre, "fps :", 18, (255, 255, 255), longueur*0.2, largeur*0.4)
    bouton_fps = menu.dessiner_texte(fenetre, str(fps), 18, (255, 255, 255), longueur*0.3, largeur*0.4)

    menu.dessiner_texte(fenetre, "sauvegarde auto :", 18, (255, 255, 255), longueur*0.2, largeur*0.5)
    bouton_save = menu.dessiner_texte(fenetre, save_auto, 18, (255, 255, 255), longueur*0.4, largeur*0.5)

    menu.dessiner_texte(fenetre, "augm.niveau auto :", 18, (255, 255, 255), longueur*0.2, largeur*0.6)
    bouton_niv = menu.dessiner_texte(fenetre, niv_auto, 18, (255, 255, 255), longueur*0.4, largeur*0.6)

    bouton_retour = menu.dessiner_texte(fenetre, "Retour", 18, (255, 255, 255), longueur*0.8, largeur*0.8)

    list_btn = [bouton_difficulte,
                bouton_fps,
                bouton_save,
                bouton_niv,
                bouton_retour]
    
    menu.gerer_collision_souri(fenetre, list_btn)

    if menu.gerer_event_options_general(list_btn, fps, difficulte, save_auto, niv_auto) :
        sous_menu["option_jeu"] = False

def option_affichage() :
    pass

def option_son() :
    pass

def option_commande() :
    pass

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
        if sous_menu["options"] == True :
            options()
        else :
            choix_menu = afficher_menu_principale()

            if choix_menu == 'continuer' :
                jeu = True
            elif choix_menu == 'nouveau' :
                jeu = True
            elif choix_menu == 'charger' : 
                jeu = True
            elif choix_menu == 'options' :
                sous_menu["options"] = True
            elif choix_menu == 'quitter' :
                continuer = False

    elif jeu == True : 
        # appel de la fonction jeu 
        pass

    # mise a jour de l'écran
    pygame.display.flip()

# arrêt de pygame complet et correctement (évite le crash)
pygame.quit()