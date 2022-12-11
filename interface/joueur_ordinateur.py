"""
La classe JoueurOrdinateur

Hérite de Joueur et contient une "intelligence artificielle" extrêmement rudimentaire.
"""

from random import randint
from jeu.joueur import Joueur


#### DÉBUT DÉFI JOUEUR ORDINATEUR ####

class JoueurOrdinateur(Joueur):  # N'oubliez pas d'hériter de Joueur !!
    def __init__(self, numero_joueur, des_initiaux, arene):
        super().__init__(numero_joueur, des_initiaux, arene)
        # Supprimer la ligne du raise, et ajoutez l'appel à super().__init__
        #raise ValueError("Le défi Joueur Ordinateur n'a pas encore été réalisé!")

    # Écrivez les 4 méthodes demandées.

    def decision_continuer(self):
        """
        Détermine si le joueur souhaite continuer son tour.
        Doit être implémenté par la classe JoueurOrdinateur.
        """
        # raise NotImplementedError("La classe enfant JoueurOrdinateur doit implémenter cette méthode. ")
        continuer = True
        valeur_aleatoire = randint(1, 4)
        if valeur_aleatoire == 1:
            continuer = False
        return continuer

    def choisir_coordonnees(self):
        """
        Détermine comment le joueur choisit les coordonnées de son lancer.
        Doit être implémenté par les classes enfant de Joueur.
        """
        # raise NotImplementedError("Les classes enfant doivent implémenter cette méthode. ")

        return self.piger_coordonnees()

    def choisir_angle(self):
        """
        Détermine comment le joueur choisit l'angle de son lancer.
        Doit être implémenté par les classes enfant de Joueur.
        """
        # raise NotImplementedError("Les classes enfant doivent implémenter cette méthode. ")

        return self.piger_angle()

    def choisir_puissance(self):
        """
        Détermine comment le joueur choisit la puissance de son lancer.
        Doit être implémenté par les classes enfant de Joueur.
        """
        # raise NotImplementedError("Les classes enfant doivent implémenter cette méthode. ")

        return self.piger_puissance()



#### FIN DÉFI JOUEUR ORDINATEUR ####
