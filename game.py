import pygame
import pytmx
import pyscroll
from pytmx.util_pygame import load_pygame
from player import Joueur
from carte import Gestionnaire_de_carte

class Game :

    def __init__(self) :
        
        # creer la fenetre du jeu
        self.fenetre = pygame.display.set_mode((800, 640))
        pygame.display.set_caption("donjon - adventure")  

        # generer le joueur
        self.joueur = Joueur(0, 0)
        self.gestionnaire_cartes = Gestionnaire_de_carte(self.fenetre, self.joueur)

    def gerer_evennement (self) :

        presser = pygame.key.get_pressed()

        if presser[pygame.K_o] :
            self.joueur.deplacer_haut()
            self.joueur.mise_a_jour_animation("haut")
        elif presser[pygame.K_l] :
            self.joueur.deplacer_bas()
            self.joueur.mise_a_jour_animation("bas")
        elif presser[pygame.K_k] :
            self.joueur.deplacer_gauche()
            self.joueur.mise_a_jour_animation("gauche")
        elif presser[pygame.K_m] :
            self.joueur.deplacer_droite()
            self.joueur.mise_a_jour_animation("droite")
    
    def mise_a_jour (self) :
        self.gestionnaire_cartes.mise_a_jour()
    
    def run (self) :

        # defini une horloge (clock)
        horloge = pygame.time.Clock()

        # boucle du jeu
        continuer = True

        while continuer :

            # limite le nombre de fps
            horloge.tick(60)

            self.joueur.sauvegarder_position()
            self.gerer_evennement()
            self.gestionnaire_cartes.dessiner()
            self.mise_a_jour()

            for event in pygame.event.get() :
                
                # quitte si on clique sur la croix rouge de la fenêtre
                if event.type == pygame.QUIT :
                    continuer = False

                if event.type == pygame.KEYDOWN :
                    # quitte si alt + f4 sont appuyé
                    if event.key == pygame.K_LALT and event.key == pygame.K_F4 :
                        continuer = False

                    if event.key == pygame.K_i :
                        self.gestionnaire_cartes.verifier_interaction()


            pygame.display.flip()

        pygame.quit()