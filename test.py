import pygame

# initialisation du module pygame
pygame.init()

# affichage de la fenêtre pygame en 720p
longueur = 1280
largeur = 720
flags = pygame.SHOWN
fenetre = pygame.display.set_mode((longueur, largeur), flags)

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
game = False # variable pour le jeux (False on est dans le menu, True on est dans le jeux)
menu = "menu" # variable pour le menu, permet de naviger dans divers menu et sous-menu
option_menu = "" # variable pour naviguer dans les sous-menu 
is_fullscreen = False # variable pour déterminé si on est en plein écran

# boucle principal
while continuer :
   
   # vérifie si game est sur vrai sinon affiche notre menu
    if game :
        fenetre.fill((255, 0, 0))

        pygame.display.flip() # mise à jour total de l'écran
    else :
        
        # on vérifie si on est dans un menu ou un sous-menu (options, affichage, ...)
        if menu == "menu":

            # éfface l'ecran
            fenetre.fill((0, 0, 0))

            # affiche les bouton de notre menu principale (écran d'accueil) et le titre 
            dessiner_texte("JDR Kingdom Heart", 32, (0, 0, 0), longueur*0.35, largeur*0.10)
            bouton_continuer = dessiner_texte("continuer", 16, (51, 101, 138), longueur*0.15, largeur*0.25)
            bouton_nouveau = dessiner_texte("nouvelle partie", 16, (51, 101, 138), longueur*0.15, largeur*0.35)
            bouton_charger = dessiner_texte("charger une partie", 16, (51, 101, 138), longueur*0.15, largeur*0.45)
            bouton_options = dessiner_texte("options", 16, (51, 101, 138), longueur*0.15, largeur*0.55)
            bouton_quiter = dessiner_texte("quitter", 16, (51, 101, 138), longueur*0.15, largeur*0.65)

            # capture les event au clavier (echap pour quitter) et les event a la souris (clique sur un bouton)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN :     
                    if event.key == pygame.K_ESCAPE :
                        continuer = False
                
                elif event.type == pygame.MOUSEBUTTONDOWN :

                    if bouton_continuer.collidepoint(event.pos):
                        pass

                    elif bouton_nouveau.collidepoint(event.pos) :
                        game = True

                    elif bouton_charger.collidepoint(event.pos) :
                        pass

                    elif bouton_options.collidepoint(event.pos) :
                        menu = "options"

                    elif bouton_quiter.collidepoint(event.pos) :
                        continuer = False

        elif menu == "options" :

            # éfface l'ecran
            fenetre.fill((0, 0, 0))

            # affiche les boutons pour les divers options (affichage, son, touche clavier, retour)
            dessiner_texte("Options", 32, (0, 0, 0), longueur*0.45, largeur*0.10)
            bouton_affichage = dessiner_texte("affichage", 16, (51, 101, 138), longueur*0.15, largeur*0.20)
            bouton_son = dessiner_texte("son", 16, (51, 101, 138), longueur*0.15, largeur*0.30)
            bouton_raccourci = dessiner_texte("raccourci clavier", 16, (51, 101, 138), longueur*0.15, largeur*0.40)
            bouton_retour = dessiner_texte("Retour", 16, (51, 101, 138), longueur*0.15, largeur*0.50)

            # affiche le paramètre des options d'affichage
            if option_menu == "affichage" :

                # éfface l'ecran
                fenetre.fill((0, 0, 0))

                # affiche les boutons pour les options d'affichage (résolution, taille ecran, ...) et le titre
                dessiner_texte("Affichage", 32, (0, 0, 0), longueur*0.45, largeur*0.10)
                dessiner_texte("Résolution", 18, (0, 0, 0), longueur*0.14, largeur*0.20)
                bouton_resolution_ntsc = dessiner_texte("720 X 480", 16, (51, 101, 138), longueur*0.15, largeur*0.30)
                bouton_resolution_svga = dessiner_texte("800 X 600", 16, (51, 101, 138), longueur*0.15, largeur*0.40)
                bouton_resolution_xga = dessiner_texte("1024 X 768", 16, (51, 101, 138), longueur*0.15, largeur*0.50)
                bouton_resolution_hd = dessiner_texte("1280 X 720", 16, (51, 101, 138), longueur*0.15, largeur*0.60)
                bouton_resolution_wsxga = dessiner_texte("1680 X 1050", 16, (51, 101, 138), longueur*0.15, largeur*0.70)
                bouton_resolution_fhd = dessiner_texte("1920 X 1280", 16, (51, 101, 138), longueur*0.15, largeur*0.80)
                bouton_fullscrenn = dessiner_texte("fullscrenn", 16, (51, 101, 138), longueur*0.50, largeur*0.25)

                for event in pygame.event.get() :
                    if event.type == pygame.MOUSEBUTTONDOWN :
                       
                       # capture les event de la souris dans les options d'affichages
                        if bouton_resolution_ntsc.collidepoint(event.pos) :
                            longueur, largeur = 720, 480
                            fenetre = pygame.display.set_mode((longueur, largeur), flags)
                        elif bouton_resolution_svga.collidepoint(event.pos) :
                            longueur, largeur = 800, 600
                            fenetre = pygame.display.set_mode((longueur, largeur), flags)
                        elif bouton_resolution_xga.collidepoint(event.pos) :
                            longueur, largeur = 1024, 768
                            fenetre = pygame.display.set_mode((longueur, largeur), flags)
                        elif bouton_resolution_hd.collidepoint(event.pos) :
                            longueur, largeur = 1280, 720
                            fenetre = pygame.display.set_mode((longueur, largeur), flags)
                        elif bouton_resolution_wsxga.collidepoint(event.pos) :
                            longueur, largeur = 1680, 1050
                            fenetre = pygame.display.set_mode((longueur, largeur), flags)
                        elif bouton_resolution_fhd.collidepoint(event.pos) :
                            longueur, largeur = 1920, 1280
                            fenetre = pygame.display.set_mode((longueur, largeur), flags)
                        elif bouton_fullscrenn.collidepoint(event.pos) :
                            if is_fullscreen == False :
                                flags = pygame.FULLSCREEN | pygame.SCALED
                                fenetre = pygame.display.set_mode((longueur, largeur), flags)
                                is_fullscreen = True
                            else :
                                flags = pygame.SHOWN
                                fenetre = pygame.display.set_mode((longueur, largeur), flags)
                                is_fullscreen = False

            # affiche les paramètre de son
            elif option_menu == "son" :

                # éfface l'ecran
                fenetre.fill((0, 0, 0))

            # affiche les paramètre des raccourci clavier
            elif option_menu == "raccourci" :

                # éfface l'ecran
                fenetre.fill((0, 0, 0))

            for event in pygame.event.get():
                
                if event.type == pygame.MOUSEBUTTONDOWN :

                    # capture les event de la souris dans les options 
                    if bouton_retour.collidepoint(event.pos) :
                        menu = "menu"

                    elif bouton_affichage.collidepoint(event.pos) :
                        option_menu = "affichage"

                    elif bouton_son.collidepoint(event.pos) :
                        option_menu = "son"

                    elif bouton_raccourci.collidepoint(event.pos) :
                        option_menu = "raccourci"
                         
        pygame.display.flip() # mise à jour total de l'écran

pygame.quit()
