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

# récupére l'object joueur du tilemap
J_riku = tmx_data.get_object_by_name("joueur")

# récupére les calce pour les collisions (mur, props)
collision = tmx_data.get_layer_by_name("mur")
tile_list = [] # liste vide qui va contenir les rectangle des les couche de collision

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
pos = [J_riku.x, J_riku.y]
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
            fenetre.blit(move_riku_up[index], (object.x - J_riku.x + (longueur*0.5), object.y - J_riku.y + (largeur*0.5)))
            index = (index + 1) %len(move_riku_up)
    elif keys[pygame.K_LEFT] :
        if index <= len(move_riku_left) :
            fenetre.blit(move_riku_left[index], (object.x - J_riku.x + (longueur*0.5), object.y - J_riku.y + (largeur*0.5)))
            index = (index + 1) %len(move_riku_left)
    elif keys[pygame.K_RIGHT] :
        if index <= len(move_riku_right) :
            fenetre.blit(move_riku_right[index], (object.x - J_riku.x + (longueur*0.5), object.y - J_riku.y + (largeur*0.5)))
            index = (index + 1) %len(move_riku_right)
    elif keys[pygame.K_DOWN] :
        if index <= len(move_riku_down) :
            fenetre.blit(move_riku_down[index], (object.x - J_riku.x + (longueur*0.5), object.y - J_riku.y + (largeur*0.5)))
            index = (index + 1) %len(move_riku_down)

def verifier_collision (player) :
    """ fonction pour vérifier si il y a une collision entre le joueur et les mur et obstacle 

    Args:
        player (Rect): rectangle du joueur + position

    Returns:
        bool: retourne True ou False
    """
    check = False
    
    # test si il y a une collision entre le joueur et un rectangle de la liste
    if (player.collidelist(tile_list)) != -1 :
        check = True

    return check

continuer = True

while continuer :

    # fix les fps à 60
    horloge.tick(fps)
    # efface l'ecran
    fenetre.fill((0, 0, 0))
    
    keys = pygame.key.get_pressed() # recherche la touche qui est maintenue

    # déssine la carte en parcourant les couche de la carte.
    # Une boucle for itére pour chaque couche, afin testé si la couche est une couche de tuile, s'il s'agit d'une couche différente,
    # on l'a déssine différemment. Une fois que l'on a une couche de tuile, on parcour chaque tuile de la couche.
    # Si une tuile à une valeur alors on l'affiche à l'écran, l'emplacement et calculé à l'aide des valeur x et y
    for layer in tmx_data.layers :
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, tile in layer.tiles() :
                if (tile) :
                    fenetre.blit(tile, [(x*tile_width) - J_riku.x + (longueur*0.5), (y*tile_height) - J_riku.y + (largeur*0.5)])
        
        elif isinstance(layer, pytmx.TiledObjectGroup) :
            for object in layer :
                if (object.name == "joueur") :
                        
                    # animation du déplacement du joueur (riku)
                    deplacer_riku()
                    
                    # affiche le joueur inactif si aucune touche pressé
                    if keys[pygame.K_UP] + keys[pygame.K_LEFT] + keys[pygame.K_RIGHT] + keys[pygame.K_DOWN] == False :
                        fenetre.blit(idle_riku[index], (object.x - J_riku.x + (longueur*0.5), object.y - J_riku.y + (largeur*0.5)))
             
    for x, y, tile in collision.tiles() :
        if (tile) :
            tile_list.append(pygame.Rect([(x*tile_width), (y*tile_height), tile_width, tile_height]))

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

    J_riku.x = pos[0]
    J_riku.y = pos[1]

    # rectangle du joueur
    playerrect = pygame.Rect([J_riku.x, J_riku.y, J_riku.width+20, J_riku.height+50])
    
    # verifie si il y a une collision entre le joueur et les diver object de liste 
    if verifier_collision(playerrect) : 
        # J_riku.x = pos_precedx
        # J_riku.y = pos_precedy
        # print(pos)
        pos[0] = pos_precedx
        pos[1] = pos_precedy
    else : 
        pos_precedx = pos[0]
        pos_precedy = pos[1]
     
    pygame.display.flip()

pygame.quit()