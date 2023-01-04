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
index = 0

continuer = True

while continuer :

    # fix les fps à 60
    horloge.tick(fps)

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
                    fenetre.blit(idle_riku[index], (object.x, object.y))
                    

    for event in pygame.event.get() :

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
        
    pygame.display.flip()

pygame.quit()