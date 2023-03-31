import pygame
import animation

class Joueur (animation.Animation_Sprite) :

    def __init__(self, x, y) -> None:
        super().__init__("joueur", "Character_009", "joueur")
        self.image = self.get_image(24, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.vitesse = 3
    
    def mise_a_jour_animation (self, name) :
        """ fonction qui fait la mise a jour de l'animation du joueur

        Args:
            name (strings): le nom de l'action 
        """
        V_animation = pygame.time.Clock()
        V_animation.tick(15)

        self.animation = {
            "haut" : self.get_image(self.animer(), 72),
            "gauche" : self.get_image(self.animer(), 24),
            "droite" : self.get_image(self.animer(), 48),
            "bas" : self.get_image(self.animer(), 0)
        }

        self.image = self.animation[name]
        self.image.set_colorkey([0, 0, 0])     
        
    def deplacer_gauche (self) :
        self.position[0] -= self.vitesse
    
    def deplacer_droite (self) :
        self.position[0] += self.vitesse

    def deplacer_haut (self) :
        self.position[1] -= self.vitesse

    def deplacer_bas (self) :
        self.position[1] += self.vitesse
    
    def update(self) :
        self.rect.topleft = self.position    