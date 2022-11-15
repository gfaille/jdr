import pygame

# initialisation du module pygame
pygame.init()

# affichage de la fenêtre pygame en 720p
longueur = 1280
largeur = 720
fenetre = pygame.display.set_mode((longueur, largeur))

# arriere plan
img = pygame.image.load("sprites\kingdom_hearts.jpg").convert_alpha()
img = pygame.transform.scale2x(img)
fenetre.blit(img, (longueur*0.10, 0))

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

# affichage des text dans la fenêtre
fenetre.blit(titre, dest=bouton_titre)
fenetre.blit(text_continuer, dest=bouton_continuer)
fenetre.blit(text_nouvelle, dest=bouton_nouvelle)
fenetre.blit(text_charger, dest=bouton_charger)
fenetre.blit(text_option, dest=bouton_option)

continuer = True
print(bouton_continuer.y, bouton_nouvelle.y, bouton_charger.y, bouton_option.y)
while continuer :
    for event in pygame.event.get() :
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
                continuer = False
    pygame.display.flip()
pygame.quit()