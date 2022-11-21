import pygame
import window
import menu


#police
police = pygame.font.SysFont("Roboto", 16)

# initialisation du menu options (rendu + position)
text_resolution = police.render("Affichage", 1, (255, 255, 255))
text_touche_clavier = police.render("Raccourcie clavier", 1, (255, 255, 255))
text_son = police.render("Son", 1, (255, 255, 255))
text_retour = police.render("Retour", 1, (255, 255, 255))
#############################################################################
bouton_resolution = text_resolution.get_rect(center=(window.longueur*0.20, window.largeur/1.25))
bouton_son = text_son.get_rect(center=(window.longueur*0.40, window.largeur/1.25))
bouton_raccourci = text_touche_clavier.get_rect(center=(window.longueur*0.60, window.largeur/1.25))
bouton_retour = text_retour.get_rect(center=(window.longueur*0.80, window.largeur/1.25))

# initialisation des options d'affichage (rendu + position)
text_resolution_ntsc = police.render("720 X 480", 1, (255, 255, 255))
text_resolution_svga = police.render("800 X 600", 1, (255, 255, 255))
text_resolution_xga = police.render("1024 X 768", 1, (255, 255, 255))
text_resolution_hd = police.render("1280 X 720", 1, (255, 255, 255))
text_resolution_wsxga = police.render("1680 X 1050", 1, (255, 255, 255))
text_resolution_fhd = police.render("1920 X 1280", 1, (255, 255, 255))
#######################################################################
bouton_resolution_ntsc = text_resolution_ntsc.get_rect(center=(window.longueur*0.20, window.largeur*0.2))
bouton_resolution_svga = text_resolution_svga.get_rect(center=(window.longueur*0.20, window.largeur*0.2))
bouton_resolution_xga = text_resolution_xga.get_rect(center=(window.longueur*0.20, window.largeur*0.2))
bouton_resolution_hd = text_resolution_hd.get_rect(center=(window.longueur*0.20, window.largeur*0.2))
bouton_resolution_wsxga = text_resolution_wsxga.get_rect(center=(window.longueur*0.20, window.largeur*0.2))
bouton_resolution_fhd = text_resolution_fhd.get_rect(center=(window.longueur*0.20, window.largeur*0.2))

# creation du selecteur de menu
select = pygame.image.load("sprites/arrow.png")
select_width = select.get_width()
select_height = select.get_height()
select = pygame.transform.smoothscale(select, (select_height/2, select_width/2))

# j'obtient la position des boutons 
liste_bouton_option_x = [bouton_resolution.x, bouton_son.x, bouton_raccourci.x, bouton_retour.x]
liste_bouton_option_y = [bouton_resolution.y, bouton_son.y, bouton_raccourci.y, bouton_retour.y]

# créer les rectangle pour mise a jour d'une zone donner
rect_menu_option = pygame.Rect(window.longueur*0, window.largeur/1.3, window.longueur, window.largeur/1.25)
rect_options = pygame.Rect(window.longueur*0, window.largeur*0, window.longueur, window.largeur/1.25)

def menu_option (nb) :
    
    # affiche les bouton 
    window.fenetre.blits(((text_resolution, bouton_resolution), (text_son, bouton_son), (text_touche_clavier, bouton_raccourci), (text_retour, bouton_retour)))
    
    # affichage du selecteur
    window.fenetre.blit(select, (liste_bouton_option_x[nb]-95, liste_bouton_option_y[nb]*0.97))

def option_affichage () :
    
    # affiche les bouton pour changer les parametre lier à l'affichage
    window.fenetre.blits(((text_resolution_ntsc, bouton_resolution_ntsc), (text_resolution_svga, bouton_resolution_svga), (text_resolution_xga, bouton_resolution_xga), (text_resolution_hd, bouton_resolution_hd), (text_resolution_wsxga, bouton_resolution_wsxga), (text_resolution_fhd, bouton_resolution_fhd)))

# variable pour la boucle, le jeu, le curseur (clavier)
continuer = True
game = 0
curseur = 0

while continuer :
    #################################################
    #                                               #
    #---affiche le menu si game est égal à zero-----#
    #                                               #
    #################################################
    if game == 0 :
        if curseur <= 3 and curseur >= 0 :
            menu.menu(curseur)

            for event in pygame.event.get() :
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_DOWN :
                        curseur += 1
                    if event.key == pygame.K_UP :
                        curseur -= 1
                    if event.key == pygame.K_RETURN :
                        curseur += 1
                        game = curseur
                    if event.key == pygame.K_ESCAPE :
                        continuer = False

            pygame.display.flip()

        else : 
            curseur = 0
    
    #####################################
    #                                   #
    #---charge la derniere sauvegarde---#
    #-------si game est égal à 1--------#
    #                                   #
    #####################################
    if game == 1 :
        window.fenetre.fill((255, 56, 100))
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :
                                continuer = False

        pygame.display.flip()

    #########################################
    #                                       #
    #---creer une nouvelle partie si game---#
    #-------------est égal à 2--------------#
    #                                       #
    #########################################
    if game == 2 :
        window.fenetre.fill((255, 156, 100))
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :
                                continuer = False

        pygame.display.flip()

    #################################
    #                               #
    #---charge une partie si game---# 
    # ---------est égale à 3--------#
    #                               #
    #################################
    if game == 3 :
        window.fenetre.fill((255, 126, 130))
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :
                                continuer = False

        pygame.display.flip()
    
    #########################################
    #                                       #
    #---charge la page des option si game---#
    #--------------est égal à 4-------------#
    #                                       #
    #########################################
    if game == 4 :
        window.effacer_ecran()
        if curseur <= 3 and curseur >= 0 :
            menu_option(curseur)

            for event in pygame.event.get() :
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RIGHT :
                        curseur += 1
                    if event.key == pygame.K_LEFT :
                        curseur -= 1
                    if event.key == pygame.K_RETURN :
                        option_affichage()
                        pygame.display.update(rect_options)
                    if event.key == pygame.K_ESCAPE :
                        continuer = False

            pygame.display.update(rect_menu_option)

        else : 
            curseur = 0

pygame.quit()
