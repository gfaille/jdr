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
                    

    for event in pygame.event.get() :

        if event.type == pygame.QUIT :
            continuer = False
        
    pygame.display.flip()

pygame.quit()