import pygame

def dessiner_texte (surf, text, size, background, x, y) :
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
    rect_bouton = pygame.draw.rect(surf, (background), rect=(x, y, texte.get_width(), texte.get_height()))
    surf.blit(texte, rect_bouton) # affiche le texte et son rectangle dans la fenêtre

    return rect_bouton, texte # retourne les coordonnées x et y du rectangle et sa dimension (largeur, hauteur)

def gerer_collision_souri (surf, list_rect) :
    """ gestion de la collision de la souris, lorsqu'on détecte le pointeur de la souris au coordoné du rectangle
        on affiche l'image qui du bouton.

    Args:
        list_rect (liste): liste des rectangle 
    """

    img = [ pygame.image.load("assets/menu/buttons_large1.png").convert(), 
            pygame.image.load("assets\menu/buttons_large2.png").convert()] # images pour les bouton 

    # position de la souris 
    mouse_pos = pygame.mouse.get_pos()

    # parcour la liste des rectangle par l'index pour vérifier la collision entre un rectangle et la souris (le pointeur),
    # affiche l'image du bouton redimensionné selon la taille du texte, puis le texte centrer à l'intérieur
    for i in range(len(list_rect)) :

        if list_rect[i][0].collidepoint(mouse_pos) :
            
            rect_width = list_rect[i][0].width
            rect_height = list_rect[i][0].height
            if pygame.mouse.get_pressed(num_buttons=3) == (1, 0, 0):
                img[1] = pygame.transform.scale(img[1], (rect_width*1.30, rect_height*1.50))
                pos_img = surf.blit(img[1], list_rect[i][0])
            else :
                img[0] = pygame.transform.scale(img[0], (rect_width*1.30, rect_height*1.50))
                pos_img = surf.blit(img[0], list_rect[i][0])

            btn_surf = pygame.Surface.copy(list_rect[i][1])
            centrer_bouton = btn_surf.get_rect(center=pos_img.center)

            surf.blit(btn_surf, centrer_bouton)          

def gerer_event_menu (list_rect) :

    # position de la souris 
    mouse_pos = pygame.mouse.get_pos()

    for i in range(len(list_rect)) :
        if list_rect[i][0].collidepoint(mouse_pos) :

            for event in pygame.event.get() :
                if pygame.mouse.get_pressed(num_buttons=3) == (1, 0, 0) :
                    if event.type == pygame.MOUSEBUTTONDOWN :

                        if list_rect[i][0] == list_rect[0][0] :
                            if list_rect[i][0].collidepoint(mouse_pos) :
                                choix = "continuer"

                        elif list_rect[i][0] == list_rect[1][0] :
                            if list_rect[i][0].collidepoint(mouse_pos) :
                                choix = "nouveau"

                        elif list_rect[i][0] == list_rect[2][0] :
                            if list_rect[i][0].collidepoint(mouse_pos) :
                                choix = "charger"

                        elif list_rect[i][0] == list_rect[3][0] :
                            if list_rect[i][0].collidepoint(mouse_pos) :
                                choix = "options"

                        elif list_rect[i][0] == list_rect[4][0] :
                            if list_rect[i][0].collidepoint(mouse_pos) :
                                choix = "quitter"

                        return choix

def gerer_event_options (list_rect) :

    # position de la souris 
    mouse_pos = pygame.mouse.get_pos()

    for i in range(len(list_rect)) :
        if list_rect[i][0].collidepoint(mouse_pos) :

            for event in pygame.event.get() :
                if pygame.mouse.get_pressed(num_buttons=3) == (1, 0, 0) :
                    if event.type == pygame.MOUSEBUTTONDOWN :

                        if list_rect[i][0] == list_rect[0][0] :
                            if list_rect[i][0].collidepoint(mouse_pos) :
                                choix = "Général"

                        elif list_rect[i][0] == list_rect[1][0] :
                            if list_rect[i][0].collidepoint(mouse_pos) :
                                choix = "Affichage"

                        elif list_rect[i][0] == list_rect[2][0] :
                            if list_rect[i][0].collidepoint(mouse_pos) :
                                choix = "Son"

                        elif list_rect[i][0] == list_rect[3][0] :
                            if list_rect[i][0].collidepoint(mouse_pos) :
                                choix = "Commande"

                        elif list_rect[i][0] == list_rect[4][0] :
                            if list_rect[i][0].collidepoint(mouse_pos) :
                                choix = "retour"

                        return choix