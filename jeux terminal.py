import keyboard
import os
import time

jeu = True

class Map :

    def __init__(self, largeur, hauteur) :
        """ initialise la map 

        Args:
            largeur (int): largeur de la map
            hauteur (int): hauteur de la map
        """
        
        self.largeur = largeur
        self.hauteur = hauteur
        self.grille = [["_" for _ in range(largeur)] for _ in range(hauteur)]
    
    def afficher_map (self) :
        """ affiche la map ou sera afficher le joueur, le decor, les énnemi 

            on parcour la grille une premiere fois par ses ligne et une seconde fois pas ses case, 
            puis on verifie s'il y a un joueur on l'affiche, sinon on affiche un underscore 
        """

        for ligne in self.grille :

            for case in ligne :

                if isinstance(case, Joueur) :
                    print("J", end="    ")
                    
                else :
                    print("_", end="    ")
            
            print("\n")
        
    def afficher_joueur (self) :
        """ méthode qui positionne le joueur au centre de la map, lors de sa premiere apparition
        """

        J_posx = self.largeur // 2
        J_posy = self.hauteur // 2

        self.grille[J_posy][J_posx] = Joueur(J_posx, J_posy)
    
    def jouer_un_tour (self) :
        """ méthode pour jouer un tour
        """

        liste_joueur = []

        for ligne in self.grille :
            for case in ligne :
                if isinstance(case, Joueur) :
                    liste_joueur.append(case)
        
        for joueur in liste_joueur :
            joueur.se_deplacer()
        
        self.afficher_map()

class Joueur :

    def __init__(self, x, y) :
        
        self.posX = x
        self.posY = y
    
    def se_deplacer (self) :
        """ méthode pour déplacé le joueur sur la map

            une boucle qui vient répéter jusqu'a ce que l'on est appuyer sur une touche du clavier correspondante,
            si une touche (left, right, up, down) et appuyer on sauvegarde sa position précédante puis on ajoute ou enleve 1 selon la touche presser,

            on vérifie si la position en x ou y ne sort pas de l'index de la liste (la map) et on déplace le joueur dans la direction souhaité,
            sinon on restore sa position actuel
        """

        event = True 

        while event :

            if keyboard.is_pressed("left") :
                posX_preced = self.posX
                self.posX -= 1 

                if self.posX >= 0 :
                    monde.grille[self.posY][self.posX] = self
                    monde.grille[self.posY][self.posX + 1] = "_"
                else :
                    self.posX = posX_preced
                event = False

            elif keyboard.is_pressed("right") :
                posX_preced = self.posX
                self.posX += 1
                
                if self.posX < monde.largeur :
                    monde.grille[self.posY][self.posX] = self
                    monde.grille[self.posY][self.posX - 1] = "_"
                else :
                    self.posX = posX_preced
                event = False

            elif keyboard.is_pressed("up") :
                posY_preced = self.posY
                self.posY -= 1

                if self.posY >= 0 :
                    monde.grille[self.posY][self.posX] = self
                    monde.grille[self.posY + 1][self.posX] = "_"
                else :
                    self.posY = posY_preced
                event = False

            elif keyboard.is_pressed("down") :
                posY_preced = self.posY
                self.posY += 1

                if self.posY < monde.hauteur :
                    monde.grille[self.posY][self.posX] = self
                    monde.grille[self.posY - 1][self.posX] = "_"
                else :
                    self.posY = posY_preced
                event = False              


monde = Map(11, 11)
monde.afficher_joueur()
monde.afficher_map()

while jeu :

    print("-----------------------")
    monde.jouer_un_tour()