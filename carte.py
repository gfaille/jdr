from dataclasses import dataclass
import pygame
from pytmx.util_pygame import load_pygame
import pytmx
import pyscroll

@dataclass
class Map :
    name: str
    collision: list[pygame.Rect]
    groupe: pyscroll.PyscrollGroup
    tmx_data: pytmx.TiledMap

class Gestionnaire_de_carte :

    def __init__(self, fenetre, joueur) :
        self.cartes = dict()
        self.fenetre = fenetre
        self.joueur = joueur
        self.carte_actuel = "carte"

        self.enregistrer_carte("carte")

        self.teleporter_joueur("joueur")
    
    def verifier_collision (self) :

        for sprite in self.obtenir_groupe().sprites() :
            if sprite.rect.collidelist(self.obtenir_collision()) != -1 :
                sprite.annuler_deplacement()
        
    def teleporter_joueur (self, nom) :
        point = self.obtenir_object(nom)
        self.joueur.position[0] = point.x
        self.joueur.position[1] = point.y
        self.joueur.sauvegarder_position()
    
    def enregistrer_carte (self, nom) :

        # charger la carte du jeu (tmx)
        tmx_data = load_pygame(f"assets/map/{nom}.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.fenetre.get_size())  
        map_layer.zoom = 2  

        # definir les rectangles de collisions
        collision = []

        for obj in tmx_data.objects :
            if obj.name == "collision" :
                collision.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le group de calque 
        groupe = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer = 3)   
        groupe.add(self.joueur) 

        # creer l'object carte
        self.cartes[nom] = Map(nom, collision, groupe, tmx_data)
    
    def obtenir_carte (self) :
        return self.cartes[self.carte_actuel]

    def obtenir_groupe (self) :
        return self.obtenir_carte().groupe
    
    def obtenir_collision (self) :
        return self.obtenir_carte().collision
    
    def obtenir_object (self, nom) :
        return self.obtenir_carte().tmx_data.get_object_by_name(nom)

    
    def dessiner (self) :
        self.obtenir_groupe().draw(self.fenetre)
        self.obtenir_groupe().center(self.joueur.rect.center)
    
    def mise_a_jour (self) :
        self.obtenir_groupe().update()
        self.verifier_collision()