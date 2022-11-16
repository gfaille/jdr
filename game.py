import pygame
import window
import menu

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
        window.fenetre.fill((225, 26, 80))
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :
                                continuer = False

        pygame.display.flip()
pygame.quit()