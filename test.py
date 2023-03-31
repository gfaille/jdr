import os
import configparser
import pygame

# initialise configparser
config = configparser.ConfigParser()

# initialisation du module pygame
pygame.init()

# si le fichier config.ini n'existe pas on le créer 
if not os.path.isfile("config.ini") :
    config["affichage"] = {
        "longueur" : 1280,
        "largeur" : 720, 
        "flags" : pygame.SHOWN
    }

    with open("config.ini", "w") as configfile :
        config.write(configfile)

# lis le fichier config.ini
config.read("config.ini")

# recupére et stocke la sections affichage
display = config["affichage"]

# affichage de la fenêtre pygame en 720p
longueur = display.getint("longueur")
largeur = display.getint("largeur")
flags = display.getint("flags")
fenetre = pygame.display.set_mode((longueur, largeur), flags)

horloge = pygame.time.Clock() # créer l'object clock (une horloge)
fps = 60 # sauvegarde les fps

# charge les images
riku_arret_haut = pygame.image.load("assets\sprites\Riku_arret_haut.png")
riku_arret_bas = pygame.image.load("assets\sprites\Riku_arret_bas.png")
riku_arret_gauche = pygame.image.load("assets\sprites\Riku_arret_gauche.png")
riku_marche_haut_gauche = pygame.image.load("assets\sprites\Riku_marche_haut2.png")
riku_marche_haut_droite = pygame.image.load("assets\sprites\Riku_marche_haut.png")
riku_marche_bas_gauche = pygame.image.load("assets\sprites\Riku_marche_bas2.png")
riku_marche_bas_droite = pygame.image.load("assets\sprites\Riku_marche_bas.png")
riku_marche_gauche_gauche = pygame.image.load("assets\sprites\Riku_marche_gauche.png")
riku_marche_gauche_droite = pygame.image.load("assets\sprites\Riku_marche_gauche2.png")
riku_marche_droite_droite = pygame.transform.flip(riku_marche_gauche_droite, True, False)
riku_marche_droite_gauche = pygame.transform.flip(riku_marche_gauche_gauche, True, False)
maison_pf = pygame.image.load("assets\environnement\maison exterieure\petite maison pf.png")
maison_po = pygame.image.load("assets\environnement\maison exterieure\petite maison po.png")

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

def dessiner_box (cocher, background, x, y , width, height) :
    """ fonction qui permet de créer des box (ils peuvent être coché)

    Args:
        cocher (Bool): vérifier si c'est la box est cocher
        background (int): donne la couleur en RGB
        x (in): donne la position en x
        y (int): donne la position en x
        width (int): donne les dimentions en largeur
        height (int): donne les dimensions en hauteur

    Returns:
        rect: retourne le rectangle créer
    """

    if cocher == False :
        # créer un rectangle vide 
        rect_btn = pygame.draw.rect(fenetre, (background), rect=(x, y, width, height))
        return rect_btn
    else :
        # créer un rectangle qui contient une croix
        rect_btn = pygame.draw.rect(fenetre, (background), rect=(x, y, width, height))
        pygame.draw.line(fenetre, (255, 255, 255), start_pos=(rect_btn.topleft), end_pos=(rect_btn.bottomright))
        pygame.draw.line(fenetre, (255, 255, 255), start_pos=(rect_btn.topright), end_pos=(rect_btn.bottomleft))
        return rect_btn

def jouer_musique (chemins, volume) :
    """ fonction pour jouer de la musique, charge, puis joue la musique 

    Args:
        chemins (string): donne le chemins du fichier
        volume (int): donne le volume à la quelle la musique sera jouer
    """

    pygame.mixer.music.load(chemins) # charge la musique selectionné
    pygame.mixer.music.set_volume(volume) # modifie le volume
    pygame.mixer.music.play() # joue la musique

