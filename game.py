import pygame
import pytmx
import pyscroll
from pytmx.util_pygame import load_pygame
from player import Joueur

class Game :

    def __init__(self) :
        
        # creer la fenetre du jeu
        self.fenetre = pygame.display.set_mode((800, 640))
        pygame.display.set_caption("donjon - adventure")

        # charger la carte du jeu (tmx)
        tmx_data = load_pygame("assets/map/carte.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.fenetre.get_size())  
        map_layer.zoom = 2  

        # generer le joueur
        self.position_joueur = tmx_data.get_object_by_name("joueur")
        self.joueur = Joueur(self.position_joueur.x, self.position_joueur.y)

        # dessiner le group de calque 
        self.groupe = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer = 1)   
        self.groupe.add(self.joueur) 
    
    def gerer_evennement (self) :

        presser = pygame.key.get_pressed()

        if presser[pygame.K_UP] :
            self.joueur.deplacer_haut()
            self.joueur.mise_a_jour_animation("haut")
        elif presser[pygame.K_DOWN] :
            self.joueur.deplacer_bas()
            self.joueur.mise_a_jour_animation("bas")
        elif presser[pygame.K_LEFT] :
            self.joueur.deplacer_gauche()
            self.joueur.mise_a_jour_animation("gauche")
        elif presser[pygame.K_RIGHT] :
            self.joueur.deplacer_droite()
            self.joueur.mise_a_jour_animation("droite")
    
    def run (self) :

        # defini une horloge (clock)
        horloge = pygame.time.Clock()

        # boucle du jeu
        continuer = True

        while continuer :

            # limite le nombre de fps
            horloge.tick(60)

            self.gerer_evennement()
            self.groupe.update()
            self.groupe.center(self.joueur.rect.center)
            self.groupe.draw(self.fenetre)

            for event in pygame.event.get() :
                
                # quitte si on clique sur la croix rouge de la fenêtre
                if event.type == pygame.QUIT :
                    continuer = False

                if event.type == pygame.KEYDOWN :
                    # quitte si alt + f4 sont appuyé
                    if event.key == pygame.K_LALT and event.key == pygame.K_F4 :
                        continuer = False


            pygame.display.flip()

        pygame.quit()