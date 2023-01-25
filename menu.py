import pygame
import crud

pygame.init()

# création de la fenêtre du jeu
display = crud.lire_fichier_config("affichage") # lis la section affichage 

# lis est stocke les valeur des clé de la section affichage
# pour obtenir la longueur et largeur de la fenetre puis le flags pour le mode de l'écran et la synchronisation verticale
longueur = display.getint("longueur")
largeur = display.getint("largeur")
flags = display.getint("flags")
vsinc = display.getint("vsinc")

fenetre = pygame.display.set_mode((longueur, largeur), flags, vsinc) # affiche la fenetre et la stocke en tant que surface

# charge les image 
fond = pygame.image.load("assets\menu/fond.png").convert() # image pour le fond du menu 
fond = pygame.transform.scale(fond, (longueur, largeur)) # change la taille de l'image par rapport a la fenêtre
img = [ pygame.image.load("assets/menu/buttons_large1.png"), 
        pygame.image.load("assets\menu/buttons_large2.png")] # images pour les bouton 

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

    police = pygame.font.SysFont("Roboto", size) # configure la police d'écriture
    texte = police.render(text, False, (255, 255, 255)) # ecrit le texte et donne sa couleur
    rect_bouton = pygame.draw.rect(fenetre, (background), rect=(x, y, texte.get_width(), texte.get_height()))
    fenetre.blit(texte, rect_bouton) # affiche le texte et son rectangle dans la fenêtre

    return rect_bouton # retourne les coordonnées x et y du rectangle et sa dimension (largeur, hauteur)

def afficher_menu_principale () :
        
    # éfface la fenêtre (le fond devient noir)
    fenetre.fill((0, 0, 0))

    # affiche le fond 
    fenetre.blit(fond, (0, 0))

    # affcihe le titre et les bouton
    #dessiner_texte("JDR Kingdom Heart", 24, (0, 0, 0), longueur*0.5, largeur*0.2)
    bouton_continuer = dessiner_texte("continuer", 16, (0, 0, 0), longueur*0.2, largeur*0.2)
    bouton_nouveau = dessiner_texte("nouvelle parti", 16, (0, 0, 0), longueur*0.2, largeur*0.4)
    bouton_charger = dessiner_texte("charger parti", 16, (0, 0, 0), longueur*0.2, largeur*0.5)
    bouton_option = dessiner_texte("options", 16, (0, 0, 0), longueur*0.2, largeur*0.6)
    bouton_quitter = dessiner_texte("quitter", 16, (0, 0, 0), longueur*0.2, largeur*0.7)