def slider (pos_start, pos_end, background_btn, pos_x, pos_y) :
    """ fonction pour créer un slider 

    Args:
        pos_start (tuple): donne la position de départ à notre ligne x et y
        pos_end (tuple): donne la position final à notre ligne x et y
        background_btn (tuple): donne la couleur de l'arriere plan (RGB)
        pos_x (int): donne la coordonnée en x 
        pos_y (int): donne la coordonnée en xy

    Returns:
        rect: retourne le rectangle du curseur 
    """

    # creer le slider
    pygame.draw.line(fenetre, (255, 255, 255), pos_start, pos_end)
    btn = pygame.draw.rect(fenetre, background_btn, (pos_x, pos_y*0.95, 20, 20))
    return btn

continuer = True
game = False # variable pour le jeux (False on est dans le menu, True on est dans le jeux)
menu = "menu" # variable pour le menu, permet de naviger dans divers menu et sous-menu
option_menu = "" # variable pour naviguer dans les sous-menu 
is_fullscreen = False # variable pour déterminé si on est en plein écran
L, l = None, None
x = longueur*0.60 # variable pour positionné le curseur du slider
volume = 1.0 # le volume du son
moving = False # variable pour déterminé si on déplace le curseur

# détermine si une case est vrai (musique, effets)
musique = True 
effets = True 

# déplacement pour le joueur
x_riku = longueur*0.4
y_riku = largeur*0.8
v_riku = 5
riku = True

# maison (porte ouvert ou fermé)
it = 0
maison = [maison_pf, maison_po]

if musique == True :
    jouer_musique("assets/son/1-01 Dearly Beloved (KINGDOM HEARTS).mp3", volume)

