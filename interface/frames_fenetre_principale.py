"""
Module contenant des frames utilitaires présents dans la fenêtre principale.
"""
import tkinter
from tkinter import Frame, Label, Button, Scale, VERTICAL, IntVar

from interface.joueur_ordinateur import JoueurOrdinateur


class FrameDescription(Frame):
    def __init__(self, master):
        """
        Constructeur de la classe FrameDescription. Affiche un descriptif
        de ce qui se passe dans le jeu.

        Args:
            master (Tk): La fenêtre dans laquelle ce frame s'insert.
        """
        super().__init__(master)
        self.label_description = Label(self, text="")
        self.label_description.grid(row=0, column=0)

    def populer(self, texte, temps_attente, suite):
        """
        Cette méthode affiche les informations sur le jeu.

        Args:
            texte (str): Le message à afficher
            temps_attente (int): Temps en millisecondes avant d'exécuter la suite
            suite (fonction): La fonction à exécuter après
        """
        self.label_description['text'] = texte
        self.after(temps_attente, suite)

    def vider(self):
        """
        Cette méthode enlève l'affichage.
        """
        self.label_description['text'] = ""


class FrameJoueurActif(Frame):
    def __init__(self, master):
        """
        Constructeur de la classe FrameJoueurActif. Affiche les informations relatives au
        joueur dont c'est le tour.

        Args:
            master (Tk): La fenêtre dans laquelle ce frame s'insert.
        """
        super().__init__(master)

        self.label_nom_joueur = Label(self, text="")
        self.label_nombre_des = Label(self, text="")

        self.label_nom_joueur.grid(row=0, column=0)
        self.label_nombre_des.grid(row=1, column=0)

        self.clic_bouton = lambda: None
        self.bouton_terminer_tour = Button(self, text="Terminer le tour", command=self.appui_bouton)
        self.bouton_terminer_tour.grid(row=1, column=1)
        self.bouton_terminer_tour["state"] = "disabled"

        self.couleurs = [
            'blue', 'green', 'red', 'orange', 'purple'
        ]

    def populer(self, joueur):
        """
        Ajoute les informations d'un joueur dans le frame.

        Args:
            joueur (Joueur): le joueur dont c'est le tour
        """
        self.label_nom_joueur["text"] = f"Joueur # {joueur.numero_joueur}"
        self.label_nombre_des["text"] = f"{len(joueur.des)} dés"
        self.label_nom_joueur["fg"] = self.couleurs[joueur.numero_joueur - 1]
        self.label_nombre_des["fg"] = self.couleurs[joueur.numero_joueur - 1]

    def activer_bouton(self, fonction):
        """
        Permet de cliquer sur le bouton fin du tour, et associe la fonction au clic.

        Args:
            fonction (fonction): La fonction à exécuter suite au clic de bouton
        """
        self.bouton_terminer_tour["state"] = "normal"
        self.clic_bouton = fonction

    def appui_bouton(self):
        """
        Effectue la fonction à exécuter suite au clic de bouton, et grise le bouton.
        """
        self.bouton_terminer_tour["state"] = "disabled"
        self.clic_bouton()


class FrameTableauJoueurs(Frame):
    def __init__(self, master):
        super().__init__(master)
        """_summary_: Constructeur de la classe FrameTableauJoueurs. 
        """
        for i in range(len(self.master.joueurs)): #pour chaque joueur
            self.label_nom_joueur = Label(self, text=f"{self.master.joueurs[i]}", fg=self.master.frame_joueur.couleurs[i]).grid(row=i, column=0) #on affiche le label du joueur
    #ce contructeur fonctionne    

        
    def mise_a_jour(self):
        """_summary_: Cette méthode met à jour le frame tableau des joueurs.
        """
        for i in range(len(self.master.joueurs)): #pour chaque joueur
            libelle_joueur=str(self.master.joueurs[i]) #on récupère la string du joueur
            if libelle_joueur[10]=="0": #si le joueur n'a plus de dés
                libelle_joueur=libelle_joueur[:9]+"Éliminé!" #on ajoute "Éliminé!" à la fin de la string
            self.label_nom_joueur = Label(self, text=libelle_joueur, fg=self.master.frame_joueur.couleurs[i]).grid(row=i, column=0) #on met à jour le label du joueur
        #cette méthode fonctionne! Enfin!

class FrameTempsAttente(Frame):
    def __init__(self, master):
        super().__init__(master)
        #### DÉBUT DÉFI TEMPS ATTENTE ####
        # Je ne sais pas comment mais ça marche... :D :D :D 
        def nouvelle_fonction():
            return int(scale_temps.get())

        valeur = 250
        scale_temps = Scale(master, from_=10, to=500,variable=valeur)
        scale_temps.grid(row=1, column=1)

        self.master.gestionnaire_io.temps_attente = nouvelle_fonction


        #### FIN DÉFI TEMPS ATTENTE ####
