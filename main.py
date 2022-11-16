import pygame

pygame.init()

 # fenêtre, image redimensionner
longueur = 1000
largeur = 1000
fenetre = pygame.display.set_mode((longueur, largeur))
fond = pygame.image.load("images/test.png").convert_alpha()
redimensionner_image = (1500, 1500)
fond = pygame.transform.scale(fond, redimensionner_image)
fenetre.blit(fond, (0, 0))
pygame.display.flip()
pygame.time.delay(5000)
