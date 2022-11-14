import pygame

pygame.init()

fenetre = pygame.display.set_mode((1280, 720))

continuer = True

while continuer :
    for event in pygame.event.get() :
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_f :
                pygame.key.start_text_input()
            if event.key == pygame.K_RETURN :
                continuer = False
    pygame.display.flip()
pygame.quit()