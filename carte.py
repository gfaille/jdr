import pygame
import pytmx
import pyscroll
from dataclasses import dataclass
from pytmx import load_pygame

@dataclass
class Object :
    monde_actuel : str
    object_cible : str
    interaction : str

@dataclass
class Portail :
    monde_actuel : str
    point_entrer : str
    monde_suivant : str
    point_sortie : str

@dataclass
class Carte :
    nom : str
    tmx_data : pytmx.TiledMap
    groupe : pyscroll.PyscrollGroup
    collision : list[pygame.Rect]
    portails : list[Portail]
    objects : list[Object]

class Gestionnaire_de_carte :

    def __init__(self, fenetre, joueur) -> None:
        self.cartes = dict()
        self.carte_actuel = "la maison abandonné"

        self.fenetre = fenetre
        self.joueur = joueur

        self.enregistrer_carte("la maison abandonné", portails=[
            Portail(monde_actuel = "la maison abandonné", 
                    point_entrer = "maison_abandonner",
                    monde_suivant = "donjon",
                    point_sortie = "entrer_donjon")
        ])
        self.enregistrer_carte("donjon", portails=[
            Portail(monde_actuel= "donjon",
                    point_entrer= "sorti_donjon",
                    monde_suivant= "la maison abandonné",
                    point_sortie= "sorti_maison_abandonner")
        ], objects=[
            Object(monde_actuel = "donjon",
                   object_cible = "bouton_porte",
                   interaction = "porte")
        ])

        self.telepoter_joueur("joueur")
    
    def enregistrer_carte (self, nom, portails=[], objects=[]) :
        tmx_data = load_pygame(f"assets/map/{nom}.tmx")

        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.fenetre.get_size())
        map_layer.zoom = 2

        groupe = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer = 3)
        groupe.add(self.joueur)

        # definir les rectangle de collision de la map
        collision =  []

        for object in tmx_data.objects :
            if object.type == "collision" :
                collision.append(pygame.Rect(object.x, object.y, object.width, object.height))
        
        self.cartes[nom] = Carte(nom, tmx_data, groupe, collision, portails, objects)

    def telepoter_joueur (self, nom) :
        point_joueur = self.obtenir_objects(nom)
        self.joueur.position[0] = point_joueur.x
        self.joueur.position[1] = point_joueur.y
        self.joueur.sauvegarder_position()
    
    def verifier_collision (self) :

        # collision
        for sprite in self.obtenir_groupe().sprites() :
            if sprite.rect_pied.collidelist(self.obtenir_collision()) != -1 :
                sprite.annuler_deplacement()
        
        # portail de deplacement 
        for portail in self.obtenir_carte().portails :
            if portail.monde_actuel == self.carte_actuel :
                point = self.obtenir_objects(portail.point_entrer)
                rect = pygame.Rect(point.x, point.y, point.width, point.height)

                if self.joueur.rect_pied.colliderect(rect) :
                    self.carte_actuel = portail.monde_suivant
                    self.telepoter_joueur(portail.point_sortie)
    
    def verifier_interaction (self) :

        # interaction porte / bouton
        for obj in self.obtenir_carte().objects :
            if obj.monde_actuel == self.carte_actuel :
                obj_interact = self.obtenir_objects(obj.object_cible)
                rect = pygame.Rect(obj_interact.x, obj_interact.y, obj_interact.width, obj_interact.height)

                if self.joueur.rect_pied.colliderect(rect) :
                    porte = self.obtenir_objects(obj.interaction)
                    rect = pygame.Rect(porte.x, porte.y, porte.width, porte.height)
                    
                    if rect in self.obtenir_collision() :
                        self.obtenir_collision().remove(rect)

    def obtenir_carte (self) :
        return self.cartes[self.carte_actuel]

    def obtenir_groupe (self) :
        return self.obtenir_carte().groupe
    
    def obtenir_collision (self) :
        return self.obtenir_carte().collision

    def obtenir_objects (self, nom_object) :
        return self.obtenir_carte().tmx_data.get_object_by_name(nom_object)
    
    def dessiner (self) :
        self.obtenir_groupe().draw(self.fenetre)
        self.obtenir_groupe().center(self.joueur.rect.center)
    
    def mise_a_jour (self) :
        self.obtenir_groupe().update()
        self.verifier_collision()