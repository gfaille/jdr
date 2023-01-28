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
img = [ pygame.image.load("assets/menu/buttons_large1.png").convert(), 
        pygame.image.load("assets\menu/buttons_large2.png").convert()] # images pour les bouton 

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
    texte = police.render(text, False, (0, 0, 0)) # ecrit le texte et donne sa couleur
    rect_bouton = pygame.draw.rect(fenetre, (background), rect=(x, y, texte.get_width(), texte.get_height()))
    fenetre.blit(texte, rect_bouton) # affiche le texte et son rectangle dans la fenêtre

    return rect_bouton, texte # retourne les coordonnées x et y du rectangle et sa dimension (largeur, hauteur)

def gerer_collision_souri (list_rect) :
    """ fonction qui vérifie si il y a collision entre la souris et la liste des rectangle 
        si il y a collision on affiche l'image du bouton redimensionné 

    Args:
        list_rect (liste): liste qui contien les rectangle 
    """

    # position de la souris 
    mouse_pos = pygame.mouse.get_pos()

    # parcour la liste des rectangle par l'index pour vérifier la collision entre un rectangle et la souris (le pointeur)
    for i in range(len(list_rect)) :

        if list_rect[i][0].collidepoint(mouse_pos) :

            rect_width = list_rect[i][0].width
            rect_height = list_rect[i][0].height
            img[0] = pygame.transform.scale(img[0], (rect_width, rect_height))
            fenetre.blit(img[0], list_rect[i][0]) # affiche l'image a la position du texte
            print(img[0])
            # copy de la surface (le texte), puis affiche le texte par dessus l'image
            btn_surf = pygame.Surface.copy(list_rect[i][1])
            fenetre.blit(btn_surf, list_rect[i][0])

def afficher_menu_principale () :
        
    # éfface la fenêtre (le fond devient noir)
    fenetre.fill((0, 0, 0))

    # affiche le fond 
    fenetre.blit(fond, (0, 0))

    # affcihe le titre et les bouton
    #dessiner_texte("JDR Kingdom Heart", 24, (0, 0, 0), longueur*0.5, largeur*0.2)
    bouton_continuer = dessiner_texte("continuer", 16, (255, 255, 255, 128), longueur*0.1, largeur*0.8)
    bouton_nouveau = dessiner_texte("nouvelle", 16, (255, 255, 255, 128), (bouton_continuer[0].x + bouton_continuer[0].width) * 1.2, largeur*0.8)
    bouton_charger = dessiner_texte("charger", 16, (255, 255, 255, 128), (bouton_nouveau[0].x + bouton_nouveau[0].width) * 1.2, largeur*0.8)
    bouton_option = dessiner_texte("options", 16, (255, 255, 255, 128), (bouton_charger[0].x + bouton_charger[0].width) * 1.7, largeur*0.8)
    bouton_quitter = dessiner_texte("quitter", 16, (255, 255, 255, 128), (bouton_option[0].x + bouton_option[0].width) * 1.2, largeur*0.8)

    # liste des bouton 
    list_btn = [bouton_continuer, 
                bouton_nouveau, 
                bouton_charger, 
                bouton_option, 
                bouton_quitter]

    # vérifi si il y a collision avec la souris
    gerer_collision_souri(list_btn)