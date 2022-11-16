import pygame

# initialisation du module pygame
pygame.init()

# affichage de la fenêtre pygame en 720p
longueur = 1280
largeur = 720
fenetre = pygame.display.set_mode((longueur, largeur))

# choix de la taille et de la police d'écriture 
police_titre = pygame.font.SysFont("Roboto", 35)
police = pygame.font.SysFont("Roboto", 16)


# le rendu des differents text (titre, continuer, nouvelle, charger une partie, options) + la couleur
titre = police_titre.render("JDR Kingdom Heart", 1, (255, 255, 255))
text_continuer = police.render("continuer", 1, (255, 255, 255))
text_nouvelle = police.render("nouvelle partie", 1, (255, 255, 255))
text_charger = police.render("charger une partie", 1, (255, 255, 255))
text_option = police.render("options", 1, (255, 255, 255))

# création d'un rectangle et positionnement dans la fenêtre pour en faire un bouton
bouton_titre = titre.get_rect(center=(longueur/2, 25))
bouton_continuer = text_continuer.get_rect(center=(longueur/4, largeur/4))
bouton_nouvelle = text_nouvelle.get_rect(center=(longueur/4, largeur/3))
bouton_charger = text_charger.get_rect(center=(longueur/4, largeur/2.5))
bouton_option = text_option.get_rect(center=(longueur/4, largeur/2))

# creation du selecteur de menu
select = pygame.image.load("sprites/arrow.png")
select_width = select.get_width()
select_height = select.get_height()
select = pygame.transform.smoothscale(select, (select_height/2, select_width/2))

def menu(nb) :
    """ affiche le menu du jeu
    """
    # arriere plan
    img = pygame.image.load("sprites\kingdom_hearts.jpg").convert_alpha()
    img = pygame.transform.scale2x(img)
    fenetre.blit(img, (longueur*0.10, 0))

    # affichage des text dans la fenêtre
    fenetre.blit(titre, dest=bouton_titre)
    fenetre.blit(text_continuer, dest=bouton_continuer)
    fenetre.blit(text_nouvelle, dest=bouton_nouvelle)
    fenetre.blit(text_charger, dest=bouton_charger)
    fenetre.blit(text_option, dest=bouton_option)

    # affichage du selecteur
    fenetre.blit(select, (150, liste[nb]*0.90))

# variable pour la boucle, le jeu, le curseur (clavier)
continuer = True
game = 0
curseur = 0

print(bouton_continuer.y, bouton_nouvelle.y, bouton_charger.y, bouton_option.y)
liste = [bouton_continuer.y, bouton_nouvelle.y, bouton_charger.y, bouton_option.y]
print(liste, "++--++")

while continuer :
    #################################################
    #                                               #
    #---affiche le menu si game est égal à zero-----#
    #                                               #
    #################################################
    if game == 0 :
        if curseur <= 3 and curseur >= 0 :
            menu(curseur)

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
        fenetre.fill((255, 56, 100))
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
        fenetre.fill((255, 156, 100))
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
        fenetre.fill((255, 126, 130))
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
        fenetre.fill((225, 26, 80))
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :
                                continuer = False

        pygame.display.flip()
pygame.quit()