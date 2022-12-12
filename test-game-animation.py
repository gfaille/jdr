import pygame

# initialisation du module pygame
pygame.init()

# affiche la fenetre pygame
longueur = 1280
largeur = 720
fenetre = pygame.display.set_mode((longueur, largeur))

horloge = pygame.time.Clock()

# charge les sprite de Riku (joueur), pour l'animation
move_riku_up = [pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-01-1.png"), 
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-01-2.png"), 
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-01-3.png"),
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-01-4.png"),
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-01-5.png"),
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-01-6.png"),
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-01-7.png"),
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-01-8.png")]

move_riku_left = [pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-02-1.png"), 
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-02-2.png"), 
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-02-3.png"),
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-02-4.png"),
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-02-5.png"),
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-02-6.png"),
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-02-7.png"),
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-02-8.png")]

move_riku_right = [pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-04-1.png"), 
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-04-2.png"), 
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-04-3.png"),
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-04-4.png"),
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-04-5.png"),
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-04-6.png"),
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-04-7.png"),
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-04-8.png")]

move_riku_down = [pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-03-1.png"), 
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-03-2.png"), 
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-03-3.png"),
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-03-4.png"),
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-03-5.png"),
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-03-6.png"),
                pygame.image.load("assets\sprites\Riku-Sprites\Riku-run-03-7.png")]

idle_riku = [pygame.image.load("assets\sprites\Riku-Sprites\Riku-idle-01.png"),
            pygame.image.load("assets\sprites\Riku-Sprites\Riku-idle-02.png"),
            pygame.image.load("assets\sprites\Riku-Sprites\Riku-idle-03.png"),
            pygame.image.load("assets\sprites\Riku-Sprites\Riku-idle-04.png")]

x = longueur*0.5
y = largeur*0.5
vel = 1
index = 0

def deplacer_riku () :
    """ fonction qui permet de changer de sprite lors du déplacement de riku (joueur),
        variable en globale (pour faire sortir de la fonctions et ainsi modifier la variable origine)
    """

    global index
    
    # affiche et changer de sprite selon la touche appuyer
    if keys[pygame.K_UP] :
        if index <= len(move_riku_up) :
            fenetre.blit(move_riku_up[index], (x,y))
            index = (index + 1) %len(move_riku_up)
    elif keys[pygame.K_LEFT] :
        if index <= len(move_riku_left) :
            fenetre.blit(move_riku_left[index], (x, y))
            index = (index + 1) %len(move_riku_left)
    elif keys[pygame.K_RIGHT] :
        if index <= len(move_riku_right) :
            fenetre.blit(move_riku_right[index], (x, y))
            index = (index + 1) %len(move_riku_right)
    elif keys[pygame.K_DOWN] :
        if index <= len(move_riku_down) :
            fenetre.blit(move_riku_down[index], (x, y))
            index = (index + 1) %len(move_riku_down)

continuer = True

# boucle principal
while continuer :
    # limite le nombre de fps
    horloge.tick(60)

    # un petit delais
    pygame.time.delay(70)

    # efface l'ecran
    fenetre.fill((0, 0, 0))

    # capture les évennement 
    for event in pygame.event.get() :

        # évennement pour quitter 
        if event.type == pygame.QUIT :
            continuer = False
        
        elif event.type == pygame.KEYUP :
            if event.key == pygame.K_UP :
                index = 0
            elif event.key == pygame.K_LEFT :
                index = 1
            elif event.key == pygame.K_DOWN :
                index = 2
            elif event.key == pygame.K_RIGHT :
                index = 3

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] :
        y -= vel

    elif keys[pygame.K_LEFT] :
        x -= vel
    
    elif keys[pygame.K_RIGHT] :
        x += vel
    
    elif keys[pygame.K_DOWN] :
        y += vel

    if vel > 10 :
        vel = 10
    else :
        vel += 0.5
        
    deplacer_riku()

    # affiche le joueur inactif
    if keys[pygame.K_UP] + keys[pygame.K_LEFT] + keys[pygame.K_RIGHT] + keys[pygame.K_DOWN] == False :
        fenetre.blit(idle_riku[index], (x, y))

    # mise a jour de l'écran complet
    pygame.display.flip()

# quitte correctement le jeu
pygame.quit()