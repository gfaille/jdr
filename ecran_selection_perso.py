import pygame

pygame.init()

pygame.display.set_caption("Sélection du personnage")

longueur = 1000
largeur = 1000
fenetre = pygame.display.set_mode((longueur, largeur))
fond = pygame.image.load("images/scala_ad_caelum.png").convert_alpha()
fond_riku = pygame.image.load("images/riku_icon_1.png").convert_alpha()
fond_riku2 = pygame.image.load("images/riku_perso.png").convert_alpha()
fond_sora = pygame.image.load("images/Sora_2.png").convert_alpha()
fond_sora2 = pygame.image.load("images/Sora_icone.png").convert_alpha()
redimensionner_image = (1000, 900)
fond = pygame.transform.scale(fond, redimensionner_image)

'''redimensionner_image_riku = (150, 150)
fond_riku = pygame.transform.scale(fond_riku, redimensionner_image_riku)

redimensionner_image_riku2 = (150, 150)
fond_riku2 = pygame.transform.scale(fond_riku2, redimensionner_image_riku2)

redimensionner_image_sora = (150, 150)
fond_sora = pygame.transform.scale(fond_sora, redimensionner_image_sora)

redimensionner_image_sora2 = (150, 150)
fond_sora2 = pygame.transform.scale(fond_sora2, redimensionner_image_sora2)
'''
fenetre.blit(fond, (0, 0))
fenetre.blit(fond_riku,(250, 500))
fenetre.blit(fond_riku2,(240, 600))
fenetre.blit(fond_sora,(500, 650))
fenetre.blit(fond_sora2,(510, 500))
pygame.display.flip()


for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_ESCAPE :
                            continuer = False
                    if event.type == pygame.MOUSEBUTTONDOWN :
                     
                       # capture les event de la souris dans les options d'affichages
                        if fond_riku.collidepoint(event.pos) :
                            L, l = 0, 200

                        elif fond_riku2.collidepoint(event.pos) :
                            L, l = 400, 200
                            
                            if L and l is not None :
                                longueur = L
                                largeur = l
                                fenetre = pygame.display.set_mode((longueur, largeur), flags)
                            if is_fullscreen == False :
                                flags = pygame.FULLSCREEN | pygame.SCALED
                                fenetre = pygame.display.set_mode((longueur, largeur), flags)
                                is_fullscreen = True
                            else :
                                flags = pygame.SHOWN
                                fenetre = pygame.display.set_mode((longueur, largeur), flags)
                                is_fullscreen = False

print(event)

#Variable qui continue la boucle si = 1, stoppe si = 0
continuer = 1

#Boucle infinie
while continuer:
    

    fenetre.fill((0, 0, 0))
    fenetre.blit(fond, (longueur, largeur))
    for event in pygame.event.get() :
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
                continuer = False

pygame.display.flip()

pygame.quit()

