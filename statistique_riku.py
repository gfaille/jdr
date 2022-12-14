import pygame

# initialisation de pygame et c'est module 
pygame.init()

# affiche la fenetre pygame 
longueur = 1000
largeur = 1000
fenetre = pygame.display.set_mode((longueur, largeur))

def afficher_image (chemins, pos_x, pos_y) :
    """ fonction qui affiche des image, attention toute fois on ne peut l'utiliser comme des bouton 
        donc il ne pourrons pas être selectionner 

    Args:
        chemins (string): donne le chemins de l'image
        pos_x (_type_): donne la position en x
        pos_y (_type_): donne la position en y
    """
    fond = pygame.image.load(chemins).convert_alpha()
    fenetre.blit(fond, (pos_x, pos_y))

def dessiner_texte (text, size, background, x, y) :
    """ fonction qui permet de dessiné du texte et le centrer dans un arriere plan (il peut être transparant, une couleur unit)
        puis l'affiche dans la fenêtre.

    Args:
        text (string): ajout du texte à afficher
        size (int): donne la taille de la police
        background (tuple): donne un tuple pour le RGB pour la couleur d'arriere plan
        x (int): donne la coordonnées en abscisse
        y (int): donne les coordonnées en ordonné 
    """
    police = pygame.font.SysFont("Roboto", size)
    texte = police.render(text, 1, (255, 255, 255))
    rect_bouton = pygame.draw.rect(fenetre, (background), rect=(x, y, texte.get_width()*1.5, texte.get_height()*1.5))
    buton_texte = texte.get_rect(center=rect_bouton.center) # permet de centrer le texte au centre du rectangle
    fenetre.blit(texte, buton_texte)
    return rect_bouton # retourne les coordonnées x et y du rectangle et sa dimension (largeur, hauteur)

continuer = True

# boucle principale (Tout ce qui est a afficher doit être dedans sauf les fonction qui eux sont a l'extérieur)
while continuer:

    # affiche les image (il ne pourrons pas être utilisé pour de futur bouton ou autre)
    afficher_image("images/riku_icon_1.png", 450, 0)

    # boucle for qui capture les d'évennements get()
    for event in pygame.event.get() :

        Niveau = dessiner_texte("Niveau", 25, (51, 101, 138), longueur*0.40, largeur*0.10)
        Stats_Niveau = dessiner_texte("1", 25, (51, 101, 138), longueur*0.50, largeur*0.10)
        Force = dessiner_texte("Force", 25, (51, 101, 138), longueur*0.30, largeur*0.20)
        Stats_Force = dessiner_texte("50", 25, (51, 101, 138), longueur*0.60, largeur*0.20)
        Vitalité = dessiner_texte("Vitalité", 25, (51, 101, 138), longueur*0.30, largeur*0.30)
        Stats_Vitalité = dessiner_texte("50", 25, (51, 101, 138), longueur*0.60, largeur*0.30)
        Dextérité = dessiner_texte("Dextérité", 25, (51, 101, 138), longueur*0.30, largeur*0.40)
        Stats_Dextérité = dessiner_texte("50", 25, (51, 101, 138), longueur*0.60, largeur*0.40)
        Intélligence = dessiner_texte("Intélligence", 25, (51, 101, 138), longueur*0.30, largeur*0.50)
        Stats_Intélligence = dessiner_texte("50", 25, (51, 101, 138), longueur*0.60, largeur*0.50)
        Esprit = dessiner_texte("Esprit", 25, (51, 101, 138), longueur*0.30, largeur*0.60)
        Stats_Esprit = dessiner_texte("50", 25, (51, 101, 138), longueur*0.60, largeur*0.60)
        Chance = dessiner_texte("Chance", 25, (51, 101, 138), longueur*0.30, largeur*0.70)
        Stats_Chance = dessiner_texte("50", 25, (51, 101, 138), longueur*0.60, largeur*0.70)
        Bouton_Guerrier = dessiner_texte("Guerrier", 25, (255, 60, 60), longueur*0.25, largeur*0.15)
        Bouton_Magicien = dessiner_texte("Magicien", 25, (60, 60, 255), longueur*0.45, largeur*0.15)
        Bouton_Équilibrer = dessiner_texte("Équilibrer", 25, (60, 255, 60), longueur*0.65, largeur*0.15) 
        Bouton_Valider = dessiner_texte("Valider", 25, (100, 100, 100), longueur*0.45, largeur*0.80)

        # capture les évennement clavier lors d'appui d'une touche
        if event.type == pygame.KEYDOWN :

            # quand on appui sur eschap on quitte 
            if event.key == pygame.K_ESCAPE :
                continuer = False

    # mise a jour total de l'écran (se fait toujour a la fin de la boucle while)
    pygame.display.flip()

# permet de quitter correctement le programe (toujour en dehors de la boucle)
pygame.quit()