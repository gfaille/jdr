import pygame

class Animation_Sprite (pygame.sprite.Sprite) :

    def __init__(self, nom_dossier, nom_image, nom_sprites) :
        super().__init__()
        self.sprite_sheet = pygame.image.load(f"assets/{nom_dossier}/{nom_image}.png")
        self.sprite_actuel = 0
        self.liste_image = animation.get(nom_sprites)
    
    def animer (self) :
        """ fonction pour animer le sprites 

        Returns:
            int: retourne la valeur de la liste selon l'index
        """

        self.sprite_actuel += 1 

        if self.sprite_actuel == len(self.liste_image) :
            self.sprite_actuel = 0

        return self.liste_image[self.sprite_actuel]
    
    def get_image (self, x, y) :
        image = pygame.Surface([24, 24])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 24, 24))
        return image

def charger_sprites_animes (nombre_sprites_x) :

    image = []
    number = 0

    for _ in range(nombre_sprites_x) :
        image.append(number)
        number += 24
    
    return image

animation = {
    "joueur" : charger_sprites_animes(3)
}
