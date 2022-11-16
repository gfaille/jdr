import pygame
import window

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
bouton_titre = titre.get_rect(center=(window.longueur/2, 25))
bouton_continuer = text_continuer.get_rect(center=(window.longueur/4, window.largeur/4))
bouton_nouvelle = text_nouvelle.get_rect(center=(window.longueur/4, window.largeur/3))
bouton_charger = text_charger.get_rect(center=(window.longueur/4, window.largeur/2.5))
bouton_option = text_option.get_rect(center=(window.longueur/4, window.largeur/2))

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
    window.fenetre.blit(img, (window.longueur*0.10, 0))

    # affichage des text dans la fenêtre
    window.fenetre.blit(titre, dest=bouton_titre)
    window.fenetre.blit(text_continuer, dest=bouton_continuer)
    window.fenetre.blit(text_nouvelle, dest=bouton_nouvelle)
    window.fenetre.blit(text_charger, dest=bouton_charger)
    window.fenetre.blit(text_option, dest=bouton_option)

    # affichage du selecteur
    window.fenetre.blit(select, (150, liste[nb]*0.90))

liste = [bouton_continuer.y, bouton_nouvelle.y, bouton_charger.y, bouton_option.y]