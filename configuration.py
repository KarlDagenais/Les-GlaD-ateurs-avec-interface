configurations = {}
with open("config.txt", "r") as fichier_config: # On ouvre le fichier en lecture
    for ligne in fichier_config: #pour chaque ligne du fichier
        if ligne != '\n':  # Si elle n'est pas vide
            cle, valeur = ligne.rstrip().split(":") # On sépare la clé et la valeur
        if valeur == None: # Si la valeur est vide
            raise KeyError # On lève une erreur
        if cle in ["dimension", "n_des"]: # Si la clé est dimension ou n_des
            if not valeur.isnumeric(): # Si la valeur n'est pas un nombre   
                raise ValueError # On lève une erreur
            configurations[cle] = valeur # On ajoute la clé et la valeur au dictionnaire
        elif cle == ["dessiner"]: # Si la clé est dessiner
            if cle.lower(() not in ["oui", "non"]): # Si la valeur n'est pas oui ou non
                raise ValueError # On lève une erreur
            configurations[cle] = valeur # On ajoute la clé et la valeur au dictionnaire
        elif cle == "joueurs": # Si la clé est joueurs
            valeur=valeur.rstrip().split(",")
            if len(valeur)<2 or len(valeur)>5: # Si la valeur n'est pas un nombre entre 2 et 5
                raise ValueError # On lève une erreur
            configurations[cle] = valeur # On ajoute la clé et la valeur au dictionnaire           
print(configurations)  