import pygame

pygame.init()

longueur = 1000
largeur = 1000
fenetre = pygame.display.set_mode((longueur, largeur))
fond = pygame.image.load("images/test_2.png").convert_alpha()
fond_perso = pygame.image.load("images/perso_1.png").convert_alpha()
fond_perso_2 = pygame.image.load("images/perso_2.png").convert_alpha()
fond_perso_3 = pygame.image.load("images/perso_3.png").convert_alpha()
fenetre.blit(fond, (0, 0))
fenetre.blit(fond_perso,(0, 200))
fenetre.blit(fond_perso_2,(400, 200))
fenetre.blit(fond_perso_3,(800, 200))
pygame.display.flip()
pygame.time.delay(5000)


for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_ESCAPE :
                            continuer = False
                    if event.type == pygame.MOUSEBUTTONDOWN :
                       
                       # capture les event de la souris dans les options d'affichages
                        if fond_perso.collidepoint(event.pos) :
                            L, l = 0, 200

                        elif fond_perso_2.collidepoint(event.pos) :
                            L, l = 400, 200

                        elif fond_perso_3.collidepoint(event.pos) :
                            L, l = 800, 200
                            
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

