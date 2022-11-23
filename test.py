import pygame

# initialisation du module pygame
pygame.init()

# affichage de la fenêtre pygame en 720p
longueur = 1280
largeur = 720
flags = pygame.SHOWN
fenetre = pygame.display.set_mode((longueur, largeur), flags)


""" # dessiner du texte sur une nouvelle Surface créer un rectangle pour la surface centrée à une position donnée du menu des options
text_resolution = police.render("Affichage", 1, (255, 255, 255))
text_touche_clavier = police.render("Raccourcie clavier", 1, (255, 255, 255))
text_son = police.render("Son", 1, (255, 255, 255))
text_retour = police.render("Retour", 1, (255, 255, 255))

bouton_resolution = text_resolution.get_rect(center=(window.longueur*0.20, window.largeur/1.25))
bouton_son = text_son.get_rect(center=(window.longueur*0.40, window.largeur/1.25))
bouton_raccourci = text_touche_clavier.get_rect(center=(window.longueur*0.60, window.largeur/1.25))
bouton_retour = text_retour.get_rect(center=(window.longueur*0.80, window.largeur/1.25))

# initialisation des options d'affichage (rendu + position)
text_resolution_ntsc = police.render("720 X 480", 1, (255, 255, 255))
text_resolution_svga = police.render("800 X 600", 1, (255, 255, 255))
text_resolution_xga = police.render("1024 X 768", 1, (255, 255, 255))
text_resolution_hd = police.render("1280 X 720", 1, (255, 255, 255))
text_resolution_wsxga = police.render("1680 X 1050", 1, (255, 255, 255))
text_resolution_fhd = police.render("1920 X 1280", 1, (255, 255, 255))
#######################################################################
bouton_resolution_ntsc = text_resolution_ntsc.get_rect(center=(window.longueur*0.20, window.largeur*0.2))
bouton_resolution_svga = text_resolution_svga.get_rect(center=(window.longueur*0.20, window.largeur*0.2))
bouton_resolution_xga = text_resolution_xga.get_rect(center=(window.longueur*0.20, window.largeur*0.2))
bouton_resolution_hd = text_resolution_hd.get_rect(center=(window.longueur*0.20, window.largeur*0.2))
bouton_resolution_wsxga = text_resolution_wsxga.get_rect(center=(window.longueur*0.20, window.largeur*0.2))
bouton_resolution_fhd = text_resolution_fhd.get_rect(center=(window.longueur*0.20, window.largeur*0.2)) """

""" # creation du selecteur de menu
select = pygame.image.load("sprites/arrow.png")
select_width = select.get_width()
select_height = select.get_height()
select = pygame.transform.smoothscale(select, (select_height/2, select_width/2)) """

##################################################################################################################################


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

            for event in pygame.event.get():
                
                if event.type == pygame.MOUSEBUTTONDOWN :
                    if bouton_retour.collidepoint(event.pos) :
                        menu = "menu"

        pygame.display.flip() # mise à jour total de l'écran

pygame.quit()
