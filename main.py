import pygame

pygame.init()

 # fenêtre, image redimensionner
longueur = 1000
largeur = 1000
fenetre = pygame.display.set_mode((longueur, largeur))
fond = pygame.image.load("images/test.png").convert_alpha()
redimensionner_image = (1500, 1500)
fond = pygame.transform.scale(fond, redimensionner_image)

# se deplacer sur la map
x = 0
y = 0

#Variable qui continue la boucle si = 1, stoppe si = 0
continuer = 1

#Boucle infinie
while continuer:
    
    fenetre.fill((0, 0, 0))
    fenetre.blit(fond, (x, y))
    for event in pygame.event.get() :
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP :
                y += 100
            if event.key == pygame.K_DOWN :
                y -= 100
            if event.key == pygame.K_RIGHT :
                x -= 100
            if event.key == pygame.K_LEFT :
                x += 100
            if event.key == pygame.K_ESCAPE :
                continuer = False

    pygame.display.flip()

pygame.quit()

# 