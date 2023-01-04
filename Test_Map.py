import pygame
import pytmx
from pytmx.util_pygame import load_pygame

# initialisation du module pygame
pygame.init()

# affiche la fenetre pygame
longueur = 1280
largeur = 720
fenetre = pygame.display.set_mode((longueur, largeur))

# créer une horloge 
horloge = pygame.time.Clock()
fps = 60 # nombre de fps

# charge la map en sprite pygame le fichier .tmx
tmx_data = load_pygame("assets/environnement/test-map.tmx")
tile_width = tmx_data.tilewidth # largeur de la tilemap
tile_height = tmx_data.tileheight # hauteur de la tilemap

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

# variable du jeu
pos = [0, 0]
index = 0

def deplacer_riku () :
    """ fonction qui permet de changer de sprite lors du déplacement de riku (joueur),
        variable en globale (pour faire sortir de la fonctions et ainsi modifier la variable origine)
    """

    global index
    horloge.tick(30)
    # affiche et changer de sprite selon la touche appuyer
    if keys[pygame.K_UP] :
        if index <= len(move_riku_up) :
            fenetre.blit(move_riku_up[index], (object.x, object.y))
            index = (index + 1) %len(move_riku_up)
    elif keys[pygame.K_LEFT] :
        if index <= len(move_riku_left) :
            fenetre.blit(move_riku_left[index], (object.x, object.y))
            index = (index + 1) %len(move_riku_left)
    elif keys[pygame.K_RIGHT] :
        if index <= len(move_riku_right) :
            fenetre.blit(move_riku_right[index], (object.x, object.y))
            index = (index + 1) %len(move_riku_right)
    elif keys[pygame.K_DOWN] :
        if index <= len(move_riku_down) :
            fenetre.blit(move_riku_down[index], (object.x, object.y))
            index = (index + 1) %len(move_riku_down)

continuer = True

while continuer :

    # fix les fps à 60
    horloge.tick(fps)
    
    keys = pygame.key.get_pressed() # recherche la touche qui est maintenue

    # déssine la carte en parcourant les couche de la carte.
    # Une boucle for itére pour chaque couche, afin testé si la couche est une couche de tuile, s'il s'agit d'une couche différente,
    # on l'a déssine différemment. Une fois que l'on a une couche de tuile, on parcour chaque tuile de la couche.
    # Si une tuile à une valeur alors on l'affiche à l'écran, l'emplacement et calculé à l'aide des valeur x et y
    for layer in tmx_data.layers :
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, tile in layer.tiles() :
                if (tile) :
                    fenetre.blit(tile, [x*tile_width, y*tile_height])
        
        elif isinstance(layer, pytmx.TiledObjectGroup) :
            for object in layer :
                if (object.name == "joueur") :
                    # animation du déplacement du joueur (riku)
                    deplacer_riku()
                    
                    # affiche le joueur inactif si aucune touche pressé
                    if keys[pygame.K_UP] + keys[pygame.K_LEFT] + keys[pygame.K_RIGHT] + keys[pygame.K_DOWN] == False :
                        fenetre.blit(idle_riku[index], (object.x, object.y))
                    #fenetre.blit(idle_riku[index], (object.x, object.y))
                    

    for event in pygame.event.get() :

        if event.type == pygame.QUIT :
            continuer = False

        # change l'index lors du relachement 
        elif event.type == pygame.KEYUP :
            if event.key == pygame.K_UP :
                index = 0
            elif event.key == pygame.K_LEFT :
                index = 1
            elif event.key == pygame.K_DOWN :
                index = 2
            elif event.key == pygame.K_RIGHT :
                index = 3

    # changer la position selon la touche appuyer            
    if keys[pygame.K_UP] :
        pos[1]-=10
    elif keys[pygame.K_LEFT] :
        pos[0]-=10
    
    elif keys[pygame.K_RIGHT] :
        pos[0]+=10
    
    elif keys[pygame.K_DOWN] :
        pos[1]+=10
    
    tmx_data.get_object_by_name("joueur").x = pos[0]
    tmx_data.get_object_by_name("joueur").y = pos[1]
        
    pygame.display.flip()

pygame.quit()