# boucle principal
while continuer :
    
   # vérifie si game est sur vrai sinon affiche notre menu
    if game :
        pygame.mixer.music.stop()
        fenetre.fill((0, 0, 0))
        
        m = fenetre.blit(maison[it], (longueur*0.5, largeur*0.1))
        arret = fenetre.blit(riku_arret_haut, (x_riku, y_riku))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :     
                if event.key == pygame.K_ESCAPE :
                    continuer = False

        # vérifie si le joueur entre en collision avec la maison
        riku_maison_arret = pygame.Rect.colliderect(riku_arret_haut.get_rect(center=(x_riku, y_riku)), m)
        riku_haut = pygame.Rect.colliderect(riku_marche_haut_droite.get_rect(center=(x_riku, y_riku)), m)

        if riku_haut == True :
            # si on appui sur entré on change l'index de l'affichage de la maison
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RETURN :
                    if riku_maison_arret == True :
                        it = 1
        else :
            # fait avancer riku vers le haut de la fenetre lorsqu'on appuis sur fleche du haut
            if pygame.key.get_pressed()[pygame.K_UP] :

                # éfface l'ecran
                fenetre.fill((0, 0, 0))
                m = fenetre.blit(maison[it], (longueur*0.5, largeur*0.1))

                pygame.time.delay(150) # on met sur pause durant 150 millisecondes
                y_riku -= v_riku # on diminue l'axe y par rapport la velocité

                # le changement de sprite (image)
                if riku == True :
                    fenetre.blit(riku_marche_haut_droite, (x_riku, y_riku))
                    riku = False
                else :
                    fenetre.blit(riku_marche_haut_gauche, (x_riku, y_riku))
                    riku = True
        # restore la variable it à 0 pour afficher la maison avec la porte fermée
        if riku_haut == False and riku_maison_arret == False :
            it = 0  
            
        # fait avancer riku vers le bas de la fenetre lorsqu'on appuis sur fleche du bas
        if pygame.key.get_pressed()[pygame.K_DOWN] :

            # éfface l'ecran
            fenetre.fill((0, 0, 0))
            m = fenetre.blit(maison[it], (longueur*0.5, largeur*0.1))

            pygame.time.delay(150) # on met sur pause durant 150 millisecondes
            y_riku += v_riku # on diminue l'axe y par rapport la velocité

            # le changement de sprite (image)
            if riku == True :
                fenetre.blit(riku_marche_bas_droite, (x_riku, y_riku))
                riku = False
            else :
                fenetre.blit(riku_marche_bas_gauche, (x_riku, y_riku))
                riku = True

        # fait avancer riku vers la gauche de la fenetre lorsqu'on appuis sur fleche gauche
        if pygame.key.get_pressed()[pygame.K_LEFT] :

            # éfface l'ecran
            fenetre.fill((0, 0, 0))
            m = fenetre.blit(maison[it], (longueur*0.5, largeur*0.1))

            pygame.time.delay(150) # on met sur pause durant 150 millisecondes
            x_riku -= v_riku # on diminue l'axe y par rapport la velocité

            # le changement de sprite (image)
            if riku == True :
                fenetre.blit(riku_marche_gauche_droite, (x_riku, y_riku))
                riku = False
            else :
                fenetre.blit(riku_marche_gauche_gauche, (x_riku, y_riku))
                riku = True
        
        # fait avancer riku vers la droite de la fenetre lorsqu'on appuis sur fleche droite
        if pygame.key.get_pressed()[pygame.K_RIGHT] :

            # éfface l'ecran
            fenetre.fill((0, 0, 0))
            m = fenetre.blit(maison[it], (longueur*0.5, largeur*0.1))

            pygame.time.delay(150) # on met sur pause durant 150 millisecondes
            x_riku += v_riku # on diminue l'axe y par rapport la velocité

            # le changement de sprite (image)
            if riku == True :
                fenetre.blit(riku_marche_droite_droite, (x_riku, y_riku))
                riku = False
            else :
                fenetre.blit(riku_marche_droite_gauche, (x_riku, y_riku))
                riku = True

        pygame.time.Clock().tick(fps) # on fixe le nombre d'image par seconde (evite une téléportation de l'image)
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
            pygame.mixer.music.stop()
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

                # affiche le titre et les sous-titres
                dessiner_texte("Affichage", 32, (0, 0, 0), longueur*0.45, largeur*0.10)
                dessiner_texte("Résolution", 18, (0, 0, 0), longueur*0.24, largeur*0.20)
                
                # affiche les boutons pour les options d'affichage (résolution, taille ecran, ...) 
                bouton_resolution_ntsc = dessiner_texte("720 X 480", 16, (51, 101, 138), longueur*0.25, largeur*0.30)
                bouton_resolution_svga = dessiner_texte("800 X 600", 16, (51, 101, 138), longueur*0.25, largeur*0.40)
                bouton_resolution_xga = dessiner_texte("1024 X 768", 16, (51, 101, 138), longueur*0.25, largeur*0.50)
                bouton_resolution_hd = dessiner_texte("1280 X 720", 16, (51, 101, 138), longueur*0.25, largeur*0.60)
                bouton_resolution_wsxga = dessiner_texte("1680 X 1050", 16, (51, 101, 138), longueur*0.25, largeur*0.70)
                bouton_resolution_fhd = dessiner_texte("1920 X 1280", 16, (51, 101, 138), longueur*0.25, largeur*0.80)
                bouton_fullscrenn = dessiner_texte("fullscrenn", 16, (51, 101, 138), longueur*0.45, largeur*0.30)
                bouton_valide = dessiner_texte("Validé", 16, (51, 101, 138), longueur*0.65, largeur*0.80)
                bouton_retour = dessiner_texte("retour", 16, (51, 101, 138), longueur*0.75, largeur*0.80)

                for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_ESCAPE :
                            continuer = False
                    if event.type == pygame.MOUSEBUTTONDOWN :
                       
                       # capture les event de la souris dans les options d'affichages
                        if bouton_resolution_ntsc.collidepoint(event.pos) :
                            config["affichage"]["longueur"], config["affichage"]["largeur"] = "720", "480"

                        elif bouton_resolution_svga.collidepoint(event.pos) :
                            config["affichage"]["longueur"], config["affichage"]["largeur"]  = "800", "600"

                        elif bouton_resolution_xga.collidepoint(event.pos) :
                            config["affichage"]["longueur"], config["affichage"]["largeur"]  = "1024", "768"

                        elif bouton_resolution_hd.collidepoint(event.pos) :
                            config["affichage"]["longueur"], config["affichage"]["largeur"]  = "1280", "720"

                        elif bouton_resolution_wsxga.collidepoint(event.pos) :
                            config["affichage"]["longueur"], config["affichage"]["largeur"]  = "1680", "1050"

                        elif bouton_resolution_fhd.collidepoint(event.pos) :
                            config["affichage"]["longueur"], config["affichage"]["largeur"]  = "1920", "1280"

                        elif bouton_fullscrenn.collidepoint(event.pos) :
                            if is_fullscreen == False :
                                flags = pygame.FULLSCREEN | pygame.SCALED
                                config["affichage"]["flags"] = str(flags)
                                is_fullscreen = True
                            else :
                                flags = pygame.SHOWN
                                config["affichage"]["flags"] = str(flags)
                                is_fullscreen = False

                        elif bouton_valide.collidepoint(event.pos) :

                            # on applique les modification
                            longueur = config.getint("affichage", "longueur")
                            largeur = config.getint("affichage", "largeur")
                            flags = config.getint("affichage", "flags")
                            fenetre = pygame.display.set_mode((longueur, largeur), flags)
                            
                            # enregistre les nouvelle valeur dans le .ini
                            with open("config.ini", "w") as configfile :
                                config.write(configfile)

                        
                        elif bouton_retour.collidepoint(event.pos) :
                            option_menu = ""

            # affiche les paramètre de son
            elif option_menu == "son" :

                # éfface l'ecran
                fenetre.fill((0, 0, 0))

                # slider pour le volume 
                btn = slider((longueur*0.30, largeur*0.20), (longueur*0.60, largeur*0.20), (51, 101, 138), x, largeur*0.20)

                # texte et bouton 
                dessiner_texte("Volumes général", 18, (0, 0, 0), longueur*0.40, largeur*0.10)
                dessiner_texte("0", 20, (0, 0, 0), longueur*0.305, largeur*0.15)
                dessiner_texte("100", 20, (0, 0, 0), longueur*0.595, largeur*0.15)
                bouton_retour = dessiner_texte("retour", 16, (51, 101, 138), longueur*0.75, largeur*0.80)
                bouton_musique = dessiner_box(musique, (51, 101, 138), longueur*0.30, largeur*0.30, 20, 20)
                bouton_effets = dessiner_box(effets, (51, 101, 138), longueur*0.38, largeur*0.30, 20, 20)
                dessiner_texte("Musique", 18, (0, 0, 0), longueur*0.28, largeur*0.27)
                dessiner_texte("Effets sonnores", 18, (0, 0, 0), longueur*0.34, largeur*0.27)

                for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_ESCAPE :
                            continuer = False

                    elif event.type == pygame.MOUSEBUTTONDOWN :
                        #  on vérifie quel bouton est appuyer
                        if btn.collidepoint(event.pos) :
                            moving = True

                        elif bouton_retour.collidepoint(event.pos) :
                            option_menu = ""
                        
                        elif bouton_musique.collidepoint(event.pos) :
                            
                            if musique == True :
                                musique = False
                            else :
                                musique = True

                        elif bouton_effets.collidepoint(event.pos) :

                            if effets == True :
                                effets = False
                            else :
                                effets = True

                    elif event.type == pygame.MOUSEBUTTONUP :
                        moving = False
                    
                    # deplace le curseur pour modifier le volume
                    elif event.type == pygame.MOUSEMOTION and moving :
                        if event.pos[0] >= longueur*0.30 and event.pos[0] <= longueur*0.60 : 
                            if event.pos[0] < btn[0] :
                                x = event.pos[0]
                                volume = (btn[0] - longueur*0.30) / x *2
                            if event.pos[0] > btn[0] :
                                x = event.pos[0]
                                volume = (btn[0] - longueur*0.30) / x *2 

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
                        
            if musique == True :
                jouer_musique("assets/son/1-01 Dearly Beloved (KINGDOM HEARTS).mp3", volume)           
        pygame.display.flip() # mise à jour total de l'écran

pygame.quit()
